import os
import re
from bs4 import BeautifulSoup
import csv


def extract_verses_to_csv(html_file, output_csv):
    # Read the HTML content
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Prepare the list to hold verses
    verses = []

    # Find all tags with id matching Vn (V1, V2, ..., V123 etc.)
    for tag in soup.find_all(id=re.compile(r'^V\d+$')):
        # Get the full line: tag + its following siblings (text)
        verse_number = tag.get_text(strip=True)  # e.g., "3"
        
        # Get the actual text after the <span> (not inside it)
        text_node = tag.next_sibling
        verse_text = ""

        # Traverse next siblings until we collect the full verse line
        while text_node and not (hasattr(text_node, 'name') and text_node.name == 'span'):
            if isinstance(text_node, str):
                verse_text += text_node.strip()
            text_node = text_node.next_sibling

        # Only add non-empty verses
        if verse_text:
            verses.append(verse_text)

    # Write to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Verse Text"])  # Header
        for verse in verses:
            writer.writerow([verse])

    print(f"Extracted {len(verses)} verses to {output_csv}")

def process_folder(folder_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder_path):
        if filename.endswith(".htm") or filename.endswith(".html"):
            # Match filenames ending with a non-zero digit before .htm/.html
            match = re.match(r'^.*[^0-9]?([1-9])\.html?$', filename)
            if match:
                html_path = os.path.join(folder_path, filename)
                base_name = os.path.splitext(filename)[0]
                csv_output = os.path.join(output_folder, f"{base_name}.csv")

                extract_verses_to_csv(html_path, csv_output)

# Example usage
process_folder("Englishbible/New_testerment", "English_Chapter_csvs")
