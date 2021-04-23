import operator

def person_lister(f):
    def inner(people):
        # complete the function
        for i in range(len(people)):
            people[i][2] = int(people[i][2])
        people.sort(key=operator.itemgetter(2))
        #print(people)
        for i in range(len(people)):
            people[i] = f(people[i])
        #print(people)
        return people
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')