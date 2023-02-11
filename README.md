# Practical 03: Fighting Software Complexity by Using Dependencies and How Poetry Makes It Easy

## Introduction

In this practical assignment, you will extend a sorting program, `sort.py`, using a dependency called [Typer](https://typer.tiangolo.com/) to improve its command-line interface. Through this process, you will learn how to manage dependencies using [Poetry](https://python-poetry.org/), a dependency management tool for Python.Through this exercise, you will put into practice the following learning objective(s):

- How to fight software complexity by using dependencies

## Instructions

Please perform each of the following steps in order.

### Install Poetry

If you do not already have Poetry installed, [install Poetry with the official installer](https://python-poetry.org/docs/master/#installing-with-the-official-installer).

### Review the Sorting Program

In the first practical assignment, you implemented a sorting program, `sort.py`, that sorts a list of numbers in either ascending or descending order.

```console
$ python sort.py 23 4 15 8 16 42
[4, 8, 15, 16, 23, 42]
```

```console
$ python sort.py desc 23 4 15 8 16 42
[42, 23, 16, 15, 8, 4]
```

### Learn About How the Sorting Program Should Change

In this practical assignment, you will modify and extend the behavior of `sort.py`. Note that this step only introduces the changes you will make and that you should not yet make these changes.

Firstly, notice that in `sort.py`, `desc` must be given as the first command-line argument after the script name to sort in descending order. You will modify `sort.py` so that it accepts a `--desc` command-line option that can be given either before or after the list of numbers to sort in descending order.

```console
$ python sort.py --desc 23 4 15 8 16 42
[42, 23, 16, 15, 8, 4]
```

```console
$ python sort.py 23 4 15 8 16 42 --desc
[42, 23, 16, 15, 8, 4]
```

Secondly, you will add a `--max` option that can be given to specify a maximum value for the list of numbers. When this `--max` option is given, the sorted list of numbers should exclude all numbers above the maximum value.

```console
$ python sort.py 23 4 15 8 16 42 --max 16
[4, 8, 15, 16]
```

The `--desc` and `--max` options should be able to be used together.

```console
$ python sort.py --desc 23 4 15 8 16 42 --max 16
[16, 15, 8, 4]
```

Lastly, you will add a `--help` option that prints a help message when given. This help message should explain the usage of `sort.py` and the meaning of its options.

```console
$ python sort.py --help
Usage: sort.py [OPTIONS]

Options:
  --desc / --no-desc              Sort numbers in descending order  [default:
                                  no-desc]
  --max INTEGER                   Exclude any numbers above this number
  --help                          Show this message and exit.
```

### Analyze `sort_no_deps.py`

The changes described in the previous step have been implemented without the use of any dependencies in `sort_no_deps.py`. Notice how these improvements to the command-line interface, which may have seemed simple, required significant additions to the code. And, although thought _was_ put into the design of `sort_no_deps.py`, it is still obviously more complex than the `sort_original.py` program.

### Use Typer to Modify and Extend the Sorting Program

Often the best way to avoid increasing the complexity of a program is to avoid adding code at all. When you need to add features to a program, such as command-line options, you should always first search the Internet for any packages that enable you to add the features with minimal additions to your code. When deciding whether or not you will use, or depend on, a package, you should evaluate the usability and sustainability of the package, or dependency.

To determine a package's usability, you should assess the simplicity and documentation of its interface. How much code will using the package add to your program? How much code will using the package help you avoid writing? Does it come with documentation that helps you quickly understand how to use the package? If you answer, "A little", "A lot", and "Yes", then the package is promising and you should move on to determining its sustainability. If you answer, "A lot", "A little", and "No", then it may be time to look for another package.

To determine a package's sustainability, you should assess its popularity and the activity of its maintainers. How many stars on GitHub does the package repository have relative to other packages that do similar things? How recent was the last commit in the package repository? These metrics will give you an approximation of the sustainability of the package, or how likely it is to be maintained over time. In general, it is better to use a package that is actively maintained; if a package is actively maintained, it is more likely that any bugs in the package will be fixed quickly and the package's interface will be routinely improved.

Typer is a package for building command-line interfaces. If you look at [its documentation](https://typer.tiangolo.com/), you will see that it takes very few lines of code to create a command-line interface with Typer. Additionally, if you look at [its GitHub repository](https://github.com/tiangolo/typer), you will see that it is a popular package that is actively maintained. For these reasons, you will use Typer to improve the command-line interface of `sort.py`.

By default, to use a Python package, you need to install it on your computer with the `pip` package installer. However, when you install Python packages on your computer with `pip`, these packages will be shared across all Python projects on your computer, which can cause several issues. Firstly, it would not be possible to have two Python projects on your computer that require different versions of the same package. Secondly, over time, if you are not vigilant about uninstalling packages you no longer need, you can end up with many Python packages installed on your computer that you are not using in current projects. Thirdly, when another person would like to collaborate on your project, they will need to install the Python packages required for your project on their computer; this is both tedious and may cause issues for the other Python projects they already have on their computer.

For these reasons, it is better to install packages _per project_ rather than _per computer_. [Poetry](https://python-poetry.org/) is a tool that allows you to do just this. When you use Poetry for your project, you can specify the packages and their versions that should be installed in a virtual environment to be used only for your project. This means that two Python projects on the same computer can have different versions of the same package since the package will be installed in a virtual environment specific to each project. Additionally, virtual environments can be easily removed when no longer needed, which makes it easier to keep your computer clean of unused packages. Lastly, when someone collaborates on your project, they can use Poetry to create an identical virtual environment that contains all Python packages required for your project on their computer.

To use Poetry for an existing project, you must first run `poetry init` in the root of the project's repository. You can press `Enter` to accept each of the default options. Once you have run `poetry init` in this repository, you should see a `pyproject.toml` file. Notice that there is a `[tool.poetry.dependencies]` section in this file. When you add a Python package, or dependency, to your project with Poetry, it will add the dependency's name and version in this section. To activate the virtual environment and install dependencies, run `poetry install` in the directory where `.toml` file of the project is located.

`sort.py` contains the start of a program that uses Typer and imports the `typer` package. Run `poetry run python sort.py 23 4 15 8 16 42`. Notice that Poetry first creates a virtual environment for your project and that starting with the command `poetry run` runs the `python sort.py 23 4 15 8 16 42` command within this virtual environment. You should see the following error.

```console
ModuleNotFoundError: No module named 'typer'
```

If you look in your `pyproject.toml`, you will notice that the `[tool.poetry.dependencies]` does not contain `typer`. This means that the virtual environment for this project does not yet have Typer installed. You can install the Typer package by running `poetry add typer`. After you run this command, you should then see `typer` in your `pyproject.toml`.

Run `poetry run python sort.py 23 4 15 8 16 42` again. Now, you should see a different error.

```console
NameError: name 'desc' is not defined
```

Referring to the Typer documentation on adding [CLI Options with Help](https://typer.tiangolo.com/tutorial/options/help/) and defining [CLI Option Names](https://typer.tiangolo.com/tutorial/options/name/), complete the `sort.py` program, without modifying the body of the `main` function, so that it produces the output described in the "Learn About How the Sorting Program Should Change" section above. Note that all of the `python sort.py` commands listed in that section should be run in the virtual environment by running `poetry run python sort.py ...`. Also, note that GatorGrader will check that the description of each option in the help message is exactly the same as written in the "Learn About How the Sorting Program Should Change" section above.

### Reflection

Answer all questions in `writing/reflection.md`. As you do, commit your changes using best commit practices. Instead of creating a commit at the end with the message, "Answer reflection questions", you should commit after answering each question and describe your changes in the commit messages.

## Running GatorGrader

You can gain an approximation of your progress on this assignment by running [GatorGrader](https://github.com/GatorEducator/gatorgrader) locally. You do need to have `gatorgrade` and Python installed to be able to run this command (see instructions above).

```bash
gatorgrade --config config/gatorgrade.yml
```

## Receiving Assistance

If you are having trouble completing any part of this project, then please talk with either the course instructor or a student technical leader during the practical session. Alternatively, you may ask questions in the Discord channel for this course. Finally, you can schedule a meeting during the course instructor's office hours.

## Practical Assessment

The grade that a student receives on this practical assignment is a checkmark grade (0 or 1) and is based on:

- **GitHub Actions CI Build Status**: Students are encouraged to repeatedly try to complete the assignment until it passes all GitHub Actions jobs. Students will receive a checkmark grade if their last before-the-deadline build passes and a green ✔ appears in their GitHub commit log instead of a red ✗.

Students will receive 1 if their solution passes all GatorGrader checks and receives a green ✔ in their last commit.

All grades for this project will be reported through a student's GitHub gradebook repository.
