# AI-CartPole-v0

CartPole-v0 from openAI Gym

random.py uses linear model with random weights.  Model records best performance weights from random numbers.  The performance is quite good.  

bin.py uses Q-learning.  Model divides the domains of observation into 10 bins.  Since observation has 4 features, we have 4 dimensional boxes with partition 10^4 small boxes.  Each box is assigned with Q-value.  Model solves the problem but it takes quite long training.  
