
prompt_template = """
You are an expert at creating exam questions.

Generate ONLY 5 important questions from the text.

IMPORTANT RULES:
- Maximum 5 questions only
- Each question MUST be on a new line
- Each question MUST end with a question mark (?)
- Do NOT number the questions
- Do NOT add explanations or extra text

TEXT:
------------
{text}
------------

Questions:
"""


refine_template = """
You are refining questions.

We already have:
{existing_answer}

IMPORTANT RULES:
- Keep total questions to MAXIMUM 5
- Do NOT add more than 5 questions total
- Each question MUST be on a new line
- Each question MUST end with a question mark (?)
- Do NOT number the questions
- Do NOT add explanations

TEXT:
------------
{text}
------------

Refined questions:
"""
