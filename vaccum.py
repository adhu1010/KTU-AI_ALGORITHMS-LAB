class VacuumCleanerAgent:
    def __init__(self, state):
        self.state = state  

    def suck(self):
        if self.state[0] == "A":
            if self.state[1] == 1:
                self.state = ("A", 0, self.state[2])
                print(f"\nSucked dirt in Room A. New state: {self.state}")
                
        elif self.state[0] == "B":
            if self.state[2] == 1:
                self.state = ("B", self.state[1], 0)
                print(f"\nSucked dirt in Room B. New state: {self.state}")

    def move_left(self):
        if self.state[0] == "B":
            self.state = ("A", self.state[1], self.state[2])
            print(f"\nRoom B is Clean.Moved left to Room A. New state: {self.state}")

    def move_right(self):
        if self.state[0] == "A":
            self.state = ("B", self.state[1], self.state[2])
            print(f"\nRoom A is clean.Moved right to Room B. New state: {self.state}")

    def clean(self):
        while self.state[1] == 1 or self.state[2] == 1:
            if self.state[0] == "A" and self.state[1] == 1:
                self.suck()
            elif self.state[0] == "B" and self.state[2] == 1:
                self.suck()
            elif self.state[0] == "A" and self.state[2] == 1:
                self.move_right()
            elif self.state[0] == "B" and self.state[1] == 1:
                self.move_left()
        if self.state[1] == 0 and self.state[2] == 0:
            print("\nBOTH RO0MS ARE CLEAN.GOAL ACHIVED \n")

agentposition=input("\nEnter the postion of agent (A|B) :")
left=int(input("\nEnter the 1 if room A is dirty else 0 :"))
right=int(input("\nEnter the 1 if room B is dirty else 0 :"))
initial_state = (agentposition.upper(),left,right)
print("INITIAL STATE",initial_state)


agent = VacuumCleanerAgent(initial_state)


agent.clean()
