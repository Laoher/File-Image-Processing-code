# File-Processing-code
This readme is showing the process of transforming images into a video

Steps:
1. 所有图片添零补位， 比如1-7000重命名为0001到7000
2. get the average size of the images
3. resize the images to be the same
4. In cmd, open path of ffmpeg.exe :  cd "D:\labeling & extracting & downloading tools\Noel_useful_script\ffmpeg\bin"
5. use command of 
   ffmpeg -f image2 -i D:\Project_Spoof(Noel)\guy_test\SPOOFDATA\TEST\real\%04d.jpg D:\Project_Spoof(Noel)\guy_test\real.mp4
