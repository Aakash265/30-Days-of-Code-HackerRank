import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    for i in range(10):
        print(n, "x", i+1, "=", n*(int(i)+1))