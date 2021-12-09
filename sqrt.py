import numpy as np

"""
牛顿法,f(x)=0 =>
初始化x0后，做切线y = f(x0) + f'(x0)(x - x0), 得到x1 = x0 - f(x0) / f'(x0),再由其为新的点做切线
推得x(n+1) = x(n) - f(x(n)) / f'(x(n))
"""
def sqrt(x):
    t = 1
    while abs(t ** 2 - x) >= 1e-8:
        t = t / 2 + x / (2 * t)
    return t

diff = sqrt(2) - np.sqrt(2)
print(diff)