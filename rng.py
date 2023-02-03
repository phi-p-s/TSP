import random

#n is how many inputs it should take
def generate_file(n, points):
    p = "input-" + str(n) + '.txt'
    try:
        file = open(p,'w')
        print("File Exists")
    except IOError:
        file = open(p, 'w+')
        print("File Created")
    file.write(str(n) + '\n')
    for point in points:
        string = point[0] + " " + point[1] + '\n'
        file.write(string)
    return 0

#n is the length of the list
def generate_list(n):
    points = []
    x = 0
    y = 0
    for i in range(n):
        #please dont give me duplicates
        while True:
            x = random.randint(-(10**4), 10**4)
            y = random.randint(-(10**4), 10**4)
            point = [str(x), str(y)]
            if point in points:
                continue
            else:
                break
        points.append(point)
    return points

def main():
    #4 sets of files I know i couldve done this in a loop but its only 4 of them
    points_10 = generate_list(10)
    points_11 = generate_list(11)
    points_8 = generate_list(8)
    points_9 = generate_list(9)
    points_7 = generate_list(7)
    generate_file(len(points_10), points_10)
    generate_file(len(points_11), points_11)
    generate_file(len(points_8), points_8)
    generate_file(len(points_9), points_9)
    generate_file(len(points_7), points_7)

    points_56 = generate_list(56)
    points_112 = generate_list(112)
    points_225 = generate_list(225)
    points_450 = generate_list(450)
    points_900 = generate_list(900)
    
    generate_file(len(points_56), points_56)
    generate_file(len(points_112), points_112)
    generate_file(len(points_225), points_225)
    generate_file(len(points_450), points_450)
    generate_file(len(points_900), points_900)
    return 0

if __name__ == "__main__":
    main()