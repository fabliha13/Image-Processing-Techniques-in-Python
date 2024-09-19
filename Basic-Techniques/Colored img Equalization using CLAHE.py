# Equalize the histogram of the degraded image I_degraded using CLAHE
# Save the result in I_recon_gray_3, display the image along with its histogram

##Method 1
I_recon_gray_3 = exposure.equalize_adapthist(I_degraded, clip_limit=0.03)

# Set figure size for the plots
fig, ax = plt.subplots(1, 2, figsize=(12, 5))  # Two subplots side by side

# Plot the equalized image (AHE result)
ax[0].imshow(I_recon_gray_3)
ax[0].set_title('Equalized Image using CLAHE')
ax[0].axis('off')

# Plot the histogram of the equalized image (AHE result)
r, g, b = I_recon_gray_3[:, :, 0], I_recon_gray_3[:, :, 1], I_recon_gray_3[:, :, 2]
ax[1].hist(r.ravel(), bins=256, color='red', alpha=0.5, label='Red channel')
ax[1].hist(g.ravel(), bins=256, color='green', alpha=0.5, label='Green channel')
ax[1].hist(b.ravel(), bins=256, color='blue', alpha=0.5, label='Blue channel')
ax[1].legend()
ax[1].set_title('Equalized Histogram using CLAHE')

# Display the plots
plt.tight_layout()
plt.show()

##Method 2
# Convert the RGB image to LAB color space
I_lab = color.rgb2lab(I_degraded)

# Extract the L channel
L_channel = I_lab[:, :, 0]

# Normalize the L channel to range [0, 1] (necessary for CLAHE)
L_normalized = (L_channel - np.min(L_channel)) / (np.max(L_channel) - np.min(L_channel))

# Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to the L channel
L_clahe = exposure.equalize_adapthist(L_normalized, clip_limit=0.03)

# Denormalize the L channel back to the original scale [0, 100]
L_clahe_denorm = L_clahe * 100

# Update the L channel in the LAB image
I_lab[:, :, 0] = L_clahe_denorm

# Convert the LAB image back to RGB
I_recon_gray_3 = color.lab2rgb(I_lab)

# Display the CLAHE equalized image and its histogram
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Plot the CLAHE equalized image
ax[0].imshow(I_recon_gray_3)
ax[0].set_title('CLAHE Equalized Image')
ax[0].axis('off')

# Plot histograms of each channel
r, g, b =I_recon_gray_3[:, :, 0], I_recon_gray_3[:, :, 1], I_recon_gray_3[:, :, 2]
ax[1].hist(r.ravel(), bins=256, color='red', alpha=0.5, label='Red channel')
ax[1].hist(g.ravel(), bins=256, color='green', alpha=0.5, label='Green channel')
ax[1].hist(b.ravel(), bins=256, color='blue', alpha=0.5, label='Blue channel')
ax[1].legend()
ax[1].set_title('Equalized Histogram')

plt.tight_layout()
plt.show()

### END SOLUTION