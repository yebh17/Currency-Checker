from contextlib import redirect_stdout
from datetime import datetime
import bs4 
import requests  
import pandas as pd

now = datetime.now()

while True:

    current_time = now.strftime("%H:%M:%S")

    url = "https://www.google.com/search?q=sek+to+inr&rlz=1C5CHFA_enSE926SE927&oq=sek+to+i&aqs=chrome.1.69i57j35i39j0l4j0i457j69i60.4923j1j9&sourceid=chrome&ie=UTF-8"  

    request_result = requests.get( url ) 

    soup = bs4.BeautifulSoup( request_result.text  
                            , "html.parser" ) 
        
    temp = soup.find( "div" , class_='BNeawe' ).text 
            
    data = {'Time': [current_time], 
            'Currency': [temp]
                    } 

    df = pd.DataFrame(data, columns = ['Time', 'Currency'])
    df.to_csv (r'data.csv', sep = '|', mode='a', index = False, header=True)
