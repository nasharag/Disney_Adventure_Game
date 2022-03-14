"""A collection of functions for doing my project."""

def StartGame():
    """Starts the adventure game.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    
    """
    
    print('Welcome To My Disney Themed Adventure Game!')
    
    play = input('Would you like to play?(yes/no) ')
    
    friends_list = ['Sleeping Beauty', 'Snow White', 'Belle', 'Tiana', 'Rapunzel']
    
    found_friends = []
    
    initial_hp = 10
    
    score = 0
    
    if play == 'yes':
        
        print('\nWonderful! Throughout this adventure you will be faced with many decisions \nthat will affect the outcome of your adventure.')
        
        character = input('\nChoose your character: Mickey Mouse, Minnie Mouse, Goofy, Donald Duck, Daisy Duck, Pluto \nType out name as shown: ')
        
        print('\nHey pal! Seems like the Princesses have gone missing somewhere in the Magic Kingdom. \nLets go find them!')
        
        # first decision
        decision1 = input('\nWalking through the castle you come across Maleficent! \nYou notice that one of the Princesses is under a spell \nthat puts them in a death like sleep. \nIt\'s Sleeping Beauty! Do you fight Maleficent or not? \n(fight/evade) ')
        
        # correct choice for decision1
        if decision1 == 'fight':
            
            # decision is True, affects health (player_health)
            decision = True
            
            current_hp = player_health(initial_hp, decision)
            
            print(f'\n{character}\'s remaining health: {current_hp}')
            
            # player score increases by 3
            score += 3
            
            # append friend found to empty list found_friends
            found_friends.append('Sleeping Beauty')
            
            # narrative
            print('\nPhew! You were able to defeat Maleficent and save the Princess! \nYou find a gem left behind and hold onto it.')
            
            # second decision
            decision2 = input('\nYou are walking through Fantasyland and you come across the Evil Queen. \nShe offers you an apple but you notice Snow White \nlying on the ground behind her. Do you take the apple? \n(yes/no) ')
            
        # wrong choice for decision1
        elif decision1 == 'evade':
                
            # decision is False, affects health (player_health)
            decision = False
            
            current_hp = player_health(initial_hp, decision)
            
            print(f'\n{character}\'s remaining health: {current_hp}')
                
            print('\nYou decided that Maleficent was too frightening and evaded the situation. \nI hope Sleeping Beauty will be okay on her own!')
                
            # second decision
            decision2 = input('\nYou are walking through Fantasyland and you come across the Evil Queen. \nShe offers you an apple but you notice Snow White \nlying on the ground behind her. Do you take the apple? \n(yes/no) ')
            
        # correct choice for decision2
        if decision2 == 'no':
                
            decision = True
            
            current_hp = player_health(current_hp, decision)
            
            print(f'\n{character}\'s remaining health: {current_hp}')
            
            score += 3
            
            found_friends.append('Snow White')
            
            print('\nAfter rejecting the apple. The Evil Queen turns into an old frail woman and dies. \nThus the spell has been broken and Snow White awakens. \nOut of the corner of your eye, you also find a gem that belongs to one of the Seven Dwarfs. \nSnow White tells you to keep the gem.')
            
            # third decision
            decision3 = input('\nYou continue your journey into Adventureland. You see Gaston trying to force Belle to marry him. \nDo you challenge him to a push-up contest to save Belle or let him marry Belle against her will? \n(challenge/engagement) ')
        
        # wrong choice for decision2
        elif decision2 == 'yes':
            
            decision = False
            
            current_hp = player_health(current_hp, decision)
            
            print(f'\n{character}\'s remaining health: {current_hp}')
            
            print('\nYou forgot your lunch today and foolishly took the apple from the Evil Queen \nand slowly start to fall under her spell. You wake up a few hours later, both Snow White \nand the Evil Queen were nowhere to be found.')
            
            # third decision
            decision3 = input('\nYou continue your journey into Adventureland. You see Gaston trying to force Belle to marry him. \nDo you challenge him to a push-up contest to save Belle or let him marry Belle against her will? \n(challenge/engagement) ')
            
        # correct choice for decision3
        if decision3 == 'challenge':
            
            decision = True
            
            current_hp = player_health(current_hp, decision)
            
            print(f'\n{character}\'s remaining health: {current_hp}')
            
            score += 3
            
            found_friends.append('Belle')
            
            print('\nYou showed Gaston who has the muscles and beat him in the contest! Gaston gives you a gem, \nthe gem that he was going to use to propose to Belle. He lets you keep it fair and square \nand Belle is relieved to have him off her back for a while.')
            
            # fourth decision
            decision4 = input('\nYou venture into New Orleans Square and find Tiana being hypnotized \nby Dr. Facilier. In order to save Tiana, you make a deal with Dr. Facilier \nto do a tarot card reading. He presents you with two cards and you must choose one. \nDo you choose the left card or the right card? \n(left/right) ')
            
        # wrong choice for decision3
        elif decision3 == 'engagement':
            
            decision = False
            
            current_hp = player_health(current_hp, decision)
            
            print(f'\n{character}\'s remaining health: {current_hp}')
            
            print('\nYou decide to let true love flourish and give the lovebirds their space and carry on with your adventure.')
            
            # fourth decision
            decision4 = input('\nYou venture into New Orleans Square and find Tiana being hypnotized \nby Dr. Facilier. In order to save Tiana, you make a deal with Dr. Facilier \nto do a tarot card reading. He presents you with two cards and you must choose one. \nDo you choose the left card or the right card? \n(left/right) ')
            
        # correct choice for decision4
        if decision4 == 'right':
            
            decision = True
            
            current_hp = player_health(current_hp, decision)
            
            print(f'\n{character}\'s remaining health: {current_hp}')
            
            score += 3
            
            found_friends.append('Tiana')
            
            print('\nYou pick the right card which grants Tiana her freedom. \nThe card also possessed a hidden gem! You keep the gem \nand continue with your journey.')
            
            # fifth decision
            decision5 = input('\nYou make your way to Frontierland. You see Rapunzel\'s step mother trying \nto lock her in a tower. Do you rescue her? \n(rescue/walk away) ')
        
        # wrong choice for decision4
        elif decision4 == 'left':
            
            decision = False
            
            current_hp = player_health(current_hp, decision)
            
            print(f'\n{character}\'s remaining health: {current_hp}')
            
            print('\nYou chose the left card and Dr. Facilier laughs menacingly, \nand says that Tiana will never be freed. You run away in fear and barely escape his clutches.')
            
            # fifth decision
            decision5 = input('\nYou make your way to Frontierland. You see Rapunzel\'s step mother trying \nto lock her in a tower. Do you rescue her? \n(rescue/walk away) ')
        
        # correct choice for decision5
        if decision5 == 'rescue':
            
            decision = True
            
            current_hp = player_health(current_hp, decision)
            
            print(f'\n{character}\'s remaining health: {current_hp}')
            
            score += 3
            
            found_friends.append('Rapunzel')
            
            print('\nYou managed to rescue Rapunzel from her evil step mother\'s grasp. \nYou both celebrate and Rapunzel gives you a gift for rescuing her. You accept the gift \nand it turns out to be a beautiful gem. You thank Rapunzel and walk through \nFrontierland and make your way back to the castle. You see a bed fit for a King! or Queen! \nYou make yourself comfortable and fall into a deep sleep.')
            
        # wrong choice for decision5
        elif decision5 == 'walk away':
            
            decision = False
            
            current_hp = player_health(current_hp, decision)
            
            print(f'\n{character}\'s remaining health: {current_hp}')
            
            print('\nYou decide to walk away and pretend like you saw nothing. After going \nfurther into Frontierland, you eventually find yourself back at the castle. You wander inside and find \na comfy bed to sleep in and fall into a deep sleep.')
            
        print(f'\nLets see how you did!\n')
        
        # display players score with get_score()
        print(get_score(score, character))
        
        # displays the names from list found_friends
        print(friends_found(friends_list, found_friends))
        
        # ending print statement
        print('\nThis is the end of your magical adventure! Thanks for playing! \nSee ya real soon!\n')
        
        # call function PlayAgain() to ask user if they want to restart
        PlayAgain()
        
    # if play == 'no' game ends
    else:
        
        print('\nThat\'s to bad, well I hope to see ya real soon! Ta-Ta for now!')
                
                

