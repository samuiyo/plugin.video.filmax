#!/usr/bin/env python
# -*- coding: utf-8 -*-

global selcine

def cineurlselector(selcine):
	if selcine == "A Coruña. Cantones Cines": urlcine = "/a-coruna/cantones-cines"
	if selcine == "A Coruña. Cinesa Marineda City": urlcine = "/a-coruna/cinesa-marineda-city"
	if selcine == "A Coruña. Yelmo Cines Espacio Coruña": urlcine = "/a-coruna/yelmo-cines-espacio-coruna"
	if selcine == "A Coruña. Yelmo Cines Los Rosales": urlcine = "/a-coruna/yelmo-cines-los-rosales"
	if selcine == "Carballo. Multicines Bergantiños": urlcine = "/carballo/multicines-bergantinos"
	if selcine == "Cee. Xunqueira Cines": urlcine = "/cee/xunqueira-cines"
	if selcine == "Narón. Odeón Multicines Narón": urlcine = "/naron/odeon-multicines-naron"
	if selcine == "Ribeira. Multicines Barbanza": urlcine = "/ribeira/multicines-barbanza"
	if selcine == "Santiago de Compostela. Cinesa As Cancelas": urlcine = "/santiago-de-compostela/cinesa-as-cancelas"
	if selcine == "Santiago de Compostela. Multicines Compostela": urlcine = "/santiago-de-compostela/multicines-compostela"
	if selcine == "Alacant-Alicante. Cines Axion San Juan": urlcine = "/alacant-alicante/cines-axion-san-juan"
	if selcine == "Alacant-Alicante. Cines Panoramis": urlcine = "/alacant-alicante/cines-panoramis"
	if selcine == "Alacant-Alicante. Yelmo Cines Puerta de Alicante": urlcine = "/alacant-alicante/yelmo-cines-puerta-de-alicante"
	if selcine == "Alcoi. Cines Axion Alcoi": urlcine = "/alcoi/cines-axion-alcoi"
	if selcine == "Cocentaina. Multicines l'Altet": urlcine = "/cocentaina/multicines-laltet"
	if selcine == "Elx. Cines ABC Elx": urlcine = "/elx/cines-abc-elx"
	if selcine == "Finestrat. Cines IMF Finestrat": urlcine = "/finestrat/cines-imf-finestrat"
	if selcine == "Ondara. Cines IMF Ondara": urlcine = "/ondara/cines-imf-ondara"
	if selcine == "Oriola-Orihuela. Cines Axion Oriola / Orihuela": urlcine = "/oriola-orihuela/cines-axion-oriola-orihuela"
	if selcine == "Petrer. Cines Max 3D": urlcine = "/petrer/cines-max-3d"
	if selcine == "Petrer. Yelmo Cines Vinalopó": urlcine = "/petrer/yelmo-cines-vinalopo"
	if selcine == "Sant Vicent del Raspeig. Cines Megarama Alicante": urlcine = "/sant-vicent-del-raspeig/cines-megarama-alicante"
	if selcine == "Santa Pola. Cines Axion Santa Pola": urlcine = "/santa-pola/cines-axion-santa-pola"
	if selcine == "Torrevieja. Cines IMF Torrevieja": urlcine = "/torrevieja/cines-imf-torrevieja"
	if selcine == "Etxabarri-Ibiña. Cines Gorbeia Zinemak": urlcine = "/etxabarri-ibina/cines-gorbeia-zinemak"
	if selcine == "Vitoria-Gasteiz. Cines Florida Guridi": urlcine = "/vitoria-gasteiz/cines-florida-guridi"
	if selcine == "Vitoria-Gasteiz. Yelmo Cines Boulevard": urlcine = "/vitoria-gasteiz/yelmo-cines-boulevard"
	if selcine == "Albacete. Yelmo Cines Imaginalia": urlcine = "/albacete/yelmo-cines-imaginalia"
	if selcine == "Albacete. Yelmo Cines Vialia Albacete": urlcine = "/albacete/yelmo-cines-vialia-albacete"
	if selcine == "Almería. Cines Monumental": urlcine = "/almeria/cines-monumental"
	if selcine == "El Ejido. Cines Ocine Copo": urlcine = "/el-ejido/cines-ocine-copo"
	if selcine == "Roquetas de Mar. Yelmo Cines Roquetas": urlcine = "/roquetas-de-mar/yelmo-cines-roquetas"
	if selcine == "Escaldes-Engordany. Cines Illa Carlemany": urlcine = "/escaldes-engordany/cines-illa-carlemany"
	if selcine == "Corvera de Asturias. Odeón Multicines Parque Astur": urlcine = "/corvera-de-asturias/odeon-multicines-parque-astur"
	if selcine == "El Entrego. Artesiete Cines Nalón": urlcine = "/el-entrego/artesiete-cines-nalon"
	if selcine == "Gijón. Yelmo Cines Ocimax Gijón": urlcine = "/gijon/yelmo-cines-ocimax-gijon"
	if selcine == "Mieres. Artesiete Cines Caudalia": urlcine = "/mieres/artesiete-cines-caudalia"
	if selcine == "Oviedo. Yelmo Cines Los Prados": urlcine = "/oviedo/yelmo-cines-los-prados"
	if selcine == "Paredes. Cinesa Intu Asturias": urlcine = "/paredes/cinesa-intu-asturias"
	if selcine == "Almendralejo. Cines Victoria Almendralejo": urlcine = "/almendralejo/cines-victoria-almendralejo"
	if selcine == "Badajoz. Cinesur Conquistadores": urlcine = "/badajoz/cinesur-conquistadores"
	if selcine == "Don Benito. Cines Victoria Don Benito": urlcine = "/don-benito/cines-victoria-don-benito"
	if selcine == "Mérida. Cinesa El Foro": urlcine = "/merida/cinesa-el-foro"
	if selcine == "Abrera. Yelmo Cines Abrera": urlcine = "/abrera/yelmo-cines-abrera"
	if selcine == "Arenys de Mar. Cines Ocine Arenys": urlcine = "/arenys-de-mar/cines-ocine-arenys"
	if selcine == "Badalona. Màgic Megacine ACEC": urlcine = "/badalona/magic-megacine-acec"
	if selcine == "Barberà del Vallès. Yelmo Cines Baricentro": urlcine = "/barbera-del-valles/yelmo-cines-baricentro"
	if selcine == "Barcelona. Arenas de Barcelona Multicines": urlcine = "/barcelona/arenas-de-barcelona-multicines"
	if selcine == "Barcelona. Aribau Club 2 Salas": urlcine = "/barcelona/aribau-club-2-salas"
	if selcine == "Barcelona. Aribau Multicines": urlcine = "/barcelona/aribau-multicines"
	if selcine == "Barcelona. Balmes Multicines 12 Salas": urlcine = "/barcelona/balmes-multicines-12-salas"
	if selcine == "Barcelona. Boliche Cines": urlcine = "/barcelona/boliche-cines"
	if selcine == "Barcelona. Bosque Multicines": urlcine = "/barcelona/bosque-multicines"
	if selcine == "Barcelona. Cine Maldà": urlcine = "/barcelona/cine-malda"
	if selcine == "Barcelona. Cinesa Diagonal Cines": urlcine = "/barcelona/cinesa-diagonal-cines"
	if selcine == "Barcelona. Cinesa Diagonal Mar Cines": urlcine = "/barcelona/cinesa-diagonal-mar-cines"
	if selcine == "Barcelona. Cinesa Heron City Cines": urlcine = "/barcelona/cinesa-heron-city-cines"
	if selcine == "Barcelona. Cinesa La Maquinista Cines": urlcine = "/barcelona/cinesa-la-maquinista-cines"
	if selcine == "Barcelona. Glòries Multicines": urlcine = "/barcelona/glories-multicines"
	if selcine == "Barcelona. Gran Sarrià Multicines": urlcine = "/barcelona/gran-sarria-multicines"
	if selcine == "Barcelona. Méliès Cines": urlcine = "/barcelona/melies-cines"
	if selcine == "Barcelona. Palau Balaña Multicines": urlcine = "/barcelona/palau-balana-multicines"
	if selcine == "Barcelona. Phenomena Cines": urlcine = "/barcelona/phenomena-cines"
	if selcine == "Barcelona. Renoir Floridablanca Cines": urlcine = "/barcelona/renoir-floridablanca-cines"
	if selcine == "Barcelona. Texas Cines": urlcine = "/barcelona/texas-cines"
	if selcine == "Barcelona. Verdi Cines": urlcine = "/barcelona/verdi-cines"
	if selcine == "Barcelona. Verdi Park Cines": urlcine = "/barcelona/verdi-park-cines"
	if selcine == "Barcelona. Yelmo Cines Comèdia": urlcine = "/barcelona/yelmo-cines-comedia"
	if selcine == "Barcelona. Yelmo Cines Icaria": urlcine = "/barcelona/yelmo-cines-icaria"
	if selcine == "Castelldefels. Cines Metropol": urlcine = "/castelldefels/cines-metropol"
	if selcine == "Castelldefels. Yelmo Cines Castelldefels": urlcine = "/castelldefels/yelmo-cines-castelldefels"
	if selcine == "Cerdanyola del Vallès. Multicines El Punt": urlcine = "/cerdanyola-del-valles/multicines-el-punt"
	if selcine == "Cornellà de Llobregat. Cines Full": urlcine = "/cornella-de-llobregat/cines-full"
	if selcine == "Cornellà de Llobregat. Cinesa Llobregat Centre Cines": urlcine = "/cornella-de-llobregat/cinesa-llobregat-centre-cines"
	if selcine == "Gavà. Cinesa Barnasud Cines": urlcine = "/gava/cinesa-barnasud-cines"
	if selcine == "Granollers. Cines Ocine Granollers": urlcine = "/granollers/cines-ocine-granollers"
	if selcine == "Hospitalet de Llobregat. Cinesa La Farga Cines": urlcine = "/hospitalet-de-llobregat/cinesa-la-farga-cines"
	if selcine == "Hospitalet de Llobregat. Multicines Filmax Gran Vía": urlcine = "/hospitalet-de-llobregat/multicines-filmax-gran-via"
	if selcine == "Manresa. Multicines Bages Centre": urlcine = "/manresa/multicines-bages-centre"
	if selcine == "Mataró. Cinesa Mataró Parc Cines": urlcine = "/mataro/cinesa-mataro-parc-cines"
	if selcine == "Sabadell. Multicines Eix Macià": urlcine = "/sabadell/multicines-eix-macia"
	if selcine == "Sabadell. Multicines Imperial": urlcine = "/sabadell/multicines-imperial"
	if selcine == "Sant Andreu de la Barca. Cines Atrium": urlcine = "/sant-andreu-de-la-barca/cines-atrium"
	if selcine == "Sant Celoni. Cines Ocine Sant Celoni": urlcine = "/sant-celoni/cines-ocine-sant-celoni"
	if selcine == "Sant Cugat del Vallès. Cinesa Sant Cugat V.O. Cines": urlcine = "/sant-cugat-del-valles/cinesa-sant-cugat-vo-cines"
	if selcine == "Sant Cugat del Vallès. Yelmo Cines Sant Cugat": urlcine = "/sant-cugat-del-valles/yelmo-cines-sant-cugat"
	if selcine == "Sant Feliu de Llobregat. CineBaix": urlcine = "/sant-feliu-de-llobregat/cinebaix"
	if selcine == "Sant Vicenç dels Horts. Multicines La Vailet": urlcine = "/sant-vicenc-dels-horts/multicines-la-vailet"
	if selcine == "Santa Margarida de Montbui. Cines Mont-Àgora": urlcine = "/santa-margarida-de-montbui/cines-mont-agora"
	if selcine == "Terrassa. Cine Catalunya": urlcine = "/terrassa/cine-catalunya"
	if selcine == "Terrassa. Cinesa Parc Vallès Cines": urlcine = "/terrassa/cinesa-parc-valles-cines"
	if selcine == "Aranda de Duero. Cines Victoria Ribera del Duero": urlcine = "/aranda-de-duero/cines-victoria-ribera-del-duero"
	if selcine == "Burgos. Odeón Multicines Burgos": urlcine = "/burgos/odeon-multicines-burgos"
	if selcine == "Arcos de la Frontera. Arcos Cinema": urlcine = "/arcos-de-la-frontera/arcos-cinema"
	if selcine == "Cádiz. Cines Al-Andalus Cádiz": urlcine = "/cadiz/cines-al-andalus-cadiz"
	if selcine == "Cádiz. Cinesur Bahía de Cádiz": urlcine = "/cadiz/cinesur-bahia-de-cadiz"
	if selcine == "Chiclana de la Frontera. Multicines Las Salinas": urlcine = "/chiclana-de-la-frontera/multicines-las-salinas"
	if selcine == "Jerez de la Frontera. Yelmo Cines Area Sur": urlcine = "/jerez-de-la-frontera/yelmo-cines-area-sur"
	if selcine == "Los Barrios. Odeón Multicines Bahía Plaza": urlcine = "/los-barrios/odeon-multicines-bahia-plaza"
	if selcine == "Puerto de Santa María. Multicines Bahía Mar": urlcine = "/puerto-de-santa-maria/multicines-bahia-mar"
	if selcine == "Rota. Cines Victoria Rota": urlcine = "/rota/cines-victoria-rota"
	if selcine == "San Fernando. Cines Plaza": urlcine = "/san-fernando/cines-plaza"
	if selcine == "Sanlúcar de Barrameda. Cines Al-Andalus Sanlúcar": urlcine = "/sanlucar-de-barrameda/cines-al-andalus-sanlucar"
	if selcine == "Astillero. Sala Bretón": urlcine = "/astillero/sala-breton"
	if selcine == "Santander. Cinesa Bahía de Santander": urlcine = "/santander/cinesa-bahia-de-santander"
	if selcine == "Santander. Peñacastillo Cinemas 12": urlcine = "/santander/penacastillo-cinemas-12"
	if selcine == "Benicarló. Cines Axion Benicarló": urlcine = "/benicarlo/cines-axion-benicarlo"
	if selcine == "Castelló-Castellón. Cinesa Salera": urlcine = "/castello-castellon/cinesa-salera"
	if selcine == "Castelló-Castellón. Neocine Puerto Azahar": urlcine = "/castello-castellon/neocine-puerto-azahar"
	if selcine == "Ceuta. Marina Cinemas 7": urlcine = "/ceuta/marina-cinemas-7"
	if selcine == "Ciudad Real. Cines Las Vías": urlcine = "/ciudad-real/cines-las-vias"
	if selcine == "Puertollano. Multicines Ortega": urlcine = "/puertollano/multicines-ortega"
	if selcine == "Valdepeñas. Multicines Valdepeñas": urlcine = "/valdepenas/multicines-valdepenas"
	if selcine == "Córdoba. Cinesur El Tablero": urlcine = "/cordoba/cinesur-el-tablero"
	if selcine == "Córdoba. Multicines Guadalquivir": urlcine = "/cordoba/multicines-guadalquivir"
	if selcine == "Lucena. Artesiete Cines Lucena": urlcine = "/lucena/artesiete-cines-lucena"
	if selcine == "Cuenca. Odeón Multicines Cuenca": urlcine = "/cuenca/odeon-multicines-cuenca"
	if selcine == "Cuenca. Odeón Multicines El Mirador de Cuenca": urlcine = "/cuenca/odeon-multicines-el-mirador-de-cuenca"
	if selcine == "Errenteria. Multicines Niessen": urlcine = "/errenteria/multicines-niessen"
	if selcine == "Irún. Cines Ocine Mendibil": urlcine = "/irun/cines-ocine-mendibil"
	if selcine == "Usurbil. Cinesa Urbil": urlcine = "/usurbil/cinesa-urbil"
	if selcine == "Blanes. Cines Ocine Blanes": urlcine = "/blanes/cines-ocine-blanes"
	if selcine == "Figueres. Multisalas Figueres": urlcine = "/figueres/multisalas-figueres"
	if selcine == "Girona. Albèniz Centre Cines": urlcine = "/girona/albeniz-centre-cines"
	if selcine == "Girona. Albèniz Plaça Cines": urlcine = "/girona/albeniz-placa-cines"
	if selcine == "Girona. Cines Ocine Girona": urlcine = "/girona/cines-ocine-girona"
	if selcine == "Olot. Multicines Olot": urlcine = "/olot/multicines-olot"
	if selcine == "Palamós. Cine Arinco": urlcine = "/palamos/cine-arinco"
	if selcine == "Platja D'Aro. Cines Ocine Platja D'Aro": urlcine = "/platja-daro/cines-ocine-platja-daro"
	if selcine == "Roses. Cines Roses": urlcine = "/roses/cines-roses"
	if selcine == "Salt. Odeón Multicines Girona": urlcine = "/salt/odeon-multicines-girona"
	if selcine == "Granada. Cinema Serrallo": urlcine = "/granada/cinema-serrallo"
	if selcine == "Granada. Cines Megarama Granada": urlcine = "/granada/cines-megarama-granada"
	if selcine == "La Zubia. Artesiete Cines Alhsur": urlcine = "/la-zubia/artesiete-cines-alhsur"
	if selcine == "Guadalajara. Multicines Guadalajara": urlcine = "/guadalajara/multicines-guadalajara"
	if selcine == "Huelva. Artesiete Cines Holea": urlcine = "/huelva/artesiete-cines-holea"
	if selcine == "Huelva. Cines Aqualón 4K": urlcine = "/huelva/cines-aqualon-4k"
	if selcine == "La Palma del Condado. El Condado Cinemas 7": urlcine = "/la-palma-del-condado/el-condado-cinemas-7"
	if selcine == "Lepe. Cinevip Lepe": urlcine = "/lepe/cinevip-lepe"
	if selcine == "Punta Umbría. Cines Al-Andalus Punta Umbría": urlcine = "/punta-umbria/cines-al-andalus-punta-umbria"
	if selcine == "Huesca. CineMundo Huesca": urlcine = "/huesca/cinemundo-huesca"
	if selcine == "Monzón. Multicines Victoria": urlcine = "/monzon/multicines-victoria"
	if selcine == "Ciutadella de Menorca. Cinemes Canal Salat": urlcine = "/ciutadella-de-menorca/cinemes-canal-salat"
	if selcine == "Eivissa. Eivissa Aficine": urlcine = "/eivissa/eivissa-aficine"
	if selcine == "Manacor. Manacor Aficine": urlcine = "/manacor/manacor-aficine"
	if selcine == "Maó. Ocimax Maó Aficine": urlcine = "/mao/ocimax-mao-aficine"
	if selcine == "Marratxinet. Cinesa Festival Park": urlcine = "/marratxinet/cinesa-festival-park"
	if selcine == "Palma de Mallorca. Artesiete Cines Fan": urlcine = "/palma-de-mallorca/artesiete-cines-fan"
	if selcine == "Palma de Mallorca. Augusta Aficine": urlcine = "/palma-de-mallorca/augusta-aficine"
	if selcine == "Palma de Mallorca. Cineciutat": urlcine = "/palma-de-mallorca/cineciutat"
	if selcine == "Palma de Mallorca. Ocimax Palma Aficine": urlcine = "/palma-de-mallorca/ocimax-palma-aficine"
	if selcine == "Palma de Mallorca. Porto Pi Aficine": urlcine = "/palma-de-mallorca/porto-pi-aficine"
	if selcine == "Palma de Mallorca. Rívoli Aficine": urlcine = "/palma-de-mallorca/rivoli-aficine"
	if selcine == "Andújar. Paris Multicines": urlcine = "/andujar/paris-multicines"
	if selcine == "Jaén. Multicines La Loma": urlcine = "/jaen/multicines-la-loma"
	if selcine == "Linares. Cines Bowling Linares": urlcine = "/linares/cines-bowling-linares"
	if selcine == "Úbeda. Multicines Úbeda": urlcine = "/ubeda/multicines-ubeda"
	if selcine == "Logroño. Cines Moderno": urlcine = "/logrono/cines-moderno"
	if selcine == "Logroño. Yelmo Cines Berceo": urlcine = "/logrono/yelmo-cines-berceo"
	if selcine == "Caleta de Fuste. Yelmo Cines Fuerteventura": urlcine = "/caleta-de-fuste/yelmo-cines-fuerteventura"
	if selcine == "Lanzarote. Multicines Atlántida": urlcine = "/lanzarote/multicines-atlantida"
	if selcine == "Lanzarote. Multicines Deiland": urlcine = "/lanzarote/multicines-deiland"
	if selcine == "Las Palmas de Gran Canaria. Cinesa El Muelle": urlcine = "/las-palmas-de-gran-canaria/cinesa-el-muelle"
	if selcine == "Las Palmas de Gran Canaria. Cinesa Siete Palmas": urlcine = "/las-palmas-de-gran-canaria/cinesa-siete-palmas"
	if selcine == "Las Palmas de Gran Canaria. Yelmo Cines Las Arenas": urlcine = "/las-palmas-de-gran-canaria/yelmo-cines-las-arenas"
	if selcine == "Santa Lucía de Tirajana. Yelmo Cines Vecindario": urlcine = "/santa-lucia-de-tirajana/yelmo-cines-vecindario"
	if selcine == "Telde. Artesiete Cines Las Terrazas": urlcine = "/telde/artesiete-cines-las-terrazas"
	if selcine == "León. Odeón Multicines León": urlcine = "/leon/odeon-multicines-leon"
	if selcine == "Alpicat. Cines JCA Lleida-Alpicat": urlcine = "/alpicat/cines-jca-lleida-alpicat"
	if selcine == "Lleida. Cines JCA Rambla": urlcine = "/lleida/cines-jca-rambla"
	if selcine == "Lleida. Teatro Principal": urlcine = "/lleida/teatro-principal"
	if selcine == "Tàrrega. Cines Majéstic": urlcine = "/tarrega/cines-majestic"
	if selcine == "Lugo. Abella Cines": urlcine = "/lugo/abella-cines"
	if selcine == "Lugo. As Termas Cines": urlcine = "/lugo/as-termas-cines"
	if selcine == "Monforte de Lemos. Multicines Hollywood": urlcine = "/monforte-de-lemos/multicines-hollywood"
	if selcine == "Alcobendas. Cinesa La Moraleja": urlcine = "/alcobendas/cinesa-la-moraleja"
	if selcine == "Alcorcón. Yelmo Cines Tres Aguas": urlcine = "/alcorcon/yelmo-cines-tres-aguas"
	if selcine == "Arroyomolinos. Cinesa Xanadú": urlcine = "/arroyomolinos/cinesa-xanadu"
	if selcine == "Collado Villalba. Yelmo Cines Planetocio": urlcine = "/collado-villalba/yelmo-cines-planetocio"
	if selcine == "Getafe. Cinesa Nassica": urlcine = "/getafe/cinesa-nassica"
	if selcine == "Las Rozas. Cinesa Las Rozas": urlcine = "/las-rozas/cinesa-las-rozas"
	if selcine == "Leganés. Cinesa Parquesur": urlcine = "/leganes/cinesa-parquesur"
	if selcine == "Madrid. Artesiete Cines Alcalá": urlcine = "/madrid/artesiete-cines-alcala"
	if selcine == "Madrid. Cine Capitol": urlcine = "/madrid/cine-capitol"
	if selcine == "Madrid. Cine Casa de América": urlcine = "/madrid/cine-casa-de-america"
	if selcine == "Madrid. Cine de la Prensa": urlcine = "/madrid/cine-de-la-prensa"
	if selcine == "Madrid. Cine Paz": urlcine = "/madrid/cine-paz"
	if selcine == "Madrid. Cine Victoria": urlcine = "/madrid/cine-victoria"
	if selcine == "Madrid. Cines Acteón": urlcine = "/madrid/cines-acteon"
	if selcine == "Madrid. Cines Callao": urlcine = "/madrid/cines-callao"
	if selcine == "Madrid. Cines Conde Duque Alberto Aguilera": urlcine = "/madrid/cines-conde-duque-alberto-aguilera"
	if selcine == "Madrid. Cines Conde Duque Auditorio Morasol": urlcine = "/madrid/cines-conde-duque-auditorio-morasol"
	if selcine == "Madrid. Cines Conde Duque Goya": urlcine = "/madrid/cines-conde-duque-goya"
	if selcine == "Madrid. Cines Conde Duque Santa Engracia": urlcine = "/madrid/cines-conde-duque-santa-engracia"
	if selcine == "Madrid. Cines MK2 Palacio de Hielo": urlcine = "/madrid/cines-mk2-palacio-de-hielo"
	if selcine == "Madrid. Cines Princesa": urlcine = "/madrid/cines-princesa"
	if selcine == "Madrid. Cines Renoir Plaza de España": urlcine = "/madrid/cines-renoir-plaza-de-espana"
	if selcine == "Madrid. Cines Renoir Retiro": urlcine = "/madrid/cines-renoir-retiro"
	if selcine == "Madrid. Cinesa La Gavia": urlcine = "/madrid/cinesa-la-gavia"
	if selcine == "Madrid. Cinesa Las Rosas": urlcine = "/madrid/cinesa-las-rosas"
	if selcine == "Madrid. Cinesa Manoteras": urlcine = "/madrid/cinesa-manoteras"
	if selcine == "Madrid. Cinesa Méndez Álvaro": urlcine = "/madrid/cinesa-mendez-alvaro"
	if selcine == "Madrid. Cinesa Plaza Loranca 2": urlcine = "/madrid/cinesa-plaza-loranca-2"
	if selcine == "Madrid. Cinesa Príncipe Pío": urlcine = "/madrid/cinesa-principe-pio"
	if selcine == "Madrid. Cinesa Proyecciones": urlcine = "/madrid/cinesa-proyecciones"
	if selcine == "Madrid. Yelmo Cines Ideal": urlcine = "/madrid/yelmo-cines-ideal"
	if selcine == "Madrid. Yelmo Cines Islazul": urlcine = "/madrid/yelmo-cines-islazul"
	if selcine == "Madrid. Yelmo Cines Plenilunio": urlcine = "/madrid/yelmo-cines-plenilunio"
	if selcine == "Majadahonda. Cines Zoco Majadahonda": urlcine = "/majadahonda/cines-zoco-majadahonda"
	if selcine == "Majadahonda. Cinesa Equinoccio": urlcine = "/majadahonda/cinesa-equinoccio"
	if selcine == "Rivas-Vaciamadrid. Yelmo Cines Rivas H20": urlcine = "/rivas-vaciamadrid/yelmo-cines-rivas-h20"
	if selcine == "San Sebastián de los Reyes. Yelmo Cines Plaza Norte 2": urlcine = "/san-sebastian-de-los-reyes/yelmo-cines-plaza-norte-2"
	if selcine == "Torrejón de Ardoz. Cinesa Parque Corredor": urlcine = "/torrejon-de-ardoz/cinesa-parque-corredor"
	if selcine == "Tres Cantos. Odeón Multicines Tres Cantos": urlcine = "/tres-cantos/odeon-multicines-tres-cantos"
	if selcine == "Valdemoro. Cine Verano Valdemoro": urlcine = "/valdemoro/cine-verano-valdemoro"
	if selcine == "Valdemoro. Restón Cinema": urlcine = "/valdemoro/reston-cinema"
	if selcine == "Antequera. Cines La Verónica": urlcine = "/antequera/cines-la-veronica"
	if selcine == "Fuengirola. Cinesur Miramar": urlcine = "/fuengirola/cinesur-miramar"
	if selcine == "Fuengirola. Multicines Alfil": urlcine = "/fuengirola/multicines-alfil"
	if selcine == "Málaga. Cinesur Málaga Nostrum": urlcine = "/malaga/cinesur-malaga-nostrum"
	if selcine == "Málaga. Multicines Rosaleda": urlcine = "/malaga/multicines-rosaleda"
	if selcine == "Málaga. Yelmo Cines Plaza Mayor": urlcine = "/malaga/yelmo-cines-plaza-mayor"
	if selcine == "Málaga. Yelmo Cines Vialia Málaga": urlcine = "/malaga/yelmo-cines-vialia-malaga"
	if selcine == "Marbella. Cinesa La Cañada": urlcine = "/marbella/cinesa-la-canada"
	if selcine == "Rincón de la Victoria. Yelmo Cines Rincón de la Victoria": urlcine = "/rincon-de-la-victoria/yelmo-cines-rincon-de-la-victoria"
	if selcine == "Ronda. Multicines Ronda": urlcine = "/ronda/multicines-ronda"
	if selcine == "Vélez-Málaga. Cinesur El Ingenio": urlcine = "/velez-malaga/cinesur-el-ingenio"
	if selcine == "Águilas. Multicines El Hornillo": urlcine = "/aguilas/multicines-el-hornillo"
	if selcine == "Cartagena. Neocine Espacio Mediterráneo": urlcine = "/cartagena/neocine-espacio-mediterraneo"
	if selcine == "Cartagena. Neocine Mandarache": urlcine = "/cartagena/neocine-mandarache"
	if selcine == "Churra. Cinesa Nueva Condomina": urlcine = "/churra/cinesa-nueva-condomina"
	if selcine == "Lorca. Acec Almenara": urlcine = "/lorca/acec-almenara"
	if selcine == "Murcia. Neocine Centrofama": urlcine = "/murcia/neocine-centrofama"
	if selcine == "Murcia. Neocine El Tiro": urlcine = "/murcia/neocine-el-tiro"
	if selcine == "Murcia. Neocine Rex": urlcine = "/murcia/neocine-rex"
	if selcine == "Murcia. Neocine Thader": urlcine = "/murcia/neocine-thader"
	if selcine == "San Javier. Neocine Dos Mares": urlcine = "/san-javier/neocine-dos-mares"
	if selcine == "Huarte. Yelmo Cines Itaroa": urlcine = "/huarte/yelmo-cines-itaroa"
	if selcine == "Tudela. Cines Ocine Tudela": urlcine = "/tudela/cines-ocine-tudela"
	if selcine == "Viana. Cines Las Cañas": urlcine = "/viana/cines-las-canas"
	if selcine == "Ourense. Cine Ponte Vella": urlcine = "/ourense/cine-ponte-vella"
	if selcine == "Pontevedra. Cinexpo": urlcine = "/pontevedra/cinexpo"
	if selcine == "Vigo. Cines Plaza Elíptica": urlcine = "/vigo/cines-plaza-eliptica"
	if selcine == "Vigo. Gran Vía Cines": urlcine = "/vigo/gran-via-cines"
	if selcine == "Vigo. Multicines Norte": urlcine = "/vigo/multicines-norte"
	if selcine == "Vigo. Yelmo Cines Vigo": urlcine = "/vigo/yelmo-cines-vigo"
	if selcine == "Vilagarcía de Arousa. Multicines Gran Arousa": urlcine = "/vilagarcia-de-arousa/multicines-gran-arousa"
	if selcine == "Salamanca. Cines Megarama Salamanca": urlcine = "/salamanca/cines-megarama-salamanca"
	if selcine == "Adeje. Multicines Gran Sur": urlcine = "/adeje/multicines-gran-sur"
	if selcine == "Candelaria. Multicines Punta Larga": urlcine = "/candelaria/multicines-punta-larga"
	if selcine == "La Orotava. Yelmo Cines La Villa de Orotava": urlcine = "/la-orotava/yelmo-cines-la-villa-de-orotava"
	if selcine == "San Cristóbal de la Laguna. Multicines Tenerife": urlcine = "/san-cristobal-de-la-laguna/multicines-tenerife"
	if selcine == "Santa Cruz de Tenerife. Yelmo Cines Meridiano": urlcine = "/santa-cruz-de-tenerife/yelmo-cines-meridiano"
	if selcine == "Segovia. Artesiete Cines Segovia": urlcine = "/segovia/artesiete-cines-segovia"
	if selcine == "Segovia. Cines Luz de Castilla": urlcine = "/segovia/cines-luz-de-castilla"
	if selcine == "Alcalá de Guadaira. Cinesur Los Alcores": urlcine = "/alcala-de-guadaira/cinesur-los-alcores"
	if selcine == "Bormujos. Cines Al-Andalus Bormujos": urlcine = "/bormujos/cines-al-andalus-bormujos"
	if selcine == "Camas. Cinesa Camas": urlcine = "/camas/cinesa-camas"
	if selcine == "Dos Hermanas. Cineapolis Dos Hermanas": urlcine = "/dos-hermanas/cineapolis-dos-hermanas"
	if selcine == "Écija. Artesiete Cines Écija": urlcine = "/ecija/artesiete-cines-ecija"
	if selcine == "Mairena del Aljarafe. Metromar Cinemas": urlcine = "/mairena-del-aljarafe/metromar-cinemas"
	if selcine == "Marchena. Cine Planelles": urlcine = "/marchena/cine-planelles"
	if selcine == "Sevilla. Alameda Multicines": urlcine = "/sevilla/alameda-multicines"
	if selcine == "Sevilla. Avenida 5 Cines": urlcine = "/sevilla/avenida-5-cines"
	if selcine == "Sevilla. Cine Cervantes": urlcine = "/sevilla/cine-cervantes"
	if selcine == "Sevilla. Cine Zona Este": urlcine = "/sevilla/cine-zona-este"
	if selcine == "Sevilla. Cinesa Plaza de Armas": urlcine = "/sevilla/cinesa-plaza-de-armas"
	if selcine == "Sevilla. Cinesur Nervión Plaza": urlcine = "/sevilla/cinesur-nervion-plaza"
	if selcine == "Sevilla. Multicines Los Arcos": urlcine = "/sevilla/multicines-los-arcos"
	if selcine == "Golmayo. Cines Lara": urlcine = "/golmayo/cines-lara"
	if selcine == "Amposta. Cines Amposta": urlcine = "/amposta/cines-amposta"
	if selcine == "Calafell. Multicines MCB": urlcine = "/calafell/multicines-mcb"
	if selcine == "Cambrils. Rambla de l'art cine": urlcine = "/cambrils/rambla-de-lart-cine"
	if selcine == "El Vendrell. Cines Ocine El Vendrell": urlcine = "/el-vendrell/cines-ocine-el-vendrell"
	if selcine == "Roquetes. Cines Ocine Roquetes": urlcine = "/roquetes/cines-ocine-roquetes"
	if selcine == "Tarragona. Cines Ocine Tarragona": urlcine = "/tarragona/cines-ocine-tarragona"
	if selcine == "Tarragona. Yelmo Cines Parc Central": urlcine = "/tarragona/yelmo-cines-parc-central"
	if selcine == "Valls. Cines JCA Valls": urlcine = "/valls/cines-jca-valls"
	if selcine == "Vila-Seca. Cines Ocine Vila-Seca": urlcine = "/vila-seca/cines-ocine-vila-seca"
	if selcine == "Teruel. Cine Maravillas": urlcine = "/teruel/cine-maravillas"
	if selcine == "Talavera de la Reina. Artesiete Cines Los Alfares": urlcine = "/talavera-de-la-reina/artesiete-cines-los-alfares"
	if selcine == "Talavera de la Reina. Cinebora": urlcine = "/talavera-de-la-reina/cinebora"
	if selcine == "Toledo. Cinesur Luz del Tajo": urlcine = "/toledo/cinesur-luz-del-tajo"
	if selcine == "Aldaia. Cinesa Bonaire": urlcine = "/aldaia/cinesa-bonaire"
	if selcine == "Alfafar. Cines MN4": urlcine = "/alfafar/cines-mn4"
	if selcine == "Alzira. Cines El Punt de la Ribera": urlcine = "/alzira/cines-el-punt-de-la-ribera"
	if selcine == "Gandia. Cines ABC Gandia": urlcine = "/gandia/cines-abc-gandia"
	if selcine == "Ontinyent. Cineapolis El Teler": urlcine = "/ontinyent/cineapolis-el-teler"
	if selcine == "Sagunt. Cines Alucine Sagunto": urlcine = "/sagunt/cines-alucine-sagunto"
	if selcine == "València. Aragó Cinema": urlcine = "/valencia/arago-cinema"
	if selcine == "València. Cines ABC El Saler": urlcine = "/valencia/cines-abc-el-saler"
	if selcine == "València. Cines ABC Park": urlcine = "/valencia/cines-abc-park"
	if selcine == "València. Cines Babel": urlcine = "/valencia/cines-babel"
	if selcine == "València. Cines Lys": urlcine = "/valencia/cines-lys"
	if selcine == "València. Cines Ocine València": urlcine = "/valencia/cines-ocine-valencia"
	if selcine == "València. Yelmo Cines Valencia": urlcine = "/valencia/yelmo-cines-valencia"
	if selcine == "Xàtiva. Cines Axion Xàtiva": urlcine = "/xativa/cines-axion-xativa"
	if selcine == "Xirivella. Cines ABC Gran Turia": urlcine = "/xirivella/cines-abc-gran-turia"
	if selcine == "Arroyo de la Encomienda. Cines Ocine Rio Shopping": urlcine = "/arroyo-de-la-encomienda/cines-ocine-rio-shopping"
	if selcine == "Valladolid. Cines Broadway": urlcine = "/valladolid/cines-broadway"
	if selcine == "Valladolid. Cines Megarama Valladolid": urlcine = "/valladolid/cines-megarama-valladolid"
	if selcine == "Zaratán. Cinesa Zaratán": urlcine = "/zaratan/cinesa-zaratan"
	if selcine == "Barakaldo. Yelmo Cines Megapark": urlcine = "/barakaldo/yelmo-cines-megapark"
	if selcine == "Bilbao. Cinesa Zubiarte": urlcine = "/bilbao/cinesa-zubiarte"
	if selcine == "Leioa. Cinesa Artea": urlcine = "/leioa/cinesa-artea"
	if selcine == "Portugalete. Dock Cine": urlcine = "/portugalete/dock-cine"
	if selcine == "Zamora. Cines Valderaduey": urlcine = "/zamora/cines-valderaduey"
	if selcine == "Zaragoza. Cine Sala Cervantes": urlcine = "/zaragoza/cine-sala-cervantes"
	if selcine == "Zaragoza. Cines Aragonia": urlcine = "/zaragoza/cines-aragonia"
	if selcine == "Zaragoza. Cines Palafox": urlcine = "/zaragoza/cines-palafox"
	if selcine == "Zaragoza. Cinesa GranCasa": urlcine = "/zaragoza/cinesa-grancasa"
	if selcine == "Zaragoza. Cinesa Puerto Venecia": urlcine = "/zaragoza/cinesa-puerto-venecia"
	if selcine == "Zaragoza. Yelmo Cines Plaza Imperial": urlcine = "/zaragoza/yelmo-cines-plaza-imperial"

	return urlcine
