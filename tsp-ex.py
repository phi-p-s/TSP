import math
import sys
import time

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

def exhaustive_tour(temp_list, p, initial_point):
    #distance back to original
    t_list = temp_list
    if len(t_list) == 1:
        return calc_distance(initial_point, p)
    else:
        print("P: " + str(p))
        print("BEFORE: " + str(temp_list))
        t_list.remove(p)
        print("AFTER: " + str(temp_list))
        for point in t_list:
            check_dist = calc_distance(p, point)
            return exhaustive_tour(t_list, point, initial_point) + check_dist
def main():
    #start_time = time.time()
    input_t, n = read_input("fixed-input.txt")
    #print(input_t)
    #start at 0 idk if this is what they want
    ex_tour_list = []
    for i in range(n):
        new_list = input_t.copy()
        print("NEW START :P  \n")
        initial_point = new_list[i]
        ex_tour_list.append(exhaustive_tour(new_list, initial_point, initial_point))
    #round
    print(ex_tour_list)
    ex_tour = min(ex_tour_list)
    ex_tour = round(ex_tour, 3)
    print("%.3f" % ex_tour)
    #print("Time in seconds: " + str(time.time() - start_time))

if __name__ == "__main__":
    main()