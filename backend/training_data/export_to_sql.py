import os, sys

import glob
import pandas as pd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from database import engine

class ExportToSQL:
    """
    Class that store list of genres and paths of song stored locally in an SQL table
    
    Args:
        - genre_path (str) : path of folder that contains all musical genres
    """
    def __init__(self, genre_path):
        self._sql_table = "audiofile"
        self.genre_paths = glob.glob(genre_path + "/*")

    def build_list(self):
        self.genre = []
        self.path = []

        for genre_path in self.genre_paths:
            element_paths = glob.glob(genre_path + "/*")
            for element_path in element_paths:
                cleaned_element_path = element_path.replace("/", "\\")
                genre_name = cleaned_element_path.split("\\")[-2]
                self.genre.append(genre_name)
                self.path.append(cleaned_element_path)

        return self.genre, self.path
    
    def send_to_sql_table(self):
        data = {"genre": self.genre, "path": self.path}

        # Format as DataFrame and send it to sql table
        df = pd.DataFrame(data)
        df.to_sql(self._sql_table, con=engine, if_exists="replace")

if __name__ == "__main__":
    new_export = ExportToSQL("../data/genres_original")
    new_export.build_list()
    new_export.send_to_sql_table()