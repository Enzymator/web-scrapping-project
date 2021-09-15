import scrapy
from scrapy.loader import ItemLoader
from datetime import datetime
import re

# ----------- CMD pour lancer -----------------
# scrapy crawl kayak -o vol_Par_Mar_21_09.csv
# scrapy crawl kayak -o vol_Par_Mar_21_09.json
# ---------------------------------------------


class Vols(scrapy.Item):
    # Creation des items pour les stockés dans le json
    ranking = scrapy.Field()
    compagnies = scrapy.Field()
    heure_depart = scrapy.Field()
    heure_arrivee = scrapy.Field()
    airoport_depart = scrapy.Field()
    airoport_arrivee = scrapy.Field()
    vol = scrapy.Field()
    heure_vol = scrapy.Field()
    price = scrapy.Field()
    time = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)


class Kayak(scrapy.Spider):
    # nom de mon scrapeur
    name = "kayak"

    def start_requests(self):
        # url = "https://w ww.kayak.fr/"
        # aller simple
        # https://www.kayak.fr/flights/PAR-MRS/2021-10-09?sort=bestflight_a
        # Definie les variables
        origin = "PAR"
        destination = "MRS"
        startdate = "2021-09-21"
        # enddate = "2021-09-09"
        # Construction de l'url
        url = "https://www.kayak.fr/flights/" + origin + "-" + \
            destination + "/" + startdate + "?sort=price_a"
        # &fs=stops=0"
        # ajouter une liste pour les dates
        # ajouter une liste pour les destinations

        print(' ------------------')
        print(url)
        print(' ------------------')

        # reaquete url
        request = scrapy.Request(
            url=url,
            callback=self.parse,
        )
        yield request

    def parse(self, response):

        # Selectionne les balises
        produits = response.css(
            'div.Base-Results-ResultsList.Flights-Results-FlightResultsList')

        # on initialise ranking
        ranking = 0

        for produit in produits.css('div.Base-Results-HorizonResult.Flights-Results-FlightResultItem'):
            print("")
            # compagnies
            compagnies = produit.css(
                'div.leg-carrier img::attr(alt)').get().strip()
            compagnies = compagnies.replace("Logo de ", "")
            compagnies = str(compagnies).strip()
            # airport depart et arrivee
            all_airport = produit.css('div.bottom span::text').getall()
            airports = []
            for airport in all_airport:
                airports.append(airport)
            # airport depart
            airoport_depart = airports[0]
            airoport_depart = str(airoport_depart).replace("\n", " ").strip()
            # airport arrivee
            airoport_arrivee = airports[2]
            airoport_arrivee = str(airoport_arrivee).replace("\n", " ").strip()
            # heure_depart
            heure_depart = produit.css('span.time-pair span::text').get()
            # heure_arrivee
            heure_arrivee = produit.css(
                'span.arrival-time.base-time::text').get()
            # vol
            vol = produit.css('span.stops-text::text').get()
            vol = str(vol).strip()
            # heure_vol
            heure_vol = produit.css('div.section.duration div::text').get()
            heure_vol = str(heure_vol).strip()
            # price
            price = produit.css('span.unit-price span::text').get()
            price = str(price).strip()
            price = str(price).replace("\xa0", " ")
            price = price.replace("\u20ac", "€").replace("€", "€")
            # heure actuelle
            my_time = datetime.now().isoformat()
            loader = ItemLoader(item=Vols())
            # ranking
            ranking = ranking + 1
            print(ranking)

            loader.add_value("ranking", ranking)
            loader.add_value("compagnies", compagnies)
            loader.add_value("heure_depart", heure_depart)
            loader.add_value("heure_arrivee", heure_arrivee)
            loader.add_value("airoport_depart", airoport_depart)
            loader.add_value("airoport_arrivee", airoport_arrivee)
            loader.add_value("vol", vol)
            loader.add_value("heure_vol", heure_vol)
            loader.add_value("price", price)
            loader.add_value("time", my_time)
            yield loader.load_item()

    # next_page = None
    # next_page = response.css("*********************").extract_first()
    # if next_page is not None:
    #     next_page = response.urljoin(next_page)
    #     request = scrapy.Request(next_page, callback=self.parse)
    #     # request.meta['ranking_start'] = ranking  #### Ranking à activer si la balise n'existe pas dans le code ########
    #     yield request
