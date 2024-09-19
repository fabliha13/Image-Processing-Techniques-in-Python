# Convert the image into a grayscale image.
# Save it to I_gray and display it
I_gray = color.rgb2gray(I)

# Display the grayscale image
plt.imshow(I_gray, cmap='gray')
plt.axis('off')  # Optional: Hide the axis
plt.show()