def friends_found(list1, list2):
    """Compares the items of two lists for similarity.
    
    Parameters
    ----------
    list1 : list
        First list, filled with names from in-game.
    list2 : list
        Second list to be compared with list1, list2
        filled with names from decisions in-game
        
    Returns
    -------
    f-string : str, joined list (names)
        if condition met : at least one list2 elem equals list1 elem.
    string : str
        if condition met : list2 is empty.
    
    """
    
    # empty list 
    output_list = []
    
    # loop to iterate over the names in list2
    for i in list2:
        
        # loop to iterate over the names in list1
        for item in list1:
            
            # conditional to determine if the names from list2 are equal to the names of list1
            if i == item:
                
                # if the names are equal, then the matching names from each list will be appended to output_list
                output_list.append(i)
                
    if len(output_list) >= 1:
        
        # joins the strings/names from output_list by a comma
        names = (', '.join(output_list))
        
        # returns names joined list
        return f'\nOut of the five Princesses, you were able to find and help:\n{names}'
    
    elif len(output_list) == 5:
        
        # joins the strings/names from output_list by a comma
        names = (', '.join(output_list))
        
        # returns names joined list
        return f'\nOut of the five Princesses, you were able to find and help:\n{names} \nWow! You helped and found all the Princesses!'
    
    else:
                
        # returns string
        return '\nYou were unable to help any of the Princesses.'
    

