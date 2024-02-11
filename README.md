# YOLO Object Recognition Application

This project aims to provide object detection capabilities using YOLO (You Only Look Once) models. It includes functionalities to detect objects both from images and videos, as well as via webcam in real-time. The project utilizes the YOLO model implemented in PyTorch along with various Python libraries for image processing and visualization.

## Technologies Used

- **YOLO**: YOLO (You Only Look Once) is a state-of-the-art, real-time object detection system.
- **PyTorch**: PyTorch is an open-source machine learning library used for various tasks including computer vision.
- **CVZone**: CVZone is a library used for displaying detections and text on images.
- **OpenCV**: OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library.
- **Python**: Python is the primary programming language used in this project.

## How to Run

### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Installation
1. Clone the repository to your local machine:
```bash
git clone <repository-url>
```

2. Navigate to the project directory:
```bash
cd <project-directory>
```

3. Install the required packages using pip:
```bash
pip install -r requirements.txt
```
### Usage

#### Object Detection from Images

Run the following command to perform object detection on an image: python yolo-object-detection.py

This will load the YOLO model and perform object detection on the specified image, displaying the results including bounding boxes and confidence levels.

#### Object Detection from Videos

Run the following command to perform object detection on a video: python yolo-object-detection.py

This will load the YOLO model and perform object detection on the specified video, displaying the results in real-time including bounding boxes and confidence levels.

#### Real-time Object Detection via Webcam

Run the following command to perform real-time object detection via webcam: python yolo-object-detection-webcam.py

This will open your webcam and perform object detection in real-time, displaying the results including bounding boxes and confidence levels.

## Directory Structure

- **Yolo-Weights**: Contains the YOLO model weights (`yolov8n.pt`).
- **Yolo-Image**: Contains images used for object detection.
- **Yolo-Webcam**: Contains the script for real-time object detection via webcam.
- **main.py**: Main script file (currently empty).
- **requirements.txt**: File containing the required Python packages and their versions.

## Acknowledgements

This project utilizes the YOLO model from the Ultralytics repository and various open-source libraries for image processing and visualization.

---

Feel free to contribute to this project by forking it and submitting pull requests. If you encounter any issues or have suggestions for improvements, please open an issue on GitHub. Thank you for using my object recognition application!
