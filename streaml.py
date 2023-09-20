
import cv2
import requests

from datetime import datetime
import streamlit as st
import tempfile
import time
from weappon import *
from facial_recognition import *
# Create tracker object


source = 1
vechicles = {}
global save_video
save_video = True  # want to save video? (when video as source)
show_video = True  # set true when using video file
save_img = True  # set true when using only image file to save the image
tracker_status = True
confidence = 0.7
emg_detector = False
accused_detection = True
object_det = True
helemet_detecation = False
Start = True

Email = 'odelapradeep12@gmail.com'
# when using image as input, lower the threshold value of image classification

# Create a Streamlit text element to display the time
time_display = st.empty()





###################################################################################################
########################################### UI PART ###############################################
###################################################################################################


st.title('Dashboard ')
st.sidebar.title('settings')

st.markdown(
    '''
	<style>
	[data-testid='sidebar'][aria-expanded='true'] > div:firstchild{width:400px}
	[data-testid='sidebar'][aria-expanded='false'] > div:firstchild{width:400px , margin-left: -400px}
	</style>
	''',
        unsafe_allow_html=True
)

st.sidebar.markdown('---')

# save_video = st.sidebar.checkbox('save video', value=True)
show_video = st.sidebar.checkbox('show video', value=True)
# save_img = st.sidebar.checkbox('save image', value=True)
st.sidebar.markdown('---')
st.sidebar.title("Video source")

use_webcam = st.sidebar.checkbox('use webcam', value=False)
if use_webcam:
    cams = [0, 1, 3]
    source = st.sidebar.multiselect('choose a cam', cams, default=0)
    listToStr = ' '.join([str(elem) for elem in source])
    in_source = int(listToStr)
    if len(source) > 1:
        st.sidebar.text('plese select only one')
    if len(source) == 0:
        st.sidebar.text('plese select a camara')
    source = int(source[0])
    print(source)

else:
    source = st.sidebar.file_uploader(
        'upload a video ', type=['mp4', 'mov', 'avi', 'm4v', 'gif'])
    show = st.sidebar.checkbox('show input video ', value=False)
    if show:
        st.sidebar.video(source)
    if source != None:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(source.read())
        in_source = tfile.name
st.sidebar.markdown('---')
st.sidebar.title("functionality's")

# emg_detector = st.sidebar.checkbox('Emergency vechicle detecation', value=True)
accused_detection = st.sidebar.checkbox(
    'Accused detection detecation', value=True)
# helemet_detecation = st.sidebar.checkbox('Helemet detection ', value=True)
object_det = st.sidebar.checkbox('object detection and tracking', value=True)
weapon_detection = st.sidebar.checkbox('weapon detection', value=True)
if object_det:
    confidence = st.sidebar.slider(
        'confidence', min_value=0.0, max_value=1.0, value=0.7)


st.sidebar.markdown('---')
st.sidebar.title("Alerts")




Start = st.sidebar.button('Start')

stop = st.sidebar.button('Stop')
if stop:
    Start = False
    cap.release()
    print(Start)


###################################################################################################
########################################### UI PART ###############################################
###################################################################################################


def shh():
    st.text('hello')
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return current_time

if Start:

    stframe = st.empty()

    cap = cv2.VideoCapture(in_source)
    while (cap.isOpened()):

        ret, frame = cap.read()
        current_time = get_current_time()


        if weapon_detection:
             frame=detect_weappon(frame)

        if accused_detection:
            frame = fcr(frame)

            # frame = cv2.resize(frame, frame_size)  # resizing image
        orifinal_frame = frame.copy()
        if show_video:  # show video
            # resizing to fit in screen
            frame = cv2.resize(frame, (900, 450))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            stframe.image(frame)
            time_display.text(f"Current Time: {current_time}")
            
            
            # cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            print('Execution completed')
            break

    cap.release()
    cv2.destroyAllWindows()
print('Execution completed')
