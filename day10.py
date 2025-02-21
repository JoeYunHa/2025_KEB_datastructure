def bubble_sort(l):
    for i in range(len(l) - 1):
        no_swap = True
        for j in range(len(l)- 1 -i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1] , l[j] # swap
                no_swap = False
                print(j , end = ' ')
            if no_swap:
                return l
    return l

print(bubble_sort([8,-11,9,1]))
print(bubble_sort([-11,1,8,9]))

