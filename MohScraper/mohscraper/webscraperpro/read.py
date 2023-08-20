def read_final_data():
    import fitz
    from docx import Document
    import PyPDF2

    # Set initial values
    title = ""
    content = ""

    # Open the PDF file
    with open('Scrapped/test.pdf', 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)

        # Get the total number of pages in the PDF
        num_pages = len(reader.pages)


            # Get the current page
        page = reader.pages[0]

            # Extract the text from the page
        text = page.extract_text()

            # Split the text into lines
        # lines = text.split('\n')

            # Process each line
            # for index, line in enumerate(lines):
            #     # Skip empty lines
            #     if line.strip() == '':
            #         continue
                # First line is considered as the title
        # title = title+lines[0]
        # title = title + lines[1]
        # title = lines[0:2]
        content = text
        # print("printing lines :")
        # print(lines)

    # Return the title and content
    return title, content


# link = input("enter website link: \n")
# web_scraper_pro(link)

# title,content = read_final_data()
# print(title)
# print(content)
