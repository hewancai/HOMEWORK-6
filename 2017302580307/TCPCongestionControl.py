import numpy as np
import matplotlib.pyplot as plt
import sys
import threading
import time

cwnds = []
fig = plt.figure()
ax = fig.add_subplot(111)

class Tcp:
    def __init__(self):
        self.cwnd = 1
        self.ssthresh = 16
        self.flag = 0 # 0:慢开始，1：避免拥塞，2：快恢复
        self.repeatingACK = 0
        cwnds.append(self.cwnd)

    def slow_start(self):
        self.cwnd *= 2
        self.repeatingACK = 0
        cwnds.append(self.cwnd)
        if self.cwnd >= self.ssthresh:
            self.flag=1

    def avoid_congestion(self):
        self.cwnd+=1
        self.repeatingACK = 0
        cwnds.append(self.cwnd)

    def fastRecover(self):
        self.ssthresh = self.cwnd / 2
        if self.repeatingACK == 3:
            self.cwnd=self.ssthresh
            self.flag=1
        else:
            self.cwnd=1
            self.flag=0
        cwnds.append(self.cwnd)
        self.repeatingACK = 0

    def duplicate(self):
        if self.repeatingACK < 3:
            self.repeatingACK += 1
        else:
            self.repeatingACK = 3
            self.flag=2


    def run(self):
        if self.flag==0:
            self.slow_start()
        elif self.flag==1:
            self.avoid_congestion()
        elif self.flag==2:
            self.fastRecover()

    def control(self,commond):
        if commond==0: # new ACK情况
            self.run()
        elif commond==1: # 重复ack
            self.duplicate()
        elif commond==2: # timeout
            if self.flag==1 or self.flag==0:
                self.ssthresh=self.cwnd/2
                self.cwnd=1
                cwnds.append(self.cwnd)
                self.repeatingACK=0
                self.flag=0
            else:
                self.run()
		


class TcpThread(threading.Thread):

    def __init__(self,n):
        super(TcpThread,self).__init__()
        self.n=n
        self.stopflag = False

    def run(self):
        tcp = Tcp()
        while not self.stopflag:
            cmd = input('输入控制命令0:new ACK,1:duplicated ACK,2:timeout,3:quit')
            if int(cmd) == 3:
                self.stop()
            tcp.control(int(cmd))
            draw(tcp.ssthresh)
            print(cwnds)

    def stop(self):
        self.stopflag=True

def draw(ssthresh):
    X = [x for x in range(len(cwnds))]
    s = [ssthresh]*len(X)
    plt.cla() # 清楚之前的线，重绘
    plt.xlabel('Transmission rounds')
    plt.ylabel('cwnd')
    ax.plot(X, cwnds,color='red',label='cwnd line')
    ax.plot(X,s,color='blue',linewidth=2,linestyle="-",label='ssthresh')
    ax.legend()
    plt.grid()
    fig.canvas.draw()

if __name__ == "__main__":
    # 控制tcp的线程，因为plt.show要在主线程中，导致之后的控制命令无法输入
    tcp = TcpThread('tcp')
    tcp.start()
    plt.show()




