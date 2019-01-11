# -*- coding: utf-8 -*-
import numpy as np

class chess:
    #定义私有属性
    __arr = np.empty(shape=(1000,1000))
    __ans = 0
    __vis = np.empty(shape=(1000))
    __n = 0
    __m = 0
    
    def __init__(self,arr):
        #self.__arr = np.zeros([n,m])
        #self.__arr = np.array(ch1.readFile(path))
        self.__arr = arr
        # 长度为列的个数
        self.__vis = np.zeros(self.__arr.shape[1])
        self.__ans = 0
        # n*m的棋盘大小, 需要放置left个点
        self.__n = self.__arr.shape[0]
        self.__m = self.__arr.shape[1]
      
        
    # 正方形棋盘 棋盘大小为 n*n
    # row 代表当前是第几行
    # left 代表当前还有多少个棋子
    # 遍历解空间
    def dfs(self,row,left):
        print("row {} left {}".format(row,left))
        if left == 0:
            # 到达边界
            self.__ans += 1
            return
        for i in range(row,self.__n):
            for j in range(self.__m):
                # 1 = can not go
                # 0 = can go
                print(i,j)
                if self.__arr[i][j] == -1 or self.__vis[j] == 1:
                    continue
                self.__vis[j] = 1
                self.dfs(i+1,left-1)
                self.__vis[j] = 0
                
    def readFile(self,fileName):
        data = []
        with open(fileName,'r') as f:
            line = f.readline()
            while line:
                eachline = line.split()
                read_data  = [int(x) for x in eachline]
                data.append(read_data)
                line = f.readline()
        return data
    
    def clear(self):
        for i in range(self.__n):
            for j in range(self.__m):
               self.__arr[i][j]=0
        self.__ans = 0
        
        
    def getAns(self):
        return self.__ans

if __name__ == "__main__":
    ch1 = chess("./in.txt")
    ch1.dfs(0,1)
    print(ch1.getAns())
    print("len")
    tmp = np.array(ch1.readFile("./in.txt"))
    print(tmp)
