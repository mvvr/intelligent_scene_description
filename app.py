import streamlit as st
import cv2
import tempfile
from utils import image_processor, description_generator

def main():
    st.title("Intelligent Scene Description for the Visually Impaired")
    
    video_input = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])
    
    if video_input is not None:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(video_input.read())
            temp_video_path = temp_file.name

        # Now, pass the temp_video_path to OpenCV
        frames = image_processor.extract_frames(temp_video_path)
        
        descriptions = description_generator.generate_descriptions(frames)
        
        for description in descriptions:
            st.write(description)

if __name__ == "__main__":
    main()
