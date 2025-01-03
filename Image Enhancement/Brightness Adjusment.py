# Increase the brightness of the image without changing the contrast.
# Save the resulting image in I_bright and display it.
I_bright = np.clip(I + 0.5, 0, 1)

# Display the brightened image
plt.imshow(I_bright, cmap='gray')
plt.axis('off')  # Optional: Hide axis
plt.show()

# Decrease the brightness of the image without changing the contrast.
# Save the resulting image in I_dark and display it.
I_dark = np.clip(I - 0.5, 0, 1)

#Display the darkened image
plt.imshow(I_dark, cmap='gray')
plt.axis('off')  # Optional: Hide the axis
plt.show()
