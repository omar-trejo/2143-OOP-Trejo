import random
import abc

"""
@Class: Dice
@Description: 
    Represents a single "die" with X number of sides.
@Methods:
    Roll - Rolls the dice and returns a value between 1 and "number of sides" 
"""
class Dice(object):
    def __init__(self,num_sides=6):
        self.NumSides = num_sides

    def Roll(self):
        return random.randint(1,self.NumSides)  

##############################################################################
##############################################################################

"""
@Class: Pig
@Description: 
    Represents the game of pig (dice game)
@Methods:
    Roll - Rolls the "die" or "dice" and returns a list of rolled values
"""
class Pig(object):
    def __init__(self,num_dice=1,dice_sides=6,skunk_value=1):
        self.NumDice = num_dice
        self.DiceSides = dice_sides
        self.DiceList = []
        self.SkunkValue = skunk_value
        for i in range(self.NumDice):
            self.DiceList.append(Dice(self.DiceSides))
    """
    @Method: Roll
    @Description: 
        One roll in a pig game, with 1 to NumDice per roll
    @Returns: int: [0=skunk value occured, total of all dice otherwise]
    """ 
    def Roll(self):
        scores = []
        for d in self.DiceList:
            scores.append(d.Roll())
            if self.SkunkValue in scores:
                return 0 
        return sum(scores)

##############################################################################
##############################################################################

class Player(object):
    def __init__(self,name,num_dice=1,strategy=('Random',7)):
        self.Name = name        # My name
        self.TotalScore = 0     # Total score
        self.LastScore = 0      # Score on last turn
        self.LastNumRolls = 0   # Last number of rolls
        self.Opponents = {}     # Dict of opponents
        self.NumDice = num_dice
        self.Strategy = strategy[0]
        self.pig = Pig(num_dice)# init pig game 
        self.Strategies = {
                'Target_Score':0,
                'Target_Rolls':0,
                'Sprint_To_Finish':0,
                'Mimic_Opponent':0,
                'Situational':0,
                'Random':0
            }
        self.Strategies[strategy[0]] = strategy[1]
    """
    @Method: AddOpponents
    @Description: Adds an opponent, or list of opponents (as long as it's not me) to a dictionary with name and score.
        Example: {
                   'bob':0.
                   'sue':0
                 }
    
    @Params: [] - Opponents
    @Returns: None
    """
    def AddOpponents(self,opponent):
        # if not type(opponent) == list and not opponent.Name == self.Name:
        #     self.Opponents[opponent.Name] = opponent
        # else:
        for op in opponent:
            if not op.Name == self.Name:
                self.Opponents[op.Name] = op

    """
    @Method: __str__
    @Description: Prints out a nice version of self
    @Returns: string representation
    """
    def __str__(self):
        tmp = " "
        for k,v in self.Opponents.items():
            tmp = tmp + "[" + k + " " + str(v.TotalScore) + "," + str(v.LastScore) + "," + str(v.LastNumRolls) + "] "
        return "Name: %s, TotScore: %s, LastScore: %s, LastNumRolls: %s, Opponents: %s" % (self.Name,self.TotalScore,self.LastScore,self.LastNumRolls,tmp)
        
    """
    @Method: __repr__
    @Description: Calls __str__
    @Returns: a call to __str__
    """
    def __repr__(self):
        return self.__str__()
        

    """
    @Method: SetStrategy
    @Description: Sets the current strategy for the player
    @Params:
        strategy: string 
        value: int    
    @Returns: None
    @Usage:
            SetStrategy('Target_Score',20)
            SetStrategy('Target_Rolls',5)     
            SetStrategy('Sprint_To_Finish',72)    
    """
    def SetStrategy(self,strategy,value):
        if strategy in self.Strategies:
            self.Strategies[strategy] = value
        else:
            raise ValueError('The strategy does not exist!')

    """
    @Method: PlayerRoll
    @Description: Implements a turn for a player. If the player rolls a 1 at any time zero is returned, 
                  otherwise the total of the rolls is returned.
    @Params:
        string: player
        int: max rolls 
    @Returns: int: total
    """
    def Roll(self):
    	if self.TotalScore / Game.t_s >= .8:
    		self.Strategy = 'Sprint_To_Finish'
    	
    	if self.Strategy == 'Random':
    		Score,NumRolls = self.RandomRoll()
    	elif self.Strategy == 'Aggressive':
    		Score,NumRolls = self.Aggressive()
    	elif self.Strategy == 'Cautious':
    		Score,NumRolls = self.Cautious()
    	elif self.Strategy == 'Robust':
    		pass
    	elif self.Strategy == 'CopyCat':
    		pass
    	elif self.Strategy == 'Sprint_To_Finish':
    		Score,NumRolls = self.Sprint_To_Finish()
    	
    	self.TotalScore += Score
    	self.LastScore = Score
    	self.LastNumRolls = NumRolls
    	
    	if self.Target_Score(self.TotalScore) is True:
    		print (self.Name,"has just reached",Game.t_s,"points and is stopping")

    def RandomRoll(self):
        Score = 0
        NumRolls = 0
        for i in range(random.randint(1,self.Strategies['Random'])):
            NumRolls += 1
            roll = self.pig.Roll()
            if roll == 0:
                break
            Score += roll
            temp = self.TotalScore + Score
            if self.Target_Score(temp) is True:
            	break
        return (Score,NumRolls)
    """
    @Method: Aggressive
    @Description: Stragety that rolls 2 or 3 rolls more than the average # of rolls (6).
    @Params: None
    @Returns: int: Score,NumRolls
    """
            
    def Aggressive(self):
        Score = 0
        NumRolls = 0
        for i in range(random.randint(8,self.Strategies['Aggressive'])):
        	NumRolls += 1
        	roll = self.pig.Roll()
        	if roll == 0:
        		return (0,NumRolls)
        	Score += roll
        	temp = self.TotalScore + Score
        	if self.Target_Score(temp) is True:
        		break
        return (Score,NumRolls)
    """
    @Method: Cautious
    @Description: Stragety that rolls 2 or 3 rolls less than the average # of rolls (6).
    @Params: None
    @Returns: int: Score,NumRolls
    """        
    def Cautious(self):
        Score = 0
        NumRolls = 0
        for i in range(random.randint(3,self.Strategies['Cautious'])):
        	NumRolls += 1
        	roll = self.pig.Roll()
        	if roll == 0:
        		return (0,NumRolls)
        	Score += roll
        	temp = self.TotalScore + Score
        	if self.Target_Score(temp) is True:
        		break
        return (Score,NumRolls)

    def Robust(self):
        pass
        
    def CopyCat(self):
        pass
    
    """
    @Method: Sprint_To_Finish
    @Description: Method that is used once the player reaches 80% of self.TotalScore. Player will continue to roll until score is reached or 0 is returned.
    @Params: None
    @Returns: int: Score,NumRolls
    """
    def Sprint_To_Finish(self):
    	Score = 0
    	NumRolls = 0
    	temp = 0
    	while not self.Target_Score(temp):
    		NumRolls += 1
    		roll = self.pig.Roll()
    		if roll == 0:
    			return (0,NumRolls)
    		Score += roll
    		temp = self.TotalScore + Score
    	return (Score,NumRolls)
    """
    @Method: Target_Score
    @Description: Compares the Total Score of player and compares it with the Total Score needed to win. If >= to Score needed to win then True is returned.
    @Params: int: temp (Current Score of Player)
    @Returns: Bool
    """    	
    def Target_Score(self,temp):
    	if temp >= Game.t_s:
    		return True

