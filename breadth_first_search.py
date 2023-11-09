import string
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

def print_labyrinth(lab: list[str], path: list[tuple[int, int]] = None):
    if path != None:
       for i in path:
            lab[i[0]]= lab[i[0]][:i[1]] + full + lab[i[0]][i[1]+1:]
    numbers= []
    for i in range(len(lab)):
        numbers.append(str(i))
    print("   "+" ".join(numbers))
    for i in range(len(lab)):
        print(str(i)+" "+lab[i])
    print("")

def prompt_integer(position: str, message: str) -> int:
    integer = input(f"{position} of {message}: ")
    while integer.isdigit() != True:
        integer = input()
    return int(integer)

def prompt_user_for_location(name: str) -> tuple[int, int]:
    row = prompt_integer("Row", name)
    col = prompt_integer("Column", name)
    print("")
    return (row, col)    
            
def bfs(lab: list[str], start: tuple[int, int] = (1, 1), end: tuple[int, int] = (8, 8)) -> list[tuple[int, int]]:
        #defining things for later
        been_there = []
        paths = [[start]]
        moves = [(-1,0), (0,-1), (1,0), (0,1)]

        #starting the search
        while end not in been_there:
            #trying all avaiable paths
            for i in range(len(paths)):
                if paths[i][-1] != False:
                    path_options = []
                    #checking how each path could extend
                    for j in moves:
                        if lab[paths[i][-1][0]+j[0]][paths[i][-1][1]+j[1]] == empty and (paths[i][-1][0]+j[0], paths[i][-1][1]+j[1]) not in paths[i]:
                            path_options.append((paths[i][-1][0]+j[0], paths[i][-1][1]+j[1]))
                    been_there.extend(path_options)

                    #extending paths + creating new if there is a fork
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
                         paths[i].append(False)

        #finding first complete path (if there are multiple)
        for i in range(len(paths)):
            if end in paths[i]:
                path = paths[i]
                return path

print_labyrinth(labyrinth)
start = prompt_user_for_location("start")    
end = prompt_user_for_location("end") 
print_labyrinth(labyrinth, bfs(labyrinth, start, end))
