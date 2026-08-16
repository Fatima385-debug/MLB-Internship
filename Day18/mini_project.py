"""
Day 18 - Mini Project: Real-Time Video Processing Tool
---------------------------------------------------------
A single tool that works on EITHER a recorded video file OR a live webcam
feed. For every frame it:

    1. Converts to grayscale
    2. Applies Gaussian Blur (noise reduction)
    3. Applies Canny Edge Detection
    4. Displays the original frame and the processed frame side by side
    5. Writes the processed frames to a new output video file

Usage:
    # Process a video file
    python mini_project.py --source video --input input.mp4 --output processed_output.mp4

    # Process the webcam live
    python mini_project.py --source webcam --output webcam_processed.mp4

Controls:
    q -> quit (works for both video file and webcam mode)
"""

import argparse
import os
import cv2
import numpy as np


def process_frame(frame: np.ndarray) -> np.ndarray:
    """Apply the full processing pipeline to a single BGR frame.

    Returns a single-channel (grayscale) edge-detected frame.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 100, 200)
    return edges


def make_side_by_side(original: np.ndarray, processed: np.ndarray) -> np.ndarray:
    """Stack the original (BGR) and processed (grayscale) frames horizontally
    for a combined preview window."""
    processed_bgr = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
    # Resize both to the same height, just in case
    h = min(original.shape[0], processed_bgr.shape[0])
    original_resized = cv2.resize(original, (original.shape[1], h))
    processed_resized = cv2.resize(processed_bgr, (processed_bgr.shape[1], h))
    return np.hstack([original_resized, processed_resized])


def run(source: str, input_path: str, output_path: str, camera_index: int = 0, display: bool = True) -> None:
    if source == "video":
        if not input_path or not os.path.exists(input_path):
            raise FileNotFoundError(f"Input video not found: {input_path}")
        cap = cv2.VideoCapture(input_path)
    else:
        cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        raise IOError("Could not open video source.")

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0 or fps != fps:
        fps = 20.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) if source == "video" else -1

    print("----- Source Properties -----")
    print(f"Mode           : {source}")
    print(f"FPS            : {fps:.2f}")
    print(f"Width x Height : {width} x {height}")
    if total_frames > 0:
        print(f"Total Frames   : {total_frames}")
    print("------------------------------")

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), isColor=False)

    frame_count = 0
    delay = int(1000 / fps) if fps > 0 else 30

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1

        edges = process_frame(frame)
        out.write(edges)

        if display:
            combined = make_side_by_side(frame, edges)
            cv2.imshow("Original | Processed (Grayscale + Blur + Canny)", combined)
            if cv2.waitKey(delay) & 0xFF == ord("q"):
                break

    print(f"Processed {frame_count} frames.")
    print(f"Saved processed video to: {output_path}")

    cap.release()
    out.release()
    if display:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Real-Time Video Processing Tool (file or webcam).")
    parser.add_argument("--source", choices=["video", "webcam"], required=True, help="Input source type")
    parser.add_argument("--input", help="Path to input video file (required if --source video)")
    parser.add_argument("--output", required=True, help="Path to save processed output video")
    parser.add_argument("--camera", type=int, default=0, help="Webcam index (only used if --source webcam)")
    parser.add_argument("--no-display", action="store_true", help="Disable live preview windows (useful on headless machines)")
    args = parser.parse_args()

    run(args.source, args.input, args.output, args.camera, display=not args.no_display)
