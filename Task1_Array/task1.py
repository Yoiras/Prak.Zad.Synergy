def sum_negatives_between_min_max(arr):
    """Находит сумму отрицательных элементов между min и max."""
    if len(arr) < 3:
        return 0
    
    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))
    start, end = min(min_idx, max_idx), max(min_idx, max_idx)
    
    return sum(x for x in arr[start + 1:end] if x < 0)


# Тесты
tests = [
    [1, -2, 3, -4, 5, -6, 7],
    [-5, 10, -3, 8, -1, 4, -7],
    [4, -1, -2, 5, -3, 0],
    [10, -1, 5, -8, 3, -2, 7]
]

for i, arr in enumerate(tests, 1):
    print(f"Тест {i}: {arr} → {sum_negatives_between_min_max(arr)}")
