I = io.imread("/content/moon.jpg")
I = I/255.0
I.shape

#a=starting of slope of pixels
#b=ending of slope of pixels
a=0.4
b=0.8
c2= a
c1=(1/(b-a))
I_stretched = np.clip(c1*(I-c2), 0, 1)