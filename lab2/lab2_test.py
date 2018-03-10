import random
import time


def selection_sort(ar):
    for i in range(len(ar)):
        x = i
        for z in range(x + 1, len(ar)):
            if ar[x] > ar[z]:
                x = z
        ar[i], ar[x] = ar[x], ar[i]
    return ar


size = 1000
for i in range(10):
    apple = [random.randint(0, 1000) for k in range(size)]
    time_start = time.clock()
    selection_sort(apple)
    time_end = time.clock()
    print('Размер: {}. Время: {}. Елем/cек: {}'.format(size, time_end-time_start, size/(time_end-time_start)))
    size += 1000
