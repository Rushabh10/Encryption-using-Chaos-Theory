## 2D Image Encryption using Chaos Theory

A notebook that uses the concepts of the Logistic and Lorenz maps to encrypt images quickly and efficiently. 

### How it works
1) Input image is converted to a matrix
2) The initial values of x and y along with the iteration to start from act as the keys for this encryption scheme (z is calculated as x*y)
3) The chaos maps are then generated using the key and the values they generate are used to create a transformation matrix (TM)
4) The key is also used to extract a number from the Logistic Map (log_num) and the TM is updated as TM = TM*(log_num)
5) The encrypted image is then calculated as the matrix multiplication of TM and the original image

Since the Logistic and Lorenz functions rely heavily on the initial values, if they key is off by an order of 10^-5, the image will not get decrypted.

### Bugs & Improvements -
1) Extend the functionality to make it work for 3D images too (ones with depth for RGB values)
2) Improve the computations involved in making TM so that the encrypted image looks more like noise

### Contributors 
1) Rushabh Musthyala (Rushabh10)

# Encryption-using-Chaos-Theory
