from tensorflow.python.framework import ops
import tflearn
from nltk_utilize import training, output

ops.reset_default_graph()

# Designing layers of the network
net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 1024, activation='relu')
net = tflearn.dropout(net, 0.3)
net = tflearn.fully_connected(net, 1024, activation='relu')
net = tflearn.dropout(net, 0.3)
net = tflearn.fully_connected(net, 1024, activation='relu')
net = tflearn.dropout(net, 0.3)
net = tflearn.fully_connected(net, len(output[0]), activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss="categorical_crossentropy")
model = tflearn.DNN(net)