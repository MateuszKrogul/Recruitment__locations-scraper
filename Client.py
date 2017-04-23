from Entity_scraper import Entity_scraper

dane = {'transport': {"przystanki_autobusowe":"http://mapa.gdansk.gda.pl/ipg/layer/index?id=przystanki_autobusowe",
                      'przystanki_tramwajowe': "http://mapa.gdansk.gda.pl/ipg/layer/index?id=przystanki_tramwajowe",
                      'stacje_pkp_pkm': "http://mapa.gdansk.gda.pl/ipg/layer/index?id=stacje_pkp_skm"},

        'zdrowie'  : {"szpitale":"http://mapa.gdansk.gda.pl/ipg/layer/index?id=szpitale"},
        'przedsiębiorczość': {'przedsiębiorczość': "http://mapa.gdansk.gda.pl/ipg/layer/index?id=przedsiebiorczosc"}
        }
# jedyne co edytujesz to zawartość zmiennej dane

entities_list = []
for kategoria in dane:
    for podkategoria in dane[kategoria]:
        entities_list.append(Entity_scraper(kategoria, podkategoria, dane[kategoria][podkategoria]))

for entity in entities_list:
    print("preparing %s"% entity.name)
    entity.prepare_data()
    entity.save_data_to_csv(entity.name)
    entity.save_data_to_csv("Zbiorczy")