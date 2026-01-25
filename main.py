from google import genai
from google.genai import types
import pathlib
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file  

api_key = os.getenv("api_key")

csv_path = "2.csv"
def read_columns(csv_path):
    try:
        df = pd.read_csv(csv_path,nrows=0)
        columns_names =df.columns.to_list()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return columns_names

def read_file(file_path):
    try:
        filepath = pathlib.Path(file_path)
        with filepath.open("r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode '{file_path}'. Check file encoding.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def ai_kpi_generator(columns,instructions):
    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            config=types.GenerateContentConfig(
                system_instruction=f"{instructions}"),
            contents=f"{columns}"
        )
        print(response.text)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def to_markdown(response):
    try:
        # Assuming response is a string that needs to be converted to markdown

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    print("Hello from kpi-generator!")
    file = read_file("Prompt.txt")
    column_names = read_columns(csv_path)
    instructions = file
    ai_kpi_generator(column_names,instructions)



if __name__ == "__main__":
    main()
