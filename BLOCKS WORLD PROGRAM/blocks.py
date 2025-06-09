class BlocksWorld: 
    def __init__(self): 
        self.state = { 
            "A": "B",   # A is on B 
            "B": "table",  # B is on table 
            "C": "table"   # C is on table 
        } 
        self.goal = { 
            "A": "B", 
            "B": "C", 
            "C": "table" 
        } 

    def is_goal_state(self): 
        return self.state == self.goal 

    def move(self, block, destination): 
        if block in self.state and self.state[block] != destination: 
            print(f"Moving {block} from {self.state[block]} to {destination}") 
            self.state[block] = destination 

    def plan_moves(self): 
        print("\nInitial State:", self.state) 
        while not self.is_goal_state(): 
            for block, target in self.goal.items(): 
                if self.state[block] != target: 
                    self.move(block, target) 
        print("\nFinal Goal State Reached:", self.state) 

# Run the Blocks World Solver 
bw = BlocksWorld() 
bw.plan_moves()
