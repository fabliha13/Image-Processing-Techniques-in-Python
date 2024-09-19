# Equalize the histogram of the degraded image I_degraded
# Save the result in I_recon_gray, display the image along with its histogram

## Method 1:
# Separating the image into its three channels
r, g, b = I_degraded[:,:,0], I_degraded[:,:,1], I_degraded[:,:,2]

# Applying histogram equalization to each channel
r_equalized = exposure.equalize_hist(r)
g_equalized = exposure.equalize_hist(g)
b_equalized = exposure.equalize_hist(b)

# Combining the equalized channels back into a single image
I_recon_gray = np.stack((r_equalized, g_equalized, b_equalized), axis=-1)

# Set figure size for the plots
fig, ax = plt.subplots(1, 2, figsize=(12, 5))  # Two subplots side by side

# Plot the equalized image
ax[0].imshow(I_recon_gray)
ax[0].set_title('Equalized Image')
ax[0].axis('off')

# Plot histograms of each channel
ax[1].hist(r_equalized.ravel(), bins=256, color='red', alpha=0.5, label='Red channel')
ax[1].hist(g_equalized.ravel(), bins=256, color='green', alpha=0.5, label='Green channel')
ax[1].hist(b_equalized.ravel(), bins=256, color='blue', alpha=0.5, label='Blue channel')
ax[1].legend()
ax[1].set_title('Equalized Histogram')

# Show the plots
plt.tight_layout()
plt.show()

## Method 1:
# Convert the RGB image to LAB color space
I_lab = color.rgb2lab(I_degraded)

# Extract the L channel
L_channel = I_lab[:, :, 0]

# Normalize the L channel to range [0, 1]
L_normalized = L_channel / np.max(L_channel)

# Apply histogram equalization to the L channel
L_equalized = exposure.equalize_hist(L_normalized)

# Denormalize the L channel back to the original scale [0, 100]
L_equalized_denorm = L_equalized * 100

# Update the L channel in the LAB image
I_lab[:, :, 0] = L_equalized_denorm

# Convert the LAB image back to RGB
I_rgb_equalized = color.lab2rgb(I_lab)

# Display the equalized image and its histogram
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Plot the equalized image
ax[0].imshow(I_rgb_equalized)
ax[0].set_title('Equalized Image')
ax[0].axis('off')

# Plot histograms of each channel
r, g, b = I_rgb_equalized[:, :, 0], I_rgb_equalized[:, :, 1], I_rgb_equalized[:, :, 2]
ax[1].hist(r.ravel(), bins=256, color='red', alpha=0.5, label='Red channel')
ax[1].hist(g.ravel(), bins=256, color='green', alpha=0.5, label='Green channel')
ax[1].hist(b.ravel(), bins=256, color='blue', alpha=0.5, label='Blue channel')
ax[1].legend()
ax[1].set_title('Equalized Histogram')

plt.tight_layout()
plt.show()