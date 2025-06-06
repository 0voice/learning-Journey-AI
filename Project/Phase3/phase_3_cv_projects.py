# 📷 阶段 3：计算机视觉实战项目代码示例

# 1️⃣ YOLOv5 目标检测实战（需安装 yolov5 环境）
def yolov5_detection():
    print("✅ 使用 yolov5 进行目标检测：")
    print("1. 安装依赖：git clone https://github.com/ultralytics/yolov5 && pip install -r requirements.txt")
    print("2. 数据标注工具：LabelImg / Roboflow / CVAT")
    print("3. 开始训练：python train.py --img 640 --batch 16 --epochs 50 --data data.yaml --weights yolov5s.pt")
    print("4. 推理检测：python detect.py --weights runs/train/exp/weights/best.pt --source your_image.jpg")

# 2️⃣ 图像分割（U-Net：如道路分割或医学图像）
import torch
import torch.nn as nn
class UNet(nn.Module):
    def __init__(self):
        super(UNet, self).__init__()
        def conv_block(in_c, out_c):
            return nn.Sequential(
                nn.Conv2d(in_c, out_c, 3, padding=1),
                nn.ReLU(),
                nn.Conv2d(out_c, out_c, 3, padding=1),
                nn.ReLU()
            )
        self.enc1 = conv_block(1, 64)
        self.pool = nn.MaxPool2d(2)
        self.dec1 = nn.ConvTranspose2d(64, 1, 2, stride=2)
        self.final = nn.Conv2d(1, 1, 1)

    def forward(self, x):
        x1 = self.enc1(x)
        x2 = self.pool(x1)
        x3 = self.dec1(x2)
        return torch.sigmoid(self.final(x3))

def unet_demo():
    model = UNet()
    dummy_input = torch.rand(1, 1, 128, 128)
    output = model(dummy_input)
    print("U-Net 输出尺寸:", output.shape)

# 3️⃣ OCR 项目：图像转文字识别

def ocr_with_tesseract():
    import pytesseract
    from PIL import Image
    img = Image.open("sample_text_image.png")
    text = pytesseract.image_to_string(img, lang='eng')
    print("识别结果：\n", text)

# 4️⃣ 摄像头实时人脸识别与打卡系统

def realtime_face_recognition():
    import cv2
    import face_recognition
    known_image = face_recognition.load_image_file("known.jpg")
    known_encoding = face_recognition.face_encodings(known_image)[0]

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        rgb = frame[:, :, ::-1]
        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)
        for (top, right, bottom, left), encoding in zip(faces, encodings):
            match = face_recognition.compare_faces([known_encoding], encoding)[0]
            name = "Known" if match else "Unknown"
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

# 5️⃣ AI绘画生成器（Stable Diffusion）
def diffusion_art_generation():
    print("🖼️ 使用 Diffusers 库运行 Stable Diffusion")
    print("1. 安装：pip install diffusers transformers accelerate")
    print("2. 示例代码：")
    print("""
from diffusers import StableDiffusionPipeline
import torch
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipe = pipe.to("cuda")
image = pipe("a fantasy landscape, oil painting").images[0]
image.save("fantasy.png")
    """)

# 主函数选择运行模块
if __name__ == '__main__':
    print("选择计算机视觉项目：")
    print("1. YOLOv5 目标检测\n2. U-Net 分割\n3. OCR 识别\n4. 实时人脸识别\n5. Diffusion AI绘画")
    choice = input("输入编号：")
    if choice == '1': yolov5_detection()
    elif choice == '2': unet_demo()
    elif choice == '3': ocr_with_tesseract()
    elif choice == '4': realtime_face_recognition()
    elif choice == '5': diffusion_art_generation()
