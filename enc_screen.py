from tensorflow.keras.preprocessing import image
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
from scipy.integrate import odeint
from PyQt5 import QtCore, QtGui, QtWidgets

def encrypt(img, key, itera):
    
    img = np.resize(img, (img.shape[0], img.shape[1]*img.shape[2]))
    
    def logistic(r, x):
        return r*x*(1-x)

    n = 10000
    r = np.linspace(2.5, 4.0, n)
    iterations = 1000
    last = 100
    x = 1e-5*np.ones(n)

    for i in range(iterations):
        x = logistic(r, x)
        
        
    key.append(key[0]*key[1])
    def lorenz(in_, t, sigma, b, r):
        x = in_[0]
        y = in_[1]
        z = in_[2]
    
        return [sigma*(y-x), r*x - y - x*z, x*y - b*z]

    def get_solution(in_0, tmax, nt, args_tuple):
        t = np.linspace(0, tmax, nt)
        soln = odeint(lorenz, in_0, t, args=args_tuple).T
        return t, soln
    
    in_0 = key
    t_max = 20
    t_steps = 50000000
    t, [solx, soly, solz] = get_solution(in_0, t_max, t_steps, 
                                                (10.0, 8/3, 28))

    print(img.shape[1])
    tm = np.zeros((img.shape[1], img.shape[1]))
    
    
    for i in range(img.shape[1]):
        for j in range(img.shape[1]):
            if(i%3 == 0):
                tm[i][j] = int(abs(solx[itera]*2344))
            elif(i%3 == 1):
                tm[i][j] = int(abs(soly[itera]*37265))
            elif(i%3 == 2):
                tm[i][j] = int(abs(solz[itera]*3589))
            itera += 3
            
   
    temp = int(key[0]*key[2]*87435)
    temp = temp%1000
    log_key = x[temp]
    print("temp = ", temp)
    tm = tm*log_key

    tm = tm%256
    
    encrypt_img = np.matmul(img, tm)
    encrypt_img = np.transpose(encrypt_img)
    print(encrypt_img.shape)
    return encrypt_img



