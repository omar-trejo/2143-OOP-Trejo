import random
import abc

class Dice(object): #---------------------------------------------------------------------------------
    def __init__(self,num_sides=6):
        self.NumSides = num_sides

    def Roll(self):
        return random.randint(1,self.NumSides)  

class Pig(object): #---------------------------------------------------------------------------------
    def __init__(self,num_dice=1,dice_sides=6,skunk_value=1):
        self.NumDice = num_dice
        self.DiceSides = dice_sides
        self.DiceList = []
        self.SkunkValue = skunk_value
        for i in range(self.NumDice):
            self.DiceList.append(Dice(self.DiceSides))

    def Roll(self):
        scores = []
        for d in self.DiceList:
            scores.append(d.Roll())
            if self.SkunkValue in scores:
                return 0 
        return sum(scores)

class Player(object): #---------------------------------------------------------------------------------
    def __init__(self,name,num_dice=1,strategy=('Random',7),targ_score = None):
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
        self.targ_score = targ_score
        self.Strategies[strategy[0]] = strategy[1]

    def AddOpponents(self,opponent):
            for op in opponent:
                if not op.Name == self.Name:
                    self.Opponents[op.Name] = op

    def __str__(self):
        tmp = " "
        for k,v in self.Opponents.items():
            tmp = tmp + "[" + k + " " + str(v.TotalScore) + "," + str(v.LastScore) + "," + str(v.LastNumRolls) + "] "
        return "Name: %s, TotScore: %s, LastScore: %s, LastNumRolls: %s, Opponents: %s" % (self.Name,self.TotalScore,self.LastScore,self.LastNumRolls,tmp)

    def __repr__(self):
        return self.__str__()

    def SetStrategy(self,strategy,value):
        if strategy in self.Strategies:
            self.Strategies[strategy] = value
        else:
            raise ValueError('The strategy does not exist!')

    def Roll(self):
        if self.Strategy == 'Random':
            Score,NumRolls = self.RandomRoll()
        elif self.Strategy == 'Aggressive':
            pass
        elif self.Strategy == 'Cautious':
            pass
        elif self.Strategy == 'Robust':
            pass
        elif self.Strategy == 'CopyCat':
            pass
        
        self.TotalScore += Score
        self.LastScore = Score
        self.LastNumRolls = NumRolls
        if self.TotalScore >= self.Target_Score(): # if player reaches total score print
        	print (self.Name,"has just reached",self.Target_Score(),"points and is stopping")
        
    def RandomRoll(self):
        Score = 0
        NumRolls = 0
        for i in range(random.randint(1,7)):
            NumRolls += 1
            roll = self.pig.Roll()
            if roll == 0:
                break
            Score += roll
            temp = self.TotalScore + Score  #Created temp variable to take the total current
            if temp >= self.Target_Score(): #total score of player + the roll + score and if
            	break                       #100 or greater no longer needs to roll
        
        return (Score,NumRolls)
            
    def Target_Score(self):
    	return Game.t_s
        
    def Target_Roll(self):
        pass

    def Sprint_To_Finish(self):
        pass
        
    def Mimic_Opponent(self):
        pass

    def Situational(self):
        pass
        
    def Combination(self):
        pass

class Game(object): #---------------------------------------------------------------------------------

	def __init__(self, **kwargs):
		self.Players = {}                           # player dictionary
		self.NumDice = kwargs['num_dice']           # number of dice per roll
		self.RandomRolls = kwargs['random_roles']   # max num random rolls
		self.TargetScore = kwargs['target_score']   # game winning score
		self.WinnerName = None                      # no winner yet
		Game.t_s = self.TargetScore                 # Class variable for future use in player class
		# initialize all players
		self.AddPlayers(kwargs['players'])
		    
		self.StartGame()
        
	def __str__(self):
		string = ""
		for name,obj in self.Players.items():
		    string += obj.__str__() + "\n"
		return string

	def AddPlayers(self,players):
		if not type(players) == list:
		    self.Players[players.Name] = players
		else:
		    for p in players:
		        self.Players[p.Name] = p
 
	def StartGame(self):
		self.UpdatePlayerOpponents()
		
		while not self.WinnerExists():
			print(self)
			for name,PlayerObj in self.Players.items():
			    PlayerObj.Roll()
	
	def WinnerExists(self):
	    for name,PlayerObj in self.Players.items():
	        if PlayerObj.TotalScore >= self.TargetScore:
	            self.WinnerName = PlayerObj.Name
	            return True
	    self.WinnerName = None
	    return False
	
	def Winner(self):
	    return self.WinnerName
	
	def UpdatePlayerOpponents(self):
	
	    for name,PlayerObj in self.Players.items():
	        PlayerObj.AddOpponents(self.Players.values())

def main():

    p1 = Player('ann')
    p2 = Player('bob')
    p3 = Player('sue')
    p4 = Player('dax')
    AllPlayers = [p1,p2,p3,p4]

    
    
    # Param values to initialize a pig game instance
    kwargs = {'num_dice':1,'random_roles':9,'target_score':100,'players':AllPlayers}

    g = Game(**kwargs)
    a = Player(Game(**kwargs))
    print (g)

    
    
main()
