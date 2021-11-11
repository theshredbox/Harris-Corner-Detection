# Harris-Corner-Detection
The Harris corner detection algorithm also called the Harris & Stephens corner detector is one of the simplest corner detectors available. The idea is to locate interest points where the surrounding neighbourhood shows edges in more than one direction. 
The basic idea of algorithm is to find the difference in intensity for a displacement of (u,v) in all directions.

<p align= "center">
<img src="https://muthu.co/wp-content/uploads/2018/09/Snip20180930_25.png">
</p>

OpenCV has the function cv2.cornerHarris() for this purpose. Its arguments are :

* img - Input image, it should be grayscale and float32 type.
* blockSize - It is the size of neighbourhood considered for corner detection
* ksize - Aperture parameter of Sobel derivative used.
* k - Harris detector free parameter in the equation.

