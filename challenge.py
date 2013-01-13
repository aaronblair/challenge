from itertools import permutations, combinations
from math import factorial
from pprint import pprint

def brute_force(input_string, perm_length):
    perms_3 = set(permutations(input_string, perm_length))

    #the first one is a gimme!
    perms_3.difference_update(set(combinations(input_string, perm_length)))

    solution_found = False
    perm_sets = [frozenset([input_string])]
    while not solution_found:
        max_perms_solved = 0
        for fset in perm_sets:
            temp_set = set(perms_3)
            for a in fset:
                temp_set.difference_update(a)
            next_best, perms_solved = _find_next_best(temp_set, list(fset), input_string, perm_length)
            if perms_solved > max_perms_solved:
                new_perm_set = set()
                max_perms_solved = perms_solved
            if perms_solved == max_perms_solved and perms_solved > 0:
                for i in next_best:
                    new_perm_set.add(frozenset(fset.union({i})))
            del temp_set

        perm_sets = list(new_perm_set)

        if max_perms_solved == 0:
            solution_found = True

    return perm_sets

def _find_next_best(perm_set, current_list, input_string, perm_length):

    for i in current_list:
        perm_set.difference_update(set(combinations(i, perm_length)))

    big_list = [''.join(a) for a in permutations(input_string)]

    max_perms_solved = 0
    best_perm_list = []
    for perm in big_list:
        solved_perms = set(combinations(perm, perm_length))
        num_solved_perms = len(perm_set.intersection(solved_perms))
        if num_solved_perms > max_perms_solved:
            del best_perm_list[:]
            max_perms_solved = num_solved_perms
        if num_solved_perms == max_perms_solved:
            best_perm_list.append(perm)

    return best_perm_list,max_perms_solved

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

bf = brute_force('ABCDE', 3)
for a in bf:
    print a
print len(bf)

#a = brute_force('EIHS', 3)
#
#pprint(a)
#print len(a[0])
#print len(a)