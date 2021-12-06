#!/usr/bin/env python
# coding: utf-8

# # Advent of Code 2021
# ## Day 5
# 
# A.T.Hannington

# # Part 1

# In[1]:


import numpy as np


# In[23]:


def read_hydrothermal_vent_data(file_path):
    data = []
    with open(file_path,"r") as f:
        for line in f:
            line_split = line.replace("->",",").replace("\n",",").replace(" ","").split(",")

            while "" in line_split:
                line_split.remove("")
            if not line_split:
                pass
            else:
                data.append(line_split)

    data = np.array(data).astype("int32").reshape(-1,2,2) 
    
    return data


# In[30]:


file_path = "day5_test_input.txt"              

test = read_hydrothermal_vent_data(file_path)
print(test)


# In[34]:


def setup_seamap(data):
    xmax = np.nanmax(data[:,:,0])
    ymax = np.nanmax(data[:,:,1])
    seamp = np.full(shape=(xmax+1,ymax+1),fill_value=0)
    return seamp


# In[37]:


test_seamap = setup_seamap(test)
print(np.shape(test_seamap))


# In[143]:


def populate_seamap(data,seamap,mode="horizontal_vertical"):
    _seamap = seamap.copy()
    for line in data:
        x1,y1,x2,y2 = line[0,0], line[0,1], line[1,0], line[1,1]
        if mode == "horizontal_vertical":
            if (x1 == x2)|(y1 == y2):
                xmin = min(x1,x2)
                xmax = max(x1,x2)+1
                ymin = min(y1,y2) 
                ymax = max(y1,y2)+1
                
                _seamap.T[xmin:xmax,ymin:ymax] += 1
        elif mode == "full":
            xmin = min(x1,x2)
            xmax = max(x1,x2)+1
            ymin = min(y1,y2) 
            ymax = max(y1,y2)+1
            
            if (x1 == x2)|(y1 == y2):
                # Do horizontal and vertical
                _seamap.T[xmin:xmax,ymin:ymax] += 1
            else:
                # Do diagonals
                #  Sign to accomodate for negative ranges
                #   Sign in stop position to accomodate for stop val not being included
                #    and relevant adjustment. e.g. np.aranage(3,2,-1) = np.array([3])
                for (xx,yy) in zip(np.arange(x1,x2+np.sign(x2-x1),np.sign(x2-x1)),np.arange(y1,y2+np.sign(y2-y1),np.sign(y2-y1))):
                    _seamap.T[xx,yy] += 1
        else:
            raise ValueError("Mode can only be 'horizontal_vertical' or 'full' ")

    return _seamap


# In[144]:


np.arange(3,2+np.sign(-1),-1)


# In[145]:


test_seamap_populated = populate_seamap(test,test_seamap,mode="horizontal_vertical")
print(test_seamap_populated)


# In[146]:


expect = 5


# In[147]:


test_score = np.shape(np.where(test_seamap_populated>=2)[0])[0]
print(test_score, f"Test passed? : {test_score==expect}")


# ### Run on data

# In[148]:


file_path = "day5_input.txt"              

data = read_hydrothermal_vent_data(file_path)
print(np.shape(data))


# In[149]:


data_seamap = setup_seamap(data)
print(np.shape(data_seamap))


# In[150]:


data_seamap_populated = populate_seamap(data,data_seamap,mode="horizontal_vertical")
print(data_seamap_populated)


# In[151]:


result = np.shape(np.where(data_seamap_populated>=2)[0])[0]
print()
print(f"Day 5 Part 1 Result is: {result}")


# ## Part 2

# In[152]:


test_seamap_populated_part2 = populate_seamap(test,test_seamap,mode="full")
print(test_seamap_populated_part2)


# In[153]:


expect_part2 = 12


# In[154]:


test_score_part2 = np.shape(np.where(test_seamap_populated_part2>=2)[0])[0]
print(test_score_part2, f"Part 2 Test passed? : {test_score_part2==expect_part2}")


# ### Run on data

# In[155]:


data_seamap_populated_part2 = populate_seamap(data,data_seamap,mode="full")
print(data_seamap_populated_part2)


# In[156]:


result_part2 = np.shape(np.where(data_seamap_populated_part2>=2)[0])[0]
print()
print(f"Day 5 Part 2 Result is: {result_part2}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




