import requests
from bs4 import BeautifulSoup
import pandas as pd

user_login = 'rfeldman9'

def collect_user_rates(user_login):
    page_num = 1
    data = []
    while True:
        url = f'https://letterboxd.com/{user_login}/films/diary/page/{page_num}/'
        html_content = requests.get(url).text
        soup = BeautifulSoup(html_content, 'lxml')
        entries = soup.find_all('tr', class_='diary-entry-row viewing-poster-container')
        if len(entries) == 0:  # Признак остановки
            break
        for entry in entries:
        # В каждом элементе <tr> ищем элемент <td> с классом 'td-film-details'
            td_film_details = entry.find('td', class_='col-production js-td-production')
        # Теперь, внутри td_film_details ищем элемент <a> и получаем его текстовое содержимое методом .text:
            film_name = td_film_details.find('a').text
            td_film_year = entry.find('td', class_='col-releaseyear').text
            td_rating_rating_green = entry.find('td', class_='col-rating')
            rating_span = td_rating_rating_green.find('span', class_='rating')
            classes = rating_span.get('class', [])
            rating = classes[1].split('-')[1]
            data.append({'film_name': film_name, 'date': td_film_year, 'rating': rating})
        page_num += 1
    return data

test_data = collect_user_rates(user_login)
print(test_data[:5])
print(len(test_data)) 

user_rates = collect_user_rates(user_login='rfeldman9')
df = pd.DataFrame(user_rates)

df.to_excel('user_rates.xlsx')

