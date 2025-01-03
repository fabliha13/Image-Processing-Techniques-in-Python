# Plot the Image and its histogram + cdf of the grayscale image I_gray

### BEGIN SOLUTION


def plot_image_and_hist_cdf(I_gray, nbins=256, normalize=False):
    plt.figure(figsize=(12, 5))  # Adjust the figure size

    # Plot the grayscale image on the left
    plt.subplot(1, 2, 1)
    plt.imshow(I_gray, cmap='gray')
    plt.title("Grayscale Image")
    plt.axis('off')  # Turn off axis

    # Plot the histogram and CDF on the right
    plt.subplot(1, 2, 2)

    # Calculate the histogram and bin centers
    hist, bins_hist = exposure.histogram(I_gray.ravel(), nbins=nbins, normalize=normalize)

    # Plot histogram
    plt.plot(bins_hist, hist, 'k')  # 'k' for black
    plt.xlabel("Pixel Values")

    if normalize:
        plt.ylabel("Probability")
    else:
        plt.ylabel("Count")

    # Set the x-axis limit based on whether the image is normalized or not
    xmax = 1 if I_gray.max() <= 1 else 255
    plt.xlim([0, xmax])

    # Calculate and plot CDF
    cdf, bins_cdf = exposure.cumulative_distribution(I_gray.ravel(), nbins=nbins)

    plt.twinx()  # Create a secondary y-axis
    plt.plot(bins_cdf, cdf, 'r', lw=3)  # 'r' for red, CDF
    plt.ylabel("CDF (Cumulative Percentage)")

    # Show the combined plots
    plt.tight_layout()
    plt.show()

# Example usage:
plot_image_and_hist_cdf(I_gray)