# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    # get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    if len(sequence) == 1:
        return [sequence]
    else:
        permutations = []
        extra = sequence[0]
        smaller = sequence[1:]
        # 最内层获得[t],[s]，然后组合成[t,s],[s,t]，最后在外层分别与u组合得到最终结果
        for small in get_permutations(smaller):
            for i in range(len(small)+1):
                permutations += [small[:i] + extra + small[i:]]  # 把extra字符依次插入0-len(small)的位置

        return permutations

if __name__ == '__main__':
#    #EXAMPLE
#     example_input = 'abc'
#     print('Input:', example_input)
#     print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#     print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'ust'
    print('Input:', example_input)
    print('Expected Output:', ['ust', 'sut', 'stu', 'uts', 'tus', 'tsu'])
    print('Actual Output:', get_permutations(example_input))
    print("----------------")
    example_input = '123'
    print('Input:', example_input)
    print('Expected Output:', ['123', '213', '231', '132', '312', '321'])
    print('Actual Output:', get_permutations(example_input))
    print("----------------")
    example_input = 'xyz'
    print('Input:', example_input)
    print('Expected Output:', ['xyz', 'yxz', 'yzx', 'xzy', 'zxy', 'zyx'])
    print('Actual Output:', get_permutations(example_input))

