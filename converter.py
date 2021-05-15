import subprocess
import cv2
import os

# this class converts a .webm file into .mp4 files and then into frames

input_name = r'C:\Users\numal\Lab3\replayApi\Recordings\replay1.webm'
output_name = r'C:\Users\numal\Lab3\replayApi\mp4vids\replay1.mp4'


class Converter:
    def convert_webm_to_mp4_subprocess(self, input, output):
        try:
            command = 'ffmpeg -i' + ' ' + input + ' ' + output
            subprocess.run((command))
        except:
            print('Some Exception')

    def convert_webm_to_mp4_module(self):
        pass


Converter().convert_webm_to_mp4_subprocess(input_name, output_name)

cam = cv2.VideoCapture(output_name)

print('Starting')

# we should change the frame rate to optimize the process
# actual frame rate = 20fps

try:
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')

# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

# frame
currentframe = 0

while(True):

    # reading from frame
    ret, frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print('Creating...' + name)

        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()

# sth
