import tools as t

for amount in [5000, 10000, 20000]:
    arr = t.gen_arr_rand_num(amount)
    for sort_func in t.arr_sort:
        sort_func(arr)
    print('==============================')
