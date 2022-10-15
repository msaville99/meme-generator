import os

from PIL import Image, ImageDraw, ImageFont

class MemeEngine():
    
    def __init__(self, output_dir):
        """Iniitialize MemeEngine with output_dir path"""
        self.output_dir = output_dir


    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a Meme With a Text Quote

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the body of the quote.
            author {str} -- The author of the quote.
        Outputs:
            out_path -- the path to the saved output image.
        """
        self.img_path = img_path
        self.text = text
        self.author = author
        self.width = width

        img = Image.open(self.img_path)
        out_path = f"{self.output_dir}/{os.path.basename(self.img_path)}"

        if self.width is not None:
            ratio = self.width/float(img.size[0])
            height = int(ratio*float(img.size[1]))
            img = img.resize((self.width, height), Image.NEAREST)
        
        if self.text is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
            draw.text((10, 30), f"{self.text}\n{self.author}", font=font, fill='white')
        
        img.save(out_path)
        return out_path
