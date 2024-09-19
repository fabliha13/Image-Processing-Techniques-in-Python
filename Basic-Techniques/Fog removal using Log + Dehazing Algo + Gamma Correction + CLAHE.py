import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, exposure, img_as_float

# Step 1: Load the foggy road image using scikit-image
I_foggy_road = io.imread('Foggy_Road.jpg')
I_foggy_road = img_as_float(I_foggy_road)  # Convert to float for processing

# Step 2: Apply Log Transformation
c = 1  # Scaling constant
log_image = c * np.log1p(I_foggy_road)  # Using np.log1p for numerical stability
# Normalize to 0-1 range
I_log_transformed = (log_image - log_image.min()) / (log_image.max() - log_image.min())

# Step 3: Apply Dehazing
# Convert to LAB color space using scikit-image
I_lab = color.rgb2lab(I_foggy_road)

# Extract the L (lightness) channel
L_channel = I_lab[:, :, 0]

# Dehaze by normalizing the L channel to a wider range (for simplicity)
L_channel_dehazed = (L_channel - L_channel.min()) / (L_channel.max() - L_channel.min()) * 100

# Replace the L channel in the LAB image
I_lab_dehazed = I_lab.copy()
I_lab_dehazed[:, :, 0] = L_channel_dehazed

# Convert back to RGB
I_dehazed = color.lab2rgb(I_lab_dehazed)

# Step 4: Apply Gamma Correction using scikit-image
gamma = 3  # A gamma value > 1 clears the bright part of image
I_gamma_corrected = exposure.adjust_gamma(I_dehazed, gamma=gamma)

# Step 5: Apply CLAHE to the L channel of the dehazed + gamma-corrected image
I_lab_gamma_corrected = color.rgb2lab(I_gamma_corrected)
L_channel = I_lab_gamma_corrected[:, :, 0]

# Apply CLAHE to the L channel (contrast limited adaptive histogram equalization)
L_channel_clahe = exposure.equalize_adapthist(L_channel / 100) * 100  # CLAHE normalizes to [0,1], so we scale it back

# Replace the L channel in the LAB image
I_lab_clahe = I_lab_gamma_corrected.copy()
I_lab_clahe[:, :, 0] = L_channel_clahe

# Convert back to RGB
I_clahe_final = color.lab2rgb(I_lab_clahe)

#contrast_stretching
# Calculate min and max values in the image
min_val = I_foggy_road.min()
max_val = I_foggy_road.max()

# Apply contrast stretching
stretched = (I_foggy_road - min_val) / (max_val - min_val)

# Step 6: Plot the original and enhanced images at each stage
plt.figure(figsize=(16, 6))

# Original Image
plt.subplot(2, 3, 1)
plt.imshow(I_foggy_road)
plt.title('Original Foggy Image')
plt.axis('off')

# Log Transformed Image
plt.subplot(2, 3, 2)
plt.imshow(I_log_transformed)
plt.title('Log Transformed Image')
plt.axis('off')

# Dehazed Image
plt.subplot(2, 3, 3)
plt.imshow(I_dehazed)
plt.title('Dehazed Image')
plt.axis('off')

# Gamma Corrected Image
plt.subplot(2, 3, 4)
plt.imshow(I_gamma_corrected)
plt.title('Gamma Corrected Image')
plt.axis('off')

# CLAHE Applied Image
plt.subplot(2, 3, 5)
plt.imshow(I_clahe_final)
plt.title('CLAHE Applied Image')
plt.axis('off')

# Conntrast Stretched Image
plt.subplot(2, 3, 6)
plt.imshow(stretched)
plt.title('Conntrast Stretched Image')
plt.axis('off')

plt.tight_layout()
plt.show()
