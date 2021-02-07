
# import module 
import requests  
import bs4 
from datetime import datetime
import sched, time
s = sched.scheduler(time.time, time.sleep)

def scheduler(sc): 

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
  
    # Generating the url   
    url = "https://www.google.com/search?q=sek+to+inr&rlz=1C5CHFA_enSE926SE927&oq=sek+to+i&aqs=chrome.1.69i57j35i39j0l4j0i457j69i60.4923j1j9&sourceid=chrome&ie=UTF-8"
  
    # Sending HTTP request  
    request_result = requests.get( url ) 
  
    # Pulling HTTP data from internet  
    soup = bs4.BeautifulSoup( request_result.text  
                            , "html.parser" ) 
  
    temp = soup.find( "div" , class_='BNeawe' ).text  
    
    print ( current_time, ':', temp )

    s.enter(30, 1, scheduler, (sc,))

s.enter(30, 1, scheduler, (s,))
s.run()
