import math
import numpy as np
import operator

file1 = open('Milestone 3\Testcase3.txt', 'r')
file2 = open('Milestone 3\Testcase3_out.txt','w')

Lines = file1.readlines()
data=[]
def top_left_from_center(center, width, height):
    x, y = center
    upper_left = (x - width / 2, y + height / 2)
    return upper_left
def lower_left_from_center(center, width, height):
    x, y = center
    lower_left = (round(x - width / 2,4), round(y - height / 2,4))
    return lower_left
def top_right_from_center(center, width, height):
    x, y = center
    top_right = (x + width / 2, y + height / 2)
    return top_right
def lower_right_from_center(center, width, height):
    x, y = center
    low_right = (x + width / 2, y - height / 2)
    return low_right
def isInside(circle_x, circle_y, rad, x, y):
    if ((x - circle_x) * (x - circle_x) +
        (y - circle_y) * (y - circle_y) <= rad * rad):
        return True
    else:
        return False

for i in Lines:
    colon=i.find(':')
    data.append(i[colon+1:].strip("\n"))
print(data)
WaferDiameter = int(data[0])
DieSize = list(map(int,data[1].split("x")))
DieShiftVector = list(map(int,data[2].strip("(").strip(")").split(",")))
ReferenceDie = list(map(int,data[3].strip("(").strip(")").split(",")))
DieStreetWidthAndHeight = list(map(int,data[4].strip("(").strip(")").split(",")))
RecticleStreetWidthAndHeight = list(map(int,data[5].strip("(").strip(")").split(",")))
DiesPerReticle = list(map(int,data[6].split("x")))

num_dies_x = WaferDiameter // DieSize[0]
num_dies_y = WaferDiameter // DieSize[1]
wafer_center = (0,0)
valid_dies = []
die_center = (round(- WaferDiameter/2 + DieSize[0]/2,4),round(WaferDiameter/2-DieSize[1]/2,4))
count=0

for i in range(num_dies_x+11):
    curr=(die_center[0]+DieSize[1]*i,die_center[1])
    for j in range(num_dies_y+11):
        count+=1
        
        curr1=(curr[0]+DieShiftVector[0],curr[1]-DieSize[0]*j+DieShiftVector[1])
        print(count,curr1)
        die_llc = lower_left_from_center(curr1,DieSize[0],DieSize[1])
        die_tlc = top_left_from_center(curr1,DieSize[0],DieSize[1])
        die_lrc = lower_right_from_center(curr1,DieSize[0],DieSize[1])
        die_trc = top_right_from_center(curr1,DieSize[0],DieSize[1])
        die_index = (i,num_dies_y-j-1)
        if die_llc == lower_left_from_center(ReferenceDie,DieSize[0],DieSize[1]):
            check=die_index
        if isInside(0,0,WaferDiameter/2,die_llc[0],die_llc[1]) or isInside(0,0,WaferDiameter/2,die_lrc[0],die_lrc[1] or isInside(0,0,WaferDiameter/2,die_tlc[0],die_tlc[1]) or isInside(0,0,WaferDiameter/2,die_trc[0],die_trc[1])):
            valid_dies.append((die_index, die_llc))
            print(die_index)

for die in valid_dies:
    file2.write(f"{tuple(map(operator.sub, die[0], check))}:{die[1]}\n")
    