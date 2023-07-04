from PIL import Image

def convert_jpg_to_png(jpg_path, png_path):
    image = Image.open(jpg_path)
    image.save(png_path, 'PNG')
    print(f"Converted {jpg_path} to {png_path}")
jpg_file_path = 'Nmk.jpg'e
png_file_path = 'output.png'
convert_jpg_to_png(jpg_file_path, png_file_path)