# AI-CartPole-v0

CartPole-v0 from openAI Gym

random.py uses linear model with random weights.  Model records best performance weights from random numbers.  The performance is quite good. (Q-learning without any function approximation)

bin.py uses Q-learning.  Model divides the domains of observation into 10 bins.  Since observation has 4 features, we have 4 dimensional boxes with partition 10^4 small boxes.  Each box is assigned with Q-value.  Model solves the problem but it takes quite long training.  (Q-learning with linear function approximation and gradient descent using scikit learn)

RBF.py uses RBF(Radial Basis Fucntion) along with Stochastic Gradient Descent.  It performs better than bin method. (Q-learning with linear function approximation and gradient descnet without using scikit learn, instead writing from scratch from numpy)  
