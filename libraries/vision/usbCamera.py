# import the opencv library
import cv2
import logging
import threading
import time
import numpy as np
from PIL import ImageEnhance
from PIL import Image as PILImage

class usbCamera:
    abort = False

    def __init__(self, cameraIndex = 0, display_stream = True, frame_name = "Stream"):

        self.vid = cv2.VideoCapture(cameraIndex)

        self.stream_frame_name = frame_name
        self.display_stream = display_stream

        self.brightness = 1.0
        self.contrast = 1.0
        self.saturation = 1.0

        self.thread = threading.Thread(target=self.thread_func)
        self.thread.start()
        self.abort = False
        self.abort_ready = False

    def thread_func(self):
        while not self.abort:
            time.sleep(0.1)
            self.ret, self.orig_frame = self.vid.read()
            if self.display_stream:
                self.frame = self.adjust_image(self.orig_frame)
                cv2.imshow(self.stream_frame_name, self.frame)
                cv2.waitKey(1)
        self.abort_ready = True

    def end(self):
        #self.x.join()
        self.abort = True;
        while not self.abort_ready:
            time.sleep(0.1)
        # Destroy all the windows
        cv2.destroyAllWindows()
        self.vid.release()

    def take_photo(self, display_photo = True, frame_name = "Photo"):
        self.photo = self.frame.copy()
        if display_photo:
            cv2.imshow(frame_name, self.photo)
            cv2.waitKey(1)
        return self.photo

    def display_photo(self, frame_name = "Photo"):
        if self.photo != None:
            cv2.imshow(frame_name, self.photo)
            cv2.waitKey(1)

    def adjust_image(self, img):
        if self.brightness == self.contrast == self.saturation == 1.:
            return img

        im_pil = PILImage.fromarray(img)

        if self.brightness != 1.:
            brightness_filter = ImageEnhance.Brightness(im_pil)
            im_pil = brightness_filter.enhance(self.brightness)

        if self.contrast != 1.:
            contrast_filter = ImageEnhance.Contrast(im_pil)
            im_pil = contrast_filter.enhance(self.contrast)

        if self.saturation != 1.:
            color_filter = ImageEnhance.Color(im_pil)
            im_pil = color_filter.enhance(self.saturation)

        # For reversing the operation:
        im_np = np.asarray(im_pil)
        return im_np

    def set_brightness(self, brightness):
        self._brightness = brightness

    def set_contrast(self, contrast):
        self._contrast = contrast

    def set_saturation(self, saturation):
        self._saturation = saturation