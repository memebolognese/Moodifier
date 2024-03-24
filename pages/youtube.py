import streamlit as st
import webbrowser
import os
from streamlit_extras.app_logo import add_logo
from streamlit_player import st_player

page_bg_img = """
<style>
div.stButton > button:first-child {
    all: unset;
    width: 300px;
    height: 60px;
    font-size: 32px;
    background: transparent;
    border: none;
    position: relative;
    color: #f0f0f0;
    cursor: pointer;
    z-index: 1;
    padding: 10px 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    white-space: nowrap;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;

}
div.stButton > button:before, div.stButton > button:after {
    content: '';
    position: absolute;
    bottom: 0;
    right: 0;
    z-index: -99999;
    transition: all .4s;
}

div.stButton > button:before {
    transform: translate(0%, 0%);
    width: 100%;
    height: 100%;
    background: #191414;
    border-radius: 10px;
}


div.stButton > button:hover::after {
    border-radius: 10px;
    transform: translate(0, 0);
    width: 100%;
    height: 100%;
    background: #FF0000;
}

[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1706604264136-cb136976fa3e?q=80&w=1228&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}

[data-testid="stSidebar"] > div:first-child {
background-position: center; 
background-repeat: no-repeat;
background-attachment: fixed;
background;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
youtube_logo = "https://upload.wikimedia.org/wikipedia/commons/e/e1/Logo_of_YouTube_%282015-2017%29.svg"
st.image(youtube_logo, width=200)


if "emotion" not in st.session_state:
    st.session_state["emotion"] = ""

if "run" not in st.session_state:
    st.session_state["run"] = ""

if not st.session_state["run"]:
    st.write("**Looks like you have skipped the face scan on the homepage and came here just for music. Please choose your current emotion:**")
    option = st.selectbox(
        'What is your vibe today?',
        ('Happy', 'Sad', 'Angry', 'Neutral'),
        key="emotion_selection"
    )

    if option == "Happy":
        st.session_state["emotion"] = "Happy"
    elif option == "Sad":
        st.session_state["emotion"] = "Sad"
    elif option == "Angry":
        st.session_state["emotion"] = "Angry"
    else:
        st.session_state["emotion"] = "Neutral"

st.write("Your current emotion is:", st.session_state["emotion"])

st.write("Next step, choose your preferred language!")

if "emotion" not in st.session_state:
    st.session_state["emotion"] = None


st.write("Next step, choose your preferred language!")


col1, col2 = st.columns(2)

with col1:
    english = st.button("English")
    if english:
        if st.session_state["emotion"] == "Happy":
            st_player("https://youtu.be/ru0K8uYEZWw?si=Uy2-oFY-0cCR-TW0")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://youtu.be/8ofCZObsnOo?si=adWQ-PRdvm27HFIN")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://youtu.be/-e_jkF20Xo4?si=zcZnqjSZMpxs0FV-")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://www.youtube.com/live/pwwT0syHmxU?si=AjQ42aIWdXUZpq3q")

    malay = st.button("Malay/Indo")
    if malay:
        if st.session_state["emotion"] == "Happy":
            st_player("https://youtu.be/ImyZRKWlZ24?si=7ucVe1VnDgXuPmDz")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://youtu.be/BP_vZ93igGQ?si=8S_p6YKt_a6qDQ0C")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://youtu.be/OjYOC9Y6A_Q?si=0sO26bCKKdO1YMMo")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://youtu.be/NBRodvj0nL8?si=8jHdjen9g6NstRu4")
     
    mandarin = st.button("Mandarin")
    if mandarin:
        if st.session_state["emotion"] == "Happy":
            st_player("https://youtu.be/rom8_r6EUAY?si=-yAorK5CCoojdWSw")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://youtu.be/Zjwd3URK8CY?si=E3dQP5Sq8Yf3ouX_")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://youtu.be/29tEEaTN_Sc?si=lKNxjxS3WIQ8JR-E")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://youtu.be/Yx6um89NRAQ?si=dI8DZrXGTYyxPMK5")
   
with col2:
   tamil = st.button("Tamil")
   if tamil:
        if st.session_state["emotion"] == "Happy":
            st_player("https://youtu.be/A_z5g0_hJN8?si=CzNA1MhTkbho5pWq")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://youtu.be/TBieFYBvhDo?si=96yrTddTC64qagVm")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://youtu.be/DFnfV9e1S1Q?si=FrrbSxoEj0YMfzX-")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://youtu.be/rd1bbljtpds?si=bRneTgkJQPGSaEXT")
            
   korean = st.button("Korean")
   if korean:
        if st.session_state["emotion"] == "Happy":
            st_player("https://youtu.be/myns4nPoprE?si=qbB6RWvvdzEMZxrR")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://youtu.be/W73aPutR74M?si=bnvFum2X4Wxg9hkv")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://youtu.be/aSlvRw0jTSo?si=p6XyyxMQy3OzPEQf")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://youtu.be/0-q1KafFCLU?si=GuPNLmiJQXoBvgyi")
            
   japanese = st.button("Japanese")
   if japanese:
        if st.session_state["emotion"] == "Happy":
            st_player("https://youtu.be/uLGwZbgEoYE?si=-u2V78MOXKETJkNw")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://youtu.be/c4pfCpZIy_s?si=vLHgupNhP6TMMRjE")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://youtu.be/U_bSs3d493M?si=wB4NaqReL6rbQMGP")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://youtu.be/n8C9c79kPks?si=51rqKdUoR-3en79g")