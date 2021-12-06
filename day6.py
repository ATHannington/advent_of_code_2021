#!/usr/bin/env python
# coding: utf-8

# # Advent of Code 2021
# ## Day 6
# 
# A.T.Hannington

# # Part 1

# In[1]:


import numpy as np


# In[2]:


file_path = "day6_test_input.txt"              

test = np.genfromtxt(file_path,delimiter=",").astype("int32")
print(test)


# In[3]:


def progress_population_of_lanternfish(data,days,countdown_mature=6,countdown_young=8):
    _data = data.copy()
    for day in range(0,days):
        where_reproduce = np.where(_data==0)[0]
        n_new_fish = int(np.shape(where_reproduce)[0])
        if n_new_fish>0:
            _data[where_reproduce] = countdown_mature+1
            new_fish = np.full(shape=(n_new_fish),fill_value=countdown_young+1)
            _data = np.concatenate((_data,new_fish),axis=0)
        
        _data -= 1
    return _data


# In[4]:


expect_n_days = [2,18,80]
expect = [6,26,5934]


# In[5]:


progress_population_of_lanternfish(test,days=2,countdown_mature=6,countdown_young=8)


# In[6]:


for (ind,(exp,n_days)) in enumerate(zip(expect,expect_n_days)):
    test_result = int(np.shape(progress_population_of_lanternfish(test,days=n_days,countdown_mature=6,countdown_young=8))[0])
    test_truthy = test_result==exp
    print(test_result, f"Test {ind} passed? : {test_truthy}")
    if test_truthy is False:
        break


# ### Run on data

# In[7]:


file_path = "day6_input.txt"              

data = np.genfromtxt(file_path,delimiter=",").astype("int32")
print(data)


# In[8]:


n_days = 80
result = int(np.shape(progress_population_of_lanternfish(data,days=n_days,countdown_mature=6,countdown_young=8))[0])

print()
print(f"Day 6 Part 1 Result is: {result}")


# ## Part 2

# In[9]:


def setup_lanternfish_record(data,countdown_mature=6,countdown_young=8):
    
    #Check assumptions on max age hold
    maxage_data = np.nanmax(data)
    if (maxage_data > countdown_mature):
        raise ValueError("Max age of fish shouldn't exceed 'countdown_mature'!")
    else:
        maxage = max(maxage_data,countdown_mature)
        
    out = {}    
    for age in range(0,maxage+1):
        n_fish = int(np.shape(np.where(data==age)[0])[0])
        out.update({age:n_fish})
        
    #Check assumptions on youth age
    if (countdown_young < countdown_mature):
        raise ValueError("Max days until offspring of Young fish (countdown_young)" +        "shouldn't be less than max days until offspring of Mature fish (countdown_mature)")

    #Now add in counting for young fish:
    for age in range(maxage+1,countdown_young+1):
        out.update({age:n_fish})
    return out


# In[10]:


test_records_dict = setup_lanternfish_record(test,countdown_mature=6,countdown_young=8)
print(test)
print(test_records_dict)


# In[11]:


def progress_population_of_lanternfish_v2(records_dict,days,countdown_mature=6,countdown_young=8):
    _records_dict = records_dict.copy()
    if (max(list(_records_dict.keys()))!=countdown_young):
        raise ValueError("countdown_young passed is does not match that passed to 'setup_lanternfish_record()'!")
   
    _records_dict_old = _records_dict.copy()
    for day in range(0,days):
        
        _records_dict_new = _records_dict_old.copy()

        #Age population by one day
        for age in range(0,countdown_young,1):
            _records_dict_new.update({age:_records_dict_old[age+1]})
            

        #If any spawning fish yesterday, generate offspring and reset mature fish of today:
        if _records_dict_old[0]>0:
            _records_dict_new.update({countdown_young:_records_dict_old[0]})
            _records_dict_new.update({countdown_mature:_records_dict_old[0]+_records_dict_old[countdown_mature+1]})
        else:
            #Need to reset 'countdown_young' bin to zero when no new fish
            _records_dict_new.update({countdown_young:0})


        _records_dict_old = _records_dict_new.copy()
    return _records_dict_new


# In[12]:


def count_fish(records_dict):
    count = 0
    for age,n_fish in records_dict.items():
        count += n_fish
        
    return count


# In[13]:


print(test_records_dict)

test_results_dict = progress_population_of_lanternfish_v2(test_records_dict,days=18,countdown_mature=6,countdown_young=8)
test_results = count_fish(test_results_dict)

print(test_results_dict)
print(test_results)


# In[14]:


expect_n_days = [2,18,80,256]
expect = [6,26,5934,26984457539]


# In[15]:


for (ind,(exp,n_days)) in enumerate(zip(expect,expect_n_days)):
    test_results_dict = progress_population_of_lanternfish_v2(test_records_dict,days=n_days,countdown_mature=6,countdown_young=8)
    test_result = count_fish(test_results_dict)
    test_truthy = test_result==exp
    print(test_result, f"Test {ind} passed? : {test_truthy}")
    if test_truthy is False:
        break


# In[18]:


n_days = 256
data_records_dict = setup_lanternfish_record(data,countdown_mature=6,countdown_young=8)

results_dict = progress_population_of_lanternfish_v2(data_records_dict,days=n_days,countdown_mature=6,countdown_young=8)

result = count_fish(results_dict)

print()
print(f"Day 6 Part 2 Result is: {result}")


# In[ ]:




