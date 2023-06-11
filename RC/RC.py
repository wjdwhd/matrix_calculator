def analyze_matrix(matrix):
    # 행렬의 크기 계산
    rows = len(matrix)
    cols = len(matrix[0])

    # 행렬의 합 계산
    matrix_sum = 0
    for row in matrix:
        for element in row:
            matrix_sum += element

    # 행렬의 평균 계산
    matrix_avg = matrix_sum / (rows * cols)

    # 행렬의 최댓값과 최솟값 계산
    matrix_max = float('-inf')
    matrix_min = float('inf')
    for row in matrix:
        for element in row:
            if element > matrix_max:
                matrix_max = element
            if element < matrix_min:
                matrix_min = element

    # 결과 반환
    return {
        'rows': rows,
        'cols': cols,
        'sum': matrix_sum,
        'avg': matrix_avg,
        'max': matrix_max,
        'min': matrix_min
    }

# 행렬 입력 받기
matrix = []
num_rows = int(input("행의 개수를 입력하세요: "))
num_cols = int(input("열의 개수를 입력하세요: "))

print("행렬의 요소를 입력하세요:")
for _ in range(num_rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# 행렬 분석 결과 출력
result = analyze_matrix(matrix)
print("\n행렬 분석 결과:")
print(f"행의 개수: {result['rows']}")
print(f"열의 개수: {result['cols']}")
print(f"합: {result['sum']}")
print(f"평균: {result['avg']}")
print(f"최댓값: {result['max']}")
print(f"최솟값: {result['min']}")