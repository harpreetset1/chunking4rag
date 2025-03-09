from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import LLMChain
from PIL import Image

class ImageParser:
    """
    Class for extracting textual data from an image using pytesseract 
    and generating information on image using LLM.
    """

    def __init__(self):
        self.llm = OpenAI(temperature=0.9)
        self.splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
        self.chain = LLMChain(llm=self.llm, input_key="question", output_key="answer", splitter=self.splitter)

    def parse_image(self, image_path: str) -> str:
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

        image = Image.open(image_path)
        content = pytesseract.image_to_string(image)
        return content

    def generate_info(self, image_path: str) -> str:
        """
        Generate information on image using LLM.
        """
        question = f"Describe the image at {image_path}"
        result = self.chain.run(question)
        return result
