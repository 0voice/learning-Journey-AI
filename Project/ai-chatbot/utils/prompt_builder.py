def build_prompt(query):
    system_prompt = "你是一个中文智能助手，请用简洁、友善的方式回答问题。"
    return f"{system_prompt}\n用户：{query}\n助手："
