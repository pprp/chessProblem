from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PLabel(QLabel):
    x=0
    y=0
    flag = 0
    signal = pyqtSignal(int, int, int)
    
    def __init__(self, i, j, flag, parent=None):
        super().__init__(parent)
        self.x = i
        self.y = j
        self.flag = flag
        
    
    def mousePressEvent(self, e):
        if self.flag == 0:
            self.setPixmap(QPixmap("./Data/-1.png"))
            self.flag = -1
        else:
            self.setPixmap(QPixmap("./Data/0.jpg"))
            self.flag = 0
        self.signal.emit(self.x, self.y, self.flag)


    
