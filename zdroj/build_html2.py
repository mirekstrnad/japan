# -*- coding: utf-8 -*-
import os
_D=os.path.dirname(os.path.abspath(__file__))
_p=lambda n: os.path.join(_D,n)
import json
rows=json.load(open(_p('reels_rated.json')))

CATS=['Vse','Jidlo & kavarny','Atrakce & zazitky','Auta / JDM','Nakupovani & anime','Vlaky & doprava','Hotely & ubytovani','Tipy & rady','Ostatni']
CAT_COLORS={'Jidlo & kavarny':'#e8623d','Atrakce & zazitky':'#3b82c4','Auta / JDM':'#8b5cf6','Nakupovani & anime':'#e0699f','Vlaky & doprava':'#2fa37a','Hotely & ubytovani':'#c99a2e','Tipy & rady':'#6b7280','Ostatni':'#94a3b8'}

U="https://www.instagram.com/reel/"
def p(name,kind,badge,real,note,slug,col):
    return {"name":name,"kind":kind,"badge":badge,"real":real,"note":note,"url":U+slug+"/","col":col}
F='#e8623d';A='#3b82c4';C='#8b5cf6';S='#e0699f';T='#2fa37a';Y='#c99a2e'

PLAN=[
 {"city":"Tokio & okoli","days":"3-4 dny","tag":"Zaklad cesty","desc":"Nejvic tvych ulozenych mist je prave tady. Idealni start.",
  "places":[
   p("teamLab Planets","🎨 Atrakce","Tripadvisor 4,3 (5 439)",True,"Imerzni digitalni umeni, chodis bosky vodou. Listky kupuj predem.","C53R4gASfUZ",A),
   p("Ginza Happo","🍽️ Bufet","Google 4,3 (2 038)",True,"All-you-can-eat krab + wagyu + piti za ~12 000 JPY. Rezervuj dopredu.","Dagy4FzPg1s",F),
   p("Note (Azabu-juban)","🥩 Wagyu","top wagyu",False,"Spickova wagyu restaurace v Tokiu.","C57c3wKrSFa",F),
   p("Shinjuku Sushi Hatsume","🍣 Sushi","",False,"Sushi v Sindzuku, nutna rezervace (info v reelu).","DZPoAGrTnUH",F),
   p("Ginza Okeya","🍣 Sushi divadlo","Tabelog 3,04",True,"Vizualne bomba, gastro prumer - spis zazitek pro oci.","Db9_s31yx_Q",F),
   p("Tsutaya Books Ginza","📚 Zastavka","",False,"Krasne knihkupectvi s architekturou, klidny odpocinek.","C6ooJFyLy1O",S),
   p("Mandarake, Akihabara","🛍️ Anime","Google 4,2 (5 825)",True,"8 pater anime, figurek a sberatelstvi.","Da8lEYhxWpp",S),
   p("Tamiya Plamodel Factory, Shimbashi","🚗 Modely","",False,"Raj pro modelare aut, oficialni Tamiya store.","C9ITiDFJ-Kr",C),
   p("Subaru STI Gallery, Mitaka","🏎️ Auta","",False,"Galerie rally Subaru, mene znama perla.","DF83MM1SO3B",C),
   p("Daikoku PA car meet, Jokohama","🏁 Car meet","",False,"Nejikoničtejsi sraz aut v Japonsku, zdarma (srazy nejsou garantovane).","C4VvutnPHfm",C),
   p("Game Boy modding workshop, Akihabara","🎮 Dilna","",False,"Postavis si vlastni Game Boy (rezervace pres Klook).","DZhteMYBPi7",A),
   p("The Railway Museum, Omija","🚆 Vlaky","",False,"Simulatory rizeni vlaku, obri areal - i pro deti.","DHmg_ABTwEe",T),
   p("Gotokuji Temple","⛩️ Chram","",False,"Rodiste maneki-neko (kocky), hodinu od centra.","DFfWkXVtatl",A),
  ]},
 {"city":"Kjoto + Uji","days":"2-3 dny","tag":"Kultura & klasika","desc":"Historicke srdce Japonska. Z Tokia Shinkansenem ~2,5 h.",
  "places":[
   p("Fushimi Inari Taisha","⛩️ Atrakce","Google priblizne 4,7",True,"Tisice cervenych torii, vstup zdarma, otevreno nonstop. Jdi brzy rano.","C4kxfI3IKiv",A),
   p("Tonkatsu Shimizu","🍤 Jidlo","Google 4,5 (440)",True,"Legendarni smazeny rizek v pohodovem baru. Levne (~2-4 tis. JPY).","C5igoKPhJEF",F),
   p("Nintendo Museum, Uji","🎮 Atrakce","Tripadvisor 4,1",True,"Nove (2024), vstup jen na losovacku predem. Must pro fanousky.","C54sBTtNz_d",A),
   p("Nintendo Kyoto (store)","🛍️ Obchod","",False,"Oficialni Nintendo store, foto na strese.","C6Jyhz8RYJ-",S),
   p("Kyoto Railway Museum","🚆 Vlaky","",False,"Pro fanousky vlaku i deti.","C5Lcz-PPpUG",T),
  ]},
 {"city":"Nara","days":"vylet z Kjota, 1/2-1 den","tag":"Klik od Kjota","desc":"~45 min z Kjota nebo Osaky.",
  "places":[
   p("Nara Park (jeleni)","🦌 Atrakce","Google priblizne 4,5",True,"Volne zijici jeleni, kteri se ukloni za susenku. Ikonicke.","DB3_9TxvNtw",A),
  ]},
 {"city":"Osaka","days":"2 dny","tag":"Jidlo & noc","desc":"Gastro mesto. Z Kjota ~15 min Shinkansenem.",
  "places":[
   p("Ichiraku Dotonbori (krab)","🦀 Jidlo","",False,"Krabi raj 5 min od stanice Nipponbashi.","DYzZxEbMK4b",F),
   p("Dotonbori & takoyaki","🐙 Atrakce","",False,"Ikonicke neony, Glico man, streetfood - srdce Osaky.","C-P4t0Dy_4A",A),
   p("The Munch","☕ Kavarna","",False,"Kavove divadlo za ~100 USD - zazitek.","DLp4anWJg-U",F),
   p("Model Garage ROM","🚗 Auta","",False,"Must pro sberatele model. aut, vzacne kousky.","C_6psNute4H",C),
   p("Shinsaibashi vintage","🛍️ Nakup","",False,"Ulice second-hand luxusu (Hermes, LV, Chanel).","DAhOafoITfY",S),
  ]},
 {"city":"Aici / Nagoya","days":"vylet, 1 den","tag":"Ghibli & auta","desc":"Mezi Kjotem a Tokiem, ~1 h Shinkansenem z Kjota.",
  "places":[
   p("Ghibli Park","🎬 Atrakce","Tripadvisor 3,0 (94)",True,"Rozporuplne - drahe, spis prochazka. Jen pokud milujes Ghibli.","C6oFQ2JPgzj",A),
   p("Liberty Walk Nagoya","🏎️ Auta","",False,"Vsechny LBWK auta na jednom miste - pro petrolheady.","DAmX9zPBeJN",C),
   p("Tsuzuki (kavove predstaveni)","☕ Kavarna","",False,"Nejvetsi videnska kava v Japonsku + show.","C61LxMHxCu8",F),
  ]},
 {"city":"Suzuka / Mie","days":"vylet pro fanousky aut, 1 den","tag":"F1 okruh","desc":"~1 h z Nagoye. Jen pokud jsi petrolhead.",
  "places":[
   p("Suzuka Circuit - Circuit Challenger","🏁 Zazitek","Google 4,1 (28)",True,"Projedes kus realneho F1 okruhu (elektricke motokary, pomalejsi).","DaF8xw2t8Wf",C),
  ]},
 {"city":"Fukuoka / Kjusu","days":"delsi vylet, 2 dny","tag":"Ramen & priroda","desc":"Jih Japonska, letecky nebo Shinkansenem. Pro delsi cestu.",
  "places":[
   p("Hakata ramen (Fukuoka)","🍜 Jidlo","",False,"Sef 20 let jen dum <-> prace, absolutni oddanost ramenu.","C7ZX9wDP_-g",F),
   p("Yanagawa river cruise","🛶 Zazitek","",False,"Plavba po kanalech na lodce, ~1,5 h z Hakaty.","C--BJtzS_aA",A),
  ]},
 {"city":"Bonus / mimo hlavni trasu","days":"pokud mas cas navic","tag":"Skryte perly","desc":"Mista, ktera stoji za odbočku, kdyz nekam zajedes.",
  "places":[
   p("Restaurace v Kanazawe","🍽️ Jidlo","",False,"Podle autorky nejmilejsi majitel, jaky v Japonsku potkala.","DamSR71JRt9",F),
   p("Takayama Inari Shrine, Aomori","⛩️ Chram","",False,"Off-the-beaten-path svatyne na severu.","C4k7x6LStJL",A),
  ]},
]

# attach gmap + category name to each curated place (lookup by reel url in rows)
by_url={r['url']:r for r in rows}
for leg in PLAN:
    for pp in leg['places']:
        r=by_url.get(pp['url'])
        pp['gmap']=r['gmap'] if r else ''
        pp['cat']=r['cat'] if r else ''

plan_js=json.dumps(PLAN,ensure_ascii=False,separators=(',',':'))
data_js=json.dumps(rows,ensure_ascii=False,separators=(',',':'))
colors_js=json.dumps(CAT_COLORS,ensure_ascii=False,separators=(',',':'))
cats_js=json.dumps(CATS,ensure_ascii=False,separators=(',',':'))

TMPL=open(_p('template.html'),encoding='utf-8').read()
out=TMPL.replace('__DATA__',data_js).replace('__COLORS__',colors_js).replace('__CATS__',cats_js).replace('__PLAN__',plan_js)
open(_p('japonsko_reels.html'),'w',encoding='utf-8').write(out)
print('written',len(out),'bytes; legs',len(PLAN),'places',sum(len(l["places"]) for l in PLAN))
