import os
_D=os.path.dirname(os.path.abspath(__file__))
_p=lambda n: os.path.join(_D,n)
import json, re
data=json.load(open(_p('japonsko.json')))

VERIFIED = {
 "https://www.instagram.com/reel/DJtrgkfy5y6/": {"place":"Coftoalc (スパイスカレー コフトアルコ), Imaike, Nagoja","ext":"Google 4,6 (142)","note":"Kari podnik proslulý tiramisu koulemi (¥650). Zavřeno ve středu, 11:00–18:00."},
 "https://www.instagram.com/reel/C94zYsCvWuv/": {"place":"Goyomatsu Cave (五代松鍾乳洞), Tenkawa, Nara","ext":"Google 4,3 (182)","note":"Krápníková jeskyně v horské vesnici Tenkawa, nahoru vede lanová dráha. Kombinuj s lázněmi Dorogawa Onsen."},
 "https://www.instagram.com/reel/Db9_s31yx_Q/": {"place":"Ginza Okeya (Okeya Kyujiro), Ginza","ext":"Tabelog 3,04","note":"Vizuálně bomba, ale gastronomicky průměr – spíš zážitek pro oči než jistota."},
 "https://www.instagram.com/reel/Dagy4FzPg1s/": {"place":"Ginza Happo, Tokio","ext":"Google 4,3 (2 038)","note":"All-you-can-eat krab + wagyu + pití, ~12 000 JPY. Rezervuj dopředu."},
 "https://www.instagram.com/reel/DaF8xw2t8Wf/": {"place":"Circuit Challenger, Suzuka","ext":"Google 4,1 (28)","note":"Kus reálného F1 okruhu, ale elektrické motokáry (pomalejší, než čekáš)."},
 "https://www.instagram.com/reel/C9-lVf7yuY5/": {"place":"Suzuka Circuit","ext":"Google 4,1 (28)","note":"F1 okruh Suzuka – zážitkové jízdy (Circuit Challenger)."},
 "https://www.instagram.com/reel/DEct_87T8Sp/": {"place":"RURU Cafe, Shibuya","ext":"-","note":"Virální kavárna s water-table konceptem, podle recenzí fajn."},
 "https://www.instagram.com/reel/C53R4gASfUZ/": {"place":"teamLab Planets, Tokio","ext":"Tripadvisor 4,3 (5 439)","note":"Jedna z nejlíp hodnocených atrakcí v Tokiu. Lístky předem."},
 "https://www.instagram.com/reel/Da8lEYhxWpp/": {"place":"Mandarake, Akihabara","ext":"Google 4,2 (5 825)","note":"8 pater anime / figurek / sběratelství."},
 "https://www.instagram.com/reel/C54sBTtNz_d/": {"place":"Nintendo Museum, Uji (Kjóto)","ext":"Tripadvisor 4,1","note":"Nové (2024), vstup jen na losovačku předem."},
 "https://www.instagram.com/reel/C6Jyhz8RYJ-/": {"place":"Nintendo Kyoto (Takashimaya)","ext":"-","note":"Oficiální Nintendo store v Kjótu."},
 "https://www.instagram.com/reel/C8cQ7C-v3ue/": {"place":"Nintendo Store Kyoto","ext":"-","note":"Nezapomeň na foto na střeše."},
 "https://www.instagram.com/reel/C6oFQ2JPgzj/": {"place":"Ghibli Park, Aiči","ext":"Tripadvisor 3,0 (94)","note":"Rozporuplné – drahé, spíš procházka. Jen pro fanoušky Ghibli."},
 "https://www.instagram.com/reel/Da5nlyHza6K/": {"place":"Pari Shokudo (kulturní památka)","ext":"-","note":"100+ let rodinná restaurace, přežila 2. sv. válku."},
 "https://www.instagram.com/reel/C7ZX9wDP_-g/": {"place":"Rámen v Hakatě, Fukuoka","ext":"-","note":"Šéf 20 let jen dům ↔ práce, oddaný rámenu."},
 "https://www.instagram.com/reel/C57c3wKrSFa/": {"place":"Note, Azabu-juban (wagyu)","ext":"-","note":"Top wagyu restaurace v Tokiu."},
 "https://www.instagram.com/reel/DZPoAGrTnUH/": {"place":"Shinjuku Sushi Hatsume","ext":"-","note":"Suši v Šindžuku, nutná rezervace."},
 "https://www.instagram.com/reel/C7WBc2dvnGZ/": {"place":"Kyo Train Garaku (Kjóto–Ósaka)","ext":"-","note":"Nádherný design vlaku za cenu běžné jízdenky."},
 "https://www.instagram.com/reel/DIqriTCPwbd/": {"place":"Kyoto Train Garaku","ext":"-","note":"Speciální vlak Kjóto ↔ Ósaka, zdarma s běžným lístkem."},
 "https://www.instagram.com/reel/C5Lcz-PPpUG/": {"place":"Kyoto Railway Museum","ext":"-","note":"Pro fanoušky vlaků i děti."},
 "https://www.instagram.com/reel/DHmg_ABTwEe/": {"place":"The Railway Museum, Omija","ext":"-","note":"Simulátory řízení vlaku, obří areál."},
 "https://www.instagram.com/reel/DafD2APoR6I/": {"place":"Otsuka Lotec (hodinky)","ext":"-","note":"Ručně dělané hodinky inspirované přístroji."},
 "https://www.instagram.com/reel/C7wGPN6Sh_C/": {"place":"Mofusand merch shop","ext":"-","note":"Originální Mofusand zboží (kočičí umělec Juno)."},
 "https://www.instagram.com/reel/DZhteMYBPi7/": {"place":"Game Boy modding workshop, Akihabara","ext":"-","note":"Postavíš si vlastní Game Boy (přes Klook)."},
 "https://www.instagram.com/reel/C7i7X_iooL6/": {"place":"Mt. Fuji spot","ext":"-","note":"Vyhlídkový spot na Fudži."},
}

