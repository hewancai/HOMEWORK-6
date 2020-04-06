print("初始拥塞窗口为1")
print("请输入发生拥塞前的拥塞窗口大小和引发超时的拥塞窗口大小")
ConWin=1
ConWin1=int(input())  #发生3个ACK重复时的拥塞窗口大小
ConWin2=int(input())  #发生超时的拥塞窗口大小
print("输入打印前n个RTT：")
n=int(input())
RTTCount=1            #RTT计数
ThreShold=10000
print("第%d个RTT，拥塞窗口大小为%d"%(RTTCount,ConWin))
while (RTTCount<n):
  RTTCount+=1
  if (ConWin<ThreShold): #小于ThreShold变量，指数增长
    ConWin*=2
  else:                  #大于ThreShold变量，线性增长
    ConWin+=1
  print("第%d个RTT，拥塞窗口大小为%d"%(RTTCount,ConWin))
  if (ConWin>=ConWin2 and RTTCount<n): #超时
    ThreShold=ConWin/2
    ConWin=1
    RTTCount+=1
    print("第%d个RTT，拥塞窗口大小为%d"%(RTTCount,ConWin))
  elif (ConWin>=ConWin1 and RTTCount<n): #3个ACK重复
    ThreShold=ConWin/2
    ConWin=ThreShold+3
    RTTCount+=1
    print("第%d个RTT，拥塞窗口大小为%d"%(RTTCount,ConWin))