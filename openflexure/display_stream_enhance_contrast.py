import cv2
import numpy as np
import panel as pn

cap = cv2.VideoCapture('http://192.168.1.199:5000/api/v2/streams/mjpeg')


def brightness_transform(value, r_low = 100 , r_high=255, g_low=100, g_high=255, b_low=100, b_high=255):
    r_array = np.array(value[:,:,0], dtype=float)
    g_array = np.array(value[:,:,1], dtype=float)
    b_array = np.array(value[:,:,2], dtype=float)

    r_array = (r_array - r_low) * 255 / (r_high - r_low)
    g_array = (g_array - g_low) * 255 / (g_high - g_low)
    b_array = (b_array - b_low) * 255 / (b_high - b_low)

    r_array = np.where(r_array < 0, 255, r_array)
    r_array = np.where(r_array > 255, 0, r_array)
    g_array = np.where(g_array < 0, 255, g_array)
    g_array = np.where(g_array > 255, 0, g_array)
    b_array = np.where(b_array < 0, 255, b_array)
    b_array = np.where(b_array > 255, 0, b_array)

    value = np.stack([r_array, g_array, b_array], axis=2)

    return value

## a panel with sliders to adjust low and high values:

r_slider = pn.widgets.RangeSlider(
    name='blue', start=0, end=255, value=(0, 255), step=0.1)
g_slider = pn.widgets.RangeSlider(
    name='blue', start=0, end=255, value=(0, 255), step=0.1)
b_slider = pn.widgets.RangeSlider(
    name='red', start=0, end=255, value=(0, 255), step=0.1)

def autocalibrate(event):
    ret, frame = cap.read()
    frame = np.array(frame, dtype=float)
    r_low = np.min(frame[:,:,0])
    r_high = np.max(frame[:,:,0])
    g_low = np.min(frame[:,:,1])
    g_high = np.max(frame[:,:,1])
    b_low = np.min(frame[:,:,2])
    b_high = np.max(frame[:,:,2])
    r_slider.value = (r_low, r_high)
    g_slider.value = (g_low, g_high)
    b_slider.value = (b_low, b_high)

autocalibrate_button = pn.widgets.Button(name='Autocalibrate')
autocalibrate_button.on_click(autocalibrate)

slider_col = pn.Column(r_slider, g_slider, b_slider, autocalibrate_button)

pn.serve(slider_col, threaded=True)



while True:
    ret, frame = cap.read()
    print("max of frame", np.max(frame))
    r_low, r_high = r_slider.value
    g_low, g_high = g_slider.value
    b_low, b_high = b_slider.value
    transformed = brightness_transform(np.array(frame,dtype=float),
                                       r_low = r_low,
                                       r_high = r_high,
                                       b_low = b_low,
                                       b_high = b_high,
                                       g_low = g_low,
                                       g_high = g_high
                                       ).astype(np.uint8)
    print("max of transformed", np.max(transformed))
    cv2.imshow('frame', frame)
    cv2.imshow('transformed', transformed)

    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()


