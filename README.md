# About

This repository demonstrates a novel approach to automating the creation and maintenance of project documentation using the capabilities of the GPT chat API

## The Main idea
* The approach leverages the power of the Chat GPT API to automatically generate and update project documentation whenever changes are merged from the `dev` branch into the `main` branch
* A GitHub workflow is configured to trigger an additional step that checks for changed files and utilizes the Chat GPT API to generate updated documentation.

## Result
The generated documentation is hosted and made accessible through [Github Pages](https://igorgorbenko.github.io/gpt_doc_generator/), providing an always up-to-date reference for the project