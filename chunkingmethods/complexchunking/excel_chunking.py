import polars as pl
from chunkingdatamodel.chunking_model import ChunkingInput 
from chunkingmethods.base_chunking import Chunking
from typing import List

class ExcelChunking(Chunking):
    """
    A class to extract data from excel using pandas.
    """

    def __init__(self, input_data: ChunkingInput):
        """
        Initialize the ExcelChunking class.
        Parameters
        file_path : str
            The path to the excel file.
        """
        self.input_data = input_data
        if input_data.file_path is None:
            raise ValueError("File path is required for excel chunking")
        else:
            self.file_path = input_data.file_path

    def chunk(self) -> List[str]:
        """
        Extract data from excel using pandas.
        Returns
        List[pd.DataFrame]
            A list of dataframes, each containing data from a sheet in the excel file.
        """
        excel_data = pl.read_excel(self.file_path)
        #sheets = excel_data.
        dataframes = []
        for frame in excel_data.iter_slices(n_rows=15_000):
            #df = frame.write_csv("test.csv")
            dataframes.append(str(frame))
        return dataframes

if __name__ == "__main__":
    input_data = ChunkingInput(text="",
        file_path="test.xlsx"
    )
    excel_chunking = ExcelChunking(input_data)
    print(excel_chunking.chunk())