import glob
import pandas as pd
from database import engine

genre = []
path = []

genre_paths = glob.glob("data/genres_original/*")

for genre_path in genre_paths:
    element_paths = glob.glob(genre_path + "/*")
    for element_path in element_paths:
        cleaned_element_path = element_path.replace("/", "\\")
        genre_name = cleaned_element_path.split("\\")[-2]
        genre.append(genre_name)
        path.append(cleaned_element_path)

data = {"genre": genre, "path": path}

# Format as DataFrame and send it to sql table
df = pd.DataFrame(data)
df.to_sql("audiofile", con=engine, if_exists="replace")

