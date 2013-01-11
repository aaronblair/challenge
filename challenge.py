from itertools import permutations, combinations
from math import factorial
from pprint import pprint

def get_perm_solution(input_string, perm_length):
    perms = list(permutations(input_string, perm_length))

def find_best_perm(letter_set, perms_left, cur_str=''):
    if not letter_set:
        return cur_str

def brute_force(input_string, perm_length):
    perms_3 = set(permutations(input_string, perm_length))

    #the first one is a gimme!
    perms_3.difference_update(set(combinations(input_string, perm_length)))

    solution_found = False
    num_perms = 5
    while not solution_found:
        big_list = list(permutations(list(permutations(input_string)), num_perms))
        print len(big_list)
        solution_found = True


def nCr(n,r):
    f = factorial
    return f(n) / f(r) / f(n-r)

def check_solution(solution_list, perm_length):
    print '\nChecking Potential Solution:'
    pprint(solution_list)
    print

    #check the list is correctly formed
    for item in solution_list:
        if len(item) != len(solution_list[0]):
            print 'Not all entries are of correct length: {0}'.format(item)
            return False
        for char in item:
            if item.count(char) > 1:
                print 'Duplicate letter {0} found in solution text {1}'.format(char, item)
                return False

    # Get all permutations
    perms = set(permutations(solution_list[0], perm_length))

    print '{0} possible permutations exist and need to be satisfied\n'.format(len(perms))

    for item in solution_list:
        num_perms = len(perms)
        perms.difference_update(set(combinations(item, perm_length)))
        print '{0}    {1} permutations satisfied'.format(item, num_perms-len(perms))

    if len(perms) == 0:
        print '\nSuccess, problem solved with {0} permutations'.format(len(solution_list))
        return True

    print '\nProblem not satisfied, {0} permutations remaining:'.format(len(perms))
    pprint(perms)
    return False

input_string = 'ABCEFHIJLMNPQTVXYZ'
#input_string = 'EISH'

#test_solution = ['EISH','HESI','IEHS','HISE','SEHI','SIHE']
#test_solution = ['ABCEFHIJLMNPQTVX','XQVTEACBPLNMJFIH','HFJIBAECTQXVMLPN','XTVQJHIFPMNLEBCA',
#                 'NLPMCAEBVQXTIFJH','NMPLIHJFVTXQCBEA','AFLQBHMTCINVEJPX','XEPJQALFVCNITBMH',
#                 'HBTMFAQLJEXPICVN','XJPETHMBVINCQFLA','NCVILAQFPEXJMBTH','NIVCMHTBPJXELFQA']

test_solution = ['ABCEFHIJL','ACBILJEHF','FEHBACJIL','FHEJLIBCA',
                 'LIJCABHEF','LJIHFECBA','AEIBFJCHL','AIECLHBJF',
                 'FBJEAIHCL','FJBHLCEIA','LCHIAEJBF','LHCJFBIEA']


#check_solution(test_solution, 3)

brute_force('EISH', 3)