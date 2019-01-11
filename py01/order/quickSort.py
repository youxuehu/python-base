def quicksort_rec(A, lft=None, rgt=None):
    if lft is None or rgt is None:
        lft, rgt = 0, len(A) - 1
    if lft >= rgt:
        return

    i = lft  # 序列最左边的哨兵
    j = rgt  # 序列最右边的哨兵
    base = lft  # 基准数的索引
    while i != j:
        while A[j] >= A[base] and i < j:  # 先从右往左找
            j -= 1
        while A[i] <= A[base] and i < j:
            i += 1
        if i < j:  # 没有相遇:交换
            A[i], A[j] = A[j], A[i]

    A[base], A[i] = A[i], A[base]  # 基准数归位, 索引 i 为序列正中
    quicksort_rec(A, lft, i - 1)  # 递归处理左边序列
    quicksort_rec(A, i + 1, rgt)  # 递归处理右边序列


A = [6, 1, 2, 7, 9, 3, 4, 2, 5, 10, 8, 1]
quicksort_rec(A)
print(A)
