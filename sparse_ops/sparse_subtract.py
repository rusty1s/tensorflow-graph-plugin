# from tensorflow.python.framework import sparse_tensor
# from tensorflow.python.ops import convert_to_sparse_tensor, gen_sparse_ops


def sparse_subtract(a, b, thresh=0):
    pass
    # sparse_classes = (sparse_tensor.SparseTensor,
    #                   sparse_tensor.SparseTensorValue)

    # if not any(isinstance(inputs, sparse_classes) for inputs in [a, b]):
    #     raise TypeError('At least one input should be SparseTensor; do you '
    #                     'mean to use tf.subtract()?')

    # if all(isinstance(inputs, sparse_classes) for inputs in [a, b]):
    #     a = convert_to_sparse_tensor(a)
    #     b = convert_to_sparse_tensor(b)

    # else:
    #     # Swap to make `a` the SparseTensor.
    #     # TODO: Subtract not symmetric.
    #     if isinstance(b, sparse_classes):
    #         a, b = b, a
    # if not any(isinstance(inp))
