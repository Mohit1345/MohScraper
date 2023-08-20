from django.shortcuts import render
from . import final,read
from multiprocessing import Process
from .pdf import app, pypeter, weasy, reverseapp, weasy2

# Create your views here.
def home(request):
    return render(request,"home.html")


def scrapped_data(request):
    if request.method == "POST":
        url = request.POST.get("url")
        #Multithreading
        if 'timesofindia' in url:
            app(url)
        elif 'indiatoday' in url or 'nbc' in url:
            weasy(url)
        elif 'moneycontrol' in url or 'economictimes' in url:
            reverseapp(url)
        elif 'medium' in url or 'crunch' in url:
            weasy2(url)
        else:
            process = Process(target=pypeter, args=(url,))
            process.start()
            process.join()
        content = read.read_final_data()
    return render(request,"scrapped_data.html",context = {"content":content})

from django.http import FileResponse
from django.shortcuts import render

def download_pdf(request):
    # Replace 'path_to_your_pdf.pdf' with the actual path to your PDF file
    pdf_path = 'Scrapped\\test.pdf'
    # with open(pdf_path, 'rb') as pdf_file:
    #     response = FileResponse(pdf_path, content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename="downloaded_file.pdf"'
    # return response
    return FileResponse(open(pdf_path, 'rb'), as_attachment=True, content_type='application/pdf')