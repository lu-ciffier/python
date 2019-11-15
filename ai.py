import numpy as np
import network
import function_lucifer as fun

A = np.array([1, 2, 3, 4])
print(np.ndim(A))
print(A.shape)
print(A.shape[0])

init = np.array([-3.0, 4.0])
y = network.gradient_descent(fun.function_1, init, lr=0.1, step_num=100)
print(y)
