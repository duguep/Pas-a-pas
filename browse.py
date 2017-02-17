#!/usr/bin/env python
import cv2
import os.path
import selection
import playing
import button
import RPi.GPIO as GPIO
import shutil
# Activates the different GPIO inputs that will be used here

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def browse_mode():
    cartoon_selector = -1
    cartoon = []
    cartoon_cursor = 1

    cartoons_number = selection.count_files("/media/pi/PAP/cartoons/")
    c_path = "/media/pi/PAP/cartoons/pap_"

    # if no USB key named PAP containing cartoons is found, displays an error and returns.
    # This will crash if it contains images that are not names pap_x and are not 1280 / 1024 size.
    if not os.path.exists("/media/pi/PAP/cartoons/"):
        cv2.imshow("window", cv2.imread("./load_failed.png"))
        cv2.waitKey(0)
        return

    while (len(cartoon) == 0):
        cartoons_number = selection.count_files("/media/pi/PAP/cartoons/")
        cv2.imshow("window", cv2.imread("background2.png"))
        cv2.waitKey(10)
        
        # builds and displays the image containing thumbnails of the cartoons
	print (cartoons_number)
        selection.build_selection(cartoon_selector, c_path, cartoons_number)
        cv2.waitKey(10)
        button_value = button.waitpressedbutton("browse")

        if (button_value == "mode"):  # the mode is no longer browse, so we return to go to the right mode
            return
        if (button_value == "next"): # sets the cursor to the next cartoon
            cartoon_selector += 1
        elif (button_value == "prev"): # sets the cursor to the previous cartoo
            cartoon_selector -= 1
        elif (button_value == "delete"):
            if ((cartoon_selector % cartoons_number + 1) == cartoons_number):
                ani_supp = cv2.imread("ani_supp.png", 1)
                cv2.imshow("window", ani_supp)
                cv2.waitKey(10)
                shutil.rmtree(c_path + str(cartoon_selector % cartoons_number + 1))
        elif (button_value == "play"): # plays the cartoon
            if ((cartoon_selector % cartoons_number + 1) <= 99):
                num = cv2.imread("/home/pi/Pas_a_pas/img/num/num" + str(cartoon_selector % cartoons_number + 1) + ".png", 1)
                cv2.imshow("window", num)
                cv2.waitKey(10)
            cartoon = playing.load_selected(c_path + str(cartoon_selector % cartoons_number + 1) + "/")
            cartoon_selector = playing.play_other(cartoon, cartoon_selector)
