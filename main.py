import cloudscraper
import telebot
import time
import os

BOT_TOKEN = "8914970207:AAHQzgcTMLWNYmW0HHqwkzqoCdZMcslF__U"
CHAT_ID = "5038370084"
API_URL = "https://tap.az/api/v1/items?shop_id=1418&per_page=100"

bot = telebot.TeleBot(BOT_TOKEN)
gonderilmis_elanlar = set()

scraper = cloudscraper.create_scraper(
    browser={'browser': 'chrome', 'platform': 'android', 'desktop': False}
)

def elanlari_yoxla():
    try:
        response = scraper.get(API_URL, timeout=20)
        if response.status_code != 200:
            return
        
        data = response.json()
        items = data.get('items', [])
        
        for item in items:
            title = item.get('title', '')
            elan_id = item.get('id')
            
            if elan_id in gonderilmis_elanlar:
                continue

            if "asus" in title.lower():
                price = item.get('price_reformatted', 'Qiymət yoxdur')
                slug = item.get('slug', '')
                link = f"https://tap.az/elanlar/{slug}/{elan_id}"
                
                mesaj = f"💻 **
