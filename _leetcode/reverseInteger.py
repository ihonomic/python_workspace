def palindrome(x: int) -> bool:
    ''' Negative numbers or numbers dividable by 10 are not palindrome'''
    if x < 0 or (x > 0 and x % 10 == 0):
        return False

    ''' Because of reverse contraints, reverse the number halfway and compare 
        At HALFWAY, 
         -if odd length - the reverse-half will become greater than the first half
         -if even length - the reverse-half will equal the first half 
        You can compare at half-way. 
    '''
    reverse = 0
    while x > reverse:
        # Reassigning reverse, by taking the last integer but adding back in multiples of 10
        reverse = 10 * reverse + x % 10
        x = x // 10  # Reassign x by removing the last Integer

    return x == reverse or x == reverse // 10  # Even or Odd


# print(palindrome(31345))
