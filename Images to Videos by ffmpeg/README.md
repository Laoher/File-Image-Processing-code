# File-Processing-code
This readme is showing the process of transforming images into a video

Steps:
1. Make image names sequential numbers of same length， like change 1-7000 to 0001-7000
2. Get the average size of the images
3. Resize the images to be the same
4. In cmd, open path of ffmpeg.exe :  cd "D:\labeling & extracting & downloading tools\Noel_useful_script\ffmpeg\bin"
5. Key in command of 
   ffmpeg -f image2 -i D:\Project_Spoof(Noel)\guy_test\SPOOFDATA\TEST\real\%04d.jpg D:\Project_Spoof(Noel)\guy_test\real.mp4
