T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    student = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        student.append(a * 0.35 + b * 0.45 + c * 0.2)
    student_grade = student[k - 1]
    student.sort(reverse=True)
    student_idx = student.index(student_grade) // (n // 10)
    print(f'#{test_case} {grade[student_idx]}')