# File-Processing-code
this folder is showing the process of transforming images into a video

Steps:
1. 所有图片重命名为0001到7000（例子）
2. cmd   cd "D:\labeling & extracting & downloading tools\Noel_useful_script\ffmpeg\bin"
3. get the average size of the images
3. resize the images to be the same
4. ffmpeg -f image2 -i D:\Project_Spoof(Noel)\guy_test\SPOOFDATA\TEST\real\%04d.jpg D:\Project_Spoof(Noel)\guy_test\real.mp4
