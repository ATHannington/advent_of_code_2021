#!/usr/bin/env python
# coding: utf-8

# # Advent of Code 2021
# ## Day 3
# 
# A.T.Hannington

# # Part 1

# In[1]:


import numpy as np


# In[2]:


data = np.genfromtxt('day3_input.txt',dtype=str)
print(np.shape(data))


# In[3]:


def split_binary(data):
    out = np.array([x[ii] for x in data for ii in range(0,len(x))]).reshape(len(data),-1).astype("int32")
    return out


# In[4]:


def get_common_column_count(row):
    row_equals_one = np.where(row==1)[0]
    row_equals_zero = np.where(row==0)[0]
    
    count_one = np.shape(row[row_equals_one])[0]
    count_zero = np.shape(row[row_equals_zero])[0]

    return count_one, count_zero


# In[5]:


def get_gamma_epsilon_as_binary(data):
    
    gamma = np.array([])
    epsilon = np.array([])
    for col in data.T:
        
        count_one, count_zero = get_common_column_count(col)
        
        if count_one>count_zero:
            gamma = np.concatenate((gamma,np.array([1])),axis=0)
            epsilon = np.concatenate((epsilon,np.array([0])),axis=0)
        else:
            gamma = np.concatenate((gamma,np.array([0])),axis=0)
            epsilon = np.concatenate((epsilon,np.array([1])),axis=0)
            
    gamma = gamma.astype(int).astype(str)
    gamma = "".join(gamma.tolist())
    
    epsilon = epsilon.astype(int).astype(str)
    epsilon = "".join(epsilon.tolist())
    return gamma, epsilon


# In[6]:


def binary_to_numeric(string):
    string = "0b" + string
    return int(string, base=2)


# In[7]:


test = np.array([
"00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010",])


# In[8]:


expect_binary_gamma = "10110"
expect_numeric_gamma = 22

expect_binary_epsilon = "01001"
expect_numeric_epsilon  = 9

expect_power = expect_numeric_gamma*expect_numeric_epsilon


# In[9]:


test_split = split_binary(test)
test_binary_gamma, test_binary_epsilon = get_gamma_epsilon_as_binary(test_split)

print(test_binary_gamma, f"Gamma Binary Test passed? : {test_binary_gamma==expect_binary_gamma}")
print(test_binary_epsilon, f"Epsilon Binary Test passed? : {test_binary_epsilon==expect_binary_epsilon}")


# In[10]:


test_numeric_gamma = binary_to_numeric(test_binary_gamma)
test_numeric_epsilon = binary_to_numeric(test_binary_epsilon)

print(test_numeric_gamma, f"Gamma Numeric Test passed? : {test_numeric_gamma==expect_numeric_gamma}")
print(test_numeric_epsilon, f"Epsilon Numeric Test passed? : {test_numeric_epsilon==expect_numeric_epsilon}")


# In[11]:


test_power = test_numeric_gamma*test_numeric_epsilon

print(test_power, f"Power Test passed? : {test_power==expect_power}")


# ### Run on data

# In[12]:


result_split = split_binary(data)
result_binary_gamma, result_binary_epsilon = get_gamma_epsilon_as_binary(result_split)
result_numeric_gamma, result_numeric_epsilon = binary_to_numeric(result_binary_gamma), binary_to_numeric(result_binary_epsilon)
result = result_numeric_gamma*result_numeric_epsilon
print(f"Day 3 Part 1 Result is: {result}")


# ## Part 2

# In[13]:


def get_ox_co2_row_wise(data,row,flag):
    count_one, count_zero = get_common_column_count(row)
    
    row_equals_one = data[np.where(row==1)[0]]
    row_equals_zero = data[np.where(row==0)[0]]

    if flag == "ox":
        if count_one>count_zero:
            out = row_equals_one
        elif count_one<count_zero:
            out = row_equals_zero  
        else:
            out = row_equals_one    
    elif flag == "co2":
        if count_one>count_zero:
            out = row_equals_zero
        elif count_one<count_zero:
            out = row_equals_one
        else:
            out = row_equals_zero  
    else:
        raise ValueError("Flag must equal 'ox' or 'co2'")
    return out


# In[14]:


def get_ox_co2_binary(data):
    nox = np.shape(data)[0]
    ox = data.copy()

    ind = 0 
    while (nox>1):
        ox = get_ox_co2_row_wise(ox,ox.T[ind],"ox")
        nox = np.shape(ox)[0]
        ind+=1

    nco2 = np.shape(data)[0]    
    co2 = data.copy()

    ind = 0 
    while (nco2>1):
        co2 = get_ox_co2_row_wise(co2,co2.T[ind],"co2")
        nco2 = np.shape(co2)[0]
        ind+=1
        
    ox = ox.flatten().astype(int).astype(str)
    ox = "".join(ox.tolist())
    
    co2 = co2.flatten().astype(int).astype(str)
    co2 = "".join(co2.tolist())

    return ox, co2


# In[15]:


expect_binary_ox = "10111"
expect_numeric_ox = 23

expect_binary_co2 = "01010"
expect_numeric_co2  = 10

expect_life_support = expect_numeric_ox*expect_numeric_co2


# In[16]:


test_binary_ox, test_binary_co2 = get_ox_co2_binary(test_split)

print(test_binary_ox, f"ox Binary Test passed? : {test_binary_ox==expect_binary_ox}")
print(test_binary_co2, f"co2 Binary Test passed? : {test_binary_co2==expect_binary_co2}")


# In[17]:


test_numeric_ox = binary_to_numeric(test_binary_ox)
test_numeric_co2 = binary_to_numeric(test_binary_co2)

print(test_numeric_ox, f"Gamma Numeric Test passed? : {test_numeric_ox==expect_numeric_ox}")
print(test_numeric_co2, f"Epsilon Numeric Test passed? : {test_numeric_co2==expect_numeric_co2}")


# In[18]:


test_life_support = test_numeric_ox*test_numeric_co2

print(test_life_support, f"Life Support Test passed? : {test_life_support==expect_life_support}")


# ### Run on data

# In[19]:


result_binary_ox, result_binary_co2 = get_ox_co2_binary(result_split)
result_numeric_ox, result_numeric_co2 = binary_to_numeric(result_binary_ox), binary_to_numeric(result_binary_co2)
result = result_numeric_ox *result_numeric_co2 
print(f"Day 3 Part 2 Result is: {result}")

