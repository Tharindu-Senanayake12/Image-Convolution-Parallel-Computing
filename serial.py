import cv2
import numpy as np
import time

BLUR_KERNEL = np.ones((7, 7), dtype=np.float32) / 49.0

def pad_image(img, pad, mode="reflect"):
    return np.pad(img, ((pad, pad), (pad, pad), (0, 0)), mode=mode)

def convolve_patch(src, kernel, x, y):
    h_k, w_k = kernel.shape
    half = h_k // 2
    patch = src[y - half : y + half + 1, x - half : x + half + 1]
    return np.tensordot(kernel, patch, axes=([0, 1], [0, 1]))

def serial_blur(img):
    h, w = img.shape[:2]
    kernel = BLUR_KERNEL
    pad = kernel.shape[0] // 2

    src = pad_image(img, pad)
    dst = np.zeros_like(img, dtype=np.float32)

    start_time = time.time()
    for y in range(pad, pad + h):
        for x in range(pad, pad + w):
            dst[y - pad, x - pad] = convolve_patch(src, kernel, x, y)
    end_time = time.time()

    duration = end_time - start_time
    print(f"Serial blur completed in {duration:.4f} seconds")
    return np.clip(dst, 0, 255).astype(np.uint8)

def main():
    img = cv2.imread("sample.jpg")
    if img is None:
        print("Image not found")
        return

    print(f"Input image shape: {img.shape}, dtype: {img.dtype}")
    img = img.astype(np.float32)

    out = serial_blur(img)

    cv2.imwrite("output_blur_serial.png", out)
    print(f"Output image saved: output_blur_serial.png")
    print(f"Kernel used: {BLUR_KERNEL.shape}, sum={BLUR_KERNEL.sum():.2f}")

if __name__ == "__main__":
    main()



