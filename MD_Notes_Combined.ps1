# Set the folder containing your markdown files
$InputFolder = "C:\path\to\Notes"  # Change this path if needed

# Define output file names (in the current folder)
$CombinedMD = "combined.md"
$PdfOutput = "output.pdf"

# Get all markdown files recursively and sort them alphabetically by FullName
$mdFiles = Get-ChildItem -Path $InputFolder -Recurse -Filter *.md | Sort-Object FullName

# Remove the combined file if it already exists
if (Test-Path $CombinedMD) {
    Remove-Item $CombinedMD -Force
}

# Combine each markdown file into one file using Out-File (which handles encoding well)
foreach ($file in $mdFiles) {
    Write-Host "Processing: $($file.FullName)"
    # Add a separator (newlines) between files
    "`r`n`r`n" | Out-File -FilePath $CombinedMD -Append -Encoding UTF8
    # Append the content of the file to the combined markdown
    Get-Content $file.FullName | Out-File -FilePath $CombinedMD -Append -Encoding UTF8
}

# Small delay to ensure file writing is complete
Start-Sleep -Seconds 2

# Convert the combined markdown file to PDF using pandoc
pandoc $CombinedMD -o $PdfOutput

Write-Host "PDF generated: $PdfOutput"
