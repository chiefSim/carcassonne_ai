
class Player:
    """
    Players must be defined in pairs
    
    MCTS player returns the node and the optimal move.
    
    All other player returns None (instead of a node) and the chosen move.
    """
    
    # Player 1 selects the optimal UCT move 
    # Player 2 selects the worst move from Player 1's position
    isFirstPlayer = True
    
    def __init__(self):
        self.isFirstPlayer = Player.isFirstPlayer
        self.name = "No Name"
        self.fullName = "Definitely has no name"
        self.isAIPlayer = True
        self.family = None
        
        # switch
        Player.isFirstPlayer = not Player.isFirstPlayer
        
    
    def chooseAction(self):
        """
        Move choice based on type of player
        """
        pass
    
    def __repr__(self):
        return self.name
    
            
class HumanPlayer(Player):
    
    def __init__(self, name = 'Human'):
        super().__init__()
        self.name = name
        self.fullName = "Human Player"
        self.isAIPlayer = False
    
    def chooseAction(self, state, TileIndex):
        """
        state - The current state of the game board
        """
        positions = state.availableMoves(TileIndex)
        
        # user input
        while True:
            print(f'Available moves: \n {positions} \n')
            choice = int(input("Input your choice:"))
            if choice in positions:
                return choice
    
            
class RandomPlayer(Player):
    
    def __init__(self, name = 'Random'):
        super().__init__()
        self.name = name
        self.fullName = "Random Player"
        
    def chooseAction(self, state):
        """
        Make a random move from all possible actions
        """
        return state.getRandomMove().move
            
            
