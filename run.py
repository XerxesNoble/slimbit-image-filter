from PIL import Image
from Slimbits import Slimbit

new_width = 600

ASCII_CHARS = [ '#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def scale_image(image):
    """Resizes an image preserving the aspect ratio.
    """
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    new_height = int(aspect_ratio * new_width)

    new_image = image.resize((new_width, new_height))
    return new_image

def convert_to_grayscale(image):
    return image.convert('L')

def get_slimbit_density_denominator(image):
    extrema = image.getextrema()
    return int((extrema[1] - extrema[0]) / 28)

def map_pixels_to_slimbits(image, range_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 ranges of 25 pixels each.
    """
    # Slimbit total size (pixel size)
    bit_size = 20
    slimbit = Slimbit(bit_size)
    
    (width, height) = image.size
    new_size = (width * bit_size, height * bit_size)

    print(image)
    d = get_slimbit_density_denominator(image)
    new_image = Image.new('RGB', new_size)
    
    pixels_in_image = list(image.getdata())
    count = len(pixels_in_image)
    
    height_index = 0
    width_index = 0
    for i in range(0, count):
        if (width_index == width):
            width_index = 0
            height_index = height_index + 1
            print((height_index / height) * 100)
        
        width_index += 1
        # Get density
        density = int(pixels_in_image[i] / d)
        # Get fill
        print(pixels_in_image[i])
        # bit = slimbit.create(density)
        # offset = (width_index * bit_size, height_index * bit_size)
        # new_image.paste(bit, offset)
        
    return new_image
    
def convert_image_to_slimbits(image):
    # image = scale_image(image)
    image = convert_to_grayscale(image)
    pixels_to_slimbits = map_pixels_to_slimbits(image)
    return pixels_to_slimbits

def playground(image):
    slimbit = Slimbit(200)
    slimbit.create()

def handle_image_conversion(image_filepath):
    image = None
    try:
        image = Image.open(image_filepath)
    except Exception as e:
        print("Unable to open image file {image_filepath}.".format(image_filepath=image_filepath))
        print(e)
        return
    
    image_slimbits = convert_image_to_slimbits(image)
    image_slimbits.save('./first.jpeg', "JPEG")

if __name__=='__main__':
    import sys

    image_file_path = sys.argv[1]
    handle_image_conversion(image_file_path)
