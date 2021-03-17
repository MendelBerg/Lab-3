import tools as t

nums = [5000, 10000, 20000]

for amount in nums:
    print(f'!!!!!!!!!!!!!!!!!!\tARR #{nums.index(amount)+1}\t!!!!!!!!!!!!!!!!!!!!!!!!')
    arr_init = t.gen_arr_rand_num(amount)
    for func_type in t.arr_sort:
        arr = [num for num in arr_init]
        for sort_func in func_type:
            sort_func(arr)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
