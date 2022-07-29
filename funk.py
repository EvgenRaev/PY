#перше завдання
def arg1(x):
    def arg2(y):
        return x + y
    return arg2


sum = arg1(10)
print(sum(5))

#друге завдання

def funk():
   xx = 1
   yy = 2
   zz = 3

print ("Кількість змінних:", funk.__code__.co_nlocals)

#третє завдання СПИСАВ У ВАС




nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]

def choose_func(nums: list, func1, func2):
    chek = [x > 0 for x in nums]

    if all(chek):
        return func1 (nums)
    return func2 (nums)




assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]


