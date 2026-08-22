# -*- coding: utf-8 -*-
import os
_D=os.path.dirname(os.path.abspath(__file__))
_p=lambda n: os.path.join(_D,n)
import json, re
rows=json.load(open(_p('reels_rated.json')))
data=json.load(open(_p('japonsko.json')))

# priority-ordered city rules (label, keywords)
RULES=[
 ("Kjóto",["kyoto","kjoto","fushimi inari","gion","arashiyama","higashiyama","nanzenji","kiyomizu","uji","kinkaku","teramachi","shijo","parkhyattkyoto","kyototravel"]),
 ("Ósaka",["osaka","dotonbori","namba","nipponbashi","shinsaibashi","umeda","shinsekai","glico","tsutenkaku","kansai"]),
 ("Nara",["nara","todaiji","narapark"]),
 ("Nagoja / Aiči",["nagoya","aichi","ghibli park","ghiblipark","mitaka","nagoyafood","chubu","tokoname"]),
 ("Fukuoka / Kjúšú",["fukuoka","hakata","yanagawa","beppu","kyushu","kjusu","tenjin","dazaifu"]),
 ("Hakone / Fudži",["mt fuji","mtfuji","mount fuji","mountfuji","fujiyoshida","kawaguchi","chureito","hakone","fujikawa","fujispeedway","fuji speedway","shizuoka","fujisan","gotemba"]),
 ("Suzuka / Mie",["suzuka","mie ","ise "]),
 ("Kamakura / Enošima",["kamakura","enoshima"]),
 ("Jokohama",["yokohama","daikoku","minato mirai"]),
 ("Kanazawa",["kanazawa","ishikawa"]),
 ("Hokkaidó",["hokkaido","sapporo","otaru","niseko"]),
 ("Hirošima / Mijadžima",["hiroshima","miyajima","itsukushima"]),
 ("Aomori / Tóhoku",["aomori","tohoku","sendai","tsugaru","yamagata"]),
 ("Wakajama",["wakayama","koyasan","kishi station","tama densha"]),
 ("Kawagoe (Saitama)",["kawagoe","saitama","omiya","omija"]),
 ("Tokio",["tokyo","tokio","shibuya","shinjuku","ginza","akihabara","asakusa","harajuku","daikanyama","azabu","shimbashi","shinbashi","marunouchi","roppongi","ueno","nakano","kichijoji","odaiba","toyosu","ikebukuro","nihonbashi","meguro","setagaya","gotokuji","nezu","skytree","tokyotower","teamlab","yurikamome","yamanote","keio tama","puroland","tama center","jingumae","aoyama","omotesando","chiyoda","minato","koto"]),
]

def city_of(o):
    t=(o['cap'] or '').lower()+' \n '+' '.join(o['tags']).lower()+' '+(o['owner'] or '').lower()
    for label,kws in RULES:
        for k in kws:
            # word-start boundary so 'uji' doesn't match 'fuji', 'nara' matches word start
            if re.search(r'\b'+re.escape(k.strip()), t):
                return label
    return "Celé Japonsko / neurčeno"

for r,o in zip(rows,data):
    r['city']=city_of(o)

json.dump(rows,open(_p('reels_rated.json'),'w'),ensure_ascii=False)
from collections import Counter
c=Counter(r['city'] for r in rows)
for k,v in c.most_common():
    print(f'{v:3d}  {k}')
