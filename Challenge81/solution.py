from math import factorial
from collections import defaultdict
#hope you enjoyed the challenge :smilecat:
def get_even_perm_count(num:str,frequency:dict[int,int],factorial_cache:dict[int,int],even_nums:list[int],mode):
    m=int(num[-1])
    if m%2==0:
        if m not in even_nums:even_nums.append(m)
    frequency[int(num[-1])]+=1
    total_length=len(num)-1
    if total_length not in factorial_cache:factorial_cache[total_length]=factorial(total_length)
    total_distinct_perms=factorial_cache[total_length]
    if mode:
        final_output = 0
        for even_num in even_nums:
            factorial_product=1
            zeros_in_first=1
            ans=0
            for other_num in frequency:
                if other_num!=even_num:
                    if other_num!=0:zeros_in_first*=factorial_cache[frequency[other_num]]
                    else:zeros_in_first*=factorial_cache[frequency[0]-1]

                    freq=frequency[other_num]
                    if freq not in factorial_cache:factorial_cache[freq] = factorial(freq)
                    factorial_product*=factorial_cache[freq]

                else:
                    if even_num!=0:zeros_in_first *= factorial_cache[frequency[even_num]-1]
                    else:
                        l = frequency[0]-2
                        if l>0:
                            if l not in factorial_cache:
                                factorial_cache[l] = factorial(l)
                            zeros_in_first *= factorial_cache[l]

                    if frequency[even_num]-1 > 1:
                        freq = frequency[even_num]-1
                        if freq not in factorial_cache:factorial_cache[freq] = factorial(freq)
                        factorial_product *= factorial_cache[freq]


            ans+=total_distinct_perms//factorial_product
            if even_num != 0 or num.count("0")>1:
                g = total_length-1
                if g not in factorial_cache:
                    factorial_cache[g] = factorial(g)
                ans -= factorial_cache[g]//zeros_in_first
            final_output+=ans
        return final_output, frequency, factorial_cache, even_nums

    else:
        ans = 0
        for even_num in even_nums:
            factorial_product = 1
            freq = 0
            for other_num in frequency.keys():
                if other_num != even_num:freq = frequency[other_num]
                else:freq = frequency[even_num]-1

                if freq not in factorial_cache:
                    factorial_cache[freq] = factorial(freq)
                factorial_product *= factorial_cache[freq]
            ans += total_distinct_perms//factorial_product
        return ans,frequency, factorial_cache, even_nums

for q in range(int(input())):
    num=input()
    final_ans=0
    factorial_cache = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120,6: 720, 7: 5040, 8: 40320}
    even_nums=[]
    mode=0
    frequency=defaultdict(lambda :0)
    for i in range(1,len(num)+1):
        n=num[:i]
        if not mode:
            if n[-1]=="0":
                mode=1
        ans,frequency,factorial_cache,even_nums=get_even_perm_count(n,frequency,factorial_cache,even_nums,mode)
        final_ans+=ans
    print(int(final_ans))
