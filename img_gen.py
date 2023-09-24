import torch
from diffusers import StableDiffusionPipeline

def text2medimage(prompt):
    model_id = "Nihirc/Prompt2MedImage"
    device = "cuda"

    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to(device)

    test_prompt = "Showing the subtrochanteric fracture in the porotic bone."
    image = pipe(prompt).images[0]  
    
    filename = prompt.split(' ').join('_')
    filepath = f"images/{filename}.png"
    image.save(filepath)

    return image, filepath 