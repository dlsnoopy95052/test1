import math
import os
import random
import re
import sys
from itertools import groupby

if __name__ == '__main__':
    d = {}
    groups = []
    nums = []
    s = input()
    ss = sorted(s)

    for _, g in groupby(ss):
        gg = list(g)
        groups.append(gg)
        nums.append(len(list(gg)))

    nums = sorted(nums, reverse=True)
    # print(nums)
    # print(groups)
    found = []
    top = 0
    for i in range(3):
        #print("checking ", nums[i])
        for j in range(len(groups)):
            k = groups[j]
            #print("checking ",k[0])
            #print(nums[i], " ",len(k))
            if (len(k) == nums[i] and k[0] not in found and top < 3):
                #print(nums[i])
                top += 1
                found.append(k[0])
                print("{} {}".format(k[0], nums[i]))
                
