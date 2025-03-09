import polars as pl
from typing import List, Literal

from pydantic import BaseModel

class ExcelParser(BaseModel):
    def __init__(self, file_path: str):
        """
        Initialize the ExcelDataExtractor class.

        Parameters
        ----------
        file_path : str
            The path to the excel file.
        """
        self.file_path = file_path
        self.excel_data = pl.read_excel(file_path)

        kind:Literal["ExcelDataExtractor"]
    def extract_column(self, column_name: str) -> List:
        """
        Extract data from a specific column.

        Parameters
        ----------
        column_name : str
            The name of the column to extract.

        Returns
        -------
        List
            A list containing data from the specified column.
        """
        return self.excel_data.select(column_name).to_series().to_list()

    def extract_rows(self, n_rows: int) -> List:
        """
        Extract a slice of rows from the excel sheet.

        Parameters
        ----------
        start : int
            The starting index of the slice.
        end : Optional[int]
            The ending index of the slice (exclusive). If None, extracts till the end.

        Returns
        -------
        pl.DataFrame
            A DataFrame containing the specified slice of rows.
        """
        excel_data = pl.read_excel(self.file_path)
        #sheets = excel_data.
        dataframes = []
        for frame in excel_data.iter_slices(n_rows=n_rows):
            #df = frame.write_csv("test.csv")
            dataframes.append(str(frame))
        return dataframes
        

    def extract_full_table(self) -> List:
        """
        Extract the entire table from the excel sheet.

        Returns
        -------
        pl.DataFrame
            A DataFrame containing the entire excel sheet data.
        """
        return self.excel_data.to_series().to_list()

       
