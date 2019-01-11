import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
#from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import  QStringListModel
from Ui_Main import *
from perimeter import *
from chess import *
import numpy as np
import random
from PLabel import *

class MainWindow(QtWidgets.QMainWindow):
    FilePath = ''
    row = 0
    col = 0
    num = 0
    data = []
    # 0 -- 棋盘问题， 1 -- 求解周长 , 2 -- 路径
    tag = 0
    x = 0
    y = 0
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_ChessPlayer()
        self.ui.setupUi(self)
        self.ui.btn_sure.setIcon(QIcon("./Data/sure.png"))
        self.ui.btn_calc.setIcon(QIcon("./Data/calc.png"))
        self.ui.btn_exit.setIcon(QIcon("./Data/exit.png"))
        self.ui.label_5.setPixmap(QPixmap("./Data/answer.png"))
        self.setWindowTitle("ChessPlayer")
        self.ui.label.setPixmap(QPixmap("./Data/Rows.png"))
        self.ui.label_2.setPixmap(QPixmap("./Data/Columns.png"))
        self.ui.label_5.setScaledContents (True)
        self.ui.label.setScaledContents(True)
        self.ui.label_2.setScaledContents(True)
        self.ui.comboBox.addItem("棋盘问题")
        self.ui.comboBox.addItem("图像周长求解")
        self.ui.comboBox.addItem("8皇后问题")
        self.ui.lineEdit_y.setVisible(False)
        self.ui.label_4.setVisible(False)
        
        slm = QStringListModel()
        self.qList = ['File1', 'File2', 'File3', 'File4', 'File5', \
                         'File6', 'File7', 'File8','File9', 'perimeter']
        self.path = ['./Data/1.txt','./Data/2.txt', './Data/3.txt', \
                           './Data/4.txt', './Data/5.txt','./Data/6.txt', \
                           './Data/7.txt', './Data/8.txt', './Data/9.txt', \
                           './Data/perimeter.txt']
        slm.setStringList(self.qList)
        self.ui.lv.setModel(slm)        
        
        self.ui.lv.clicked.connect(self.lvProcess)
        self.ui.btn_sure.clicked.connect(self.repaint)
        self.ui.btn_calc.clicked.connect(self.getAns)
        self.ui.btn_exit.clicked.connect(self.exits)
        self.ui.comboBox.currentIndexChanged.connect(self.selectionChange)
        
        self.ui.lineEdit_num.textChanged.connect(self.leChangeNum)
        self.ui.lineEdit_row.textChanged.connect(self.leChangeRow)
        self.ui.lineEdit_col.textChanged.connect(self.leChangeCol)
        self.ui.lineEdit_y.textChanged.connect(self.leChangeY)
    
    def leChangeY(self):
        if self.ui.lineEdit_y !='':
            self.y = int(self.ui.lineEdit_y.text())
        print('Y changed:', self.y)
        
    def leChangeNum(self):
        if self.ui.lineEdit_num.text() != '':
            if self.tag == 0:
                self.num = int(self.ui.lineEdit_num.text())
                print("num changed:", self.num)
            elif self.tag == 1:
                self.x = int(self.ui.lineEdit_num.text())
                print('X changed:', self.x)
            
    
    def leChangeRow(self):
        if self.ui.lineEdit_row.text() != '':
            self.row = int(self.ui.lineEdit_row.text())
            print("row changed:", self.row)
            
    def leChangeCol(self):
        if self.ui.lineEdit_col.text() != '':
            self.col = int(self.ui.lineEdit_col.text())
            print("col changed:", self.col)
    
    # ComboBox 改变的时候的响应函数
    def selectionChange(self, i):
        self.tag = i
        if i == 1:
            self.ui.lineEdit_y.setVisible(True)
            self.ui.label_4.setVisible(True)
            self.ui.label_6.setText("X：")
        elif i == 0:
            self.ui.lineEdit_y.setVisible(False)
            self.ui.label_4.setVisible(False)
            self.ui.label_6.setText("棋数：")
        QMessageBox.information(self, "changed","你选择了"+self.ui.comboBox.currentText())
    
    # Button退出函数
    def exits(self):
        self.close()
    
    # 根据文件重绘
    def paintFile(self):
        for i in range(int(self.row)):
            for j in range(int(self.col)):
                if self.data[i][j] == -1:
                    label = PLabel(i, j, -1)
                    self.data[i][j] = -1
                    label.signal.connect(self.processData)
                    label.setPixmap(QPixmap("./Data/-11.jpg"))
                else:
                    self.data[i][j] = 0
                    label = PLabel(i, j, 0)
                    label.signal.connect(self.processData)
                    label.setPixmap(QPixmap("./Data/0.jpg"))
                label.setScaledContents (True)
                self.ui.grid.addWidget(label, i, j)
    
    # 进行随机重绘
    def repaint(self):
        self.setThree()
        if self.ui.lineEdit_col.text() != '' and self.ui.lineEdit_row.text() != '' and self.ui.lineEdit_num.text() != '':
            self.data = [[0]*self.col for row in range(self.row)]
            for i in range(int(self.row)):
                for j in range(int(self.col)):
                    if random.randint(0, 99)%2 == 0:
                        label = PLabel(i, j, -1)
                        self.data[i][j] = -1
                        label.signal.connect(self.processData)
                        label.setPixmap(QPixmap("./Data/-11.jpg"))
                    else:
                        self.data[i][j] = 0
                        label = PLabel(i, j, 0)
                        label.signal.connect(self.processData)
                        label.setPixmap(QPixmap("./Data/0.jpg"))
                    label.setScaledContents (True)
                    self.ui.grid.addWidget(label, i, j)
                    
    # PLabel的事件响应函数
    def processData(self, i, j, flag):
        print(i, j)
        #QMessageBox.information(self, "error", "")
        self.data[i][j] = flag
        print(np.array(self.data))
    
    #进行计算的结果
    def getAns(self):
        if self.tag == 0:
            ch = chess(np.array(self.data))
            ch.dfs(0, int(self.num))
            self.ui.lineEdit_ans.setText(str(ch.getAns()))
        elif self.tag == 1:
            p = perimeter(self.row, self.col, self.x, self.y, np.array(self.data))
            #p.process("./perimeter.txt")
            self.ui.lineEdit_ans.setText(str(p.getAns()))
    
    #从文件中加载一系列参数--ok
    def LoadFile(self, file):
        self.FilePath = file
        self.data = []
        with open(self.FilePath, 'r') as f:
            print(self.FilePath)
            line = f.readline()
            if self.tag == 0: # 期盼问题
                [self.row, self.col, self.num] = line.split()
            elif self.tag == 1:
                [self.row, self.col, self.x, self.y] = line.split()

            line = f.readline()
            while line:
                eachline = line.split()
                read_data = [int(x) for x in eachline]
                self.data.append(read_data)
                line = f.readline()
                
    # 设置三个主要参数 ---ok
    def setThree(self):
        if self.ui.lineEdit_col.text() != '' and self.ui.lineEdit_row.text() != '' \
                                                       and self.ui.lineEdit_num.text() != '' \
                                                       and self.tag == 0:
            QMessageBox.information(self, "ListWidget","success")
            self.row = int(self.ui.lineEdit_row.text())
            self.col = int(self.ui.lineEdit_col.text())
            self.num = int(self.ui.lineEdit_num.text())
        elif self.ui.lineEdit_col.text() != '' and self.ui.lineEdit_row.text() != '' \
                                                       and self.ui.lineEdit_num.text() != ''\
                                                       and self.ui.lineEdit_y.text() != ''\
                                                       and self.tag == 1:
            QMessageBox.information(self, "ListWidget","success")
            self.row = int(self.ui.lineEdit_row.text())
            self.col = int(self.ui.lineEdit_col.text()) 
            self.x = int(self.ui.lineEdit_num.text())
            self.y = int(self.ui.lineEdit_y.text())
        else:
            QMessageBox.information(self, "error", "行列以及棋子数不能为空")
            
    # listView的事件处理响应函数
    def lvProcess(self, qModelIndex):
        #加载文件
        self.LoadFile(self.path[qModelIndex.row()])
        self.ui.lineEdit_row.setText(str(self.row))
        self.ui.lineEdit_col.setText(str(self.col))
        if self.tag == 1:
            self.ui.lineEdit_num.setText(str(self.x))
            self.ui.lineEdit_y.setText(str(self.y))
        elif self.tag == 0:
            self.ui.lineEdit_num.setText(str(self.num))
        QMessageBox.information(self, "ListWidget","你选择了"+self.qList[qModelIndex.row()])
        self.paintFile()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    #app.setStyleSheet("QPushButton { margin: 1ex;font-size: 15pt; }")
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    
    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()    

    sys.exit(app.exec_())
