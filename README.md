# Bible_Text_Data_collection

This repository contains scripts to help extract, organise, and process Bible chapter .htm files structured by verses — and convert them into usable formats ie CSV for text processing and analysis.

## What This Project Does
### 1. Organize Files by Names
Collects a list of filenames from a source folder (e.g., .txt files with Bible chapter names).

Looks for .htm files with matching names in another folder.

Copies (or moves) the .htm files to a destination folder for further processing.

### 2. Extract Verses from HTML
Parses .htm files that have verses marked using <span id="Vn">...</span>.

Extracts the text following each verse marker (e.g., id="V3").

Outputs each verse into a .csv file, one verse per line.

## Tools Used
Python (with os, shutil, csv, and BeautifulSoup for HTML parsing)

BeautifulSoup for extracting verse text from HTML
