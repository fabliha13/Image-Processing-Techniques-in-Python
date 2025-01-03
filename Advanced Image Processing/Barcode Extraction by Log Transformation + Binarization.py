import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, exposure, img_as_float
from skimage.filters import threshold_otsu

# Step 1: Load the barcode image
I_barcode = io.imread('Read_the_code.jpg')
I_barcode = img_as_float(I_barcode)  # Convert to float for better processing

# Step 2: Convert to grayscale
I_gray = color.rgb2gray(I_barcode)

# Step 3: Enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
I_clahe = exposure.equalize_adapthist(I_gray, clip_limit=0.03)

# Step 4: Apply log transformation
I_log_transformed = np.log1p(I_clahe)  # log transformation

# Step 5: Apply thresholding (Binarization) using Otsu's method
thresh = threshold_otsu(I_log_transformed)
I_binary = I_log_transformed > thresh  # Convert to binary image (True for white, False for black)
# Otsu's Method:
# Otsu's method automatically determines the optimal threshold value by analyzing the histogram of the grayscale image.
#  It aims to minimize the intra-class variance, which is the variance within each of the two groups (black and white) created by the threshold.

# Step 6: Display the original and processed images
fig, ax = plt.subplots(1, 3, figsize=(20, 10))

# Original image
ax[0].imshow(I_barcode)
ax[0].set_title("Original Barcode Image")
ax[0].axis('off')

# After CLAHE and log transformation
ax[1].imshow(I_log_transformed, cmap='gray')
ax[1].set_title("Log Transformed Image")
ax[1].axis('off')

# Final binary image
ax[2].imshow(I_binary, cmap='gray')
ax[2].set_title("Binarized Image (Thresholding)")
ax[2].axis('off')

plt.tight_layout()
plt.show()

# Step 7: Save the final processed image (optional)
io.imsave('Processed_Barcode.png', I_binary.astype(np.uint8) * 255)
