import numpy as np

# 简单卷积,img2col方案
def conv2d_simple_img2col(feature, kernel, stride=1):
    assert len(feature.shape) == 2
    assert len(kernel.shape) == 2
    kh, kw = kernel.shape
    out_h = (feature.shape[0] - kh) // stride + 1
    out_w = (feature.shape[1] - kw) // stride + 1
    feature_ = np.zeros((out_h * out_w, kw * kh))
    for i in range(out_h):
        for j in range(out_w):
            inp = feature[j:j+kh, i:i+kw].reshape(-1)
            feature_[i * out_w + j] = inp
    kernel_ = kernel.reshape(-1, 1)
    out_feature = np.dot(feature_, kernel_).reshape(out_h, out_w)
    return out_feature

def conv2d_simple_naive(feature, kernel, stride=1):
    assert len(feature.shape) == 2
    assert len(kernel.shape) == 2
    kh, kw = kernel.shape
    out_h = (feature.shape[0] - kh) // stride + 1
    out_w = (feature.shape[1] - kw) // stride + 1
    feature_ = np.zeros((out_h, out_w))
    for i in range(out_h):
        for j in range(out_w):
            inp = feature[j:j+kh, i:i+kw]
            feature_[i, j] = (inp * kernel).sum()
    return feature_
feature = np.random.rand(5, 5)
kernel = np.random.rand(3, 3)

result_img2col = conv2d_simple_img2col(feature, kernel, stride=1)
result_naive = conv2d_simple_naive(feature, kernel, stride=1)
print(result_img2col - result_naive)


# 4维tensor
def conv2d_img2col(feature, kernel, stride=1):
    kcout, kcin, kh, kw = kernel.shape
    n, c, h, w = feature.shape
    out_h = (feature.shape[0] - kh) // stride + 1
    out_w = (feature.shape[1] - kw) // stride + 1
    feature_ = np.zeros((out_h * out_w, kw * kh))
    for i in range(out_h):
        for j in range(out_w):
            inp = feature[j:j+kh, i:i+kw].reshape(-1)
            feature_[i * out_w + j] = inp
    kernel_ = kernel.reshape(-1, 1)
    out_feature = np.dot(feature_, kernel_).reshape(out_h, out_w)
    return out_feature

def conv2d_simple_naive(feature, kernel, stride=1):
    assert len(feature.shape) == 2
    assert len(kernel.shape) == 2
    kh, kw = kernel.shape
    out_h = (feature.shape[0] - kh) // stride + 1
    out_w = (feature.shape[1] - kw) // stride + 1
    feature_ = np.zeros((out_h, out_w))
    for i in range(out_h):
        for j in range(out_w):
            inp = feature[j:j+kh, i:i+kw]
            feature_[i, j] = (inp * kernel).sum()
    return feature_
