wall = "⬛"
empty = "🟩"
full = "❎"
labyrinth = [
"⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛",
"🟥🟩⬛🟩🟩🟩🟩⬛🟩⬛",
"⬛🟩⬛🟩⬛🟩🟩⬛🟩⬛",
"⬛🟩🟩🟩⬛⬛🟩🟩🟩⬛",
"⬛⬛⬛🟩🟩⬛🟩⬛⬛⬛",
"⬛🟩🟩🟩⬛🟩🟩🟩🟩⬛",
"⬛🟩⬛⬛⬛⬛🟩⬛🟩⬛",
"⬛🟩⬛🟩⬛🟩🟩⬛🟩⬛",
"⬛🟩🟩🟩🟩🟩⬛🟩🟩🟦",
"⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"]

#start = (int(input("Starting row: ")), int(input("Starting column: ")))


def bfs(lab, start=(1,1), end=(8,8)):
        #printing the unsolved labyrinth
        print("Original labyrinth:\n")
        numbers= []
        for i in range(len(lab)):
            numbers.append(str(i))
        print("   "+" ".join(numbers))

        for i in range(len(lab)):
            print(str(i)+" "+lab[i])

        print("")

        #defining things for later
        been_there = []
        paths = [[start]]
        moves = [(-1,0), (0,-1), (1,0), (0,1)]

        #starting the search
        while end not in been_there:
            #trying all avaiable paths
            for i in range(len(paths)):
                if paths[i][-1] != "Dead End":
                    path_options = []
                    #checking how each path could extend
                    for j in moves:
                        if lab[paths[i][-1][0]+j[0]][paths[i][-1][1]+j[1]] == empty and (paths[i][-1][0]+j[0], paths[i][-1][1]+j[1]) not in paths[i]:
                            path_options.append((paths[i][-1][0]+j[0], paths[i][-1][1]+j[1]))
                    been_there.extend(path_options)

                    #extending paths + crearing new if there is a fork
                    if len(path_options)>2:
                        paths.append([])
                        paths.append([])
                        paths[-2]=paths[i]+[path_options[2]]
                        paths[-1]=paths[i]+[path_options[1]]
                        paths[i].append(path_options[0])

                    elif len(path_options)==2:
                        paths.append([])
                        paths[-1]=paths[i]+[path_options[1]]
                        paths[i].append(path_options[0])


                    elif len(path_options) == 1:
                        paths[i].append(path_options [0])
                    else:
                         paths[i].append("Dead End")
        #finding first complete path (if there are multiple)
        for i in range(len(paths)):
            if end in paths[i]:
                path = paths[i]
                break
        #printing the solution
        print("The fastest solution:\n")
        solution = lab
        for i in path:
            solution[i[0]]= solution[i[0]][:i[1]] + full + solution[i[0]][i[1]+1:]

        numbers= []
        for i in range(len(solution)):
            numbers.append(str(i))
        print("   "+" ".join(numbers))

        for i in range(len(solution)):
            print(str(i)+" "+solution[i])

bfs(labyrinth)
