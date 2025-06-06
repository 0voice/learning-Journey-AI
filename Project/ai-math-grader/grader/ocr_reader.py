import easyocr

reader = easyocr.Reader(['en'])

def extract_text(image):
    results = reader.readtext(image, detail=0)
    return ' '.join(results)
