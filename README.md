# Splaining Analysis

An exploratory Python/NLTK project for analyzing transcript files for speaker-role and gender-pattern markers.

## Overview

This project was created to analyze transcriptions of audio files and identify interaction patterns involving speaker role and gender metadata.

The original script was developed for map-task transcript files, where speakers may be labeled by role, such as giver or follower, and by gender metadata. The current version scans transcript files for a target pattern involving male/female speaker markers and a giver-start marker.

## Features

- Reads `.txt` transcript files from a folder
- Tokenizes transcripts with NLTK
- Searches for speaker metadata markers
- Identifies files matching a target interaction pattern
- Exports matching file names to a text report

## Target Pattern

The current exploratory pattern checks for:

- A `male` speaker marker
- A later `female` speaker marker
- A giver-role start marker: `who=G n=1`

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```
Download required NLTK data:
```python
import nltk

nltk.download("punkt")
```
## How to Run
```bash
python splaining_analysis.py
```
You will be prompted for:
1. A folder path containing `.txt` files
2. An output name
### Example Output
```
Splaining Analysis Results
==========================
Matching files: 3

Files matching the target pattern:
- git01_fit1.txt
- git04_fit1.txt
- git09_fit1.txt
```
## Skills Demonstrated
* Python scripting
* Natural language processing
* Transcript analysis
* Corpus pre-processing
* Pattern matching
* File and directory handling

## Limitations
This project depends on specific transcript metadata conventions. It may need to be adapted for corpora with different speaker labels, role markers, or formatting.

## Future Improvements
* Add command-line arguments
* Count speaker turns and world totals
* Compare giver/follower speech volume
* Remove metadata from word counts
* Export structured CSV results
* Support paired `fit1` and `fit2` transcript analysis
