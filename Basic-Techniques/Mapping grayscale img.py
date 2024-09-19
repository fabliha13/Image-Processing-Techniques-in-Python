# Artificially degrade the **grayscale image** by reducing it contrast
# You can do so by recaling the gray values and concentrating them in a narrow range,
# say between 0.3 and 0.6.
# Save the image as I_degraded and display it
# HINT: SEE lec-4-demo-code
# I_degraded =a+(b−a)×I
I_degraded = 0.3+(0.6-0.3)*I_gray
# Display the degraded image
plt.imshow(I_degraded, cmap='gray')
plt.axis('off')  # Optional: Hide the axis
plt.show()