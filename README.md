# KPI Generator

A Python-based tool that automatically generates Key Performance Indicators (KPIs) from CSV data files using Google's Gemini AI model.

## Overview

KPI Generator analyzes CSV files and uses AI to intelligently generate relevant KPIs based on the data structure and content. It processes your data files and outputs markdown reports with generated KPI recommendations.

## Requirements

- **Python**: 3.11 or higher
- **Google API Key**: A valid API key for Google's Gemini AI model

## Installation

### 1. Clone or Download the Project

Download the KPI Generator project to your local machine.

### 2. Create a Virtual Environment (Recommended)

```cmd
python -m venv .venv
```

Activate the virtual environment:

```cmd
.venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```cmd
pip install -r requirements.txt
```

Or install them individually:

```cmd
pip install dotenv>=0.9.9 google-genai>=1.60.0 pandas>=3.0.0 
```

### 4. Configure Your API Key

Create a `.env` file in the project root directory and add your Google API key:

```
api_key=your_google_api_key_here
```

**Note**: Replace `your_google_api_key_here` with your actual Google Gemini API key. Do not commit this file to version control.

## Usage

### Command Line Interface

Run the tool using the `kpi_gen.bat` batch file:

```cmd
kpi_gen.bat "path_to_data_directory" "filename.csv"
```

### Parameters

- **path_to_data_directory**: The path to the directory containing your CSV file(s)
- **filename.csv**: The name of the specific CSV file to analyze

### Example

```cmd
kpi_gen.bat "C:\Users\marcel\Documents\Projects\KPI Generator\sample data" dim_geography.csv
```

This command will:
1. Navigate to the project directory
2. Activate the virtual environment
3. Process the `dim_geography.csv` file from the `sample data` directory
4. Generate KPIs based on the data structure
5. Save the results as a markdown file in the `markdowns` folder

### Output

The tool generates a markdown file with a timestamped name in the `markdowns/` directory:
- Example: `response_20260125_165703.md`
- Contains: AI-generated KPI recommendations based on your data

## Project Structure

```
kpi_gen.bat               # Batch script to run the tool
main.py                   # Main application logic
parser.py                 # CSV parsing utilities
Prompt.txt               # AI prompt template for KPI generation
pyproject.toml           # Project configuration and dependencies
README.md                # This file
sample data/             # Sample CSV files for testing
  dim_geography.csv      # Example geography dimension file
markdowns/               # Output directory for generated markdown files
```

## File Descriptions

- **main.py**: Core application that orchestrates CSV reading, AI processing, and markdown output
- **parser.py**: Handles command-line argument parsing to validate file paths and directory inputs
- **Prompt.txt**: Contains the system instructions sent to the AI model for KPI generation
- **kpi_gen.bat**: Windows batch wrapper that sets up the environment and runs the tool

## Troubleshooting

### "Python not found" error
- Ensure Python 3.11+ is installed and added to your PATH
- Verify by running: `python --version`

### API Key errors
- Check that your `.env` file exists in the project root
- Verify the API key is correct and valid
- Ensure your Google Gemini API is enabled in Google Cloud Console

### Virtual environment not activating
- Check the path in `kpi_gen.bat` matches your actual `.venv` location
- Update the path if needed: `call path\to\.venv\Scripts\activate.bat`

### Permission denied errors
- On Windows, you may need to run the command prompt as Administrator
- Alternatively, run Python scripts directly: `python main.py "path" "filename.csv"`

## Development

### Running Directly with Python

If you prefer not to use the batch file:

```cmd
python main.py "C:\path\to\data" "filename.csv"
```

### Building an Executable

To create a standalone executable:

```cmd
pyinstaller --onefile main.py
```

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| dotenv | >=0.9.9 | Load environment variables from .env file |
| google-genai | >=1.60.0 | Google Gemini AI API client |
| pandas | >=3.0.0 | Data analysis and CSV processing |
| pyinstaller | >=6.18.0 | Create standalone executables |

## License

[Add your license information here]

## Support

For issues or questions, please refer to the project documentation or contact the development team.
