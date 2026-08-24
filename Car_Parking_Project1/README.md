# Smart Parking Lot Occupancy Analyzer
A computer vision system that detects occupied and vacant parking spaces
in parking lot images, combining a YOLOv8 object detector with a classical OpenCV pipeline
used for slot-boundary discovery and pipeline demonstration.

## Project Overview

Given an image of a parking lot, the system:
1. Detects `occupied` and `empty` parking-space regions directly using
   a YOLOv8 model fine-tuned on a Roboflow dataset labeled with those
   two slot-state classes.
2. Runs a classical OpenCV pipeline (grayscale → denoise → contrast
   enhancement → Canny edge detection → morphological closing/dilation
   → contour detection) to demonstrate slot-boundary discovery, and to
   provide an automatic-fallback slot-region detector for images/camera
   angles with no pre-existing annotations.
3. Renders color-coded results (green = vacant, red = occupied) with a
   live occupancy-percentage stats banner over the original image.

## Dataset Used
[Parking Space Occupancy Dataset]: (https://universe.roboflow.com/parking-gvjqh/parking-lot-9sjil)
- 312 images, 2 classes: `occupied`, `empty`
- Split: 70%  train / 20 % valid / 2% test
- Downloaded in YOLOv8 format via the `roboflow` Python package

## Project Workflow

```
                Input Image
                     │
                     ▼
     ┌───────────────────────────────┐
     │ Preprocessing & Enhancement    │  grayscale, Gaussian blur,
     │                                 │  CLAHE contrast enhancement
     └───────────────┬────────────────┘
                      │
                      ▼
     ┌───────────────────────────────┐
     │ Edge Detection                 │  auto-thresholded Canny
     └───────────────┬────────────────┘
                      │
                      ▼
     ┌───────────────────────────────┐
     │ Morphological Operations       │  closing + dilation to
     │                                 │  reconnect broken slot lines
     └───────────────┬────────────────┘
                      │
                      ▼
     ┌───────────────────────────────┐
     │ Contour-Based Slot Detection    │  fallback slot-region
     │ (fallback / demonstration)      │  discovery when no manual
     │                                 │  slot annotations exist
     └───────────────┬────────────────┘
                      │
                      ▼
     ┌───────────────────────────────┐
     │ YOLOv8 Inference                │  predicts `occupied` /
     │ (occupied / empty)              │  `empty` directly per slot
     └───────────────┬────────────────┘
                      │
                      ▼
     ┌───────────────────────────────┐
     │ Occupancy Tally                 │  count occupied vs empty
     │                                 │  predictions, compute %
     └───────────────┬────────────────┘
                      │
                      ▼
         Annotated Output Image + Live Stats Banner
```


### Sample annotated output
![alt text](C:\Users\HP\Desktop\MLB-Internship\Car_Parking_Project1\content\outputs\annotated_2022-11-15-14-07-04_mp4-0_jpg.rf.664cc58561ab5c1ad7f5852a300bec6f.jpg)

## Technologies Used

| Tool | Purpose |
|---|---|
| YOLOv8 (Ultralytics) | Slot occupancy detection (`occupied` / `empty`), fine-tuned on the Roboflow dataset |
| OpenCV | Preprocessing, CLAHE, Canny edge detection, morphological ops, contour detection, drawing/visualization |
| NumPy | Array/mask arithmetic for slot-region overlap calculations |
| Matplotlib | In-notebook visualization of every pipeline stage |
| Pandas | Aggregating per-image occupancy statistics into a summary table |
| Roboflow | Dataset hosting, versioning, and YOLOv8-format download |
| Google Colab  | 

## Results

- Trained YOLOv8n on Google Colab. Early stopping (`patience=10`)
  halted training at **epoch 40**, with the best-performing checkpoint
  captured at **epoch 30**; total training time was **~2.1 hours**.
  (Note: this run executed on Colab's CPU backend rather than a GPU —
  still practical for a nano model on a ~2-class dataset, but a GPU
  run would train significantly faster on a larger model/dataset.)
- **Validation results** (120 images, 856 slot instances):

  | Class | Images | Instances | Precision | Recall | mAP50 | mAP50-95 |
  |---|---|---|---|---|---|---|
  | all | 120 | 856 | 0.877 | 0.877 | **0.940** | 0.584 |
  | empty | 114 | 556 | 0.889 | 0.820 | 0.926 | 0.558 |
  | occupied | 106 | 300 | 0.864 | 0.935 | 0.955 | 0.610 |

  Inference speed: ~170ms/image (CPU) — 1.6ms preprocess, 170.3ms
  inference, 3.6ms postprocess.
- A validation mAP50 of 0.94 with balanced precision/recall across
  both classes indicates the model reliably distinguishes occupied vs.
  empty slots on this dataset; the `occupied` class has slightly
  higher recall (0.935) than `empty` (0.820), suggesting a small bias
  toward flagging ambiguous slots as occupied rather than missing
  them.
- Sample annotated outputs: see [`outputs/`](outputs) and
  [`data/sample_images/`](data/sample_images).

## Challenges Faced

- **Local CPU training was impractically slow.** An initial attempt to
  train on a local machine without a GPU projected roughly 5-6 days
  *per epoch* based on the reported iteration rate — made clear only
  after reading the training progress bar's ETA rather than assuming
  epoch count alone was the bottleneck. Training was moved to a free
  GPU runtime (Colab/Kaggle) instead of trying to shrink the job to fit
  CPU constraints.
- **Silent kernel crashes when training inside Jupyter on Windows.**
  Training would kill the kernel with no Python traceback. The two
  leading causes on Windows are (a) multiprocessing DataLoader workers
  being fragile when spawned from inside a notebook kernel, fixed with
  `workers=0`, and (b) an OpenMP runtime conflict between bundled
  `libiomp5md.dll` copies from `torch`/`numpy`, fixed by setting
  `KMP_DUPLICATE_LIB_OK=TRUE` before any other imports.
- **Class-name ambiguity across dataset versions.** An earlier version
  of the dataset used 4 overlapping class names (`occupied`,
  `space-occupied`, `space-empty`, `unoccupied`) representing only 2
  true states, requiring a keyword-normalization step before tallying
  occupancy; the final dataset (`occupied` / `empty`) avoided this
  entirely by using exactly 2 unambiguous classes.
- **Forgetting to mount Google Drive before starting training.**
  `project="/content/drive/MyDrive/runs_parking"` doesn't fail if
  Drive isn't mounted — Colab just creates a normal local folder at
  that path, which looks identical to a real Drive folder until you
  try to mount Drive afterward and hit `ValueError: Mountpoint must
  not already contain files`. Lesson: always mount Drive as the very
  first cell in the notebook, before any training or file-writing
  begins, to avoid this path collision entirely.


## How to Run

The full pipeline is contained in a single Colab/Kaggle-ready notebook
— no separate script files required.

```bash
# 1. Open notebooks/Smart_Parking_Roboflow.ipynb in Google Colab or Kaggle Notebooks
# 2. Enable a GPU runtime (Colab: Runtime > Change runtime type > GPU;
#    Kaggle: Settings > Accelerator > GPU, and Settings > Internet > On)
# 3. Run the install cell:
!pip install -q roboflow ultralytics opencv-python-headless numpy matplotlib pandas

# 4. Fill in your Roboflow credentials and run the download cell
# 5. Run the training cell, then the inference/visualization cells in order
```

Local/offline run (slower without a GPU):
```bash
pip install -r requirements.txt
jupyter notebook notebooks/Smart_Parking_Roboflow.ipynb
```
