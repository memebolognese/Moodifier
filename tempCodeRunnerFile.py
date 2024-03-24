import streamlit as st

from streamlit_webrtc import webrtc_streamer

from homepage import EmotionProcessor


if st.session_state["run"] != "false":
    webrtc_streamer(key="key", desired_playing_state=True , video_processor_factory=EmotionProcessor)