import random
from time import sleep

width = 50
high  = 20
char = "A"

def sort(List):
    for _ in range(len(List)):
        for i in range((len(List))) :
            if len(List) == i+1:
                break
            a = List[i]
            b = List[i + 1]
            if a < b :
                List[i]     = b
                List[i + 1] = a

    List.reverse()
    return List

while True :
    my_list = random.sample(range(0, width), high)
    sorted = sort(my_list)
    for i in sorted :
        print(" " * (width - i), end= char)
        print(char * i * 2)
    print("\n")
    sleep(1)
