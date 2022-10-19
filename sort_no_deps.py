import sys


def print_help():
    """
    Print a help message and exit.
    """
    print(
        """Usage: sort.py [OPTIONS]

Options:
  --desc / --no-desc              Sort numbers in descending order  [default:
                                  no-desc]
  --max INTEGER                   Exclude any numbers above this number
  --help                          Show this message and exit.
"""
    )
    sys.exit()


# Globals
desc = False
max_value = None
numbers = []


def parse_args():
    """
    Parse the command-line arguments to get options and numbers.
    """
    args = sys.argv
    args.pop(0)  # Remove script name
    if "--help" in args:
        print_help()
    if "--desc" in args:
        global desc
        desc = True
        args.remove("--desc")
    if "--max" in args:
        max_option_index = args.index("--max")
        try:
            global max_value
            max_value = int(args[max_option_index + 1])
        except ValueError:
            print(
                f"Error: Invalid value for '--max': '{max_value}' is not a valid integer."
            )
        del args[
            max_option_index : max_option_index + 2
        ]  # Remove the '--max' option and its value
    global numbers
    numbers = [int(number) for number in args]  # args now contains only the numbers


if __name__ == "__main__":
    parse_args()
    numbers.sort(reverse=desc)
    if max_value is not None:
        numbers = [number for number in numbers if number <= max_value]

    for index, number in enumerate(numbers):
        print(f"[{index}] {number}")
