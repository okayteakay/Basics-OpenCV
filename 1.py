

# import cv2
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read()
#     cv2.imshow('frame', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()

import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# output = cv2.VideoWriter('Output1.avi', fourcc, 25.0, (640,480))
while True:
    ret, frame = cap.read()
    if ret == True:
        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # output.write(frame)
        cv2.imshow('frame',grey)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
output.release()
cv2.destroyAllWindows()