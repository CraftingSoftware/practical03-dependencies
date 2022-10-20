from typing import List
import typer


def main(
    numbers: List[int],
    # TODO: Add --desc and --max options
):
    # Do not modify this function body
    numbers = list(numbers)  # Work around Typer issue #127
    numbers.sort(reverse=desc)
    if max_value is not None:
        numbers = [number for number in numbers if number <= max_value]

    print(numbers)


if __name__ == "__main__":
    typer.run(main)
