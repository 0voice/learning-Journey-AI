# 通用推荐系统

基于多模态数据（文本 + 图像）融合的推荐引擎，支持：

- 文本与图像特征联合提取
- 向量化索引（基于 Faiss）
- 多种相似度计算与推荐结果排序
- API 服务调用

## 技术栈

- PyTorch / TensorFlow (图像和文本模型)
- Faiss 向量搜索库
- Flask API 服务

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行示例
```bash
python app.py
```

发送用户兴趣描述 + 图片，返回个性化推荐列表。

