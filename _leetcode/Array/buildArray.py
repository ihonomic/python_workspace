def buildArray():
    """ Build array from permutation. 
        nums =[0,2,1,5,3,4]
        ans = [0,1,2,4,5,3]
        such that ans[i] = nums[nums[i]] 
    Method 1 - Traverse through apply the formular. (time, space) = 0(n)
    Method 2 - Traverse twice. 
                * First Traverse, Apply (qb + r) to each element, 
                * Second Traverse, remove (q) from each element
                (time, space) = 0(n), 0(1)
    Method 3 - Flag previous value and new value, return old values
    """
    nums = [0, 2, 1, 5, 3, 4]

    #   Method 1
    # res = []
    # for i in range(len(nums)):
    #     res.append(nums[nums[i]])
    # return res

    #   Method 2
    #                               ---> 1
    """     For each element use the formular a = qb + r
      where q = len(nums),
            b = Given build formular => nums[nums[i]] % q
            r = nums[i]
    """
    q = len(nums)

    for i in range(len(nums)):
        r = nums[i]
        b = nums[nums[i]] % q
        nums[i] = q*b + r
    #                               ---> 2
    # extract just the final b values
    for i in range(len(nums)):
        nums[i] = nums[i] // q
    return nums

    #   Method 3
    # Flag previous value and new value, return old values
    str_maker = None
    for i in range(len(nums)):
        if type(nums[nums[i]]) == int:
            str_maker = str(nums[i]) + "|" + str(nums[nums[i]])
            nums[i] = str_maker
        else:
            str_maker = str(nums[i]) + "|" + nums[nums[i]].split('|')[0]
            nums[i] = str_maker

    for i in range(len(nums)):
        nums[i] = int(nums[i].split('|')[1])

    return (nums)


# print(buildArray())
