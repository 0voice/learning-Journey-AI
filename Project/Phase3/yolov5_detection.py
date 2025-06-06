def yolov5_detection():
    print("\U00002705 使用 yolov5 进行目标检测：")
    print("1. 安装依赖：git clone https://github.com/ultralytics/yolov5 && pip install -r requirements.txt")
    print("2. 数据标注工具：LabelImg / Roboflow / CVAT")
    print("3. 开始训练：python train.py --img 640 --batch 16 --epochs 50 --data data.yaml --weights yolov5s.pt")
    print("4. 推理检测：python detect.py --weights runs/train/exp/weights/best.pt --source your_image.jpg")
