"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import StartGame, friends_found, get_score, player_health, PlayAgain
##
##

def test_StartGame():

    assert callable(StartGame)

    
def test_friends_found():

    friends_list = ['Sleeping Beauty', 'Snow White', 'Belle', 'Tiana', 'Rapunzel']
    found_friends = ['Sleeping Beauty', 'Belle']
    
    assert type(friends_list) == list
    assert len(friends_list) == 5
    assert type(found_friends) == list
    assert len(found_friends) == 2
    assert callable(friends_found)
    
    
def test_get_score():
    
    score = 0
    assert type(score) == int
    score += 3
    assert score == 3
    assert callable(get_score)
    
    
def test_player_health():
    
    initial_hp = 10
    decision = True
    assert player_health(initial_hp, decision) == 10
    decision = False
    assert player_health(initial_hp, decision) == 8
    assert callable(player_health)
    
    
    
def test_PlayAgain():
    
    assert callable(PlayAgain)
    



                 
    