import cv2
import mss
import numpy


with mss.mss() as sct:
    monitor = {"top": 40, "left": 22, "width": 640, "height": 360}

    def perspective_transform(img):
        imshape = img.shape
        #print (imshape)
        vertices = numpy.array([[(.55*imshape[1], 0.63*imshape[0]), (imshape[1],imshape[0]),
                           (0,imshape[0]),(.45*imshape[1], 0.63*imshape[0])]], dtype=numpy.float32)
        #print (vertices)
        src= numpy.float32(vertices)
        dst = numpy.float32([[0.75*img.shape[1],0],[0.75*img.shape[1],img.shape[0]],
                          [0.25*img.shape[1],img.shape[0]],[0.25*img.shape[1],0]])
        #print (dst)
        M = cv2.getPerspectiveTransform(src, dst)

        Minv = cv2.getPerspectiveTransform(dst, src)
        img_size = (imshape[1], imshape[0])
        perspective_img = cv2.warpPerspective(img, M, img_size, flags = cv2.INTER_LINEAR)
        return perspective_img

    while 1:
        img = numpy.array(sct.grab(monitor))
        roi = img[200:340, 0:610]
        #edges = cv2.Canny(roi, 75, 150)
        #lines = cv2.HoughLinesP(edges, 1, numpy.pi/180, 30, maxLineGap=250)

        #for line in lines:
        #    x1, y1, x2, y2 = line[0]
        #    cv2.line(img, (x1, y1 + 200), (x2, y2 + 200), (0, 0, 255), 5)

        #cv2.imshow("Edges", edges)
        cv2.imshow("abc", perspective_transform(img))
        #cv2.imshow("roi", roi)
        #cv2.imshow("Image", img)
        # Display the picture


        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
