import cv2

# ids = []
# for id in range(0,20):
#     capid=cv2.VideoCapture(id, cv2.CAP_DSHOW)
#     if capid.isOpened():
#         ids.append(id)
#         print(f'Video capture{id}:found')
#     else:
#         print(f'Video capture{id}:None')
#     capid.release()

cap_ther1= cv2.VideoCapture(5,cv2.CAP_DSHOW)
cap_rgb1 = cv2.VideoCapture(2, cv2.CAP_DSHOW)
cap_ther2= cv2.VideoCapture(3,cv2.CAP_DSHOW)
cap_rgb2 = cv2.VideoCapture(4, cv2.CAP_DSHOW)
flag1 = True
print(cap_ther1)
print(cap_rgb1)
print(cap_ther2)
print(cap_rgb2)

while flag1:
    result_ther1, frame_ther1 = cap_ther1.read()
    result_rgb1, frame_rgb1 = cap_rgb1.read()
    result_ther2, frame_ther2 = cap_ther2.read()
    result_rgb2, frame_rgb2 = cap_rgb2.read()

    # if not result_rgb2:
        # print('miss load')
        # break

    cv2.imshow('THERMAL1', frame_ther1)
    cv2.imshow('RGB1', frame_rgb1)
    cv2.imshow('THERMAL2', frame_ther2)
    cv2.imshow('RGB2', frame_rgb2)
    key1 = cv2.waitKey(1)
    if (key1 == 13) or (key1 == 113):
        break
cap_ther1.release()
cap_rgb1.release()
cap_ther2.release()
cap_rgb2.release()
cv2.destroyAllWindows()