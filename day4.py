#!/usr/bin/env python
# coding: utf-8

# # Advent of Code 2021
# ## Day 4
# 
# A.T.Hannington

# # Part 1

# In[1]:


import numpy as np


# In[2]:


def read_bingo_data(file_path):
    data_numbers = []
    data_boards = []
    with open(file_path,"r") as f:
        for ind,line in enumerate(f):
            if ind == 0:
                line_split = line.replace("\n","").split(",")
                while "" in line_split:
                    line_split.remove("")
                data_numbers = np.array(line_split)
            else:
                line_split = line.replace("\n"," ").split(" ")
                while "" in line_split:
                    line_split.remove("")
                if not line_split:
                    pass
                else:
                    data_boards.append(line_split)

    data_numbers = data_numbers.astype("int32")
    data_boards = np.array(data_boards).astype("int32").reshape(-1,5,5) 
    
    return data_numbers, data_boards


# In[3]:


file_path = "day4_input.txt"              

data_numbers, data_boards = read_bingo_data(file_path)
print(data_numbers)
print()
print(data_boards)


# In[4]:


file_path = "day4_test_input.txt"              

test_numbers, test_boards = read_bingo_data(file_path)
print(test_numbers)
print()
print(test_boards)


# In[5]:


def create_scorecards(data_boards):
    scorecards = np.full(shape=np.shape(data_boards),fill_value=False)
    game_dict = {"Board":data_boards,"Scorecard":scorecards}
    print("Generated game_dict!")
    print(f"game_dict keys : {list(game_dict.keys())}")
    
    return game_dict


# In[6]:


test_game_dict = create_scorecards(test_boards)


# In[7]:


def check_for_winners(game_dict,a_board_axes=[1,2]):
        where_winners = np.where(np.all(game_dict['Scorecard']==True,axis=a_board_axes[0])                                |np.all(game_dict['Scorecard']==True,axis=a_board_axes[1]))
        winner = np.unique(where_winners[0])
        winners_bool = np.any(where_winners)
        
        return winner,winners_bool


# In[8]:


winner_test = np.full(shape=(5,5),fill_value=True)
loser_test = np.full(shape=(5,5),fill_value=False)
winner_test_scorecards = np.array([loser_test,winner_test,loser_test])
winner_test_game_dict = {"Scorecard":winner_test_scorecards}


# In[9]:


check_for_winners(winner_test_game_dict)


# In[10]:


def play_bingo(numbers,game_dict,winner_type="first"):
    _game_dict = {}
    for key in game_dict.keys():  
        _game_dict[key] =  game_dict[key].copy()
    #Find which axes make up a board for check for winners
    board_shape = np.shape(game_dict['Board'])
    a_board_axes = []
    for ind,ax_size in enumerate(board_shape):
        if ax_size == 5:
            a_board_axes.append(ind)

    #Set default in case 5 boards are played        
    if len(a_board_axes)>2:
        a_board_axes = [1,2]
    
    print(f"Let's Play Bingo! Winners type is '{winner_type}'")
    
    winners_bool = False
    
    #Start playing
    if winner_type == "first":
        ind =0
        while (winners_bool == False):
            value = numbers[ind]
            _game_dict['Scorecard'][np.where(_game_dict['Board']==value)] = True
            where_winners,winners_bool = check_for_winners(_game_dict,a_board_axes)

            ind +=1
            if ind>len(numbers):
                raise ValueError("No winners found!")

        #Get winning board
        winner = {}
        for key in _game_dict.keys():
            if key not in list(winner.keys()):
                winner.update({key:_game_dict[key][where_winners]})
            else:
                raise ValueError("More than one winner found!")        
                
                
                
    elif winner_type=="last":
        
        _game_dict_diminishing = {}
        for key in game_dict.keys():  
            _game_dict_diminishing[key] =  game_dict[key].copy()
        
        ind = 0
        
        available_axes = np.array(list(range(0,np.shape(np.shape(game_dict['Board']))[0])))

        boards_axis = np.array(available_axes[~np.isin(available_axes,np.array(a_board_axes))]).astype("int32")        
    
        winners = []

        for _value in numbers:
            _game_dict_diminishing['Scorecard'][np.where(_game_dict_diminishing['Board']==_value)] = True
            where_winners,winners_bool = check_for_winners(_game_dict_diminishing,a_board_axes)

            if winners_bool ==True:
                where_winners = where_winners
                value = _value
                
                #Get winning boards
                _winner = {}
                for key in _game_dict.keys():
                    _winner.update({key:_game_dict_diminishing[key][where_winners]})
                
                winners.append(_winner)
                
                #Remove previous winners from the game
                for key,dat in _game_dict_diminishing.items():
                    n_remaining_boards = np.shape(dat)[boards_axis[0]]
                    remaining = np.where(~np.isin(np.arange(0,n_remaining_boards),where_winners))
                    _game_dict_diminishing.update({key : dat[remaining]})
            
            ind +=1
            if ind>len(numbers):
                raise ValueError("No winners found!")
        
        #Get last board to win
        winner = winners[-1]
    else:
        raise ValueError("kwarg winner_type must be first or last!")
        
    
    return winner,value


# In[11]:


test_winner_dict, test_winning_value = play_bingo(test_numbers,test_game_dict)
print(test_winner_dict, test_winning_value)


# In[12]:


def get_score(winner_dict,winning_value):
    sum_of_marked = np.sum(winner_dict['Board'][np.where(winner_dict['Scorecard']==False)])
    return sum_of_marked*winning_value


# In[13]:


expect_score = 4512


# In[14]:


test_score = get_score(test_winner_dict, test_winning_value)
print(test_score, f"Test passed? : {test_score==expect_score}")


# ### Run on data

# In[15]:


game_dict = create_scorecards(data_boards)
winner_dict, winning_value = play_bingo(data_numbers,game_dict)
print(winner_dict, winning_value)
result = get_score(winner_dict, winning_value)
print()
print(f"Day 4 Part 1 Result is: {result}")


# ## Part 2

# In[16]:


expect_score_part2 = 1924


# In[17]:


test_part2_winner_dict, test_part2_winning_value = play_bingo(test_numbers,test_game_dict,winner_type='last')
print(test_part2_winner_dict, test_part2_winning_value)
test_part2_result = get_score(test_part2_winner_dict, test_part2_winning_value)
print()
print(test_part2_result, f"Test passed? : {test_part2_result==expect_score_part2}")


# In[18]:


winner_dict_part2, winning_value_part2 = play_bingo(data_numbers,game_dict,winner_type='last')
print(winner_dict_part2, winning_value_part2)
result_part2 = get_score(winner_dict_part2, winning_value_part2)
print()
print(f"Day 4 Part 2 Result is: {result_part2}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




