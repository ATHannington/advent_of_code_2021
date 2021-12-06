#!/usr/bin/env python
# coding: utf-8

# # Advent of Code 2021
# ## Day 2
# 
# A.T.Hannington

# # Part 1

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.read_table('day2_input.txt',sep=" ",names=["direction","values"])


# In[3]:


data


# In[4]:


test = pd.DataFrame({"direction": np.array(["forward", "down", "forward", "up", "down", "forward"]),                     "values": np.array([5,5,8,3,8,2])                    })
test


# In[5]:


def move_submarine(direc, vals):
    vals = float(vals)
    direc_sign = {"forward": +1., "down":+1., "up": -1.}
    
    horizontal = 0.
    depth = 0.
    
    if direc == "forward":
        horizontal = direc_sign[direc] * vals
    else:
        depth = direc_sign[direc] * vals
    return pd.Series({"depth":depth, "horizontal":horizontal})


# In[6]:


expect = 150


# In[7]:


test_result = test.copy()
test_result[["depth","horizontal"]] = test_result[["direction","values"]].apply(lambda x: move_submarine(x[0],x[1]),axis=1)
test_result_sum = test_result[["depth","horizontal"]].sum()
test_result_multiplied = test_result_sum["depth"]*test_result_sum["horizontal"]

print(test_result_multiplied, f"Test passed? : {test_result_multiplied==expect}")


# In[8]:


result = data.copy()
result[["depth","horizontal"]] = result[["direction","values"]].apply(lambda x: move_submarine(x[0],x[1]),axis=1)
result_sum = result[["depth","horizontal"]].sum()
result_multiplied = result_sum["depth"]*result_sum["horizontal"]

print(f"The number of increases (Day 2 Part 1 Result) is: {result_multiplied}")


# # Part 2

# In[9]:


expect_part2 = 900.


# In[10]:


def move_submarine_alter_depth(horizontal,run_tot_depth):
    depth = run_tot_depth * horizontal
    return pd.Series({"depth":depth})


# In[11]:


test_result["run_tot_depth"] = test_result["depth"].cumsum()
test_result[["depth_part2"]] = test_result[["horizontal","run_tot_depth"]].apply(lambda x: move_submarine_alter_depth(x[0],x[1]),axis=1)
test_result_sum = test_result[["depth_part2","horizontal"]].sum()
test_result_multiplied = test_result_sum["depth_part2"]*test_result_sum["horizontal"]

print(test_result_multiplied, f"Test passed? : {test_result_multiplied==expect_part2}")


# In[12]:


result["run_tot_depth"] = result["depth"].cumsum()
result[["depth_part2"]] = result[["horizontal","run_tot_depth"]].apply(lambda x: move_submarine_alter_depth(x[0],x[1]),axis=1)
result_sum = result[["depth_part2","horizontal"]].sum()
result_multiplied = result_sum["depth_part2"]*result_sum["horizontal"]

print(f"The number of increases (Day 2 Part 2 Result) is: {result_multiplied}")


# In[ ]:




