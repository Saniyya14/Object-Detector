# Object Detection for the Visually Impaired

## Project Overview

This project is an object detection system designed to assist visually impaired individuals by providing real-time audio descriptions of objects in their environment. It leverages computer vision techniques and text-to-speech synthesis to identify and announce objects detected by a camera.

## Features

* **Real-time Object Detection:** Uses a pre-trained SSD MobileNet v3 model to detect common objects.
* **Audio Feedback:** Employs text-to-speech (TTS) to verbally announce the detected objects.
* **Camera Input:** Processes live camera feed for continuous object detection.
* **Customizable Object List:** Utilizes a `coco.names` file to specify the objects to be detected.

## Technical Details

* **Computer Vision:**
    * Uses OpenCV (cv2) for image processing and object detection.
    * Employs a pre-trained SSD MobileNet v3 model for efficient object detection.
* **Text-to-Speech (TTS):**
    * Uses the `pyttsx3` library for text-to-speech conversion.
* **Model and Configuration:**
    * `frozen_inference_graph.pb`: The pre-trained object detection model.
    * `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`: The model configuration file.
    * `coco.names`: A list of object names that the model can detect.
* **Programming Language:**
    * Python.

## Files

* `final.py`: The main script that integrates object detection with audio feedback.
* `ObjectDetectorModule.py`: Contains the object detection function.
* `text-to-speech.py`: Object detection with drawing bounding boxes along with speech.
* `camerafeed.py`: (If you have it, explain what this does)
* `coco.names`: The list of object names.
* `frozen_inference_graph.pb`: The trained model.
* `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`: The model configuration.
* `lena.png`: (If you have it, explain what this does)
* `testimage.py`: (If you have it, explain what this does)
* `.idea/` and `__pycache__/`: Development environment files.

## How to Run

1.  **Install Dependencies:**
    ```bash
    pip install opencv-python pyttsx3
    ```
2.  **Ensure Model Files:** Make sure the `frozen_inference_graph.pb`, `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`, and `coco.names` files are in the same directory as the Python scripts.
3.  **Run the Script:**
    ```bash
    python final.py
    ```
4.  **Exit:** Press 'q' to stop the camera feed and exit the program.

## Skills Required

* **Computer Vision:** Implementation of real-time object detection using OpenCV.
* **Deep Learning:** Utilization of a pre-trained SSD MobileNet v3 model.
* **Python Programming:** Development of the application logic and integration of libraries.
* **Text-to-Speech (TTS) Integration:** Implementation of audio feedback using `pyttsx3`.
* **Model Integration:** Correctly implementing the model and the configuration files.

## Product Management Skills
* **User-Centered Design:** Focused on creating a tool to assist visually impaired individuals.
* **Problem-Solving:** Addressing the challenge of object identification for those with visual impairments.
* **Rapid Prototyping:** Creation of a working prototype to demonstrate the concept.


## Potential Improvements

* **Improved Accuracy:** Explore fine-tuning the model or using a more advanced architecture.
* **Directional Audio:** Implement spatial audio to indicate the direction of detected objects.
* **Customizable Object Lists:** Allow users to add or remove objects from the detection list.
* **Portable Device Integration:** Integrate the system into a wearable device for enhanced mobility.
* **Background Noise Filtering:** Filter out background noise from the audio output.
* **Multi Language Support:** Adding the ablity to change the language of the audio output.

