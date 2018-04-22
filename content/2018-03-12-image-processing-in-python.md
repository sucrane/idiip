Title: Image Processing in Python
Date: 2018-03-12

PIL is the Python Imaging Library by Fredrik Lundh and Contributors. [Pillow](https://pypi.org/project/Pillow/) is the friendly PIL fork by Alex Clark and Contributors. We can use Pillow to processing image, e.g., adding watermark to an image.

```python
from PIL import Image, ImageDraw, ImageFont

# Add watermark to the image.
image = Image.open('/path/to/your-image.png')
draw = ImageDraw.Draw(image)

text = 'Sample Watermark'
position = (0, 0)
font = ImageFont.truetype('/path/to/your-font.ttf', 40)
draw.text(position, text, (255, 255, 255), font=font)

image.save('/path/to/your-new-image.png', quality=90)
```