from pathlib import Path
#Imports for streamlit
import streamlit as st
import av
import cv2
from streamlit_webrtc import (
    RTCConfiguration,
    VideoProcessorBase,
    WebRtcMode,
    webrtc_streamer,
)
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.app_logo import add_logo
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Imports for ml model
import numpy as np
import mediapipe as mp
from keras.models import load_model
import tensorflow as tf


st.set_page_config(
    page_title="Moodifier",
    page_icon="🎵",
)


page_bg_img = """
<style>

div.stButton > button:first-child {
    all: unset;
    width: 150px;
    height: 40px;
    font-size: 32px;
    background: transparent;
    border:;
    position: relative;
    color: #f0f0f0;
    cursor: pointer;
    z-index: 1;
    padding: 15px 37px;
    display: flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    user-select: none;
}

div.stButton > button:before, div.stButton > button:after {
    content: '';
    position: absolute;
    bottom: 0;
    right: 0;
    z-index: -99999;
}


div.stButton > button:before {
    transform: translate(0%, 0%);
    width: 100%;
    height: 100%;
    background: black;
    border-radius: 10px;
}
div.stButton > button:after {
  transform: translate(10px, 10px);
  width: 0px;
  height: 0px;
  background: #150050;
}

div.stButton > button:hover::after {
    border-radius: 10px;
    transform: translate(0,0);
    width: 100%;
    height: 100%;
}

div.stButton > button:active::after {
    transition: 0s;
    transform: translate(0, 0%);
}



[data-testid="stAppViewContainer"] {
  background-image: url("https://i.pinimg.com/originals/f2/f8/3d/f2f83dc46d615600dc839539be10398e.jpg");
  background-size: cover;
  background-position: top left;
  background-repeat: no-repeat;
  background-attachment: local;
}

[data-testid="stSidebar"] > div:first-child {
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
background : light;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}

</style>

"""

moodifier_logo = "https://i.pinimg.com/originals/b3/5f/a5/b35fa57402f53d945a880dd39eb9d0ee.png"

st.markdown(page_bg_img, unsafe_allow_html=True)

moodifier_logo = "https://i.pinimg.com/originals/bc/63/40/bc6340b2b36a308315370e77b9dc4d91.png"
st.markdown(
    "<h1 style='text-align: center; margin-top: -90px; margin-bottom: 20px; '><img src='" + moodifier_logo + "' style='width:300px;'></h1>",
    unsafe_allow_html=True
)

st.write("Welcome to Moodifier! Our AI is ready to turn your emotions into a personalized music experience. Just let your webcam capture your mood, and we'll curate a playlist that speaks to your feelings. Ready for a musical journey? Hit that webcam and let's dive in!")

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{
        "urls": ["stun:stun.l.google.com:19302"]
    }]})

HERE = Path(__file__).parent

model = load_model("model.h5")
label = np.load("labels.npy")

holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

if "run" not in st.session_state:
    st.session_state["run"] = ""

run = np.load("emotion.npy")[0]

try:
    emotion = np.load("emotion.npy")[0]
except:
    emotion = ""

class EmotionProcessor(VideoProcessorBase):
    def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
        frm = frame.to_ndarray(format="bgr24")
        frm = cv2.flip(frm, 1)  
        res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
        
        lst = []
        if res.face_landmarks:
            for i in res.face_landmarks.landmark:
                lst.append(i.x - res.face_landmarks.landmark[1].x)
                lst.append(i.y - res.face_landmarks.landmark[1].y)
        
            if res.left_hand_landmarks:
                for i in res.left_hand_landmarks.landmark:
                    lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
            else:
                for i in range(42):
                    lst.append(0.0)
        
            if res.right_hand_landmarks:
                for i in res.right_hand_landmarks.landmark:
                    lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
            else:
                for i in range(42):
                    lst.append(0.0)
        
            lst = np.array(lst).reshape(1, -1)
        
            pred = label[np.argmax(model.predict(lst))]
            print(pred)
            cv2.putText(frm, pred, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            
            np.save("emotion.npy",np.array([pred]))            
            emotion = pred
       
        drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_CONTOURS)
        drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS) 
        drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)
    
        return av.VideoFrame.from_ndarray(frm, format="bgr24")
    
webrtc_streamer(key="key", desired_playing_state=st.session_state.get("run", "") == "true" ,mode=WebRtcMode.SENDRECV,  rtc_configuration=RTC_CONFIGURATION, video_processor_factory=EmotionProcessor, media_stream_constraints={
        "video": True,
        "audio": False
    },
    async_processing=True)


col1, col2, col6 = st.columns([1, 1, 1])

with col1:
    start_btn = st.button("START")
with col6:
    stop_btn = st.button("STOP")

st.write("(or feel free to skip the face scan and choose your favorite streaming platform directly!)")

if start_btn:
    st.session_state["run"] = "true"
    st.experimental_rerun()

if stop_btn:
    st.session_state["run"] = "false"
    st.experimental_rerun()
else:
    if not emotion:
        pass
    else:
        np.save("emotion.npy", np.array([""]))
        st.session_state["emotion"] = run
        st.success("Your current emotion is: " + emotion)
        st.subheader("Choose your streaming service")

col3, col4, col5 = st.columns(3)

with col4:
    btn = st.button("Spotify")
    if btn:
        switch_page("Spotify")

with col5:
    btn2 = st.button("Youtube")
    if btn2:
        switch_page("Youtube")

with col3:
    btn3 = st.button("Soundcloud")
    if btn3:
        switch_page("Soundcloud")