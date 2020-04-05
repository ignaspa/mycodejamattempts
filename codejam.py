import sys

def find_answer(my_array):
    n = len(my_array)
    my_cols = {}
    num_rep_row = 0
    num_rep_col = 0
    trace = 0
    for k in range(len(my_array)):
        my_cols[k] = []

    for k in range(len(my_array)):
        row_safe = True
        for y in range(len(my_array[k])):
            if row_safe and my_array[k][y] in my_array[k][:y]:
                num_rep_row += 1
                row_safe = False
            if my_cols[y] != -1 and my_array[k][y] in my_cols[y]:
                my_cols[y] = -1
                num_rep_col += 1
            if my_cols[y] != -1:
                my_cols[y].append(my_array[k][y])
            if k == y:
                trace += int(my_array[k][y].strip())
    
    return ": " + str(trace) + " " + str(num_rep_row) + " " + str(num_rep_col)

my_array = sys.stdin.readlines()
num_tests = int(my_array[0].strip())
iter = 1
solution = ""
for k in range(num_tests):
    size = int(my_array[iter].strip())
    iter += 1
    this_array = []
    for z in range(size):
        this_array.append(my_array[iter].split(" "))
        iter += 1
    
    if k < num_tests - 1:
        solution = solution + "Case #" + str(k + 1) + find_answer(this_array) + "\n"
    else:
        solution = solution + "Case #" + str(k + 1) + find_answer(this_array)

print(solution)