def decrypt(e_img, key, itera):
    
    def logistic(r, x):
        return r*x*(1-x)

    n = 10000
    r = np.linspace(2.5, 4.0, n)
    iterations = 1000
    last = 100
    x = 1e-5*np.ones(n)

    for i in range(iterations):
        x = logistic(r, x)
        
    
    e_img = np.transpose(e_img)
    key.append(key[0]*key[1])
    def lorenz(in_, t, sigma, b, r):
        x = in_[0]
        y = in_[1]
        z = in_[2]
    
        return [sigma*(y-x), r*x - y - x*z, x*y - b*z]

    def get_solution(in_0, tmax, nt, args_tuple):
        t = np.linspace(0, tmax, nt)
        soln = odeint(lorenz, in_0, t, args=args_tuple).T
        return t, soln
    
    in_0 = key
    t_max = 20
    t_steps = 50000000
    t, [solx, soly, solz] = get_solution(in_0, t_max, t_steps, 
                                                (10.0, 8/3, 28))
    
    tm = np.zeros((e_img.shape[1], e_img.shape[1]))
    
    
    for i in range(e_img.shape[1]):
        for j in range(e_img.shape[1]):
            if(i%3 == 0):
                tm[i][j] = int(abs(solx[itera]*2344))
            elif(i%3 == 1):
                tm[i][j] = int(abs(soly[itera]*37265))
            elif(i%3 == 2):
                tm[i][j] = int(abs(solz[itera]*3589))
            itera += 3
            
    temp = int(key[0]*key[2]*87435)
    temp = temp%1000
    log_key = x[temp]
    print("temp = ", temp)
    tm = tm*log_key
    tm = tm%256

    tm_inv = np.linalg.pinv(tm)
    print(e_img.shape)
    print(tm_inv.shape)
    decrypt_img = np.matmul(e_img, tm_inv)
    
    decrypt_img = np.around(decrypt_img)
    decrypt_img = decrypt_img.astype(int)
    decrypt_img = np.resize(decrypt_img, (decrypt_img.shape[0], decrypt_img.shape[1]//3, 3))
    return decrypt_img

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1204, 771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(290, 20, 631, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(60, 180, 381, 381))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("noimg.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.key_1_label = QtWidgets.QLabel(self.centralwidget)
        self.key_1_label.setGeometry(QtCore.QRect(90, 590, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.key_1_label.setFont(font)
        self.key_1_label.setObjectName("key_1_label")
        self.key_2_label = QtWidgets.QLabel(self.centralwidget)
        self.key_2_label.setGeometry(QtCore.QRect(90, 630, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.key_2_label.setFont(font)
        self.key_2_label.setObjectName("key_2_label")
        self.key_3_label = QtWidgets.QLabel(self.centralwidget)
        self.key_3_label.setGeometry(QtCore.QRect(90, 670, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.key_3_label.setFont(font)
        self.key_3_label.setObjectName("key_3_label")
        self.encrypt_button = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt_button.setGeometry(QtCore.QRect(550, 280, 101, 41))
        self.encrypt_button.setObjectName("encrypt_button")
        self.decrypt_button = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt_button.setGeometry(QtCore.QRect(550, 360, 101, 41))
        self.decrypt_button.setObjectName("decrypt_button")
        self.photo1 = QtWidgets.QLabel(self.centralwidget)
        self.photo1.setGeometry(QtCore.QRect(760, 180, 381, 381))
        self.photo1.setText("")
        self.photo1.setPixmap(QtGui.QPixmap("noimg.png"))
        self.photo1.setScaledContents(True)
        self.photo1.setObjectName("photo1")
        self.key_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.key_1.setGeometry(QtCore.QRect(150, 590, 91, 31))
        self.key_1.setObjectName("key_1")
        self.key_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.key_2.setGeometry(QtCore.QRect(150, 630, 91, 31))
        self.key_2.setObjectName("key_2")
        self.key_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.key_3.setGeometry(QtCore.QRect(150, 670, 91, 31))
        self.key_3.setObjectName("key_3")
        self.img_label = QtWidgets.QLabel(self.centralwidget)
        self.img_label.setGeometry(QtCore.QRect(430, 630, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.img_label.setFont(font)
        self.img_label.setObjectName("img_label")
        self.img_path = QtWidgets.QTextEdit(self.centralwidget)
        self.img_path.setGeometry(QtCore.QRect(500, 630, 251, 41))
        self.img_path.setObjectName("img_path")
        self.select_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_button.setGeometry(QtCore.QRect(810, 630, 111, 41))
        self.select_button.setObjectName("select_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1204, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.select_button.clicked.connect(self.set_image)
        self.encrypt_button.clicked.connect(self.encrypt_photo)
        self.decrypt_button.clicked.connect(self.decrypt_photo)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "Image Encryption"))
        self.key_1_label.setText(_translate("MainWindow", "Key 1"))
        self.key_2_label.setText(_translate("MainWindow", "Key 2"))
        self.key_3_label.setText(_translate("MainWindow", "Key 3"))
        self.encrypt_button.setText(_translate("MainWindow", "Encrypt"))
        self.decrypt_button.setText(_translate("MainWindow", "Decrpyt"))
        self.img_label.setText(_translate("MainWindow", "Image:"))
        self.select_button.setText(_translate("MainWindow", "Select"))

    def set_image(self):
        global path
        path = self.img_path.toPlainText()
        self.photo.setPixmap(QtGui.QPixmap(path))

    def encrypt_photo(self):
        key1 = self.key_1.toPlainText()
        key2 = self.key_2.toPlainText()
        key3 = self.key_3.toPlainText()
        keys = [float(key1), float(key2)]
        key3 = int(key3)
        img = Image.open(path)
        p = np.array(img)
        final = encrypt(p, keys, key3)
        np.save("test_1.npy", final)
        mpimg.imsave("test_1.png", final)
        self.photo1.setPixmap(QtGui.QPixmap("test_1.png")) 

    def decrypt_photo(self):
        key1 = self.key_1.toPlainText()
        key2 = self.key_2.toPlainText()
        key3 = self.key_3.toPlainText()
        keys = [float(key1), float(key2)]
        key3 = int(key3)
        path1 = path.replace(".png", ".npy")
        print("path = ", path1)
        p = np.load(path1)
        print(p.shape)
        final = decrypt(p, keys, key3)
        mpimg.imsave('orig_1.png', final)   
        self.photo1.setPixmap(QtGui.QPixmap("orig_1.png"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
