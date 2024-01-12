import math
import numpy as np
file1 = open('.\Testcase3.txt', 'r')
file2 = open('.\\testcase3_out.txt','w')
Lines = file1.readlines()
data=[]
for i in Lines:
    colon=i.find(':')
    data.append(int(i[colon+1:]))
WaferDiameter = data[0]
NumberOfPoints = data[1]
Angle = data[2]
result=set()
print(math.cos(Angle))
x1,y1 = round(math.cos(Angle*0.01745329) * WaferDiameter/2,4),round(math.sin(Angle*0.01745329) * WaferDiameter/2,4)
o_x,o_y = -1.0 * x1 if x1!=0 else 0.0,-1.0 * y1 if y1!=0 else 0.0
print(x1,y1,o_x,o_y)
print(x1,y1)
x_cor = np.linspace(o_x, x1, num=NumberOfPoints)
y_cor = np.linspace(o_y, y1, num=NumberOfPoints)
print(x_cor,y_cor)
for i in range(len(x_cor)):
    result.add((round(x_cor[i],4),round(y_cor[i],4)))
    file2.write(f"{(round(x_cor[i],4),round(y_cor[i],4))}\n")
