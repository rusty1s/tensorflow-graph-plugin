import tensorflow as tf
from sparse_ops import sparse_subtract

a = tf.SparseTensorValue(indices=[[0, 0]])
b = tf.SparseTensorValue(indices=[[0, 0], [1, 1], [2, 2]])

print('hihi')
