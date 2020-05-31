#Next bigger number with the same digits
#a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.
'''
 For example:
 12 ==> 21
513 ==> 531
2017 ==> 2071
'''


from itertools import permutations
def next_bigger(n):
    #your code here
    if len(str(n)) == 1:
        return n
    else:
        permute = list(permutations(int(dig) for dig in str(n)))
        num_list = [int(''.join([str(each_dig) for each_dig in list(nums)])) for nums in permute]
        return max(num_list)
