def get_prompt(style, text):
    base = f"\n\nPaper content:\n{text}"

    if style == "brief":
        return "Summarize this research paper in 3 sentences. Be concise." + base
    elif style == "bullet":
        return "Summarize this research paper as clean bullet points covering: objective, methods, results, conclusion." + base
    elif style == "detailed":
        return "Give a detailed structured summary of this research paper. Cover: objective, background, methodology, results, conclusions and limitations." + base
    elif style == "research":
        return """
Analyze this research paper and generate a structured summary in markdown covering:
- The gap or problem the paper identifies
- The role and contribution of this research
- Methodology used
- Key data, results and charts cited as evidence
- Conclusions and limitations
""" + base