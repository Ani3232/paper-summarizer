import click
import requests
import fitz  # pymupdf
from prompts import get_prompt
import sys
from termcolor import colored
import threading
import time
import json
color = (218, 119, 86)


class spinner:
    def __init__(self, start_message="└─Assistant : ", end_message="└─Assistant : "):
        self.start_message  =   start_message
        self.end_message    =   end_message
        self.thred          =   None
        
    def start(self):
        self.running = True 
        # Print the start message once
        sys.stdout.write(colored(f"{self.start_message} ", color))
        sys.stdout.flush()
        # Run animation in a seperate thread
        self.thred = threading.Thread(target=self._animate)
        self.thred.daemon = True 
        self.thred.start()
        
    def stop(self):
        self.running = False
        if self.thred:
            self.thred.join() # wait for thread to finish
        sys.stdout.write('\r' + colored(f"{self.end_message}",color))
        sys.stdout.flush()
        
    def _animate(self):
        frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        
        i = 0
        while self.running:
            frame  = frames[i % len(frames)]
            sys.stdout.write('\r' + colored(f"{self.start_message}{frame} Thinking...  ", color))
            sys.stdout.flush()
            time.sleep(0.2)
            i += 1




def load_paper(filepath):
    if filepath.endswith(".pdf"):
        doc = fitz.open(filepath)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    elif filepath.endswith(".txt"):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError("Unsupported file type. Use .pdf or .txt")

def chunk_text(text, chunk_size=3000):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0

    for word in words:
        current_chunk.append(word)
        current_length += len(word) + 1
        if current_length >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def call_ollama(prompt, model):
    spinner_11 = spinner(start_message="└─Assistant : ", end_message="└─Assistant : ")
    spinner_11.start()
    
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": True
    }
    response = requests.post(url, json=payload, stream=True)
    response.raise_for_status()
    
    full_response = ""
    first_token = True
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            token = data.get("response", "")
            if first_token:
                spinner_11.stop()
                first_token = False
            
            print(token, end="", flush=True)
            full_response += token
            if data.get("done"):
                break
    
    print()  # newline when done
    return full_response

def summarize_paper(filepath, model, style, output, chunk):
    # 1. load
    click.echo("Analyzing the paper....")
    text = load_paper(filepath)
    click.echo(f"📄 Paper loaded: {len(text.split())} words / {len(text)} characters")
    
    # 2. chunk or not
    if chunk:
        chunks = chunk_text(text)
        click.echo(f"Split into {len(chunks)} chunks.")
        summaries = []
        for i, chunk_text_piece in enumerate(chunks):
            click.echo(f"Summarizing chunk {i+1}/{len(chunks)}...")
            prompt = get_prompt(style, chunk_text_piece)
            summaries.append(call_ollama(prompt, model))
        final = "\n\n---\n\n".join(summaries)
    else:
        prompt = get_prompt(style, text)
        final = call_ollama(prompt, model)

    # 3. output
    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(final)
        click.echo(f"Summary saved to {output}")
    else:
        click.echo("\n--- SUMMARY ---\n")
        click.echo(final)