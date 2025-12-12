from ascii_magic import AsciiArt
from PIL import ImageEnhance

my_art = AsciiArt.from_image('ImageForAscii.png')
my_art.image = ImageEnhance.Brightness(my_art.image).enhance(1.2)

my_art.to_terminal()
