# Day 18 — Video Processing with OpenCV

## What's in this folder

| File | Purpose |
|---|---|
| `video_processing.py` | Reads a video file, prints its properties, converts frames to grayscale, applies Canny Edge Detection, and saves the result. |
| `webcam_processing.py` | Captures live webcam video, processes each frame (grayscale → blur → Canny), displays it in real time, and saves the recording. |
| `mini_project.py` | The combined tool — works on either a video file **or** the webcam, shows original + processed side by side, and saves the processed output. |
| `challenge_process_videos.py` | Runs the pipeline over multiple videos in one go and prints a comparison summary. |
| `sample_input.mp4` | A short placeholder test clip (see note below). |
| `sample_output_edges.mp4` | The processed (Canny edge) output of `sample_input.mp4`, produced by `video_processing.py`. |
| `sample_mini_output.mp4` | Output of `mini_project.py` on the same sample clip. |

> **Note on the sample video:** this sandbox doesn't have network access to Pexels/Pixabay, so `sample_input.mp4` is a small synthetic clip generated with OpenCV, only included so the scripts could be tested end-to-end. **Before submitting, replace it with a real short clip downloaded from [Pexels](https://www.pexels.com/videos/) or [Pixabay](https://pixabay.com/videos/)**, then re-run the scripts to regenerate the real outputs. All four scripts were tested and run correctly — you just need to point `--input` at your real downloaded video(s).

## How to run

```bash
# 1. Basic video processing (prints properties, saves grayscale+Canny output)
python video_processing.py --input your_video.mp4 --output processed.mp4

# 2. Live webcam processing (press 'q' to stop and save)
python webcam_processing.py --output webcam_output.mp4

# 3. Mini project — works on a file or webcam, shows original+processed side by side
python mini_project.py --source video --input your_video.mp4 --output mini_output.mp4
python mini_project.py --source webcam --output mini_webcam_output.mp4

# 4. Challenge task — process 3+ videos and compare
python challenge_process_videos.py --inputs video1.mp4 video2.mp4 video3.mp4 --outdir processed/
```

Add `--no-display` to `video_processing.py` or `mini_project.py` if you're running on a machine without a GUI (e.g. a remote server).

---

## How OpenCV reads videos

OpenCV treats a video as a **sequence of images (frames)**. You open a video with `cv2.VideoCapture(path)`, which acts like a stream you can pull frames from one at a time using `cap.read()`. Each call returns:

- `ret` — a boolean, `True` if a frame was successfully read, `False` once the video has ended (or if the file/camera couldn't be read).
- `frame` — the actual image as a NumPy array in **BGR** color order (note: OpenCV uses BGR, not RGB).

This is why almost every video-processing script has the same core loop:

```python
cap = cv2.VideoCapture(path)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # ... do something with frame ...
cap.release()
```

`cap.release()` at the end frees the underlying video file/device — skipping it can leave the file locked or the camera busy.

## What FPS means

**FPS (Frames Per Second)** is how many individual images make up one second of video. A 30 FPS video shows 30 frames every second; a 24 FPS video shows 24. It directly controls:

- **Smoothness** — higher FPS looks smoother (more in-between frames).
- **Total frame count** — `total_frames ≈ FPS × duration_in_seconds`. In OpenCV you can read this yourself: `cap.get(cv2.CAP_PROP_FPS)` and `cap.get(cv2.CAP_PROP_FRAME_COUNT)`.
- **Playback timing when writing videos** — when saving a processed video with `cv2.VideoWriter`, you must tell it the FPS to use, or the output will play back too fast or too slow.
- **Real-time display delay** — when previewing a video with `cv2.imshow`, `cv2.waitKey(delay)` should roughly equal `1000 / FPS` (in milliseconds) so the playback speed matches the original.

Webcams often *report* an FPS value that doesn't match their real, achievable capture rate (depends on lighting, USB bandwidth, resolution, etc.), which is why `webcam_processing.py` falls back to a default of 20 FPS if the camera reports something invalid (0 or NaN).

## Processing techniques applied

1. **Grayscale conversion** (`cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)`) — reduces each pixel from 3 color channels to 1 intensity value. This simplifies later processing and is a required input for Canny.
2. **Gaussian Blur** (`cv2.GaussianBlur(gray, (5,5), 0)`) — smooths out small noise/high-frequency detail before edge detection, since Canny is sensitive to noise and would otherwise pick up a lot of tiny false edges.
3. **Canny Edge Detection** (`cv2.Canny(blurred, 100, 200)`) — finds strong intensity gradients (edges/outlines) in the frame using two thresholds: pixels above the high threshold (200) are definitely edges, pixels below the low threshold (100) are definitely not, and pixels in between are kept only if they connect to a strong edge.
4. **Video writing** (`cv2.VideoWriter`) — re-encodes the processed frames into a new playable video file, frame by frame, using the same FPS/resolution as the source (with `isColor=False` since the Canny output is single-channel).

## Challenges faced working with video frames

- **Color channel order**: OpenCV reads/writes in BGR, not RGB, which trips people up when mixing OpenCV with other libraries (e.g. Matplotlib expects RGB) — colors look swapped if you forget to convert.
- **VideoWriter needs an exact matching frame size/color mode**: if the frame shape you `write()` doesn't match the size passed into `cv2.VideoWriter(...)`, or if you pass a grayscale (2D) frame with `isColor=True` (or vice versa), the output file can end up empty or corrupted with no clear error message — the fix is being careful to set `isColor=False` for single-channel Canny/grayscale output.
- **FPS = 0 or NaN from live cameras**: unlike video files, many webcams don't report a reliable FPS through `cap.get(cv2.CAP_PROP_FPS)`, so the code needs a fallback default rather than trusting the camera blindly.
- **`cv2.waitKey()` delay vs. real playback speed**: forgetting to base the wait delay on the video's actual FPS makes preview playback look sped up or slowed down compared to the original.
- **Codec/container compatibility**: not every fourcc code (e.g. `mp4v`, `XVID`, `avc1`) works on every OS/OpenCV build — if `VideoWriter` silently fails to open, the codec is usually the first thing to check.
- **Headless environments**: `cv2.imshow()` requires a GUI/display backend and throws an error on servers or CI without one, so scripts need a `--no-display` fallback to still be testable.

---

## Challenge Task — Comparing 3 videos

Run:

```bash
python challenge_process_videos.py --inputs video1.mp4 video2.mp4 video3.mp4 --outdir processed/
```

This saves an `_original.mp4` and `_processed.mp4` copy for each input inside `processed/`, and prints an **average edge density** (percentage of pixels detected as edges) per video — a simple, objective way to compare how "detailed"/busy each processed video is. Fill in your own observations here once you've run it on your three real videos, e.g.:

| Video | Content | Avg Edge Density | Observation |
|---|---|---|---|
| video1 | (describe) | X% | (e.g. lots of fine edges from foliage/text) |
| video2 | (describe) | X% | (e.g. smoother output, fewer strong edges) |
| video3 | (describe) | X% | (e.g. motion blur reduced edge clarity) |

---

## Hugging Face Space

- [ ] Push this code to a public Hugging Face Space (e.g. using `gradio` or `streamlit` to wrap `mini_project.py`'s processing pipeline so it runs on an uploaded video in the browser, since raw `cv2.imshow`/webcam capture won't work inside a hosted Space).
- [ ] Add example input/output images or GIFs to the Space's README/app page.
- [ ] Share the Space link here: `<add your Hugging Face Space URL>`
