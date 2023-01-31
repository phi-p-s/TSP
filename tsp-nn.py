import math
#Read file, give me n and also 2xn array for all the points
def read_input(fname):
    f_input = open(fname, "r").read().split('\n')
    n = int(f_input[0])
    input_t = f_input[1:]
    input_a = []
    #split input into 2d array
    for i in range(n):
        input_a.append(input_t[i].split())
        #change from string to int
        for j in range(2):
            input_a[i][j] = int(input_a[i][j])
    return input_a, n

#distance formula
def calc_distance(point_1, point_2):
    p1 = point_1
    p2 = point_2
    d = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return d

#input_t is the input, i is which point its visiting
def nearest_neighbor(not_visited_list, p, initial_point):
    #distance back to original
    if len(not_visited_list) == 1:
        return calc_distance(initial_point, p)
    else:
        print("P: " + str(p))
        print("BEFORE: " + str(not_visited_list))
        not_visited_list.remove(p)
        print("AFTER: " + str(not_visited_list))
        min = calc_distance(p, not_visited_list[0])
        closest_point = not_visited_list[0]
        for point in not_visited_list:
            check_dist = calc_distance(p, point)
            if check_dist < min:
                min = check_dist
                closest_point = point
        return nearest_neighbor(not_visited_list, closest_point, initial_point) + min
            
            
        
    

def is_visited(point):
    return point[-1]

input_t, n = read_input("fixed-input.txt")
print(input_t)
not_visited_list = input_t
#start at 0
print(nearest_neighbor(not_visited_list, not_visited_list[0], not_visited_list[0]))

