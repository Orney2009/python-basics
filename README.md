# Python Basics Exercises

This repository contains a set of small Python exercises and utilities (ex_01 through ex_14) used to practice basic Python concepts: argument handling, dictionaries, lists, regular expressions, and simple I/O patterns.

## Repository layout

- [01_basics_04/required.py](01_basics_04/required.py) — contains [`REQUIRED`](01_basics_04/required.py).
- [ex_01/script.py](ex_01/script.py) — defines [`ex_01.asciiCounter`](ex_01/script.py).
- [ex_02/my_args_handler.py](ex_02/my_args_handler.py) — defines [`ex_02.my_args_handler`](ex_02/my_args_handler.py).
- [ex_03/double_return.py](ex_03/double_return.py) — defines [`ex_03.double_return`](ex_03/double_return.py).
- [ex_04/loader.py](ex_04/loader.py) — imports [`REQUIRED`](01_basics_04/required.py) via [ex_04/loader.py](ex_04/loader.py).
- [ex_05/show_methods.py](ex_05/show_methods.py) — defines [`ex_05.show_methods`](ex_05/show_methods.py).
- [ex_06/my_show_platypus.py](ex_06/my_show_platypus.py) — defines [`ex_06.my_show_platypus`](ex_06/my_show_platypus.py).
- [ex_07/display_all.py](ex_07/display_all.py) — defines [`ex_07.display_all`](ex_07/display_all.py).
- [ex_08/display_all.py](ex_08/display_all.py) — defines [`ex_08.display_all`](ex_08/display_all.py).
- [ex_09/display_all.py](ex_09/display_all.py) — defines [`ex_09.display_all`](ex_09/display_all.py).
- [ex_10/increment.py](ex_10/increment.py) — defines [`ex_10.increment`](ex_10/increment.py).
- [ex_11/shows.py](ex_11/shows.py) — defines [`ex_11.shows`](ex_11/shows.py).
- [ex_12/count_words.py](ex_12/count_words.py) — defines [`ex_12.my_count_words`](ex_12/count_words.py).
- [ex_13/sum_sub.py](ex_13/sum_sub.py) — defines [`ex_13.add`](ex_13/sum_sub.py).
- [ex_14/regexp.py](ex_14/regexp.py) — contains [`EMAIL`](ex_14/regexp.py) regular expression.

## Purpose of each exercise (brief)

- [`ex_01.asciiCounter`](ex_01/script.py): Count ASCII alphanumeric characters across provided CLI arguments.
  - File: [ex_01/script.py](ex_01/script.py)
- [`ex_02.my_args_handler`](ex_02/my_args_handler.py): Concatenate given arguments with `, ` separation and return as a string.
  - File: [ex_02/my_args_handler.py](ex_02/my_args_handler.py)
- [`ex_03.double_return`](ex_03/double_return.py): Return the keys and values of a dictionary as two lists (tuple).
  - File: [ex_03/double_return.py](ex_03/double_return.py)
- [`ex_04.loader`](ex_04/loader.py): Example of modifying `sys.path` to import [`REQUIRED`](01_basics_04/required.py).
  - Files: [ex_04/loader.py](ex_04/loader.py), [01_basics_04/required.py](01_basics_04/required.py)
- [`ex_05.show_methods`](ex_05/show_methods.py): Print the list of methods/attributes for the provided object.
  - File: [ex_05/show_methods.py](ex_05/show_methods.py)
- [`ex_06.my_show_platypus`](ex_06/my_show_platypus.py): Print the word "Platypus" `n` times.
  - File: [ex_06/my_show_platypus.py](ex_06/my_show_platypus.py)
- [`ex_07.display_all`](ex_07/display_all.py): Print all dictionary values with type annotations.
  - File: [ex_07/display_all.py](ex_07/display_all.py)
- [`ex_08.display_all`](ex_08/display_all.py): Print all dictionary items (key and value with type).
  - File: [ex_08/display_all.py](ex_08/display_all.py)
- [`ex_09.display_all`](ex_09/display_all.py): Print all dictionary items with index of the key.
  - File: [ex_09/display_all.py](ex_09/display_all.py)
- [`ex_10.increment`](ex_10/increment.py): Return a list where integer elements are incremented by 1; non-integers are preserved.
  - File: [ex_10/increment.py](ex_10/increment.py)
- [`ex_11.shows`](ex_11/shows.py): Print dictionary entries in a specific format including type.
  - File: [ex_11/shows.py](ex_11/shows.py)
- [`ex_12.my_count_words`](ex_12/count_words.py): Return a dictionary mapping each element of the input iterable to its count (uses `param.count`).
  - File: [ex_12/count_words.py](ex_12/count_words.py)
- [`ex_13.add`](ex_13/sum_sub.py): Reduce a list of CLI numeric strings with alternating add/sub behavior depending on parity of accumulator.
  - File: [ex_13/sum_sub.py](ex_13/sum_sub.py)
- [`ex_14.EMAIL`](ex_14/regexp.py): A compiled regular expression intended to validate email-like strings.
  - File: [ex_14/regexp.py](ex_14/regexp.py)

## How to run

These are simple Python scripts/modules. Use Python 3:

- Run an exercise script directly:
  - Example: python3 ex_01/script.py arg1 arg2
- Import a module and call functions inside a Python REPL or another script:
  - Example:
    ```python
    from ex_02.my_args_handler import my_args_handler
    print(my_args_handler("one", "two", "three"))
    ```

## Examples

- Call the argument handler:
  - [`ex_02.my_args_handler`](ex_02/my_args_handler.py)
  - Command: python3 -c "from ex_02.my_args_handler import my_args_handler; print(my_args_handler('a','b'))"
- Use the increment helper:
  - [`ex_10.increment`](ex_10/increment.py)
  - In REPL: from ex_10.increment import increment; increment([1, 'x', 3]) -> [2, 'x', 4]

## Notes & known issues

Some files contain logic or minor bugs you may want to address:

- [`ex_01.asciiCounter`](ex_01/script.py) — uses parameter name `string` but iterates over `arg` inside function; this will raise a NameError. See [ex_01/script.py](ex_01/script.py).
- [`ex_13.add`](ex_13/sum_sub.py) — uses a reduce with conversion and odd/even parity logic that may not match intended behavior for non-numeric input. See [ex_13/sum_sub.py](ex_13/sum_sub.py).
- [`ex_12.my_count_words`](ex_12/count_words.py) — uses `param.count(key)` which is O(n^2) for large lists/strings and may be unexpected for some input types. See [ex_12/count_words.py](ex_12/count_words.py).
- [`ex_14.EMAIL`](ex_14/regexp.py) — current regex appears malformed (contains spaces and brace expressions inside character classes). Verify and replace with a tested pattern. See [ex_14/regexp.py](ex_14/regexp.py).
- Many modules use `except Exception as e: print(e); exit(84)` — this will terminate the interpreter with status 84 on any exception. Adjust per desired error-handling strategy.

## Contributing / Extending

- Add unit tests for each module (recommended).
- Clean up error handling to raise exceptions instead of calling `exit(84)` where appropriate.
- Improve `ex_14/regexp.py` with a standard email regex or use a library for validation.

## License & attribution

This repo is a simple exercise collection. No license file is included — add one if you intend to publish.

If you want, I can:
- create a proper `README.md` file in the repo (I already formatted this content for [README.md](README.md)),
- open PR-style suggestions to fix the known issues above,
- or generate unit tests for selected exercises.
