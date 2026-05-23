"""
Author: Eliana Mugar

Analyze transcript files for speaker-role and gender-pattern markers.

This script was designed for exploratory analysis of map-task transcript files.
It scans transcript files for metadata markers indicating speaker gender and
speaker role, then reports files matching a selected interaction pattern.
"""

from pathlib import Path

import nltk


def tokenize_file(file_path):
    """Read and tokenize a transcript file."""
    text = file_path.read_text(encoding="utf-8")
    return nltk.word_tokenize(text)


def has_pattern(tokens):
    """
    Check whether a transcript contains the target exploratory pattern.

    Current target pattern:
    - A male speaker marker appears
    - A female speaker marker appears later
    - The giver role begins with markers: who=G n=1
    """
    found_male = False
    found_female_after_male = False
    giver_starts = False

    for index, token in enumerate(tokens):
        if token.lower() == "male":
            found_male = True

        if found_male and token.lower() == "female":
            found_female_after_male = True

        if (
            token == "who=G"
            and index + 1 < len(tokens)
            and tokens[index + 1] == "n=1"
        ):
            giver_starts = True

    return found_male and found_female_after_male and giver_starts


def analyze_directory(input_dir):
    """Analyze all .txt transcript files in a directory."""
    matching_files = []

    for file_path in sorted(input_dir.glob("*.txt")):
        tokens = tokenize_file(file_path)

        if has_pattern(tokens):
            matching_files.append(file_path.name)

    return matching_files


def format_results(matching_files):
    """Format analysis results."""
    lines = [
        "Splaining Analysis Results",
        "==========================",
        f"Matching files: {len(matching_files)}",
        "",
    ]

    if matching_files:
        lines.append("Files matching the target pattern:")
        for file_name in matching_files:
            lines.append(f"- {file_name}")
    else:
        lines.append("No files matched the target pattern.")

    return "\n".join(lines)


def main():
    """Run the transcript analysis workflow."""
    input_dir = Path(input("Enter folder path containing transcript .txt files: ").strip())
    output_file = Path(input("Enter output filename, e.g. splaining_results.txt: ").strip())

    if not input_dir.exists() or not input_dir.is_dir():
        print("Error: input folder does not exist.")
        return

    matching_files = analyze_directory(input_dir)
    results = format_results(matching_files)

    output_file.write_text(results, encoding="utf-8")

    print(f"Found {len(matching_files)} matching files.")
    print(f"Saved results to {output_file}")


if __name__ == "__main__":
    main()
