import sys

def readGraph(input_file):
    with open(input_file, 'r') as f:
        raw = [line.split(',') for line in f.read().splitlines()]

    N = int(raw[0][0])
    sin = raw[1]
    s = []
    for st in sin:
        s.append(int(st))
    adj_list = []
    for line in raw[2:]:
        if line == ['-']:
            adj_list.append([])
        else:
            adj_list.append([int(index) for index in line])
    return N, s, adj_list

def writeOutput(output_file, level):
    with open(output_file, 'w') as f:
        for i in level:
            f.write(str(i) + '\n')

 

def Run(input_file, output_file):
    N, s, adj_list = readGraph(input_file)
    level =   BFS(N, s, adj_list)
    writeOutput(output_file, level)

def  BFS(N, s, adj_list):

    level = ['x']*N
    checked = ['false']*N

    level[s[0]] = 0
    queue = [s[0]]

    while queue:
        node = queue.pop(0)
        if checked[node] == 'true':
          continue
        else:
          for x in adj_list[node]:
              if level[x] == "x":
                level[x] = level[node] + 1
                queue.append(x)
        checked[node] = 'true'

    return level

def main(args=[]):
    Run('input', 'output')


if __name__ == "__main__":
    main(sys.argv[1:])    
