import sys
try:
    from PIL import Image, ImageDraw
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image, ImageDraw

def crop_to_circle(input_image_path, output_image_path):
    # Open the input image
    img = Image.open(input_image_path).convert("RGBA")
    
    # Make it a square if it isn't
    min_dim = min(img.size)
    left = (img.size[0] - min_dim) / 2
    top = (img.size[1] - min_dim) / 2
    right = (img.size[0] + min_dim) / 2
    bottom = (img.size[1] + min_dim) / 2
    img = img.crop((left, top, right, bottom))
    
    # Create a mask
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + img.size, fill=255)
    
    # Apply the mask
    result = Image.new("RGBA", img.size)
    result.paste(img, (0, 0), mask=mask)
    
    # Save the output image
    result.save(output_image_path)
    print("Successfully created rounded image!")

crop_to_circle("Raman4rayanan.jpeg", "Raman4rayanan_round.png")
