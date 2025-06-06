def ocr_with_tesseract():
    import pytesseract
    from PIL import Image
    img = Image.open("sample_text_image.png")
    text = pytesseract.image_to_string(img, lang='eng')
    print("识别结果：\n", text)
