## Image Encryption using Chaos Theory

A notebook that uses the concepts of the Logistic and Lorenz maps to encrypt images quickly and efficiently. 

### How it works
1) Input image is converted to a matrix
2) The initial values of x and y along with the iteration to start from act as the keys for this encryption scheme (z is calculated as x*y)
3) The chaos maps are then generated using the key and the values they generate are used to create a transformation matrix (TM)
4) The key is also used to extract a number from the Logistic Map (log_num) and the TM is updated as TM = TM*(log_num)
5) The encrypted image is then calculated as the matrix multiplication of TM and the original image

Since the Logistic and Lorenz functions rely heavily on the initial values, if they key is off by an order of 10^-5, the image will not get decrypted.

### Running instructions -
The following libraries/packages need to be installed:
tensorflow, numpy, matplotlib, PIL, scipy, PyQt5, pandas
1) Run the img_screen.py file
2) Choose an image by entering it's path into the textbox and pressing "Select"
3) Enter the key and press encrypt/decrypt to see the result
4) As of now, all encrypted images are saved as "test_1.png" and decrypted images as "orig_1.png"

### Bugs & Improvements -
1) Improve the computations involved in making TM so that the encrypted image looks more like noise
2) Currently saving the numpy array of the encrypted image separately, not sure how to save a 2 channel array as an image
3) UI improvements

### Contributors 
1) Rushabh Musthyala (Rushabh10)

# Encryption-using-Chaos-Theory
