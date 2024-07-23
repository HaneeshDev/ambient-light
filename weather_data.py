from requests_html import HTMLSession


def scrap_weather() -> list:
    s = HTMLSession()

    query = 'hyderabad'
    url = f'https://www.google.com/search?q=weather+{query}'

    r = s.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})

    temperature  = r.html.find('span#wob_tm',first=True).text
    unit = r.html.find("div.vk_bk.wob-unit span.wob_t",first=True).text
    weather_type = r.html.find("div.VQF4g",first=True).find("span#wob_dc",first=True).text
    precipitation = r.html.find('span#wob_pp',first=True).text
    humidity = r.html.find('span#wob_hm',first=True).text
    wind = r.html.find('span#wob_tws',first=True).text
    
    return [temperature,weather_type,precipitation,humidity,wind]

# print(scrap_weather())