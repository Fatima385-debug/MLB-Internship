"""
Day 18 - Real-Time Webcam Processing with OpenCV
--------------------------------------------------
Captures live video from your webcam, applies grayscale + Gaussian Blur +
Canny Edge Detection to every frame, shows the live feed, and saves the
processed stream to a video file.

Controls:
    q  -> quit and save the output video

Usage:
    python webcam_processing.py --output webcam_output.mp4 --camera 0
"""

import argparse
import cv2


def run_webcam(output_path: str, camera_index: int = 0) -> None:
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        raise IOError("Could not access the webcam. Check the camera index/permissions.")

    # Webcams often don't report FPS reliably, so fall back to a sane default.
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0 or fps != fps:  # NaN check
        fps = 20.0

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f"Webcam opened: {width}x{height} @ {fps:.1f} FPS (approx)")

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), isColor=False)

    print("Press 'q' to stop recording and save the video.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame from webcam.")
            break

        # Process the frame: grayscale -> blur -> edges
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 100, 200)

        # Show both the raw feed and the processed feed
        cv2.imshow("Webcam - Original", frame)
        cv2.imshow("Webcam - Processed (Canny)", edges)

        # Save the processed frame
        out.write(edges)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Saved recorded webcam video to: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capture, process, and save live webcam video.")
    parser.add_argument("--output", default="webcam_output.mp4", help="Path to save the processed webcam video")
    parser.add_argument("--camera", type=int, default=0, help="Webcam device index (default 0)")
    args = parser.parse_args()

    run_webcam(args.output, args.camera)
