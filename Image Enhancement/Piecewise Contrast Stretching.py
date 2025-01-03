# Prototype: piecewise_contrast_stretch(I_gray, r1, r2, s1, s2)
# Assuming both input and output images are normalized between 0 and 1

def piecewise_contrast_stretch(I, r1, r2, s1, s2):
      # Initialize an array for the output image
    I_stretched = np.zeros_like(I)

    # Case 1: 0 <= I(x) < r1
    mask1 = I < r1
    I_stretched[mask1] = (s1 / r1) * I[mask1]

    # Case 2: r1 <= I(x) < r2
    mask2 = (I >= r1) & (I < r2)
    I_stretched[mask2] = ((s2 - s1) / (r2 - r1)) * (I[mask2] - r1) + s1

    # Case 3: r2 <= I(x) <= 1
    mask3 = I >= r2
    I_stretched[mask3] = ((1 - s2) / (1 - r2)) * (I[mask3] - r2) + s2

    return I_stretched