# encoding: utf-8
from typing import List

def is_square(point1: List[int], point2: List[int], point3: List[int], point4: List[int]) -> bool:
    """
     :param point1: 第一个点的坐标，需要是列表类型，列表长度需要为2；其他三个参数以此类推
     :return: 四个点可否构成正方形
     """

    points = [point1, point2, point3, point4]
    distances = []

    # 每个点两两之间形成一条边，计算这些边的长度(的平方)，保存到 distances 里
    for i in range(3):
        for j in range(i + 1, 4):
            x, y = points[i][0] - points[j][0], points[i][1] - points[j][1]
            distance = x * x + y * y
            distances.append(distance)

    # 按边的长度排序，默认是升序
    distances.sort()

    # 条件1：四条边长度相等（保证是菱形）
    # 条件2：两条对角线长度相等（一个菱形的两条对角线相等，那么这个菱形就是正方形）
    return (distances[0] == distances[1]) and (distances[1] == distances[2]) and (
            distances[2] == distances[3]) and (distances[4] == distances[5])


def solve_method(n: int, points: List[List[int]]) -> int:
    count = 0
    # 通过四重循环来不重复地挑选 4个点，通过调用 is_square 判断是否构成正方形
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for p in range(k + 1, n):
                    if is_square(points[i], points[j], points[k], points[p]):
                        count += 1
    return count


if __name__ == '__main__':
    # 1. 处理输入
    n = int(input())
    points = []
    for i in range(n):
        # input().split()的结果是 一个字符串列表["0","0"]
        # 我们使用 map(int,input().split())，即对input().split()的里的每个元素执行 int()，即转化为int类型
        # x,y = (int("0"),int("0")) = 0,0
        x, y = map(int, input().split())
        points.append([x, y])

    # 2.调用 solve_method 方法，计算能构成多少个正方形
    res = solve_method(n, points)

    # 3.打印输出
    print(res)




"""
以下被注释掉的部分是4个给定用例的测试。
注释掉上面的__main__方法，恢复下面的测试代码，可以直接运行main测试方法正确性。
"""

# import unittest
#
# if __name__ == '__main__':
#     # unittest.main()语句用于执行4个给定的测试用例; 注释掉这条语句才能读取键盘输入
#     unittest.main()
#
# class MethodTest(unittest.TestCase):
#     def test1(self):
#         n = 3
#         points = [[1, 3], [2, 4], [3, 1]]
#         self.assertEqual(solve_method(n, points), 0)
#
#     def test2(self):
#         n = 4
#         points = [[0, 0], [1, 2], [3, 1], [2, -1]]
#         self.assertEqual(solve_method(n, points), 1)
#
#     def test3(self):
#         n = 5
#         points = [[0, 0], [1, 2], [3, 1], [2, -1], [1, 1]]
#         self.assertEqual(solve_method(n, points), 1)
#
#     def test4(self):
#         n = 7
#         points = [[0, 0], [1, 2], [3, 1], [2, -1], [1, 1], [1, 0], [0, 1]]
#         self.assertEqual(solve_method(n, points), 2)
