def read_table(fname):
    table = []

    with open(fname, "r") as f:
        table = []
        while True:
            line = f.readline().strip()
            if (len(line)):
                table.append([float(x) for x in line.split()])
            else:
                break
    
    return table

def print_table(table):
    print("{:10s}|{:10s}".format("    X", "     Y"))
    for i in range(len(table)):
        print("{:10.3f}|{:10.3f}".format(table[i][0], table[i][1]))
