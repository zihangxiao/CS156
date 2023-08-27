import numpy as np 
from numpy import random 
import matplotlib.pyplot as plt
from tqdm import tqdm
size = 999
runtime_arr = np.zeros(size)
z=0
for z in tqdm(range(999), desc="Processing", unit="iteration"):
    x=random.uniform(-1,1,100)
    y=random.uniform(-1,1,100)
    random_line_x=random.uniform(-1,1,100)
    random_line_y=random.uniform(-1,1,100)
    # Generate two distinct random indices for x and y
    index_1 = random.randint(0, len(x) - 1)
    index_2 = random.randint(0, len(x) - 1)
    while index_2 == index_1:  # Ensure distinct indices
        index_2 = random.randint(0, len(x) - 1)

    # Use the indices to get the x and y coordinates
    random_point_1_x = random_line_x[index_1]
    random_point_1_y = random_line_y[index_1]
    random_point_2_x = random_line_x[index_2]
    random_point_2_y = random_line_y[index_2]
    #to do this point may have chance of overlapping with each other solve this
    def calculateline(x1,y1,x2,y2):
        gradient=(y1-y2)/(x1-x2)
        b=y2-gradient*x2
        line=np.array([gradient,b])
        return(line)
    line=calculateline(random_point_1_x,random_point_1_y,random_point_2_x,random_point_2_y)
    y_output=np.zeros(100)
    for i in range(len(x)):
        x_testpoint=(y[i]-line[1])/line[0]
        if x_testpoint<x[i]:
            y_output[i]=1
        else:
            y_output[i]=-1
    X=(2,100)
    X=np.zeros(X)
    X[0,:]=x
    X[1,:]=y
    weights=(1,2)
    weights=np.zeros(weights)
    status=(100)
    status=np.zeros(status)
    runtime=0
    bias=[0]
    learning_rate=1
    new_status=(10)
    new_status=np.zeros(new_status)
    while not np.array_equal(status,y_output):
        indices=np.where(new_status == 0)[0]
        selected_index = np.random.choice(indices)
        weights=weights+X[:,selected_index]*y_output[selected_index]
        bias=bias+y_output[selected_index]
        print(bias)
        for i in range(len(X[0,:])):
            sign_X=np.dot(weights,X[0:2,i])*learning_rate+bias
            if sign_X>=0:
                status[i]=1
            elif sign_X<0:
                status[i]=-1
        runtime=runtime+1
        new_status=status+y_output
        if runtime>1000:
            break
    runtime_arr[z]=runtime
print(np.mean(runtime_arr))
print(runtime_arr)
   