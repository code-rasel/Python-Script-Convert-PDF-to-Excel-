import pandas as pd

# Load the PDF file
df = pd.read_pdf('input.pdf')

# Convert the PDF to an Excel spreadsheet
df.to_excel('output.xlsx', index=False)
