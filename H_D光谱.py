import numpy as np
LambdaHg1m=float(input('输入1号Hg峰波长(546nm)'))
LambdaHg2m=float(input('输入2号Hg峰波长(435nm)'))
LambdaHg1s,LambdaHg2s=546.074,435.834
array_a=np.array([[LambdaHg1s-LambdaHg1m,1],[LambdaHg2s-LambdaHg2m,1]])
array_b=np.array([[LambdaHg1m,LambdaHg1s-LambdaHg1m],[LambdaHg2m,LambdaHg2s-LambdaHg2m]])
array_delta=np.array([[LambdaHg1m,1],[LambdaHg2m,1]])
a=np.linalg.det(array_a)/np.linalg.det(array_delta)
b=np.linalg.det(array_b)/np.linalg.det(array_delta)
delta=np.linalg.det(array_delta)
print('array_a=',array_a)
print('array_b=',array_b)
print('array_delta=',array_delta)
print('校正参数如下：')
print('a=',a)
print('b=',b)
print('delta=',delta)
H_M=[]
D_M=[]
status=1   #设定输入状态
while 1<= status <= 6:
    temp1=float(input("输入第%d个H峰波长"%(status)))
    temp2=float(input("输入第%d个D峰波长"%(status)))
    H_M.append(temp1)
    D_M.append(temp2)
    status=status+1
print(H_M)
print(D_M)
H_C=[((1+a)*x+b)*1e-9 for x in H_M ]
D_C=[((1+a)*x+b)*1e-9 for x in D_M ]
print(H_C[2:5])
print(D_C[2:5])
print(H_C)
print(D_C)
WNH_C=[1/x for x in H_C]
WND_C=[1/x for x in D_C]
WNH_C0=WNH_C[2:5]
WND_C0=WND_C[2:5]
print('H波数',WNH_C0)
print('D波数',WND_C0)
R=10973731.568549#units:m-1
m=9.1095e-31
M=1.6726e-27
h=6.6202e-34
c=2.9979e8
M_H=M
M_D=2*M
#R_H=R/(1+m/M)
#R_D=R/(1+m/M)
#print('R_H=',R_H)
#print('R_D=',R_D)
#print(len(WND_C))
R_H=[WNH_C0[n]/(0.25-1/((n+3)**2)) for n in range(len(WNH_C0))]
R_D=[WND_C0[n]/(0.25-1/((n+3)**2)) for n in range(len(WND_C0))]
print('H里德堡常数：',R_H)
print('D里德堡常数：',R_D)
R_H_mean=np.mean(R_H)
R_D_mean=np.mean(R_D)
R_H_th=R/(1+m/M_H)
R_D_th=R/(1+m/M_D)
print("H里德堡常数理论值",R_H_th)
print("D里德堡常数理论值",R_D_th)
print('H里德堡常数平均值:',R_H_mean)
print('H里德堡常数平均误差:',np.std(R_H))
print('D里德堡常数平均值:',R_D_mean)
print('D里德堡常数平均误差:',np.std(R_D))
massRatio=(R_D_mean/R_H_mean)/(1-M_H/m*(R_D_mean/R_H_mean-1))#质量比
massRatio_th=(R_D_th/R_H_th)/(1-M_H/m*(R_D_th/R_H_th-1))
print('H/D质量比理论值：',massRatio_th)
print('H/D质量比实验值：',massRatio)
print("质量比误差：",massRatio_th-massRatio)
print('H波数：',WNH_C)
print('D波数：',WND_C)
print('极限波数：',R_H_mean/4)
E_H=[-h*c*(R_H_mean/4-x) for x in WNH_C]
print('能级：',E_H)
delta_lambda=np.mean([(D_C[n]-H_C[n]) for n in range(6)])
print('同位素位移实验值：',delta_lambda)





