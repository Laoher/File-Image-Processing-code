import os

os.chdir(r'D:\Project_Spoof(Noel)\guy_test\SPOOFDATA\TEST\real')
print(os.getcwd())
count = 0
for file in os.listdir("."):
    if file.endswith(".jpg") or file.endswith(".png"):
        os.rename(file, str(count) + ".jpg")
        count = count + 1
max_digit = len(str(count))
for file in os.listdir("."):
    if file.endswith(".jpg"):
        miss =max_digit - len(file[:-4])
        os.rename(file, "0"*miss+file)
