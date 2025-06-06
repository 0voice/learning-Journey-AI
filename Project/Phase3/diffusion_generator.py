def diffusion_art_generation():
    print("\U0001f5bc️ 使用 Diffusers 库运行 Stable Diffusion")
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
