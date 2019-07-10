import numpy as np

if __name__ == '__main__':
    arr1 = np.array([2, 3, 4])
    print(arr1)
    print(arr1.dtype)  # int64

    arr2 = np.array([1.2, 2.3, 4.5])
    print(arr2)
    print(arr2.dtype)  # float64

    # 数学计算
    print(arr1 + arr2)  # 一一对应相加

    # 直接和标量运算
    print(arr2 * 10)

    # 定义矩阵
    data = [[1, 2, 3], [4, 5, 6]]
    a3 = np.array(data)
    print(a3)  # 转换成了二维矩阵
    print(a3.dtype)

    # 全 0 的一维矩阵
    print(np.zeros(10))
    # 全 0 的 3*5 的二维矩阵
    print(np.zeros([3, 5]))  # 或者 print(np.zeros((3, 5)))

    # 全 1 矩阵
    print(np.ones((4, 6)))

    # 空值矩阵，三维矩阵，里面会填充随机值
    print(np.empty([2, 3, 2]))

    """numpy数组的索引和切面"""
    # 生成一个数组
    a0 = np.arange(10)
    # 切片获取第六个元素
    print(a0[5:8])
    # 切片后赋值
    a0[5:8] = 10
    print(a0)

    """重新赋值但不改变原有数组，副本的概念"""
    arr_slice = a0[5:8].copy()
    arr_slice[:] = 15
    print(arr_slice)
    print(a0)
