# YOLO-Kalman Person Tracker

## Overview

This repository showcases a real-time person tracking system built using:
- **YOLO (You Only Look Once)** for real-time object detection.
- **Kalman Filter** for predicting and tracking the movement of detected persons across frames.

The project demonstrates the fusion of computer vision and motion estimation techniques to achieve efficient multi-object tracking.

---

## Features

- **Accurate Person Detection**: Leveraging a pre-trained YOLO model for detecting people in videos or real-time streams.
- **Motion Tracking**: Using a Kalman filter to maintain track IDs and handle motion noise.
- **Customizable**: Supports tuning of Kalman filter parameters and YOLO thresholds for specific applications.
- **Visualization**: Annotated output with tracked IDs and motion paths.

---

## Installation

### Prerequisites
Ensure you have Python 3.8+ installed along with the following libraries:
- `numpy`
- `opencv-python`
- `torch`
- `torchvision`
- `matplotlib`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yolo-kalman-tracker.git
   cd yolo-kalman-tracker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Install YOLOv5 dependencies:
   ```bash
   cd models/yolov5
   pip install -U -r requirements.txt
   ```

---

## Usage

### Run Tracker
1. Place your input video in the `data/` folder (e.g., `data/input_video.mp4`).
2. Run the main script:
   ```bash
   python main.py --input data/input_video.mp4 --output data/output_video.mp4
   ```

3. Output will be saved in the `data/` folder as `output_video.mp4`.

### Customize Parameters
Modify the `config.yaml` file to adjust:
- Detection confidence thresholds.
- Kalman filter process noise and measurement noise.

---

## File Structure

```
yolo-kalman-tracker/
├── models/
│   ├── yolov5/              # YOLOv5 model files
├── utils/
│   ├── kalman_filter.py     # Kalman filter implementation
│   ├── association.py       # Object association logic
├── data/
│   ├── input_video.mp4      # Example input video
│   ├── output_video.mp4     # Processed output video
├── notebooks/
│   ├── demo.ipynb           # Interactive demo in Jupyter Notebook
├── main.py                  # Entry point for the application
├── requirements.txt         # Required Python packages
├── config.yaml              # Config file for detection/tracking parameters
├── README.md                # Project documentation
```

---

## Examples

### Input
![Input Example](https://via.placeholder.com/800x400?text=Input+Video+Placeholder)

### Output
![Output Example](https://via.placeholder.com/800x400?text=Tracked+Video+Placeholder)

---
