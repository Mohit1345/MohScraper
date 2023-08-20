from .extract import *


def pypeter(url):
    from pyppeteer import launch
    import asyncio
    async def generate_pdf(url):
        # Launch a headless browser
        browser = await launch()

        # Open a new tab and navigate to the URL
        page = await browser.newPage()
        await page.goto(url)

        # Generate the PDF
        pdf_bytes = await page.pdf()

        # Close the browser
        await browser.close()

        return pdf_bytes

    # Generate the PDF using Pyppeteer
    pdf_bytes = asyncio.run(generate_pdf(url))

    # Save the PDF to a file
    with open('Scrapped/test.pdf', 'wb') as f:
        f.write(pdf_bytes)
    pdf2extract("Scrapped/test.pdf")
    pdf3extract()



def reverseapp_peter(url):
   from pyppeteer import launch
   import asyncio
   async def generate_pdf(url):
        # Launch a headless browser
        browser = await launch()

        # Open a new tab and navigate to the URL
        page = await browser.newPage()
        await page.goto(url)

        # Generate the PDF
        pdf_bytes = await page.pdf()

        # Close the browser
        await browser.close()

        return pdf_bytes
   pdf_bytes = asyncio.run(generate_pdf(url))
   with open('Scrapped\\test.pdf', 'wb') as f:
        f.write(pdf_bytes)
   pdf3extract()
   pdf2extract("Scrapped\\test.pdf")


def reverseapp(url):
         #scrapping part
    import pdfkit


    pdf_file = 'Scrapped/test.pdf'


    options = {
        'page-size': 'Letter',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'no-print-media-type': None, 
    }



    # Convert the webpage to PDF and save it to disk
    pdfkit.from_url(url, pdf_file, options=options)
    pdf3extract()

def weasy(url):
    from weasyprint import HTML
# Path to save the PDF
    pdf_path = 'Scrapped/test.pdf'

    # Generate the PDF from the webpage using WeasyPrint
    HTML(url).write_pdf(pdf_path)
    pdf3extract()
    pdf2extract(pdf_path)

def weasy2(url):
    from weasyprint import HTML
# Path to save the PDF
    pdf_path = 'Scrapped/test.pdf'

    # Generate the PDF from the webpage using WeasyPrint
    HTML(url).write_pdf(pdf_path)
    pdf2extract(pdf_path)
    pdf3extract()
    # return pdf2extract(pdf_path)
    

def app(url):
    #scrapping part
    import pdfkit


    pdf_file = 'Scrapped/test.pdf'


    options = {
        'page-size': 'Letter',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'no-print-media-type': None, 
    }



    # Convert the webpage to PDF and save it to disk
    pdfkit.from_url(url, pdf_file, options=options)
    pdf2extract(pdf_file)