# **Parallel Image Convolution and Filtering**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

This project demonstrates how image convolution can be accelerated using parallel computing. It applies common image filters using both serial and parallel approaches, then compares execution time to evaluate performance improvements.

---

## **Project Overview**

Image convolution is widely used in image processing tasks such as blurring, sharpening, edge detection, and smoothing.
This project applies convolution kernels to an input image and measures the speed difference between normal CPU processing and multiprocessing based parallel execution.

The system includes:

* Serial convolution implementation
* Parallel convolution using Python multiprocessing
* Adjustable kernel sizes and filter intensity
* Command line usage for quick testing
* Execution time reporting
* Side by side output comparison

---

## **Features**

* Built in filters

  * Blur
  * Sharpen
  * Edge detection
  * Custom kernels
* Parallel processing using multiple CPU cores
* Adjustable blur strength through kernel size
* Modular and organized codebase
* Automatic image chunk distribution across workers
* Can process large images
* Simple command line interface

---

## **Technologies Used**

* Python
* OpenCV (cv2) for loading and saving images
* NumPy for matrix operations
* Multiprocessing module for parallelism
* Time module for benchmarking

---

## **How the Parallel Approach Works**

1. The image is split into equal row based chunks
2. Each worker process receives a section of the image
3. Convolution is applied independently in each worker
4. Processed chunks are combined into the final image
5. Parallel execution reduces the overall computation time

This approach scales automatically with image size and number of workers.

---

## **Performance Evaluation**

The program displays execution time for both serial and parallel modes.
By experimenting with different configurations, you can analyze:

* Speedup achieved
* Processing efficiency
* Effect of kernel size
* Effect of number of workers
* Influence of image size

These insights help understand the practical benefits of parallel computing.

---

## **Code Architecture**

* **read_image**
  Loads the input image
* **generate_kernel**
  Creates blur, sharpen, and edge detection kernels
* **convolve_serial**
  Performs convolution on a single CPU core
* **convolve_parallel**
  Splits the workload and runs convolution in parallel
* **merge_results**
  Combines processed chunks
* **main**
  Handles arguments and manages workflow

---

## **Usage**

### **1. Install Dependencies**

```
pip install numpy opencv-python
```

### **2. Run Serial Convolution**

```
python parallel_convolution.py --input sample.jpg --kernel blur --mode serial
```

### **3. Run Parallel Convolution**

```
python parallel_convolution.py --input sample.jpg --kernel blur --mode parallel --workers 4
```

### **4. Increase Blur Intensity**

Example with an 11 by 11 blur kernel:

```
python parallel_convolution.py --input sample.jpg --kernel blur --kernel-size 11 --mode parallel
```

---

## **Outputs**

The program generates:

* A serially processed output image
* A parallel processed output image
* Execution time for each mode

These outputs make comparisons easy and clear.

---