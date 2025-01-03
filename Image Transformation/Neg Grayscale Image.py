# Display the negative of the grayscale image

I_negative = 1 - I_gray

#Display the negative image
plt.imshow(I_negative, cmap='gray')
plt.axis('off')  # Optional: Hide the axis
plt.show()