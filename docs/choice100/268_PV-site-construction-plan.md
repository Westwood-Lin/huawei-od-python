# 268 光伏场地建设规划

## 题目描述

祖国西北部有大片荒地，其中零星分布着一些湖泊、保护区、矿区，整体上常年光照良好，但是也有一些地区光照不太好。某电力公司希望在这里建设多个光伏电站，生产清洁能源。对每平方公里的土地进行了发电评估，其中不能建设的区域发电量为0kw，可以发电的区域根据光照、地形等给出了每平方公里年发电量`x`千瓦。我们希望能够找到其中的集中矩形区域建设电站，能够获得良好的收益。

## 输入描述

第一行输入为调研地区的长、宽，以及准备建设电站（长宽相等的正方形）的边长、最低要求的发电量。之后每行为调研区域每平方公里的发电量。
例如，输入为：
```
2 5 2 6
1 3 4 5 8
2 3 6 7 1
```
表示调研的区域大小为长2宽5的矩形，我们要建设的电站边长为2，建设电站最低发电量为6

## 输出描述

输出为符合要求的区域有多少个。

上述输入长宽为2的正方形满足发电量大于等于6的区域有4个，则输出为4

**说明：** 其中被调研的区域长宽均大于等于1，建设电站的边长大于等于1，任何区域的发电量大于等于0

## 示例描述

### 示例一

**输入：**
```
2 5 2 6
1 3 4 5 8
2 3 6 7 1
```

**输出：**
```
4
```

**说明：**  
输入长为2、宽为5的场地，建设的场地为正方形场地，边长为2，要求场地的发电量大于等于6。

### 示例二


**输入：**
```
2 5 1 6
1 3 4 5 8
2 3 6 7 1
```

**输出：**
```
3
```

**说明：**  
输入长为2、宽为5的场地，建设的场地为正方形场地，边长为1，要求场地的发电量大于等于6。

### 示例三


**输入：**
```
2 5 1 0
1 3 4 5 8
2 3 6 7 1
```

**输出：**
```
10
```

**说明：**  
输入长为2、宽为5的场地，建设的场地为正方形场地，边长为1，要求场地的发电量大于等于0即可。

## 解题思路

1. 使用两层循环遍历所有满足正方形边长的子矩阵，记录左上角的坐标位置`(i, j)`
2. 使用`sum`函数，计算子矩阵中所有发电量总和
3. 与所要求的发电量进行对比，记录满足条件的子矩阵的个数
4. 返回子矩阵的个数

## 解题代码

```python
def solve_method(row, col, width, power, region):
    result = 0
    # 贪心算法
    for i in range(row - width + 1):
        for j in range(col - width + 1):
            # 统计场地的所有发电量总和
            total_power = sum(
                region[m][n]
                for m in range(i, i + width)
                for n in range(j, j + width)
            )
            # 判断是否满足最低发电量
            if total_power >= power:
                result += 1

    return result
```