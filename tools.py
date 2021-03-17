from datetime import datetime as time
import random


def timeit(func):
    def wrapper(arr):
        print(func.__name__, end=' => ')
        start = time.now()
        func(arr)
        print(time.now() - start)

    return wrapper


@timeit
def sort_insert(arr):
    for top in range(1, len(arr)):
        i = top
        while i > 0 and arr[i - 1] > arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


@timeit
def sort_bubble(arr):
    for bypass in range(1, len(arr)):
        for i in range(len(arr) - bypass):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


@timeit
def sort_choice(arr):
    for current in range(len(arr) - 1):
        for following in range(current + 1, len(arr)):
            if arr[following] < arr[current]:
                arr[following], arr[current] = arr[current], arr[following]


@timeit
def sort_insert_rev(arr):
    for top in range(1, len(arr)):
        i = top
        while i > 0 and arr[i - 1] < arr[i]:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


@timeit
def sort_bubble_rev(arr):
    for bypass in range(1, len(arr)):
        for i in range(len(arr) - bypass):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


@timeit
def sort_choice_rev(arr):
    for current in range(len(arr) - 1):
        for following in range(current + 1, len(arr)):
            if arr[following] > arr[current]:
                arr[following], arr[current] = arr[current], arr[following]


arr_sort = [
            [sort_bubble, sort_bubble, sort_bubble_rev],
            [sort_choice, sort_choice, sort_choice_rev],
            [sort_insert, sort_insert, sort_insert_rev]
        ]


def gen_arr_rand_num(amount):
    return [random.randint(0, 10000) for _ in range(amount)]
