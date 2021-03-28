import json

language_dict = {'en': {'TEXTS': {'WINNER_TEXT': 'YOU WON!', 'LINE_TEXTS': [None, 'Coding:', 'Ömer Furkan İşleyen', 'Design:', 'Ömer Furkan İşleyen', 'Icons made by Freepik from www.flaticon.com', 'Background vector created by freepik - www.freepik.com', 'Music:', '"beeps-18 1.wav" by Greencouch ( https://freesound.org/people/Greencouch/ )', 'licensed under CCBY 3.0']}, 'IMAGES': {'PLAY_BUTTON': 'play_button_en.png', 'CONTRIBUTORS_BUTTON': 'contributors_button_en.png', 'INFO_SCREEN': 'info_screen_en.jpg'}},
                 'tr': {'TEXTS': {'WINNER_TEXT': 'KAZANDIN!', 'LINE_TEXTS': [None, 'Kodlama:', 'Ömer Furkan İşleyen', 'Tasarım:', 'Ömer Furkan İşleyen', 'İkonlar www.flaticon.com adresinden Freepik tarafından yapılmıştır', 'Arka plan vektörü freepik tarafından oluşturulmuştur - www.freepik.com', 'Müzik:', 'Greencouch tarafından "beeps-18 1.wav" ( https://freesound.org/people/Greencouch/ )', 'CCBY 3.0 altında lisanslıdır']}, 'IMAGES': {'PLAY_BUTTON': 'play_button_tr.png', 'CONTRIBUTORS_BUTTON': 'contributors_button_tr.png', 'INFO_SCREEN': 'info_screen_tr.jpg'}}}

config_dict = {'LEVEL': 1, 'FIRST_OPENING': True, 'LANGUAGE': 'en'}

with open("language.json", "w") as f:
    json.dump(language_dict, f, indent=4)

with open("config.json", "w") as f:
    json.dump(config_dict, f, indent=4)
