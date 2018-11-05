import requests
import json
from pyquery import PyQuery as pq
from pprint import pprint

county_list = [
  "http://www.akpartybrussels.com/",
  "http://www.akpartiadana.org.tr/",
  "http://www.akpartiadiyaman.org.tr/",
  "http://www.akpartiafyonkarahisar.org.tr/",
  "http://www.akpartiagri.org.tr/",
  "http://www.akpartiaksaray.org.tr/",
  "http://www.akpartiamasya.org.tr/",
  "http://www.akpartiankara.org.tr/",
  "http://www.akpartiantalya.org.tr/",
  "http://www.akpartiardahan.org.tr/",
  "http://www.akpartiartvin.org.tr/",
  "http://www.akpartiaydin.org.tr/",
  "http://www.akpartibalikesir.org.tr/",
  "http://www.akpartibartin.org.tr/",
  "http://www.akpartibatman.org.tr/",
  "http://www.akpartibayburt.org.tr/",
  "http://www.akpartibilecik.org.tr/",
  "http://www.akpartibingol.org.tr/",
  "http://www.akpartibitlis.org.tr/",
  "http://www.akpartibolu.org.tr/",
  "http://www.akpartiburdur.org.tr/",
  "http://www.akpartibursa.org.tr/",
  "http://www.akparticanakkale.org.tr/",
  "http://www.akparticankiri.org.tr/",
  "http://www.akparticorum.org.tr/",
  "http://www.akpartidenizli.org.tr/",
  "http://www.akpartidiyarbakir.org.tr/",
  "http://www.akpartiduzce.org.tr/",
  "http://www.akpartiedirne.org.tr/",
  "http://www.akpartielazig.org.tr/",
  "http://www.akpartierzincan.org.tr/",
  "http://www.akpartierzurum.org.tr/",
  "http://www.akpartieskisehir.org.tr/",
  "http://www.akpartigaziantep.org.tr/",
  "http://www.akpartigiresun.org.tr/",
  "http://www.akpartigumushane.org.tr/",
  "http://www.akpartihakkari.org.tr/",
  "http://www.akpartihatay.org.tr/",
  "http://www.akpartiigdir.org.tr/",
  "http://www.akpartiisparta.org.tr/",
  "http://www.akpartiistanbul.org.tr/",
  "http://www.akpartiizmir.org.tr/",
  "http://www.akpartikahramanmaras.org.tr/",
  "http://www.akpartikarabuk.org.tr/",
  "http://www.akpartikaraman.org.tr/",
  "http://www.akpartikars.org.tr/",
  "http://www.akpartikastamonu.org.tr/",
  "http://www.akpartikayseri.org.tr/",
  "http://www.akpartikilis.org.tr/",
  "http://www.akpartikirikkale.org.tr/",
  "http://www.akpartikirklareli.org.tr/",
  "http://www.akpartikirsehir.org.tr/",
  "http://www.akpartikocaeli.org.tr/",
  "http://www.akpartikonya.org.tr/",
  "http://www.akpartikutahya.org.tr/",
  "http://www.akpartimalatya.org.tr/",
  "http://www.akpartimanisa.org.tr/",
  "http://www.akpartimardin.org.tr/",
  "http://www.akpartimersin.org.tr/",
  "http://www.akpartimugla.org.tr/",
  "http://www.akpartimus.org.tr/",
  "http://www.akpartinevsehir.org.tr/",
  "http://www.akpartinigde.org.tr/",
  "http://www.akpartiordu.org.tr/",
  "http://www.akpartiosmaniye.org.tr/",
  "http://www.akpartirize.org.tr/",
  "http://www.akpartisakarya.org.tr/",
  "http://www.akpartisamsun.org.tr/",
  "http://www.akpartisanliurfa.org.tr/",
  "http://www.akpartisiirt.org.tr/",
  "http://www.akpartisinop.org.tr/",
  "http://www.akpartisirnak.org.tr/",
  "http://www.akpartisivas.org.tr/",
  "http://www.akpartitekirdag.org.tr/",
  "http://www.akpartitokat.org.tr/",
  "http://www.akpartitrabzon.org.tr/",
  "http://www.akpartitunceli.org.tr/",
  "http://www.akpartiusak.org.tr/",
  "http://www.akpartivan.org.tr/",
  "http://www.akpartiyalova.org.tr/",
  "http://www.akpartiyozgat.org.tr/",
  "http://www.akpartizonguldak.org.tr/"
]

county_reis_path = "tr/akkadro/ilce-baskanlari"

def flatten(outer_list):
    flattened = []
    for sub_list in outer_list:
        if sub_list:
            for elem in sub_list:
                flattened.append(elem)

    return flattened


def query_personnel(personnel):
    return {
        'bio': personnel.find('.personnel-bio p').eq(0).text(),
        'title': personnel.find('.personnel-info .personnel-job').eq(0).text(),
        'county': personnel.find('.personnel-info .personnel-job').eq(1).text(),
        'name': personnel.find('.personnel-info .personnel-name').eq(0).text(),
        'photo': personnel.find('.personnel-photo img').eq(0).attr('src')
    }

    
def query_personnels(url):
    try:
        d = pq(url=url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'})
    
        return [query_personnel(personnel) for personnel in d.items('.personnel')]
    except:
        print('Cought exception for url {url}'.format(url=url))


def traverse_counties(counties, middle_path):
    return flatten([query_personnels(county + middle_path) for county in counties])


def dump_personnels(personnels, filename):
    personnels_json = json.dumps(personnels, ensure_ascii=False)

    with open(filename, 'w', encoding='utf8') as personnels_file:
        personnels_file.write(personnels_json)


personnels = traverse_counties(county_list, county_reis_path)
pprint(personnels)
dump_personnels(personnels, filename='ak_personnels.json')