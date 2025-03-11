import io
from PIL import Image
from typing import IO, Literal

from pydantic import BaseModel

class ImageDocument(BaseModel):
    """
    Class for extracting textual data from an image using pytesseract 
    and generating information on image using LLM.
    """

    kind: Literal['ImageDocument'] 
    
    def get_content(self, image:bytes ) -> str:
        """
        Extract textual data from an image using pytesseract.
        """
        try:
            import pytesseract
            from PIL import Image
        except ImportError:
            raise ImportError(
                """pytesseract or PIL package not found, please 
                install them with `pip install pytesseract pillow`"""
            )

        img = Image.open(io.BytesIO(image))
        content = pytesseract.image_to_string(img)
        return content

    def parse_image(self, image_path: str) -> str:
        """
        Generate information on image using LLM.
        """
        question = f"Describe the image at {image_path}"
        "use LLM of your choice to generate information on image"
       
        result = "This is a description of the image"
        return result
