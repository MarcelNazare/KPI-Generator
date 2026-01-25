import os
import argparse
import sys


def file_parser():
    """Parse command-line input and return a validated file path.

    Accepts either a full file path as the positional argument, or a directory
    path plus an optional --file-name to join. Also strips common accidental
    characters like a trailing '>' or surrounding quotes that users sometimes
    paste from prompts.
    """

    parser = argparse.ArgumentParser(
        description="Process a file path passed via command-line arguments."
    )

    parser.add_argument(
        "--file_path",
        "-p",
        type=str,
        help="Path to a file or to a directory (if using --file-name)."
    )

    parser.add_argument(
        "--file-name",
        "-n",
        dest="file_name",
        type=str,
        help="Optional file name when the first argument is a directory."
    )

    args = parser.parse_args()

    # Defensive cleaning: users sometimes paste paths with a trailing '>'
    # (for example when copying from a shell prompt), or include surrounding
    # quotes. Strip those here so we validate the intended path.
    cleaned_path = args.file_path.rstrip('> ').strip('"\'')

    file_name = args.file_name
    if file_name:
        file_name = file_name.strip('"\'')

    # If the user provided a directory and a file name, join them.
    if file_name:
        candidate = os.path.abspath(os.path.join(cleaned_path, file_name))
    else:
        candidate = os.path.abspath(cleaned_path)

    # If the provided path is a directory and no file name was given, tell
    # the user how to fix it.
    if os.path.isdir(candidate) and not file_name:
        print(f"Error: The path '{candidate}' is a directory. Provide a file path or use --file-name.")
        sys.exit(1)

    if not os.path.isfile(candidate):
        print(f"Error: The file path '{candidate}' does not exist.")
        sys.exit(1)

    print(f"File path received: {candidate}")
    return candidate


