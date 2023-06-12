from PIL import Image, ImageEnhance

# Load the image
image_path = "dog.jpeg"
image = Image.open(image_path)

# Adjust contrast
contrast_factor = 1.5
enhancer = ImageEnhance.Contrast(image)
enhanced_image = enhancer.enhance(contrast_factor)

# Save the modified image
output_path = "output.jpg"
enhanced_image.save(output_path)

print("Image with contrast adjustment saved successfully.")