def cat_of(o):
    t=(o['cap'] or '').lower()+' '+' '.join(o['tags']).lower()+' '+(o['owner'] or '').lower()
    def has(*ws): return any(w in t for w in ws)
    if has('jdm','gtr','skyline','tomica','diecast','autobacs','tamiya','subaru','liberty walk','daikoku','model car','modelcar','motorsport','carguy','car meet','carmeet','carentusiast','carenthusiast','r34','r32','r35','nismo','spoon','mugen','porsche','apit','initiald','carsof','cargirl','carcommunity','jdmcar'):
        return 'Auta / JDM'
    if has('suzuka','circuit','formula1','fujispeedway','gokart','go kart','racing','racecar'):
        return 'Auta / JDM'
    if has('teamlab','museum','nintendo','ghibli','shrine','temple','torii','tower','deer','disney','universal','cat island','aquarium','observation','pagoda','castle','snow monkey','skytree','robot cafe','planets','falls','cave','ferris'):
        return 'Atrakce & zážitky'
    if has('sushi','ramen','wagyu','crab','tonkatsu','kissaten','izakaya','steak','buffet','dessert','tiramisu','pastr','beef','michelin','coffee','café','cafe','restaurant','dining','omakase','takoyaki','yakiniku','sando','noodle','snack','konbini','7eleven','seven eleven','cola','egg sando','ice cream','bar '):
        return 'Jídlo & kavárny'
    if has('train','shinkansen','railway','monorail','densha','yurikamome','ferry','cruise','saphir','spacia','kintetsu','jrpass','jr pass'):
        return 'Vlaky & doprava'
    if has('shop','store','mall','mandarake','quijote','donki','loft','thrift','secondhand','second-hand','souvenir','uniqlo','bookoff','book off','figur','anime','manga','109','parco','ginza six','itoya','muji','vintage','preloved','towel','skincare','beauty','purikura','sanrio','lego'):
        return 'Nakupování & anime'
    if has('hotel','ryokan','lovehotel','love hotel','park hyatt','ritz','accommod','ubytov'):
        return 'Hotely & ubytování'
    if has('tips','mistake',"don't",'do not','hack','apps','tax-free','tax free','luggage','etiquette','sim card','esim','takkyubin','how to','respect','itinerary','travel tips','traveltips'):
        return 'Tipy & rady'
    return 'Ostatní'

CAT_BASE={'Atrakce & zážitky':4.0,'Jídlo & kavárny':3.8,'Auta / JDM':3.6,'Vlaky & doprava':3.5,'Nakupování & anime':3.4,'Hotely & ubytování':3.2,'Tipy & rady':2.6,'Ostatní':3.0}

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
