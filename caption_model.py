from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load model & processor once at startup
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):
    """
    Takes a PIL Image and returns a generated caption string.
    """
    image = image.convert('RGB')
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption
