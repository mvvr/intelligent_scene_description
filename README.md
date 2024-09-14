

# Intelligent Scene Description for the Visually Impaired

## Project Overview

This project aims to create a real-time system that generates context-aware descriptions of surroundings for visually impaired individuals. Using a combination of image and video inputs, the system utilizes object detection and natural language generation techniques to provide meaningful descriptions of the environment.

## Features

- Real-time scene description using video input.
- Object detection using YOLO.
- Context-aware text generation using GPT-2.
- Streamlit-based web interface for easy interaction.

## Prerequisites

- Python 3.8 or later
- Required libraries listed in `requirements.txt`

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/intelligent-scene-description.git
   cd intelligent-scene-description
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

2. **Upload a video file:**

   - Navigate to the Streamlit web interface that opens in your browser.
   - Use the file uploader to upload a video in `.mp4` or `.avi` format.
   - The application will process the video and display real-time descriptions of the scene.

## File Structure

- **`app.py`**: Main application script that integrates the components and runs the Streamlit interface.
- **`utils/image_processor.py`**: Handles video frame extraction and object detection.
- **`utils/description_generator.py`**: Generates textual descriptions based on detected objects.
- **`requirements.txt`**: Lists the required Python packages.

## Dependencies

The project requires the following Python libraries:

- `streamlit`
- `opencv-python`
- `transformers`
- `torch`
- `yolov5`

These are listed in `requirements.txt`, which can be installed using `pip`.

## Notes

- Ensure you have the YOLO model weights and GPT-2 model available in your environment.
- For improved performance, consider using pre-trained models or adjusting hyperparameters based on your needs.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.


