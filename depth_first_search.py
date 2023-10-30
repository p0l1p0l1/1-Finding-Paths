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
start = (1, 1)
end = (8, 8)

def search(lab, start, end):
        print("Original labyrinth:\n")
        numbers= []
        for i in range(len(lab)):
            numbers.append(str(i))
        print("   "+" ".join(numbers))

        for i in range(len(lab)):
            print(str(i)+" "+lab[i])

        print("")

        path = [start]
        position = start
        forks = [start]
        dead_ends = []
        earlier_paths = []

        print("Paths tried: \n")
        while position != end:
            path_counter = 0
            directions = [(position[0]-1, position[1]), (position[0], position[1]-1),(position[0]+1, position[1]), (position[0], position[1]+1)]

            for i in directions:
                if lab[i[0]][i[1]] == empty and i not in dead_ends and i not in path:
                    path_counter += 1

            if path_counter > 1:
                forks.append(position)

            if path_counter > 0:
                for i in directions:
                    if lab[i[0]][i[1]] == empty and i not in path and i not in dead_ends:
                        position = i
                        path.append(position)
                        break


            elif path_counter<1:
                path.append(position)
                print(path, "Failure :c")
                if path in earlier_paths:
                    dead_ends += path[path.index(forks[-2]):]
                    path = path[:path.index(forks[-2])+1]
                    position = forks[-2]
                else:
                    earlier_paths.append(path)
                    dead_ends += path[path.index(forks[-1]):]
                    path = path[:path.index(forks[-1])+1]
                    position = forks[-1]


        print(path, "Success!\n\nA solution:\n")

        solution = lab
        for i in path:
            solution[i[0]]= solution[i[0]][:i[1]] + full + solution[i[0]][i[1]+1:]

        numbers= []
        for i in range(len(solution)):
            numbers.append(str(i))
        print("   "+" ".join(numbers))

        for i in range(len(solution)):
            print(str(i)+" "+solution[i])

print("")
search(labyrinth, start, end)
