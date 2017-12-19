# tic-tac-toe
Getting the hang of github with a basic project...

Update:
vanilla_tabular_q.py: Q-Learning agent plays and learns against a random-playing opponent. States are represented by numpy matrices (for easy visualization). q function is a dictionary which stores state tuple: (Positions of Xs, Positions of Os) and action tuple: (Indices of 3x3 matrix). This does not converge in 10000 steps. This is as vanilla as possible. Possible ways of quickening converge is to consider symmetric states / different simpler encoding of states / tune hyperparameters.
