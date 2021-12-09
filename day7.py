#!/usr/bin/env python
# coding: utf-8

# # Advent of Code 2021
# ## Day 7
# 
# A.T.Hannington

# # Part 1

# In[1]:


import numpy as np


# In[2]:


file_path = "day7_test_input.txt"              

test = np.genfromtxt(file_path,delimiter=",").astype("int32")
print(test)


# In[3]:


def move_crab_submarines(data):
    #Get optimal distance, median less affected by outliers
    median_distance = np.nanmedian(data)
    
    #Get distance each crab moves, and thus fuel per crab
    diff = np.absolute(data-median_distance)
    
    #Get total fuel used by all crabs
    fuel_used = np.sum(diff)
    
    return median_distance, fuel_used


# In[4]:


expect_pos = 2.0
expect_fuel = 37.0


# In[5]:


test_pos,test_fuel = move_crab_submarines(test)

print(test_pos, f"Test Position passed? : {test_pos==expect_pos}")
print(test_fuel, f"Test Fuel passed? : {test_fuel==expect_fuel}")


# ### Run on data

# In[6]:


file_path = "day7_input.txt"              

data = np.genfromtxt(file_path,delimiter=",").astype("int32")
print(data)


# In[7]:


result_pos,result_fuel = move_crab_submarines(data)

print(f"Day 7 Part 1 Result is: {result_fuel}")


# ## Part 2

# In[8]:


def get_fuel(data,hist,data_range,target_distance):
    
    data_max = np.nanmax(data)
    data_min = np.nanmin(data)
    
    where_nonzero = np.where(hist!=0,True,False)
    
    #Make an array of weights
    weights = np.array([np.sum(np.arange(0,dist+1)) for (dist,truthy) in zip(data_range,where_nonzero) if truthy ])

    #Total fuel used at this distance is sum of histogram*weights
    fuel = np.sum(np.absolute(hist[where_nonzero])*weights)

    return fuel
    
def move_crab_submarines_thorough(data):

    #Summarise data in histogram
    hist, _ = np.histogram(data,bins=int(data.max())+1,range=(0,data.max()))
    data_range = np.arange(0,data.max()+1)

    data_max = np.nanmax(data)
    data_min = np.nanmin(data)
    
    distance_and_fuel = np.array([[target_distance, get_fuel(data,hist,np.absolute(data_range-target_distance),target_distance)]                                  for target_distance in range(data_min,data_max+1)])
    loc_min_fuel = np.argmin(distance_and_fuel[:,1])
    
    target_distance = distance_and_fuel[loc_min_fuel,0]
    fuel_used = distance_and_fuel[loc_min_fuel,1]
    
    
    return target_distance, fuel_used


# In[9]:


def fuel(x,c):
    return np.sum(np.arange(0,abs(x-c)+1))

def vec_fuel(vec,c):
    return np.apply_along_axis(fuel,0,vec,c)

def move_crab_submarines_fast(data):
    """ It can be shown mathematically that the gradient of the fuel function applied 
        to our input vector is at its minimum at the mean of the input vector.
        Thus, we can find the mean of our data and search around that value and
        be guaranteed to find the minimum.    
    """
    #Summarise data in histogram
    hist, _ = np.histogram(data,bins=int(data.max())+1,range=(0,data.max()))
    where_nonzero = np.where(hist!=0)[0]
    data_range = np.arange(0,data.max()+1).reshape(1,-1)
    
    init_distance = int(round(np.mean(data),0))
    d1 = init_distance+1
    d2 = init_distance-1
    
    f0 = np.sum(hist[where_nonzero]*vec_fuel(data_range,c=init_distance)[where_nonzero])
    f1 = np.sum(hist[where_nonzero]*vec_fuel(data_range,c=d1)[where_nonzero])
    f2 = np.sum(hist[where_nonzero]*vec_fuel(data_range,c=d2)[where_nonzero])   

    
    distances = np.array([init_distance,d1,d2])
    fuels = np.array([f0,f1,f2])
    min_fuel_index = np.argmin(fuels)

    return distances[min_fuel_index], fuels[min_fuel_index]


# In[10]:


expect_pos_part2 = 5.0
expect_fuel_part2 = 168.0


# In[11]:


test_pos_part2,test_fuel_part2 = move_crab_submarines_thorough(test)

print(test_pos_part2, f"Test Position passed? : {test_pos_part2==expect_pos_part2}")
print(test_fuel_part2, f"Test Fuel passed? : {test_fuel_part2==expect_fuel_part2}")


# In[12]:


test_pos_part2,test_fuel_part2 = move_crab_submarines_fast(test)

print(test_pos_part2, f"Test Position passed? : {test_pos_part2==expect_pos_part2}")
print(test_fuel_part2, f"Test Fuel passed? : {test_fuel_part2==expect_fuel_part2}")


# In[13]:


result_pos_part2,result_fuel_part2 = move_crab_submarines_fast(data)

print()
print(f"Day 7 Part 2 Result is: {result_pos_part2,result_fuel_part2}")


# In[14]:


result_pos_part2,result_fuel_part2 = move_crab_submarines_thorough(data)

print()
print(f"Day 7 Part 2 Result is: {result_pos_part2,result_fuel_part2}")


# In[ ]:




