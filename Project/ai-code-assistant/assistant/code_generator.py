import openai

def generate_code(prompt):
    # 可替换为本地模型，如 CodeLlama、Phind 等
    response = openai.ChatCompletion.create(
        model=\"gpt-3.5-turbo\",
        messages=[{\"role\": \"user\", \"content\": f\"{prompt}\\n请用 Python 写出函数。\"}]
    )
    return response.choices[0].message.content.strip()
