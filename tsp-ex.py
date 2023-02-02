import math
import sys
import time
from itertools import permutations
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
    return input_a

#distance formula
def calc_distance(point_1, point_2):
    p1 = point_1
    p2 = point_2
    d = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return d

#TODO: Implement this
def exhaustive_tour(temp_list, start_index):
    points = []
    start_point = temp_list[start_index]
    for point in temp_list:
        #don't store the initial point, because we only need to examine one start point for exhaustive (repeats)
        if point != start_point:
            points.append(point)
    #get all permutations of the points
    distances = []
    #j = 0
    for permutation in permutations(points):
        current_distance = 0
        for i in range(len(permutation)-1):
            #get the first side
            if i == 0:
                current_distance += calc_distance(temp_list[start_index], permutation[i])
            current_distance += calc_distance(permutation[i], permutation[i+1])
        #get the last side
        current_distance += calc_distance(temp_list[start_index], permutation[i+1])
        #store into a list
        distances.append(current_distance)
    return min(distances)
    

def main():
    start_time = time.time()
    if len(sys.argv) != 1:
        input_t = read_input(str(sys.argv[1]))
    else: 
        input_t = read_input("input-10.txt")
    ex_tour = exhaustive_tour(input_t, 0)
    #round
    ex_tour = round(ex_tour, 3)
    print("%.3f" % ex_tour)
    print("Time in seconds: " + str(time.time() - start_time))

if __name__ == "__main__":
    main()