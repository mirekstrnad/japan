import os
_D=os.path.dirname(os.path.abspath(__file__))
_p=lambda n: os.path.join(_D,n)
import json, re
data=json.load(open(_p('japonsko.json')))

VERIFIED = {
 "https://www.instagram.com/reel/Db9_s31yx_Q/": {"place":"Ginza Okeya (Okeya Kyujiro), Ginza","ext":"Tabelog 3,04","note":"Vizualne bomba, ale gastro prumer - spis zazitek pro oci nez jistota."},
 "https://www.instagram.com/reel/Dagy4FzPg1s/": {"place":"Ginza Happo, Tokio","ext":"Google 4,3 (2 038)","note":"All-you-can-eat krab + wagyu + piti, ~12 000 JPY. Rezervuj dopredu."},
 "https://www.instagram.com/reel/DaF8xw2t8Wf/": {"place":"Circuit Challenger, Suzuka","ext":"Google 4,1 (28)","note":"Kus realneho F1 okruhu, ale elektricke motokary (pomalejsi, nez cekas)."},
 "https://www.instagram.com/reel/C9-lVf7yuY5/": {"place":"Suzuka Circuit","ext":"Google 4,1 (28)","note":"F1 okruh Suzuka - zazitkove jizdy (Circuit Challenger)."},
 "https://www.instagram.com/reel/DEct_87T8Sp/": {"place":"RURU Cafe, Shibuya","ext":"-","note":"Viral kavarna s water-table konceptem, podle recenzi fajn."},
 "https://www.instagram.com/reel/C53R4gASfUZ/": {"place":"teamLab Planets, Tokio","ext":"Tripadvisor 4,3 (5 439)","note":"Jedna z nejlip hodnocenych atrakci v Tokiu. Listky predem."},
 "https://www.instagram.com/reel/Da8lEYhxWpp/": {"place":"Mandarake, Akihabara","ext":"Google 4,2 (5 825)","note":"8 pater anime / figurek / sberatelstvi."},
 "https://www.instagram.com/reel/C54sBTtNz_d/": {"place":"Nintendo Museum, Uji (Kjoto)","ext":"Tripadvisor 4,1","note":"Nove (2024), vstup jen na losovacku predem."},
 "https://www.instagram.com/reel/C6Jyhz8RYJ-/": {"place":"Nintendo Kyoto (Takashimaya)","ext":"-","note":"Oficialni Nintendo store v Kjotu."},
 "https://www.instagram.com/reel/C8cQ7C-v3ue/": {"place":"Nintendo Store Kyoto","ext":"-","note":"Nezapomen na foto na strese."},
 "https://www.instagram.com/reel/C6oFQ2JPgzj/": {"place":"Ghibli Park, Aici","ext":"Tripadvisor 3,0 (94)","note":"Rozporuplne - drahe, spis prochazka. Jen pro fanousky Ghibli."},
 "https://www.instagram.com/reel/Da5nlyHza6K/": {"place":"Pari Shokudo (kulturni pamatka)","ext":"-","note":"100+ let rodinna restaurace, prezila 2. sv. valku."},
 "https://www.instagram.com/reel/C7ZX9wDP_-g/": {"place":"Ramen v Hakata, Fukuoka","ext":"-","note":"Sef 20 let jen dum <-> prace, oddany ramenu."},
 "https://www.instagram.com/reel/C57c3wKrSFa/": {"place":"Note, Azabu-juban (wagyu)","ext":"-","note":"Top wagyu restaurace v Tokiu."},
 "https://www.instagram.com/reel/DZPoAGrTnUH/": {"place":"Shinjuku Sushi Hatsume","ext":"-","note":"Sushi v Sindzuku, nutna rezervace."},
 "https://www.instagram.com/reel/C7WBc2dvnGZ/": {"place":"Kyo Train Garaku (Kjoto-Osaka)","ext":"-","note":"Nadherny design vlaku za cenu bezne jizdenky."},
 "https://www.instagram.com/reel/DIqriTCPwbd/": {"place":"Kyoto Train Garaku","ext":"-","note":"Specialni vlak Kjoto <-> Osaka, zdarma s beznym listkem."},
 "https://www.instagram.com/reel/C5Lcz-PPpUG/": {"place":"Kyoto Railway Museum","ext":"-","note":"Pro fanousky vlaku i deti."},
 "https://www.instagram.com/reel/DHmg_ABTwEe/": {"place":"The Railway Museum, Omija","ext":"-","note":"Simulatory rizeni vlaku, obri areal."},
 "https://www.instagram.com/reel/DafD2APoR6I/": {"place":"Otsuka Lotec (hodinky)","ext":"-","note":"Rucne delane hodinky inspirovane pristroji."},
 "https://www.instagram.com/reel/C7wGPN6Sh_C/": {"place":"Mofusand merch shop","ext":"-","note":"Originalni Mofusand zbozi (kocici umelec Juno)."},
 "https://www.instagram.com/reel/DZhteMYBPi7/": {"place":"Game Boy modding workshop, Akihabara","ext":"-","note":"Postavis si vlastni Game Boy (pres Klook)."},
 "https://www.instagram.com/reel/C7i7X_iooL6/": {"place":"Mt. Fuji spot","ext":"-","note":"Vyhledovy spot na Fudzi."},
}

