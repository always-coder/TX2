import cv2

def open_board_camera(width, height):
    
    gst_str = ('nvcamerasrc ! '
    	       'video/x-raw(memory:NVMM), '
	       'width=(int)2592, height=(int)1458, '
	       'format=(string)I420, framerate=(fraction)30/1 ! '
	       'nvvidconv ! '
	       'video/x-raw, width=(int){}, height=(int){}, '
	       'format=(string)BGRx ! '
	       'videoconvert ! appsink').format(width, height)
    
    cap =  cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
    return cap;

def read_camera(capture):
    while True:
        image = capture.read()
        cv2.imshow(WINDOWS_NAME, image)
        key = cv2.waitKey(10)
        if key == 27:
            break;
    
def main()
    capture = open_board_camera(640, 480)
    read_camera(capture)

    captrue.release()
    cv2.destroyAllWindows()

if __name__ == "__main"
    main()
