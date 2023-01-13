import numpy as np
import cv2
import pickle

# Load previously saved data
calib_result_pickle = pickle.load(open("../camera_calib_pickle.p", "rb"))
mtx = calib_result_pickle["mtx"]
omatrix = calib_result_pickle["optimal_camera_matrix"]
dist = calib_result_pickle["dist"]


def draw(img, corners, imgpts):
    imgpts = np.int32(imgpts).reshape(-1,2)
    # draw ground floor in green
    img = cv2.drawContours(img, [imgpts[:4]],-1,(0,255,0),-3)
    # draw pillars in blue color
    for i,j in zip(range(4),range(4,8)):
        img = cv2.line(img, tuple(imgpts[i]), tuple(imgpts[j]),(255),3)
    # draw top layer in red color
    img = cv2.drawContours(img, [imgpts[4:]],-1,(0,0,255),3)
    return img


filename = '3dcube.jpg'

number_of_squares_X = 10  # Number of chessboard squares along the x-axis
number_of_squares_Y = 7  # Number of chessboard squares along the y-axis
nX = number_of_squares_X - 1  # Number of interior corners along x-axis
nY = number_of_squares_Y - 1  # Number of interior corners along y-axis
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
objp = np.zeros((6*9,3), np.float32)
objp[:,:2] = np.mgrid[0:6,0:9].T.reshape(-1,2)
axis1 = np.float32([[0,0,0], [0,3,0], [3,3,0], [3,0,0],
                   [0,0,-3],[0,3,-3],[3,3,-3],[3,0,-3] ])
axis = np.float32([[0,0,0], [0,1,0], [1,1,0], [1,0,0],
                   [0,0,-1],[0,1,-1],[1,1,-1],[1,0,-1] ])

def main():


    # Load an image
    image = cv2.imread(filename)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find the corners on the chessboard
    success, corners = cv2.findChessboardCorners(gray, (nY, nX), None)
    testimg = cv2.drawChessboardCorners(image, (nY, nX), corners, success)

    if success == True:
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1), criteria)
        # Find the rotation and translation vectors.
        ret ,rvecs, tvecs = cv2.solvePnP(objp, corners2, mtx, dist, flags=0)
        # project 3D points to image plane
        imgpts, jac = cv2.projectPoints(axis1, rvecs, tvecs, mtx, dist)
        image = draw(testimg, corners2, imgpts)
        cv2.imshow('img',image)
        cv2.waitKey(100000)
cv2.destroyAllWindows()


main()