##############################################################################
##############################################################################

"""
This Class represents one instance of a game with X players rolling X dice playing to a score of X.
"""
class Game(object):
    """
    @Method: Init
    @Description: Initializes a pig game instance
    @Params:
        list: Players - A list of player names
        int: NumDice - Number of dice per roll
        int: RandomRolls - Top value of random range for rolls
        int: TargetScore - Target score to trigger a winner
    @Returns: None
    """
    def __init__(self, **kwargs):
        self.Players = {}                           # player dictionary
        self.NumDice = kwargs['num_dice']           # number of dice per roll
        self.RandomRolls = kwargs['random_roles']   # max num random rolls
        self.TargetScore = kwargs['target_score']   # game winning score
        self.WinnerName = None                      # no winner yet
        Game.t_s = self.TargetScore
        # initialize all players
        self.AddPlayers(kwargs['players'])
            
        self.StartGame()
        
    def __str__(self):
        string = ""
        for name,obj in self.Players.items():
            string += obj.__str__() + "\n"
        return string
        
    """
    @Method: AddPlayers
    @Description: Adds a new player or players to the game
        Example: {
                   'bob':<player_object>
                   'sue':<player_object>
                 }
    
    @Params: [] - players
    @Returns: None
    """
    def AddPlayers(self,players):
        if not type(players) == list:
            self.Players[players.Name] = players
        else:
            for p in players:
                self.Players[p.Name] = p
                    
    """
    @Method: WinnerExists
    @Description: Checks to see if a player has acheived the target score.
    @Params:None
    @Returns: bool
    """         
    def StartGame(self):

        self.UpdatePlayerOpponents()
        
        # Main game loop
        while not self.WinnerExists():
            print(self)
            for name,PlayerObj in self.Players.items():
                PlayerObj.Roll()
       
    """
    @Method: WinnerExists
    @Description: Checks to see if a player has acheived the target score.
    @Params:None
    @Returns: bool
    """
    def WinnerExists(self):
        for name,PlayerObj in self.Players.items():
            if PlayerObj.TotalScore >= self.TargetScore:
                self.WinnerName = PlayerObj.Name
                return True
        self.WinnerName = None
        return False

    """
    @Method: Winner
    @Description: Returns the winner, if there is one.
    @Params:None
    @Returns: [string,None]: Players name or None
    """
    def Winner(self):
        return self.WinnerName
        
    """
    @Method: UpdatePlayerOpponents
    @Description: Gives a copy of each player in the game, to every other player in the game. 
    @Params:None
    @Returns: None
    """   
    def UpdatePlayerOpponents(self):

        for name,PlayerObj in self.Players.items():
            PlayerObj.AddOpponents(self.Players.values())

##############################################################################
##############################################################################



def main():

    p1 = Player('ann')
    p2 = Player('bob',1,('Aggressive',9)) # used 9 since Aggressive = avg #rolls + 2 or 3
    p3 = Player('sue')
    p4 = Player('bill',1,('Cautious',4))
    
    AllPlayers = [p1,p2,p3,p4]
    
    # Param values to initialize a pig game instance
    kwargs = {'num_dice':1,'random_roles':9,'target_score':100,'players':AllPlayers}

    g = Game(**kwargs)
    
    print(g)
    
    
main()
