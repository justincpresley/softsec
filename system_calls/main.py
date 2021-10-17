def generate_output_for_strace_file(input_file, output_file):
    structure = []
    with open(input_file, "r") as fhandle:
        temp = []

def main():
    input_file = "buggy-python.txt"
    output_file = "output-buggy-python.txt"
    generate_output_for_strace_file(input_file, output_file)

    input_file = "neutral-python.txt"
    output_file = "output-neutral-python.txt"
    generate_output_for_strace_file(input_file, output_file)

if __name__=='__main__':
    main()