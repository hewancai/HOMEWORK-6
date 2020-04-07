# HOMEWORK6

李沛昊 2017302580288

## P22

**问题：**

考虑一个GBN协议，其发送方窗口为4,序号范围为1024。假设在$t$时刻接收方期待的下一个有 序分组的序号是$k$。假设媒体不会对报文重新排序。回答以下问题：

 a. 在$t$时刻，发送方窗口内的报文序号可能是多少？论证你的回答。

 b. 在$t$时刻，在当前传播回发送方的所有可能报文中，ACK字段的所有可能值是多少？论证你的 回答。 

**解答：**

a.考虑sendor已经接收到ACK k-1，则在发送方窗口中的报文序号范围为：$[k,k+3]$

​	因为接收方已经接收到报文 k-1，则发送方至少已经收到ACK k-5，所以考虑发送方未收到ACK k-4的情况，则窗口内的报文序号范围为$[k-4,k-1]$

​	综上所述，报文序号的取值范围为$[k-4,k+3]$

b.因为接收方已经接收到报文 k-1，则发送方至少已经收到ACK k-5，所以正在飞行中的ACK序号为$[k-4, k-1]$

## P26

**问题：**

考虑从主机A向主机B传输L字节的大文件，假设MSS为536字节。 

a. 为了使得TCP序号不至于用完，$L$的最大值是多少？前面讲过TCP的序号字段为4字节。

 b. 对于你在（a）中得到的$L$，求出传输此文件要用多长时间？假定运输层、网络层和数据链路层 首部总共为66字节，并加在每个报文段上，然后经155Mbps链路发送得到的分组。忽略流量控 制和拥塞控制，使主机A能够一个接一个和连续不断地发送这些报文段。

**解答：**

a.$L_{max}=2^{32}bytes=4GB$

b.总的头部大小$H_{sum}=66*\frac{L_{max}}{536}$

 总花费时间$t=\frac{L_{max}+H_{sum}}{155Mbps}=249s$

## P46

**问题：**考虑仅有一条单一的TCP （Reno）连接使用一条10Mbps链路，且该链路没有缓存任何数据。假设 这条链路是发送主机和接收主机之间的唯一拥塞链路。假定某TCP发送方向接收方有一个大文件要 发送，而接收方的接收缓存比拥塞窗口要大得多。我们也做下列假设：每个TCP报文段长度为1500 字节；该连接的双向传播时延是150ms；并且该TCP连接总是处于拥塞避免阶段，即忽略了慢 启动。 

a.这条TCP连接能够取得的最大窗口长度（以报文段计）是多少？ 

b. 这条TCP连接的平均窗口长度（以报文段计）和平均吞吐量（以bps计）是多少？ 

c. 这条TCP连接在从丢包恢复后，再次到达其最大窗口要经历多长时间？ 

**解答：**

a. 因为 $\frac{W_{max}MSS}{RTT}=10Mbps$

所以$W_{max}=\frac{10Mbps*150ms}{1500bytes}=125$

b. $W_{avg} = \frac{3W_{max}}{4}=94$

​    平均吞吐量$\frac{W_{avg}MSS}{RTT} = 7.52Mbps$

c. $t = (W_{max}-W_{avg})RTT=9s$