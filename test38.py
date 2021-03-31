n = int(input())
n_students = set(map(int,input().split()))
b = int(input())
b_students = set(map(int,input().split()))

both = n_students.difference(b_students)
print(len(both))