#!/usr/bin/env python
# coding: utf-8

# # Advent of Code 2021
# ## Day 1
# 
# A.T.Hannington

# # Part 1

# In[1]:


import numpy as np


# In[2]:


data = np.genfromtxt('day1_input.txt')


# In[3]:


def get_diff(a):
    diff = np.array([x-y for (x,y) in zip(a[1:],a[:-1])])
    return diff


# In[4]:


test = np.array([
199,
200,
208,
210,
200,
207,
240,
269,
260,
263])


# In[5]:


expect = 7


# In[13]:


test_result = np.shape(np.where(get_diff(test)>0)[0])[0]
print(test_result, f"Test passed? : {test_result==expect}")


# ### Run on data

# In[86]:


diff_arr = get_diff(data)
where_increase = np.where(diff_arr>0)[0]
print(f"The number of increases (Day 1 Part 1 Result) is: {np.shape(where_increase)[0]}")


# ## Part 2

# In[87]:


def get_sum_delta_window(data,delta_window=2):
    out = np.array([sum(data[ii:jj]) for (ii,jj) in                     zip(list(range(0,len(data)+1,1)),                        list(range(delta_window,len(data)+1,1)))])
    return out


# In[88]:


delta_window_part2 = 3
expect_part2 = 5


# In[89]:


test_result = np.shape(np.where(get_diff(get_sum_delta_window(test,delta_window=delta_window_part2))>0)[0])[0]
print(test_result, f"Test passed? : {test_result==expect_part2}")


# ### Run on data

# In[90]:


diff_arr = get_diff(get_sum_delta_window(data,delta_window=delta_window_part2))
where_increase = np.where(diff_arr>0)[0]
print(f"The number of increases (Day 1 Part 2 Result) is: {np.shape(where_increase)[0]}")


# In[ ]:




