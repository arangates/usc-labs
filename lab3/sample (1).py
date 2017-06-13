# go to https://nimblenet.readthedocs.io/en/latest/index.html for installation and more information

############################################################
########################Neural Nets#########################
############################################################

from nimblenet.activation_functions import sigmoid_function
from nimblenet.cost_functions import cross_entropy_cost
from nimblenet.learning_algorithms import RMSprop
from nimblenet.data_structures import Instance
from nimblenet.neuralnet import NeuralNet

dataset        = [
	Instance( [0,0], [0] ), Instance( [1,0], [1] ), Instance( [0,1], [1] ), Instance( [1,1], [0] )
]

settings       = {
	"n_inputs" : 2,
	"layers"   : [  (2, sigmoid_function), (1, sigmoid_function) ]
}

network        = NeuralNet( settings )
# make sure you use 80% of dataset as training data
# and the rest of dataset as testing data
# This is just a simple example.
training_set   = dataset
test_set       = dataset
cost_function  = cross_entropy_cost

# training neural nets
RMSprop(
	network,           # the network to train
	training_set,      # specify the training set
	test_set,          # specify the test set
	cost_function,     # specify the cost function to calculate error

	max_iterations = 5000, # specify the number of epoches
						   # if you don't mentioned it, it becomes very slow
)

# Using the network to make a prediction
prediction_set = [Instance([0, 1]), Instance([1, 0])]
prediction_outcome = network.predict(prediction_set)
print prediction_outcome