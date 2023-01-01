# Importing all necessary libraries
import cv2
import os


# ======================================
# declare variables
framerate = 0  # frame rate
currentframe = 0  # current frame value
imagecount = 0  # image count
video = "trax1_FSL_EO_image_rect.mp4"


# read the video
cam = cv2.VideoCapture(video)

# obtain framerate of video
framerate = cam.get(cv2.CAP_PROP_FPS)

try:
    # creating a folder to store images
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created raise error
except OSError:
    print('Error: Something happened when creating directory for data')


# cycle through the video
while(True):

    # reading the frame
    ret, frame = cam.read()

    # if frame exists create image
    if ret:
        # want the first frame of every second so use % framerate
        if(currentframe % framerate == 0):
            # name the videos based off of # of second in video (currentframe/framerate)
            name = './data/frame' + str(currentframe/framerate) + '.jpg'
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            imagecount += 1
        currentframe += 1
    else:
        print(imagecount + " images created...")
        break

# # Release all space and windows once done
cam.release()
# cv2.destroyAllWindows()
