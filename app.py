import streamlit as st
from utils import image_processor, description_generator

def main():
    st.title("Intelligent Scene Description for the Visually Impaired")
    
    video_input = st.file_uploader("Upload a video", type=["mp4", "avi"])
    
    if video_input is not None:
        # Process the video and get scene description
        frames = image_processor.extract_frames(video_input)
        descriptions = description_generator.generate_descriptions(frames)
        
        for description in descriptions:
            st.write(description)

if __name__ == "__main__":
    main()
