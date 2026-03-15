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

```bash
summerize paper.pdf --style bullet --output summery.md
```
| Argument | Description |
|---|---|
| `filepath` | Path to your PDF or TXT file |
| `--style` | `research`, `brief`, `detailed`, `bullet` |
| `--model` | Ollama model to use (default: `qwen3.5:4b`) |
| `--output` | Save to file e.g. `summary.md` |
| `--chunk` | Split long papers into chunks |
---

## Project Structure
```
root/
|-cli.py
|-prompts.py
|-summerizer.py
└-README.md
```
---

## License
MIT License — feel free to use, modify and distribute.
