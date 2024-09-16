# Image-Processing-Techniques-in-Python
Welcome to **Image Processing and Enhancement in Python**, a comprehensive repository demonstrating a wide range of image manipulation techniques. This project includes practical implementations, making it a valuable resource for students, professionals, and researchers interested in digital image processing.

## 📋 Table of Contents

1. **Basic Image Operations**
2. **Image Transformations**
3. **Image Enhancement Techniques**
4. **Advanced Image Processing**
5. **Histogram Analysis**
6. **Binarization**
7. **Color Adjustments**
8. **Artificial Image Degradation**
9. **Image Reconstruction**
10. **Other Techniques**

## 1. Basic Image Operations

- **Reading an Image**: Loading images using libraries like scikit-image.
- **Finding Image Width and Height**: Extracting image dimensions (width and height).
- **Normalizing the Image**: Scaling pixel values between 0 and 1 or 0 and 255.
- **Clipping Pixel Values**: Restricting pixel values to a specific range (e.g., 0 to 1).
- **Brightness Increase/Decrease**: Modifying image brightness by adding/subtracting a constant value to pixel intensities.
- **Color Shifting**: Multiplying all image channels by a factor to alter color balance.

## 2. Image Transformations

- **Convert to Grayscale**: Converting RGB images to grayscale by averaging or using weighted sums.
- **Negative Image Transformation**: Inverting pixel values to create a negative image effect.
- **Image Degradation**: Artificially reducing image quality by decreasing contrast or adding noise.

## 3. Image Enhancement Techniques

- **Piecewise Linear Contrast Stretching**: Enhancing contrast by mapping pixel intensities to a new range.
- **Histogram Equalization**: Applied to both grayscale and color images (using individual channels). Enhancing contrast by redistributing pixel intensities.
- **Adaptive Histogram Equalization (AHE)**: Applying AHE for localized contrast enhancement in grayscale and color images.
- **Contrast Limited Adaptive Histogram Equalization (CLAHE)**: Enhanced contrast with limitation to prevent noise amplification in both grayscale and color images.

## 4. Advanced Image Processing

- **LAB Color Space Conversion**: Converting images from RGB to LAB color space and back. Extracting the L channel (lightness) for manipulation.
- **Logarithmic Transformation**: Applying log transformation to enhance the visibility of darker regions.
- **Gamma Correction**: Adjusting image brightness and contrast using gamma correction.
- **Dehazing**: Enhancing low-contrast (foggy) images by normalizing and stretching the L channel in LAB color space.

## 5. Histogram Analysis

- **Plotting Histogram**: Displaying the distribution of pixel intensities for both grayscale and color channels.
- **Cumulative Distribution Function (CDF) Plotting**: Visualizing the CDF of an image, essential for understanding histogram equalization.

## 6. Binarization

- **Thresholding**: Converting images to binary (black and white) using techniques like Otsu’s method for separating foreground and background.

## 7. Color Adjustments

- **Color Shift**: Altering colors by multiplying image channels by specific factors.
- **Brightness Adjustments**: Increasing or decreasing brightness by adding/subtracting pixel values.

## 8. Artificial Image Degradation

- **Contrast Reduction**: Degrading contrast by scaling the L channel in LAB color space to a narrow range (e.g., between 0.3 and 0.6).

## 9. Image Reconstruction

- **Reconstructing LAB Images**: After manipulating the L channel, reassembling the LAB image and converting it back to RGB.

## 10. Other Techniques

- **Negative Image Creation**: Inverting pixel values to create a negative.
- **Log Transformation for Image Enhancement**: Improving dark areas by applying logarithmic transformations.
- **Contrast Stretching for Foggy Images**: Enhanced visibility by stretching contrast across the dynamic range.

