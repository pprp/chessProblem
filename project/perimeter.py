# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:01:09 2019

@author: pprp
"""
import numpy as np

class perimeter:
    dx = [1,1,0,-1,-1,-1,0,1]
    dy = [0,1,1,1,0, -1,-1,-1]
    
    output = 0
    
    data = np.empty(shape=(1000,1000))
    #棋盘大小
    m = 0
    n = 0
    #点击位置
    clickx = 0
    clicky = 0
    
    def __init__(self, m, n, x, y, data):
        self.m = m
        self.n = n
        self.clickx = x
        self.clicky = y
        self.data = data
        self.process()
    
    def search(self,x,y):
        tx = 0
        ty = 0
        for i in range(8):
            tx = x+self.dx[i]
            ty = y+self.dy[i]
            if x < 0 or y < 0 or x > self.m or y > self.n:
                continue
            if tx >= 0 and tx < self.m and ty >= 0 and ty < self.n:
                if self.data[tx][ty] == -1:
                    self.data[tx][ty] = 1
                    self.search(tx,ty)
                    
    def getAns(self):
        for i in range(self.m):
            for j in range(self.n):
                if self.data[i][j] == 1:
                    if i-1 < 0 or self.data[i-1][j] == 0:
                        self.output += 1
                    if j-1 < 0 or self.data[i][j-1] == 0:
                        self.output += 1
                    if i+1 >= self.m or self.data[i+1][j] == 0:
                        self.output += 1
                    if j+1 >= self.n or self.data[i][j+1] == 0:
                        self.output += 1
        return self.output
    
    def readFile(self,File):
        tmp = []
        with open(File,'r') as f:
            line = f.readline()
            [self.m,self.n,self.clickx,self.clicky] = line.split()
            line = f.readline()
            while line:
                read_line = line.split()
                tmp.append([int(read_line[0]),int(read_line[1]), \
                            int(read_line[2]),int(read_line[3])])
                line = f.readline()
            self.data = np.array(tmp)
            
    def process(self):
        # init data
        #self.readFile(File)
        print("Before processing")
        print(self.data)
        print("parameters:")
        print(self.m, self.n, self.clickx, self.clicky)
        # from str to int
        self.m = int(self.m)
        self.n = int(self.n)
        self.clickx = int(self.clickx)
        self.clicky = int(self.clicky)
        #print(self.m,self.n,self.clickx,self.clicky)
        
        if self.data[self.clickx-1][self.clicky-1] == 0:
            print("图像不存在")
        elif self.data[self.clickx-1][self.clicky-1] == -1:
            self.data[self.clickx-1][self.clicky-1] = 1
            self.search(self.clickx-1,self.clicky-1)
        print("After processing:")
        print(self.data)
            
    
if __name__ == "__main__":
    p = perimeter()
    p.process("./perimeter.txt")
    print(p.getAns())
    
