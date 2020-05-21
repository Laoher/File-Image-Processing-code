import os
import cv2

# Take the bottom and top parts and save them into the same folder
def half_crop(path_list, iftop=1, ifbottom=1):
    for i in path_list:
        os.chdir(i)
        print(os.getcwd())
        for file in os.listdir("."):
            if file.endswith(".jpg"):
                img = cv2.imread(file)
                print(img)
                if img is not None:
                    height, width, channels = img.shape
                    if iftop is 1:
                        top = img[:int(height / 2), :]
                        cv2.imwrite(os.path.join(i, file[:-4] + '_top' + '.jpg'), top)
                        print(type(top))
                    if ifbottom is 1:
                        bottom = img[int(height / 2):, :]
                        cv2.imwrite(os.path.join(i, file[:-4] + '_bottom' + '.jpg'), bottom)
                        print(type(bottom))


path_list = [r'D:\Project_SATS (Yu Han)\classes_door\Open', r'D:\Project_SATS (Yu Han)\classes_door\Close']
half_crop(path_list, 1, 1)
