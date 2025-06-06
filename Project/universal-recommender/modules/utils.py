import base64
from PIL import Image
import io

def decode_base64_image(image_base64: str) -> Image.Image:
    """
    将 base64 编码的字符串解码为 PIL Image 对象。
    """
    if not image_base64:
        return None
    try:
        image_bytes = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
        return image
    except Exception as e:
        print(f"Failed to decode image: {e}")
        return None

def normalize_text(text: str) -> str:
    """
    简单文本预处理，如去除前后空格、转小写等。
    """
    if not text:
        return ""
    return text.strip().lower()

def batchify_list(data_list, batch_size):
    """
    将列表分批，返回批次列表。
    """
    for i in range(0, len(data_list), batch_size):
        yield data_list[i:i + batch_size]

