from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
import sys

def scrape(keyword):
    # lance le driver
    try:
        # create posts df to append to
        posts_df = pd.DataFrame()
        
        try:
            # définition du web driver
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-infobars")
            options.add_argument("--mute-audio")
            #options.add_argument('headless')
            #options.add_argument('window-size=1920x1080')
            #options.add_argument("disable-gpu")
            time.sleep(5)
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            time.sleep(3)
            driver.get('https://twitter.com/search?q={}&src=typed_query'.format(keyword))
            time.sleep(5)
        except Exception as e:
            print("Une erreur est survenue lors du démarrage du driver")
            print(sys.exc_info()[0])
            exit()
            
        # Combien de fois le navigateur doit-il faire défiler vers le bas ?
        scroll_down_num = 3  #
        
        post_element_xpath = '//div/div/article/div/div'# l'élément que nous obtenons de la page web
        
        time.sleep(5)
        
        for i in range(0, scroll_down_num):
            # scroll down
            driver.find_element_by_xpath('//body').send_keys(Keys.END)
            time.sleep(10)

        post_list = driver.find_elements_by_xpath(post_element_xpath)    # obtenir le texte seulement de chaque élément
        post_text = [x.text for x in post_list]    # créer un jeu de données temporaire pour chaque tweet
        driver.quit()
        temp_df = pd.DataFrame(post_text, columns={'all_text'})    # ajouter le jeu de données temporaire au jeu de données que nous allons sauvegarder
        posts_df = posts_df.append(temp_df)
        return posts_df
    except Exception as e:
        print("Une erreur est survenue lors du scraping")
        print(e)
        exit()

def parse_text(text):    # split by new line
    text_list = str.splitlines(text)     # récupérer le nom d'utilisateur (toujours le premier élément de la liste)
    username = text_list[0]      # dans les premiers éléments, trouvez l'élément
    # avec le symbole @, ce sera l'identifiant de l'utilisateur.
    handle = ''.join(x for x in text_list[1:3] if '@' in x)    # obtenir la date, en utilisant le point unique pour identifier son 
    # emplacement de l'index
    dot_position = text_list[1:4].index('·')  
    date = text_list[dot_position + 2]  # la date vient après le point # vérifier si c'est une réponse à quelqu'un d'autre
    if text_list[4] == "Réponse à ":
        reply_to = True
        reply_to_handle = text_list[5]
        text = text_list[6]
    else:
        reply_to = False
        reply_to_handle = ''
        # trouver la chaîne la plus longue dans la liste index 4:6
        # ceci sera le texte du tweet
        text = max(text_list[4:6], key=len)    # retourner les variables que nous avons analysées à partir du texte
    return pd.Series([username, handle,date, reply_to, reply_to_handle, text])

def get_posts_text(keyword):
    try:
        posts_df = scrape(keyword)
        time.sleep(3)
        posts_df[['username', 'handle', 'date', 'reply_to', 'reply_to_handle', 'atext']] = posts_df['all_text'].apply(parse_text)
        time.sleep(3)
        posts_list = posts_df['atext'].to_list()[:6]
        return posts_list
    except Exception as e:
        print("Une erreur est survenue lors du scraping")
        print(e)
        return []
    
