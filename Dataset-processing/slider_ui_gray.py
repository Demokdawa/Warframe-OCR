import PySimpleGUI as sg
from sys import exit
from PIL import Image
import base64
import cv2
from io import BytesIO
import numpy as np

# Load image as numpy format
image_source = cv2.imread("theme_source.png")
rgb_source = cv2.cvtColor(image_source, cv2.COLOR_BGR2GRAY)
# Downscale image for interface
downscale = cv2.resize(rgb_source, (1024, 576), interpolation=cv2.INTER_CUBIC)
kernel = np.ones((1, 1), np.uint8)
eroded = cv2.erode(downscale, kernel, iterations=1)
dilate = cv2.dilate(eroded , kernel, iterations=1)
# Convert it to PIL format
pil_img = Image.fromarray(dilate)


def encode_to_64(img):
    # Convert image to Base64 string
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue())
    return img_str


def apply_filter(img, slider_dict):
    ret, imgtresh = cv2.threshold(img, slider_dict['sliderdown'], slider_dict['sliderup'], cv2.THRESH_BINARY)
    filter_pil_img = Image.fromarray(imgtresh)
    filter_new_img = encode_to_64(filter_pil_img)
    return filter_new_img


layout = [[sg.Text('VALUE  '), sg.Slider(range=(0, 255), default_value=0, orientation='h', size=(30, 20), key='sliderdown', enable_events=True), sg.Text(' TO '), sg.Slider(range=(0, 255), default_value=0, orientation='h', size=(30, 20), key='sliderup', enable_events=True)],
          [sg.Image(data=encode_to_64(pil_img), key='image')],
          [sg.Quit()]
          ]

# Display the window and get values
window = sg.Window('Filter-Creator', layout)

while True:
    event, values = window.Read()
    new_img = apply_filter(dilate, values)
    window.FindElement('image').Update(data=new_img)
    if event is 'sliderup' or 'sliderdown':
        window.FindElement('image').Update(data=new_img)
    if event is None:
        break
    if event == 'Quit':
            exit(0)
