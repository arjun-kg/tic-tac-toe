import numpy as np 
import random
import pdb
from tqdm import tqdm
from matplotlib import pyplot as plt


#constants
no_episodes = 200
class Tic_Tac_Toe:

    def __init__(self,alpha = 0.8,epsilon = 0.1, gamma = 0.9, q = {},state = np.zeros((3,3))):

    #constants
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.q = q
        self.state = state
        self.status = 'c'
        self.action = None
        self.random_picked = False

    def new_game(self):
        self.state = np.zeros((3,3))
        return 

    def p1_end_game(self):
        value = max(np.sum(self.state,axis = 0))
        value = max(value, max(np.sum(self.state,axis=1)))
        value = max(value, np.trace(self.state))
        value = max(value, np.sum([self.state[0,2],self.state[1,1],self.state[2,0]])) #Poor. 

        if value == 3:
            return 'w'
        elif 0 in self.state:
            return 'c'
        else:
            return 'd'

    def p2_end_game(self):
        value = min(np.sum(self.state,axis = 0))
        value = min(value, min(np.sum(self.state,axis=1)))
        value = min(value, np.trace(self.state))
        value = min(value, np.sum([self.state[0,2],self.state[1,1],self.state[2,0]])) #Poor. 

        if value == -3:
            return 'l'
        elif 0 in self.state:
            return 'c'
        else:
            return 'd'

    def opponent_move(self):
        x,y = np.where(self.state==0)
        i = np.random.randint(len(x))
        old_state = self.state
        self.state[x[i],y[i]] = -1

        self.status = self.p2_end_game()

        reward = 0
        if self.status == 'l':
            # print("Agent lost the game!")
            reward = -1
        # elif self.status == 'd':
            # print("Game drawn!")

        if not self.random_picked: 
            self.update_q(state = old_state,action = self.action,next_state = self.state,reward = reward)

        return

    
    def player_move(self):
        self.random_picked = False
        x,y = np.where(self.state==0)
        matches = [x for x in self.q if x[0] == self.state_to_tuple(self.state)]
        values = [self.q[x] for x in matches]

        random_index = random.choice(range(len(x)))
        xi,yi = x[random_index],y[random_index]

        if np.random.rand(1) < self.epsilon:
            self.action = (xi,yi)
            self.random_picked = True
        else:
            if len(values)==0:
                values = 0
                self.action = (xi,yi)
            else:
                # pdb.set_trace()
                (xi,yi) = matches[np.argmax(values)][1]
                self.action = (xi,yi)

        old_state = self.state
        self.state[xi,yi] = 1

        self.status = self.p1_end_game()

        reward = 0
        if self.status == 'w':
            # print("Agent won!")
            reward = 1
        # elif self.status == 'd':
        #     print("Game Drawn!")

        if not self.random_picked: 
            self.update_q(state = old_state,action = self.action,next_state = self.state,reward = reward)

        return

    def state_to_tuple(self,state):
        (x,y) = np.where(state==1)
        pos_a = tuple(3*x+y)
        (x,y) = np.where(state==-1)
        pos_o = tuple(3*x+y)

        return (pos_a,pos_o)


    def update_q(self,state,action,next_state,reward):

        matches = [x for x in self.q if x[0] == self.state_to_tuple(next_state)]
        values = [self.q[x] for x in matches]
        if len(values) == 0:
            values = 0
        # pdb.set_trace()
        key = (self.state_to_tuple(state),action)
        if key not in self.q:
            self.q[key] = 0
        self.q[key] = self.q[key]*(1-self.alpha) + self.alpha*(reward + self.gamma*(np.max(values)))

    def play_game(self):
        while True:

            old_state = self.state
            self.player_move()
            if self.status == 'w' or self.status == 'd':
                return
            self.opponent_move()
            if self.status == 'l' or self.status == 'd':
                return

if __name__ == "__main__":

    win_loss = []
    wins_in_10 = []
    new_len = 0
    agent1 = Tic_Tac_Toe()    
    for episodes in tqdm(range(no_episodes)):
        agent1.play_game()
        win_loss += [agent1.status]
        if episodes % 10 == 0 and not episodes ==0:
            wins_in_10+= [[x=='w' for x in win_loss].count(True)]
            win_loss = []
        agent1.new_game()
        if episodes % 100 == 0 and not episodes ==0:
            old_len = new_len
            new_len = len(agent1.q)
            print(new_len)
            if new_len - old_len < 10:
                break

    plt.plot(wins_in_10)
    plt.show()


