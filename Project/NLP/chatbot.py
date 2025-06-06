def simple_chatbot():
    from transformers import AutoModelForCausalLM, AutoTokenizer
    model_name = "uer/gpt2-chinese-cluecorpussmall"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    while True:
        query = input("你说: ")
        if query.lower() in ['exit', 'quit']:
            break
        inputs = tokenizer.encode(query, return_tensors='pt')
        outputs = model.generate(inputs, max_length=50, pad_token_id=tokenizer.eos_token_id)
        print("机器人:", tokenizer.decode(outputs[0], skip_special_tokens=True))
