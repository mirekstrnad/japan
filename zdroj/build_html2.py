# -*- coding: utf-8 -*-
import os
_D=os.path.dirname(os.path.abspath(__file__))
_p=lambda n: os.path.join(_D,n)
import json
rows=json.load(open(_p('reels_rated.json')))

CATS=['Vše','Jídlo & kavárny','Atrakce & zážitky','Auta / JDM','Nakupování & anime','Vlaky & doprava','Hotely & ubytování','Tipy & rady','Ostatní']
CAT_COLORS={'Jídlo & kavárny':'#e8623d','Atrakce & zážitky':'#3b82c4','Auta / JDM':'#8b5cf6','Nakupování & anime':'#e0699f','Vlaky & doprava':'#2fa37a','Hotely & ubytování':'#c99a2e','Tipy & rady':'#6b7280','Ostatní':'#94a3b8'}

U="https://www.instagram.com/reel/"
def p(name,kind,badge,real,note,slug,col):
    return {"name":name,"kind":kind,"badge":badge,"real":real,"note":note,"url":U+slug+"/","col":col}
F='#e8623d';A='#3b82c4';C='#8b5cf6';S='#e0699f';T='#2fa37a';Y='#c99a2e'

PLAN=[
 {"city":"Tokio & okolí","days":"3-4 dny","tag":"Základ cesty","desc":"Nejvíc tvých uložených míst je právě tady. Ideální start.",
  "places":[
   p("teamLab Planets","🎨 Atrakce","Tripadvisor 4,3 (5 439)",True,"Imerzivní digitální umění, chodíš bosky vodou. Lístky kupuj předem.","C53R4gASfUZ",A),
   p("Ginza Happo","🍽️ Bufet","Google 4,3 (2 038)",True,"All-you-can-eat krab + wagyu + pití za ~12 000 JPY. Rezervuj dopředu.","Dagy4FzPg1s",F),
   p("Note (Azabu-juban)","🥩 Wagyu","top wagyu",False,"Špičková wagyu restaurace v Tokiu.","C57c3wKrSFa",F),
   p("Shinjuku Sushi Hatsume","🍣 Sushi","",False,"Suši v Šindžuku, nutná rezervace (info v reelu).","DZPoAGrTnUH",F),
   p("Ginza Okeya","🍣 Sushi divadlo","Tabelog 3,04",True,"Vizuálně bomba, gastronomicky průměr – spíš zážitek pro oči.","Db9_s31yx_Q",F),
   p("Tsutaya Books Ginza","📚 Zastávka","",False,"Krásné knihkupectví s architekturou, klidný odpočinek.","C6ooJFyLy1O",S),
   p("Mandarake, Akihabara","🛍️ Anime","Google 4,2 (5 825)",True,"8 pater anime, figurek a sběratelství.","Da8lEYhxWpp",S),
   p("Tamiya Plamodel Factory, Shimbashi","🚗 Modely","",False,"Ráj pro modeláře aut, oficiální Tamiya store.","C9ITiDFJ-Kr",C),
   p("Subaru STI Gallery, Mitaka","🏎️ Auta","",False,"Galerie rally Subaru, méně známá perla.","DF83MM1SO3B",C),
   p("Daikoku PA car meet, Jokohama","🏁 Car meet","",False,"Nejikoničtější sraz aut v Japonsku, zdarma (srazy nejsou garantované).","C4VvutnPHfm",C),
   p("Game Boy modding workshop, Akihabara","🎮 Dílna","",False,"Postavíš si vlastní Game Boy (rezervace přes Klook).","DZhteMYBPi7",A),
   p("The Railway Museum, Omija","🚆 Vlaky","",False,"Simulátory řízení vlaku, obří areál – i pro děti.","DHmg_ABTwEe",T),
   p("Gotokuji Temple","⛩️ Chrám","",False,"Rodiště maneki-neko (kočky), hodinu od centra.","DFfWkXVtatl",A),
  ]},
 {"city":"Kjóto + Uji","days":"2-3 dny","tag":"Kultura & klasika","desc":"Historické srdce Japonska. Z Tokia šinkansenem ~2,5 h.",
  "places":[
   p("Fushimi Inari Taisha","⛩️ Atrakce","Google přibližně 4,7",True,"Tisíce červených torií, vstup zdarma, otevřeno nonstop. Jdi brzy ráno.","C4kxfI3IKiv",A),
   p("Tonkatsu Shimizu","🍤 Jídlo","Google 4,5 (440)",True,"Legendární smažený řízek v pohodovém baru. Levné (~2–4 tis. JPY).","C5igoKPhJEF",F),
   p("Nintendo Museum, Uji","🎮 Atrakce","Tripadvisor 4,1",True,"Nové (2024), vstup jen na losovačku předem. Must pro fanoušky.","C54sBTtNz_d",A),
   p("Nintendo Kyoto (store)","🛍️ Obchod","",False,"Oficiální Nintendo store, foto na střeše.","C6Jyhz8RYJ-",S),
   p("Kyoto Railway Museum","🚆 Vlaky","",False,"Pro fanoušky vlaků i děti.","C5Lcz-PPpUG",T),
  ]},
 {"city":"Nara","days":"výlet z Kjóta, ½–1 den","tag":"Kousek od Kjóta","desc":"~45 min z Kjóta nebo Ósaky.",
  "places":[
   p("Nara Park (jeleni)","🦌 Atrakce","Google přibližně 4,5",True,"Volně žijící jeleni, kteří se ukloní za sušenku. Ikonické.","DB3_9TxvNtw",A),
  ]},
 {"city":"Ósaka","days":"2 dny","tag":"Jídlo & noc","desc":"Gastro město. Z Kjóta ~15 min šinkansenem.",
  "places":[
   p("Ichiraku Dotonbori (krab)","🦀 Jídlo","",False,"Krabí ráj 5 min od stanice Nipponbashi.","DYzZxEbMK4b",F),
   p("Dotonbori & takoyaki","🐙 Atrakce","",False,"Ikonické neony, Glico man, streetfood – srdce Ósaky.","C-P4t0Dy_4A",A),
   p("The Munch","☕ Kavárna","",False,"Kávové divadlo za ~100 USD – zážitek.","DLp4anWJg-U",F),
   p("Model Garage ROM","🚗 Auta","",False,"Must pro sběratele modelů aut, vzácné kousky.","C_6psNute4H",C),
   p("Shinsaibashi vintage","🛍️ Nákup","",False,"Ulice second-hand luxusu (Hermès, LV, Chanel).","DAhOafoITfY",S),
  ]},
 {"city":"Aiči / Nagoja","days":"výlet, 1 den","tag":"Ghibli & auta","desc":"Mezi Kjótem a Tokiem, ~1 h šinkansenem z Kjóta.",
  "places":[
   p("Ghibli Park","🎬 Atrakce","Tripadvisor 3,0 (94)",True,"Rozporuplné – drahé, spíš procházka. Jen pokud miluješ Ghibli.","C6oFQ2JPgzj",A),
   p("Liberty Walk Nagoya","🏎️ Auta","",False,"Všechna LBWK auta na jednom místě – pro petrolheady.","DAmX9zPBeJN",C),
   p("Tsuzuki (kávové představení)","☕ Kavárna","",False,"Největší vídeňská káva v Japonsku + show.","C61LxMHxCu8",F),
  ]},
 {"city":"Suzuka / Mie","days":"výlet pro fanoušky aut, 1 den","tag":"F1 okruh","desc":"~1 h z Nagoji. Jen pokud jsi petrolhead.",
  "places":[
   p("Suzuka Circuit – Circuit Challenger","🏁 Zážitek","Google 4,1 (28)",True,"Projedeš kus reálného F1 okruhu (elektrické motokáry, pomalejší).","DaF8xw2t8Wf",C),
  ]},
 {"city":"Fukuoka / Kjúšú","days":"delší výlet, 2 dny","tag":"Rámen & příroda","desc":"Jih Japonska, letecky nebo šinkansenem. Na delší cestu.",
  "places":[
   p("Hakata rámen (Fukuoka)","🍜 Jídlo","",False,"Šéf 20 let jen dům ↔ práce, absolutní oddanost rámenu.","C7ZX9wDP_-g",F),
   p("Yanagawa river cruise","🛶 Zážitek","",False,"Plavba po kanálech na loďce, ~1,5 h z Hakaty.","C--BJtzS_aA",A),
  ]},
 {"city":"Bonus / mimo hlavní trasu","days":"pokud máš čas navíc","tag":"Skryté perly","desc":"Místa, která stojí za odbočku, když někam zajedeš.",
  "places":[
   p("Restaurace v Kanazawě","🍽️ Jídlo","",False,"Podle autorky nejmilejší majitel, jakého v Japonsku potkala.","DamSR71JRt9",F),
   p("Takayama Inari Shrine, Aomori","⛩️ Chrám","",False,"Off-the-beaten-path svatyně na severu.","C4k7x6LStJL",A),
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
