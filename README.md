Here is a clean and professional GitHub README tailored for your **Parallel Image Convolution / Filtering** project.
It avoids em dashes as you requested.

---

# **Parallel Image Convolution and Filtering**

This project implements image convolution using both serial and parallel approaches to demonstrate performance improvement through parallel computing techniques. The focus is on applying common image filters while comparing execution time between normal CPU processing and parallel processing using multiple cores.

---

## **Project Overview**

Image convolution is a fundamental operation in image processing. It is used for blurring, sharpening, edge detection, smoothing, and many other transformations.
This project applies convolution kernels to an input image and evaluates the performance of parallel execution compared to a serial baseline.

The project contains the following:

* Serial image convolution
* Parallel convolution using Python multiprocessing
* Adjustable kernel sizes and intensity
* CLI support for experiments
* Execution time measurement
* Side by side output comparison

---

## **Features**

* Multiple built in kernels

  * Blur
  * Sharpen
  * Edge detection
  * Custom kernels
* Parallel convolution using process based parallelism
* Ability to change blur intensity by adjusting kernel size
* Clean and modular code structure
* Automatic image chunk splitting for workers
* Support for large images
* CLI arguments for easy testing

---

## **Technologies Used**

* Python
* OpenCV (cv2) for image loading and saving
* NumPy for matrix calculations
* Multiprocessing module for parallelism
* Time measurement for benchmarking

---
