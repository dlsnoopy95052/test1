input()
en_list = set(map(int, input().split())) 
input()
fr_list = set(map(int, input().split())) 

print(len(en_list.symmetric_difference(fr_list)))