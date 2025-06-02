import numpy as np

def compute_integral_image(img):
    h, w = img.shape
    integral = np.zeros((h + 1, w + 1), dtype=np.int64)
    integral[1:, 1:] = np.cumsum(np.cumsum(img, axis=0), axis=1)
    return integral