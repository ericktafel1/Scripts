#!/bin/bash

# Set the folder containing your markdown files
INPUT_FOLDER="C:\Users\erick\OneDrive\Desktop\Main-Notes"   # <-- Change this path accordingly

# Temporary file to store the list of markdown files (sorted alphabetically)
FILE_LIST=$(mktemp)

# Combined output file
COMBINED_MD="combinedNOTES.md"

# Find all markdown files in the input folder and sort them alphabetically
find "$INPUT_FOLDER" -type f -name "*.md" | sort > "$FILE_LIST"

# Remove previous combined file if exists
rm -f "$COMBINED_MD"

# Concatenate each markdown file into the combined markdown file
while IFS= read -r file; do
    echo "Processing: $file"
    # Add a new page or separator if needed
    echo -e "\n\n" >> "$COMBINED_MD"
    cat "$file" >> "$COMBINED_MD"
done < "$FILE_LIST"

# Clean up temporary file
rm "$FILE_LIST"

# Convert the combined markdown file to PDF using pandoc
pandoc "$COMBINED_MD" -o output.pdf

echo "PDF generated: output.pdf"
