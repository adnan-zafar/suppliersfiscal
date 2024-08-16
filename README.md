# Python Bot: Fiscal Supplier Scraper
This Python bot efficiently scrapes data from **[suppliers fiscal](https://suppliers.fiscal.ca.gov/psc/psfpd1/SUPPLIER/ERP/c/ZZ_PO.ZZ_SCPRS1_CMP.GBL?FolderPath=PORTAL_ROOT_OBJECT.ZZ_FISCAL_SCPRS.ZZ_SCPRS1_CMP_GBL&IsFolder=false&IgnoreParamTempl=FolderPath%2cIsFolder)** and downloads it into a CSV file.

## Prerequisites
Follow these steps to use the scraper:
- Download latest python from [here](https://www.python.org/downloads/) depending on the OS, if you don't have it already.
- Install Python packages from requirements file, either using pip, conda or virtualenv:
Example:
  `pip install seleniumbase`

## Run the Script
Open your terminal or command prompt and navigate to the directory containing the script (main.py). Then, run the following command: `python main.py`
This will launch the Chrome browser, automate the scraping process, and save the extracted data to a CSV file.

**Note**: Python >= 3.12 is required.
