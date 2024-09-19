# Load the image I
I = io.imread('/content/Dark_Room.jpg')  # Replace with your image file path

# Convert the image to float (range 0 to 1)
I_float = img_as_float(I)

# Apply log transformation
c = 0.5 # Scaling constant
I_log = c * np.log(1 + I_float)

# Normalize the result back to range [0, 1]
I_log_normalized = (I_log - np.min(I_log)) / (np.max(I_log) - np.min(I_log))


#Applying CLAHE
I_enhanced = exposure.equalize_adapthist(I_log_normalized, clip_limit=0.03)


# Display the original and log-transformed images
fig, ax = plt.subplots(1, 3, figsize=(12, 4))


# Original image
ax[0].imshow(I)
ax[0].set_title('Original Image')
ax[0].axis('off')

# Log-transformed image
ax[1].imshow(I_log_normalized, cmap='gray')
ax[1].set_title('Log Transformed Image')
ax[1].axis('off')

# Display the enhanced image
ax[2].imshow(I_enhanced)
ax[2].set_title('Enhanced Dark Room Image')
ax[2].axis('off')


plt.tight_layout()
plt.show()