def cat_of(o):
    t=(o['cap'] or '').lower()+' '+' '.join(o['tags']).lower()+' '+(o['owner'] or '').lower()
    def has(*ws): return any(w in t for w in ws)
    if has('jdm','gtr','skyline','tomica','diecast','autobacs','tamiya','subaru','liberty walk','daikoku','model car','modelcar','motorsport','carguy','car meet','carmeet','carentusiast','carenthusiast','r34','r32','r35','nismo','spoon','mugen','porsche','apit','initiald','carsof','cargirl','carcommunity','jdmcar'):
        return 'Auta / JDM'
    if has('suzuka','circuit','formula1','fujispeedway','gokart','go kart','racing','racecar'):
        return 'Auta / JDM'
    if has('teamlab','museum','nintendo','ghibli','shrine','temple','torii','tower','deer','disney','universal','cat island','aquarium','observation','pagoda','castle','snow monkey','skytree','robot cafe','planets','falls','cave','ferris'):
        return 'Atrakce & zazitky'
    if has('sushi','ramen','wagyu','crab','tonkatsu','kissaten','izakaya','steak','buffet','dessert','tiramisu','pastr','beef','michelin','coffee','café','cafe','restaurant','dining','omakase','takoyaki','yakiniku','sando','noodle','snack','konbini','7eleven','seven eleven','cola','egg sando','ice cream','bar '):
        return 'Jidlo & kavarny'
    if has('train','shinkansen','railway','monorail','densha','yurikamome','ferry','cruise','saphir','spacia','kintetsu','jrpass','jr pass'):
        return 'Vlaky & doprava'
    if has('shop','store','mall','mandarake','quijote','donki','loft','thrift','secondhand','second-hand','souvenir','uniqlo','bookoff','book off','figur','anime','manga','109','parco','ginza six','itoya','muji','vintage','preloved','towel','skincare','beauty','purikura','sanrio','lego'):
        return 'Nakupovani & anime'
    if has('hotel','ryokan','lovehotel','love hotel','park hyatt','ritz','accommod','ubytov'):
        return 'Hotely & ubytovani'
    if has('tips','mistake',"don't",'do not','hack','apps','tax-free','tax free','luggage','etiquette','sim card','esim','takkyubin','how to','respect','itinerary','travel tips','traveltips'):
        return 'Tipy & rady'
    return 'Ostatni'

CAT_BASE={'Atrakce & zazitky':4.0,'Jidlo & kavarny':3.8,'Auta / JDM':3.6,'Vlaky & doprava':3.5,'Nakupovani & anime':3.4,'Hotely & ubytovani':3.2,'Tipy & rady':2.6,'Ostatni':3.0}

def score(o,cat):
    s=CAT_BASE[cat]
    cap=(o['cap'] or ''); low=cap.lower()
    if '📍' in cap or 'address' in low or 'located' in low or 'location:' in low or '📌' in cap: s+=0.4
    if any(w in low for w in ['must','best','iconic','world famous','must-visit','must visit','hidden gem','bucket list','legendary','favourite','favorite']): s+=0.25
    if any(w in low for w in ['michelin','national','cultural property','100 years','over 100','registered','75 years','135 year']): s+=0.25
    if len(cap.strip())<40 and '📍' not in cap: s-=0.6
    if low.count('#')>6 and '📍' not in cap and 'address' not in low: s-=0.2
    if any(w in low for w in ['comment ','link in bio','discount code','use my code','use code','promo code']): s-=0.15
    return max(2.0,min(5.0,round(s*2)/2))

rows=[]
for i,o in enumerate(data):
    cat=cat_of(o)
    v=VERIFIED.get(o['url'])
    sc=score(o,cat)
    if v: sc=max(sc,4.0)
    rows.append({'i':i,'owner':o['owner'] or '(bez jmena)','url':o['url'],'cat':cat,'score':sc,
        'tags':o['tags'][:8],'cap':(o['cap'] or '').strip(),
        'place':v['place'] if v else '','ext':v['ext'] if v else '','note':v['note'] if v else ''})

json.dump(rows, open(_p('reels_rated.json'),'w'), ensure_ascii=False)
from collections import Counter
print(Counter(r['cat'] for r in rows))
print('total',len(rows),'verified',sum(1 for r in rows if r['place']))
