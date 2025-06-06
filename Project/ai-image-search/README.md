# AI 图像搜索引擎

基于图像特征提取 + Faiss 向量检索的本地图像搜索引擎。支持上传图片，返回图像库中最相似的图片。

## 💡 项目功能

- 使用 CNN 提取图像特征（默认 ResNet50）
- 利用 Faiss 构建向量索引
- 支持图像相似度查询
- 本地部署，轻量快速

## 📦 依赖安装

```bash
pip install -r requirements.txt
```
**项目结构:**
project/ai-image-search/
├── README.md
├── requirements.txt
├── app.py
├── utils/
│   ├── feature_extractor.py
│   └── index_builder.py
├── models/
│   └── resnet_model.py
├── static/
│   └── images/                # 存储图像库
├── example/
│   ├── query.jpg
│   └── search_results/
└── index/
    └── faiss_index.bin        # 已构建的向量索引
