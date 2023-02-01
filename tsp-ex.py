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

#TODO: Implement this shit god damn Im bad at recursion
def exhaustive_tour():
    return 0
    

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