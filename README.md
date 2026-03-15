# Research Paper Summerizer

This project is a local running ollama model based document summerizer.
Written solely for offline usages and as a command line tool.
---
## Features
- It uses the locally available llms via ollama.
- Parses your document and generates the summery for papers.
- Has controlls over model choosing and style selection.
- Has optionality to save as .md or read it in the terminal.
---

## Requirements
- click
- requests
- pymupdf
- Ollama installed and default model is used qwen3.5:4b model, change if needed in summerizer.py search Ctrl+f "model"
---

## Installation
- download the dir
- cd directory
- pip install -e .
---

## Usage

```
summerize paper.pdf --style bullet --output summery.md
```
summerize - The command initiating the tool
paper.pdf - Name of the Pdf file.
--style   - Defining the style of summery -> research, brief, detailed, bullet
--output  - Defining the filename it would give output to. eg. summery.md
--chunk   - Flag if passed document is passed into smaller chunks for larger documents
---

## Project Structure
root/
|-cli.py
|-prompts.py
|-summerizer.py
└-README.md
---

## License
MIT License — feel free to use, modify and distribute.
```

And create a `LICENSE` file in your project root with this content:
```
MIT License

Copyright (c) 2025 Ani

Just Do whatever you want.
