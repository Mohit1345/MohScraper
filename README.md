# Web Scraper Project

This is a Python project that allows you to scrape web content and save it as a PDF and DOCX file. The project supports different scraping methods based on the provided URL.

## Functionality

The project consists of the following functions:

### `web_scraper_pro(url)`

This function acts as the entry point for the web scraper project. It takes a `url` parameter and determines the appropriate scraping method based on the URL domain. If the URL contains "timesofindia", it calls the `app(url)` function; otherwise, it calls the `pypeter(url)` function.

### `app(url)`

This function is used for scraping web content from URLs that contain "timesofindia". It converts the webpage to a PDF file using the `pdfkit` library and saves it to disk. The resulting PDF file is then passed to the `pdf2extract(pdf_file)` function.

### `pdf2extract(pdf_file)`

This function extracts text from a PDF file and saves it as a DOCX file. It uses the `fitz` library to open the PDF file, iterates over each page, extracts the text blocks, and processes them to find the most relevant news content. The extracted news content is saved in a DOCX file using the `docx` library. The function returns the path of the generated DOCX file.

### `pypeter(url)`

This function is used for scraping web content from URLs that don't contain "timesofindia". It utilizes the `pyppeteer` library to launch a headless browser, navigate to the URL, generate a PDF of the webpage, and save it to disk. The resulting PDF file is then passed to the `pdf3extract()` function.

### `pdf3extract()`

This function extracts text from a PDF file and saves it as a DOCX file. It uses the `PyPDF2` library to open the PDF file, iterate over each page, extract the text, and process it to find the relevant news content. The extracted news content is saved in a DOCX file using the `docx` library. The function returns the path of the generated PDF file.

### `read_final_data()`

This function reads the generated PDF file and extracts the title and content. It uses the `PyPDF2` library to open the PDF file, extract the text from the first page, and split it into lines. The first two lines are considered as the title, and the remaining lines are considered as the content. The function returns the extracted title and content.

## Usage

To use this project, follow these steps:

1. Call the `web_scraper_pro(url)` function, passing the desired website URL as the `url` parameter.
2. The function will scrape the web content, generate a PDF file, and save it as "test.pdf".
3. The relevant news content will be extracted from the PDF and saved as "test.docx".
4. You can use the `read_final_data()` function to read the generated PDF file and extract the title and content.

Example usage:

```python
link = input("Enter the website link: \n")
web_scraper_pro(link)

title, content = read_final_data()
print("Title:", title)
print("Content:", content)
```

#Future Releases
We are excited to announce that a new version of this web scraper project will be released soon, featuring a web user interface (UI). This new version will be more powerful with the added capabilities of AI to scrape data. Stay tuned for updates!

Feel free to modify and enhance the project as per your requirements. Contributions are welcome.

For detailed instructions on setting up the project and its dependencies, please refer to the documentation provided.