def get_score(score, character):
    """Displays a string based on players score in-game, at end of game.
    
    Parameters
    ----------
    score : int
        Number recieved at end of game.
    character : str
        player name inputed at beginning of game.
        
    Returns
    -------
    f-string : str, character, score
        if condition met : returns string with score
        and players name defined at beginning of game.
    
    """
    
    # max_score is the most amount of points on can get in the game
    max_score = 15
    
    # if score is equal to max_score
    if score == max_score:
        
        # returns message and ending score
        return f'Congratulations {character}! You made all the right decisions! Your score is {score}.'
    
    # else if score is greater than or equal to 10 and less than max_score
    elif score >= 10 and score < max_score:
        
        return f'Great job {character}! You almost got a perfect score. Your score is {score}.'
    
    # else if score is greater than or equal to 5 and less than 10
    elif score >= 5 and score < 10:
        
        return f'Made a few mistakes along the way but I know you can do better {character}.\nYour score is {score}.'
    
    # else if score is less than 5
    elif score < 5:
        
        return f'I know you can do better {character}. Your score is {score}.'
    

def player_health(hp, decision = None):
    """Keeps track of players health throughout
       game based on decisions made in-game.
       
    Parameters
    ----------
    hp : int
        Number that represents players health,
        initialized at beginning of game.
    decision : bool, default None
        decision is updated in-game depending
        on choices made in-game.
        
    Returns
    -------
    hp : int
        if condition met : hp remains the same.
    hp : int
        if condition met : hp remains the same.
    hp : int
        if condition met : hp decreases by 2.
    
    """
    
    # variable health is the max amount of health player can have
    health = 10
    
    # if decision is True and hp is equal to health, hp remains the same
    if decision == True and hp == health:
        
        #return remaining hp (health points)
        return hp
    
    # else if decision is True and hp is less than health hp remains constant
    elif decision == True and hp < health:
        
        return hp
    
    # else decision is False hp decreases by 2
    else:
        
        hp -= 2
        
        return hp
    
def PlayAgain():
    """Asks player if they would like to play again.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    start() : function
        if condition met : starts game over.
    string : str
        if condition met : terminates game
    
    """
    
    answer = input('\nWould you like to go on another adventure?(yes/no) ')
    
    if answer == 'yes':
        
        StartGame()
        
    else:
        
        return '\nThat\'s too bad, well I hope to see ya real soon! Goodbye!'
    
    