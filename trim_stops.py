import sys

def main():
    if len(sys.argv) != 3:
        print "Usage: trim_trips.py <input.txt> <output.txt>"
        return

    with open(sys.argv[1]) as input_file, open(sys.argv[2], "w") as output_file:
        first_line = next(input_file)
        # Remove parent_station column
        output_file.write(",".join(first_line.split(",")[:-1]) + "\n")
        for line in input_file:
            line_cells = line.split(",")
            output_file.write(",".join(line_cells[:-1]) + "\n")

if __name__ == "__main__":
    main()
