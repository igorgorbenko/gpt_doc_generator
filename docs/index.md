# Code Documentation

This repository consists of utility functions for automating the process of generating documentation for code snippets from a repository. The key functions in this codebase are as follows:

## `prepare_documentation(code_snippet)`

This function uses OpenAI's GPT-3.5 Turbo model to generate documentation for a given code snippet. It takes the code snippet as input and returns a formatted documentation suitable for GitHub Pages.

## `get_changed_files()`

This function retrieves a list of files that have changed in the repository. It utilizes Git commands to determine the changed files compared to the previous commit.

## `read_code_from_files(file_list)`

This function reads code snippets from a list of files and concatenates them into a single string. It filters out files that do not have a `.py` extension.

## `get_sum(a, b)`

A sample function that calculates the sum of two input numbers and returns the result.

## `print_it(some_message)`

A sample function that prints the input message to the console.

These functions work together to automate the process of extracting code snippets, generating documentation for them, and saving the documentation in a markdown file (`docs/index.md`) for publishing on GitHub Pages.

For more details on how to use these functions and integrate them into your workflow, refer to the code snippets and function descriptions above.