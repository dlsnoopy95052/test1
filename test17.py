def reduce_the_tools(string):
    uniqs = '' 
    for x in string: 
        if x not in uniqs: 
            uniqs = uniqs + x 
    return uniqs 

def merge_the_tools(string, k):
    split_string = []
    for i in range(0, len(string), k):
        print(reduce_the_tools(string[i:i+k]))


s = input()
k = int(input())
merge_the_tools(s, k)