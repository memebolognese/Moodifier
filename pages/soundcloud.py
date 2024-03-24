import streamlit as st
import webbrowser
from streamlit_extras.app_logo import add_logo
import streamlit.components.v1 as components
from streamlit_player import st_player

page_bg_img = """
<style>
div.stButton > button:first-child {
    all: unset;
    width: 250px;
    height: 60px;
    font-size: 35px;
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
    background: #333333;
    border-radius: 10px;
}

div.stButton > button:hover::after {
    border-radius: 10px;
    transform: translate(0, 0);
    width: 100%;
    height: 100%;
    background: #ff5500;
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
background: ;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

[data-testid="stToolbar"] {
right: 2rem;
}
</style>
"""

soundcloud_logo = "https://logowik.com/content/uploads/images/312_soundcloud.jpg"
st.image(soundcloud_logo, width=200)
st.markdown(page_bg_img, unsafe_allow_html=True)

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


col1, col2 = st.columns(2)

with col1:
    english = st.button("English")
    if english:
        if st.session_state["emotion"] == "Happy":
            st_player("https://soundcloud.com/user-802072483/sets/happy-songs-everyone-knows?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://soundcloud.com/user-25916804/sets/sad-songs-to-sleep?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://soundcloud.com/kaitlyn-cervantez-365526515/sets/angry-songs?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://soundcloud.com/playlist-beast/sets/english-top-hits-of-all-time?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
    

    malay = st.button("Malay/Indo")
    if malay:
        if st.session_state["emotion"] == "Happy":
            st_player("https://soundcloud.com/rendi-agustian-545096784/sets/pop-indo?si=557ad603d8a34dde9fd9310c55d2935b&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://soundcloud.com/dka-320586109/sets/indo-sad?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://soundcloud.com/abas-surya/sets/pop-cover-rock?si=db5dfc682b024fad94238a7fdd07300d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://soundcloud.com/yhanuk-riyanto/sets/top-50-pop-indonesia-2023?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
       
    
    mandarin = st.button("Mandarin")
    if mandarin:
        if st.session_state["emotion"] == "Happy":
            st_player("https://soundcloud.com/legacybarzz-sg/sets/shhpplnqjaao?si=bfcfa995495a474cbae104420a5d1881&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://soundcloud.com/chee-yin-theng-moe/sets/oru1guusnmpk?si=6c72b7d02b824a9fa9e6f03e7cad2027&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://soundcloud.com/user-911823302/sets/nh-ng-b-n-nh-c-trung-t-m-tr-ng?si=0690d1b575e74312a277f4bced0cb38b&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://soundcloud.com/tu-anh-tran-83145169/sets/chinese-song-2023?si=50584ba8961145cc8eff07dda8b08e77&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
     
   
with col2:
   tamil = st.button("Tamil")
   if tamil:
        if st.session_state["emotion"] == "Happy":
            st_player("https://soundcloud.com/karuna-mahendra/sets/happy-tamil-songs?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://soundcloud.com/shanmugarajah-balasupramaniam/sets/tamil-sad-songs-1?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://soundcloud.com/santhosh-rangit/sets/tamil-kuthu-and-fast-beat?si=35f9ab309ea24c119cf3fe089ab132a6&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://soundcloud.com/srivatsag/sets/tamil-hits?si=3b5a47cf7add45619010313a14138e33&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
   
   korean = st.button("Korean")
   if korean:
        if st.session_state["emotion"] == "Happy":
            st_player("https://soundcloud.com/astri-dinnaryanti/sets/kpop-happy-melody?si=026a427f4cec4a65962edc0f166cb6a1&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://soundcloud.com/tr-n-m-a-935155819/sets/sad-korean-songs?si=b3d3c7cb060d4a128940eeef9b384895&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://soundcloud.com/kube-martins/sets/korean-songs-calming?si=0c0b7ad9909e406fb3a5cb2fd8dd34b0&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://soundcloud.com/user-115366034/sets/korean-hits?si=b782b59cfb3b472787408c7268997464&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")

   japanese = st.button("Japanese")
   if japanese:
        if st.session_state["emotion"] == "Happy":
            st_player("https://soundcloud.com/user-636367953-300927817/sets/happy-japanese-music?si=f3ba64d4d2cb480bbc3accd051da6e4d&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Sad":
           st_player("https://soundcloud.com/user-744449168/sets/sad-japanese-songs?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Angry":
            st_player("https://soundcloud.com/user-899020439/sets/calming-japanese-songs?si=9fd615318cfe4ef49cae8b7218a29a12&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
        elif st.session_state["emotion"] == "Neutral":
            st_player("https://soundcloud.com/aveltheromantic/sets/japanese-top-hits?si=3a1564bc96ff4c1ea4f0670673f47a26&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing")
    
            