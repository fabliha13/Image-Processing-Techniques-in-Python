# Multiply the three channels of image I with three DIFFERENT numbers between 0.3 and 3
# Save the resulting image in I_tint and display it.
# The resulting image should have some color shift
I_tint = np.zeros(I.shape)
# Apply the tint factors to each channel (R, G, B)
I_tint[:, :, 0] = np.clip(I[:, :, 0] * 0.3, 0, 1)  # Red channel
I_tint[:, :, 1] = np.clip(I[:, :, 1] * 1.2, 0, 1)  # Green channel
I_tint[:, :, 2] = np.clip(I[:, :, 2] * 3, 0, 1)  # Blue channel

# Step 5: Display the tinted image
plt.imshow(I_tint)
plt.axis('off')  # Optional: Hide the axis
plt.show()