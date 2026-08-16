"""
Day 18 - Video Processing with OpenCV
--------------------------------------
This script demonstrates the core building blocks of video processing:

1. Reading a video file
2. Reading video properties (FPS, width, height, total frame count)
3. Looping through the video frame by frame
4. Converting each frame to grayscale
5. Applying Canny Edge Detection
6. Writing/saving the processed frames as a new video file

Usage:
    python video_processing.py --input path/to/input_video.mp4 --output path/to/output_video.mp4
"""

import argparse
import os
import cv2


def get_video_properties(cap: cv2.VideoCapture) -> dict:
    """Read and return the basic properties of an opened video."""
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration_sec = total_frames / fps if fps > 0 else 0

    return {
        "fps": fps,
        "width": width,
        "height": height,
        "total_frames": total_frames,
        "duration_sec": duration_sec,
    }


def process_video(input_path: str, output_path: str, display: bool = True) -> None:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input video not found: {input_path}")

    # 1. Read the video
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise IOError(f"Could not open video: {input_path}")

    # 2. Print video properties
    props = get_video_properties(cap)
    print("----- Video Properties -----")
    print(f"FPS            : {props['fps']:.2f}")
    print(f"Width x Height : {props['width']} x {props['height']}")
    print(f"Total Frames   : {props['total_frames']}")
    print(f"Duration (sec) : {props['duration_sec']:.2f}")
    print("-----------------------------")

    # 3. Set up the VideoWriter to save the processed (edge-detected) video.
    #    Canny output is single-channel (grayscale), so isColor=False.
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(
        output_path,
        fourcc,
        props["fps"] if props["fps"] > 0 else 25.0,
        (props["width"], props["height"]),
        isColor=False,
    )

    frame_count = 0
    while True:
        ret, frame = cap.read()  # ret=False when the video ends
        if not ret:
            break

        frame_count += 1

        # 4. Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 5. Apply Canny Edge Detection
        edges = cv2.Canny(gray, threshold1=100, threshold2=200)

        # 6. Write the processed frame to the output video
        out.write(edges)

        # 7. Optionally display frames live while processing
        if display:
            cv2.imshow("Original", frame)
            cv2.imshow("Canny Edges", edges)
            # Press 'q' to stop early
            if cv2.waitKey(int(1000 / props["fps"]) if props["fps"] > 0 else 30) & 0xFF == ord("q"):
                break

    print(f"Processed {frame_count} frames.")
    print(f"Saved processed video to: {output_path}")

    cap.release()
    out.release()
    if display:
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Read, process (grayscale + Canny), and save a video.")
    parser.add_argument("--input", required=True, help="Path to the input video file")
    parser.add_argument("--output", required=True, help="Path to save the processed output video")
    parser.add_argument("--no-display", action="store_true", help="Disable live preview windows (useful on headless machines)")
    args = parser.parse_args()

    process_video(args.input, args.output, display=not args.no_display)
