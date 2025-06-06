from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_chat_model(model_name="uer/gpt2-chinese-cluecorpussmall"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()
    return tokenizer, model
