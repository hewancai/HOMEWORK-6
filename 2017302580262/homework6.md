P48
a. W*MSS/RTT = 10Gbps
    W = 125000
b. 7.52Gbps
c. 156.2min

P52
1.S=W/2+W/2(1+a)+W/2(1+a)^2+...+W
设 W/2(1+a)n=WW2(1+a)n=W   
得 n=log1+a2
从而 S=W(2a+1)/2a
则丢包率 L=1/S=2a/W(2a+1)
2.
从 W/2 增加到 W 需要的时间：
n∗RTT=log1+a2∗RTTn∗RTT=log1+a2∗RTT      
跟吞吐量无关

P54
优点是无需经历慢启动过程
 缺点是 t1 时刻的 cwnd 和 ssthresh 比较陈旧，不能正确反映 t2 时刻的线路拥塞状态