def translate_zh_en():
    from transformers import MarianMTModel, MarianTokenizer
    src_text = ["我爱自然语言处理"]
    model_name = 'Helsinki-NLP/opus-mt-zh-en'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    inputs = tokenizer(src_text, return_tensors="pt", padding=True)
    translated = model.generate(**inputs)
    print("翻译结果:", tokenizer.batch_decode(translated, skip_special_tokens=True))
