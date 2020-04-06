## TCP拥塞控制演示程序

```python
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
```

运行截图![运行截图](/img/1.png)

## 习题

### P40

![1](/img/p40.png)

1. [1,6]以及[23,26]
2. [6,16]以及[17,22]
3. 3个冗余ACK
4. 超时
5. 32
6. 21
7. 29/2=14
8. [1,6]轮回传输1+2+4+8+16+32=63，第7个轮回内传输第70份报文段
9. ssthresh为4，窗口大小为7
10. ssthresh为21，窗口大小为`1*2*2=4`
11. `1+2+4+8+16+21=52`

### P44

![P44](/img/p44.png)

1. 6个RTT

2. $$
   6+7+8+9+10+11=51\\51/6=8.5
   $$

   

### P45

![P45](/img/p45.png)

1. 从 W/2RTT 到 W/RTT 期间总共发送的分组数：
   $$
   \frac{W}{2}+(\frac{W}{2}+1)+(\frac{W}{2}+2)+...+W=\frac{3}{8}W^2+\frac{3}{4}W
   $$
   

   丢包率为
   $$
   1/(\frac{3}{8}W^2+\frac{3}{4}W)=\frac{1}{\frac{3}{8}W^2+\frac{3}{4}W}
   $$

2. 当W很大时，
   $$
   3W^2/8>>3W/4\\L\approx\frac{3W^2}{8}\\W\approx\sqrt{8/3L}\\平均吞吐率为\frac{0.75W}{RTT}\approx\frac{1.22MSS}{RTT*\sqrt{L}}
   $$
   


​	