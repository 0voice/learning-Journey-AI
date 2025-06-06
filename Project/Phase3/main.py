from yolov5_detection import yolov5_detection
from unet_segmentation import unet_demo
from ocr_tesseract import ocr_with_tesseract
from realtime_face_recognition import realtime_face_recognition
from diffusion_generator import diffusion_art_generation

if __name__ == '__main__':
    print("选择计算机视觉项目：")
    print("1. YOLOv5 目标检测")
    print("2. U-Net 图像分割")
    print("3. OCR 图像识别")
    print("4. 实时人脸识别打卡系统")
    print("5. Stable Diffusion AI 绘画生成器")
    choice = input("请输入编号：")
    if choice == '1':
        yolov5_detection()
    elif choice == '2':
        unet_demo()
    elif choice == '3':
        ocr_with_tesseract()
    elif choice == '4':
        realtime_face_recognition()
    elif choice == '5':
        diffusion_art_generation()
    else:
        print("请输入正确编号（1-5）")
