import torch
from diffusers import StableDiffusionPipeline

def text_2_medimage(prompt):
    model_id = "Nihirc/Prompt2MedImage"
    device = "cuda"

    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe = pipe.to(device)

    prompt = "Showing the subtrochanteric fracture in the porotic bone."
    image = pipe(prompt).images[0]  
    
    filename = prompt.split(' ').join('_')
    image.save(f"images/{filename}.png")

    return image 
