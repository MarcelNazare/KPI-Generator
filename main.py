import os
import sys
import pathlib
import pandas as pd
from google import genai
from datetime import datetime
from google.genai import types
from parser import file_parser
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file  
api_key = os.getenv("api_key")

def read_columns(csv_path):
    try:
        df = pd.read_csv(csv_path,nrows=0)
        return df.columns.to_list()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

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
        return response.text
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def to_markdown(file_name,response):
    dir_path = pathlib.Path.cwd() / "markdowns"
    dir_path.mkdir(parents=True, exist_ok=True)
    file_name = file_name.strip('.csv')
    filename = f"{file_name.upper()}_response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    file_path = dir_path / filename

    try:
        with file_path.open("w", encoding="utf-8") as md_file:
            md_file.write(response)
        print(f"✅ Response saved to '{file_path}'")
    except OSError as e:
        print(f"❌ Error saving file: {e}", file=sys.stderr)
    
def main():
    print("Hello from kpi-generator!")
    instructions = read_file("Prompt.txt")
    file_name,csv_path = file_parser()
    column_names = read_columns(csv_path)
    response = ai_kpi_generator(column_names,instructions)
    if response:
        to_markdown(file_name,response)

if __name__ == "__main__":
    main()
 