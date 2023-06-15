#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from cv2 import VideoCapture, resize, INTER_AREA, destroyAllWindows, cvtColor, COLOR_BGR2RGB
from PyQt5.QtGui import QImage, QPixmap, QFont
import sys
import numpy as np
from keras.models import load_model
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(819, 581)  # 設定視窗大小
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(7, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(30, 60))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setFont(QFont("Arial", 32))
        
        self.verticalLayout_2.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 672, 471))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
                
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 672, 471))
        self.label_2.setObjectName("label_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.scrollArea.setWidgetResizable(True)
        #self.scrollArea.setWidget(self.label_2)

        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 300, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 85)
        self.horizontalLayout.setStretch(1, 15)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.show_result)
        #self.pushButton_2.clicked.connect(self.choose_area)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def classify(self):
        model = load_model('keras_modeltai2.h5', compile=False)
        camera = VideoCapture(0)
        labels = open('labeltai2s.txt', 'r',encoding="utf-8").readlines()
        ret, image = camera.read()
        image = resize(image, (224, 224), interpolation=INTER_AREA)
        image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)
        image = (image / 127.5) - 1
        probabilities = model.predict(image)
        
        result = labels[np.argmax(probabilities)]
        results=str(result.strip())
        
        camera.release()
        destroyAllWindows()
        
        return results
    
    def show_result(self):
        results = self.classify()
        self.label.setText("分類結果:"  + results)
        self.label.setFont(QFont("Arial", 32))
        self.show_image()

   
    def show_image(self):
        # 讀取圖片，轉換為Qt圖像
        camera = VideoCapture(0)
        ret, image = camera.read()
        image = resize(image, (672, 471), interpolation=INTER_AREA)
        rgb_image = cvtColor(image, COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)

        scroll_area_width = self.scrollArea.width()
        scroll_area_height = self.scrollArea.height()

        # 縮放圖片以符合滾動區域的大小
        scaled_image = pixmap.scaled(scroll_area_width, scroll_area_height, QtCore.Qt.KeepAspectRatio)

        # 設定圖片顯示在label_2上
        self.label_2.setPixmap(scaled_image)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)

        # 在滾動區域中顯示圖像
        self.scrollAreaWidgetContents.setFixedSize(w, h)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_2.setPixmap(pixmap)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "台北垃圾分類"))
        self.label.setText(_translate("MainWindow", "辨識結果"))
        self.pushButton.setText(_translate("MainWindow", "開始辨識"))
        self.pushButton_2.setText(_translate("MainWindow", "選擇地區"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



# In[ ]:





# In[ ]:




