def faq_qa_system():
    from sentence_transformers import SentenceTransformer, util
    model = SentenceTransformer('shibing624/text2vec-base-chinese')
    faq = ["如何联系客服？", "如何退货？", "如何修改密码？"]
    faq_emb = model.encode(faq, convert_to_tensor=True)
    query = "怎么联系客服啊"
    q_emb = model.encode(query, convert_to_tensor=True)
    scores = util.cos_sim(q_emb, faq_emb)
    best_idx = scores.argmax()
    print(f"匹配到问题: {faq[best_idx]}")
