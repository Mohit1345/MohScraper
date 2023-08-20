from .pdf import * 
def web_scraper_pro(url):
    if 'timesofindia' in url :
        app(url)
    elif 'indiatoday' in url or 'nbc' in url:
        weasy(url)
    elif 'moneycontrol' in url or 'economictimes' in url:
        reverseapp(url)
    elif  'medium'  in url or 'crunch' in url  :
        weasy2(url)
    else:
        pypeter(url)

