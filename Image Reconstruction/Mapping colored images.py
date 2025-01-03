# Artificially degrade the original **RGB image** by reducing it contrast
# You can do so by recaling the values of the L channel (in LAB color space)
# and concentrating them in a narrow range, say between 0.3 and 0.6.
# Save the image as I_rgb_degraded and display it


# Load the original RGB image
I_rgb = io.imread("/content/sample.jpeg")

# Convert the RGB image to LAB color space
I_lab = color.rgb2lab(I_rgb)

# Extract the L channel (lightness)
L_channel = I_lab[:, :, 0]

# Normalize the L channel to the range [0, 1]
L_normalized = (L_channel - np.min(L_channel)) / (np.max(L_channel) - np.min(L_channel))

# Rescale the L channel to a narrow range between 0.3 and 0.6 to reduce contrast
L_degraded = 0.3 + L_normalized * 0.3  # This will map values to the range [0.3, 0.6]

# Denormalize the L channel back to the original scale [0, 100]
L_degraded_denorm = L_degraded * 100

# Replace the degraded L channel back in the LAB image
I_lab[:, :, 0] = L_degraded_denorm

# Convert the degraded LAB image back to RGB
I_rgb_degraded = color.lab2rgb(I_lab)

# Display the original and degraded images side by side
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# Display original image
ax[0].imshow(I_rgb)
ax[0].set_title('Original Image')
ax[0].axis('off')

# Display degraded image
ax[1].imshow(I_rgb_degraded)
ax[1].set_title('Degraded Image (Low Contrast)')
ax[1].axis('off')

# Save the degraded image
io.imsave('I_rgb_degraded.png', (I_rgb_degraded * 255).astype(np.uint8))  # Saving as PNG

plt.tight_layout()
plt.show()