#<tr class="diary-entry-row viewing-poster-container" data-viewing-id="1034865881" data-owner="rfeldman9" data-object-id="viewing:1034865881" data-object-name="review">
# 	<td class="col-monthdate _aligncenter"> <div class="monthdate"> <svg xmlns="http://www.w3.org/2000/svg" role="presentation" class="glyph -default" width="63" height="54" viewBox="0 0 63 54"><g fill-rule="evenodd"><path d="M59.22 4H52v4.5a2.5 2.5 0 0 1-5 0V4H34v4.5a2.5 2.5 0 0 1-5 0V4H16v4.5a2.5 2.5 0 0 1-5 0V4H3.78C1.69 4 0 5.87 0 8.18v37.64C0 48.13 1.69 50 3.78 50h55.44c2.09 0 3.78-1.87 3.78-4.18V8.18C63 5.87 61.31 4 59.22 4Z"></path><rect width="3" height="9" x="12" rx="1.5"></rect><rect width="3" height="9" x="30" rx="1.5"></rect><rect width="3" height="9" x="48" rx="1.5"></rect><path d="M58.8 51.75H3.8A4 4 0 0 1 0 49a4.98 4.98 0 0 0 3.79 1.75H58.8c1.52 0 2.87-.68 3.79-1.75a4 4 0 0 1-3.8 2.75Z"></path><path d="M58.8 53.75H3.8A4 4 0 0 1 0 51a4.98 4.98 0 0 0 3.79 1.75H58.8c1.52 0 2.87-.68 3.79-1.75a4 4 0 0 1-3.8 2.75Z"></path></g></svg> <svg xmlns="http://www.w3.org/2000/svg" role="presentation" class="glyph -small" width="34" height="31" viewBox="0 0 34 31"><g fill-rule="evenodd"><path d="M25 3h-6v2a2 2 0 1 1-4 0V3H9v2a2 2 0 1 1-4 0V3H2.04C.91 3 0 4.06 0 5.36v21.28C0 27.94.91 29 2.04 29h29.92c1.13 0 2.04-1.06 2.04-2.36V5.36C34 4.06 33.09 3 31.96 3H29v2a2 2 0 1 1-4 0V3ZM31.96 31H2.04C1 31 .14 30.23.02 29.25A3 3 0 0 0 2 30h29.98a3 3 0 0 0 2-.75A2.03 2.03 0 0 1 31.95 31Z"></path><rect width="2" height="5" x="6" rx="1"></rect><rect width="2" height="5" x="16" rx="1"></rect><rect width="2" height="5" x="26" rx="1"></rect></g></svg> <a class="month" href="/rfeldman9/films/diary/for/2025/10/">Oct</a> <a class="year" href="/rfeldman9/films/diary/for/2025/">2025</a> </div> </td> 
# <td class="col-daydate _aligncenter _paddinginlinelg"> <a class="daydate" href="/rfeldman9/films/diary/for/2025/10/07/">07</a> </td> 
# <td class="col-production js-td-production"> <div class="productiondetails js-productiondetails"> <div class="react-component figure" data-component-class="LazyPoster" data-request-poster-metadata="true" data-likeable="true" data-watchable="true" data-rateable="true" data-image-width="35" data-image-height="52" data-item-name="V/H/S/HALLOWEEN (2025)" data-item-slug="v-h-s-halloween" data-item-link="/film/v-h-s-halloween/" data-item-full-display-name="V/H/S/HALLOWEEN (2025)" data-film-id="1260087" data-postered-identifier="{&quot;lid&quot;:&quot;QS3Q&quot;,&quot;uid&quot;:&quot;film:1260087&quot;,&quot;type&quot;:&quot;film&quot;,&quot;typeName&quot;:&quot;film&quot;}" data-poster-url="/film/v-h-s-halloween/image-150/" data-resolvable-poster-path="{&quot;postered&quot;:{&quot;lid&quot;:&quot;QS3Q&quot;,&quot;uid&quot;:&quot;film:1260087&quot;,&quot;type&quot;:&quot;film&quot;,&quot;typeName&quot;:&quot;film&quot;},&quot;posteredBaseLink&quot;:&quot;/film/v-h-s-halloween/&quot;,&quot;isAdultThemed&quot;:false,&quot;hasDefaultPoster&quot;:true,&quot;cacheBustingKey&quot;:&quot;214d9e30&quot;}" data-empty-poster-src="https://s.ltrbxd.com/static/img/empty-poster-35-vLSHh7kq.png" data-is-linked="true" data-target-link="/rfeldman9/film/v-h-s-halloween/" data-details-endpoint="/film/v-h-s-halloween/json/" data-hide-tooltip="true"><div class="poster film-poster"><img src="https://a.ltrbxd.com/resized/film-poster/1/2/6/0/0/8/7/1260087-v-h-s-halloween-0-35-0-52-crop.jpg?v=8bd6255f16" width="35" height="52" alt="Poster for V/H/S/HALLOWEEN (2025)" class="image" loading="lazy" srcset="https://a.ltrbxd.com/resized/film-poster/1/2/6/0/0/8/7/1260087-v-h-s-halloween-0-70-0-105-crop.jpg?v=8bd6255f16 2x"><a href="/rfeldman9/film/v-h-s-halloween/" class="frame"><span class="frame-title">V/H/S/HALLOWEEN (2025)</span><span class="overlay"></span></a></div></div> <div class="body"> <header class="inline-production-masthead -film -diary-entry-row"> <span> <h2 class="name -primary prettify"><a href="/rfeldman9/film/v-h-s-halloween/">V/H/S/HALLOWEEN</a></h2><span class="releasedate"> <a href="/films/year/2025/">2025</a> </span> </span> </header> </div> </div> </td> 
# <td class="col-releaseyear _aligncenter"><span>2025</span></td>
#  <td class="col-rating _paddinginlinelg"> <div class="rating-green">  <div class="hide-for-owner" data-owner="rfeldman9"> <span class="rating rated-7"> ★★★½ </span> </div> </div> </td> 
# <td class="col-like _aligncenter _paddinginlinelg">  </td> <td class="col-rewatch _aligncenter _paddinginlinelg js-td-rewatch icon-status-off"><span class="has-icon icon-rewatch icon-16"><span class="icon"></span></span></td> <td class="col-review _aligncenter _paddinginlinelg js-td-review"> <a href="/rfeldman9/film/v-h-s-halloween/" class="has-icon icon-review icon-16 tooltip" data-original-title="Read the review"><span class="icon"></span>Read the review</a> </td> <td class="col-mode _aligncenter _paddinginlinelg js-td-mode"> </td>
	
		
	
# </tr>