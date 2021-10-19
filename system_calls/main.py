



def generate_output_for_strace_file(input_file, output_file):
    structure = []
    with open(input_file, "r") as fhandle:
        lines = fhandle.readlines()
        index = 0
        while index < (len(lines) - 2):
            temp = {}
            temp["time"] = lines[index].partition(" ")[0]
            temp["func"] = lines[index].partition(" ")[2].partition("(")[0]
            while "=" not in lines[index]:
                index = index + 1
            while "<" not in lines[index]:
                index = index + 1
            tstr = lines[index]
            while "<" in tstr:
                tstr = tstr.partition("<")[2]
            temp["duration"] = float( tstr.partition(">")[0] ) * 1000
            structure.append(temp)
            index = index + 1

    analysis_list = []
    for call in structure:
        funcs = [ i['func'] for i in analysis_list ]
        if call["func"] in funcs:
            analysis_list[funcs.index(call["func"])]["num"] = analysis_list[funcs.index(call["func"])]["num"] + 1
            analysis_list[funcs.index(call["func"])]["time"] = analysis_list[funcs.index(call["func"])]["time"] + call["duration"]
        else:
            temp = {}
            temp["func"] = call["func"]
            temp["num"] = 1
            temp["time"] = float(call["duration"])
            analysis_list.append(temp)
    for temp in analysis_list:
        temp["time"] = temp["time"] / temp["num"]

    with open(output_file, "w") as fhandle:
        for ele in analysis_list:
            string = str(ele["func"]) + "," + str(ele["num"]) + "," + str("{0:.3f}".format(ele["time"])) + "\n"
            fhandle.write(string)

def main():
    input_file = "buggy-python.txt"
    output_file = "output-buggy-python.txt"
    generate_output_for_strace_file(input_file, output_file)

    input_file = "neutral-python.txt"
    output_file = "output-neutral-python.txt"
    generate_output_for_strace_file(input_file, output_file)

if __name__=='__main__':
    main()