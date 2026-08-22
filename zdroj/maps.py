# -*- coding: utf-8 -*-
import os
_D=os.path.dirname(os.path.abspath(__file__))
_p=lambda n: os.path.join(_D,n)
import json, re, urllib.parse
rows=json.load(open(_p('reels_rated.json')))
data=json.load(open(_p('japonsko.json')))

CITY_HINT={
 "Tokio":"Tokyo","Kjóto":"Kyoto","Ósaka":"Osaka","Nara":"Nara","Nagoja / Aiči":"Nagoya",
 "Suzuka / Mie":"Suzuka","Hakone / Fudži":"Mount Fuji","Jokohama":"Yokohama",
 "Kamakura / Enošima":"Kamakura","Kawagoe (Saitama)":"Kawagoe","Kanazawa":"Kanazawa",
 "Fukuoka / Kjúšú":"Fukuoka","Hirošima / Mijadžima":"Hiroshima","Aomori / Tóhoku":"Aomori",
 "Wakajama":"Wakayama","Hokkaidó":"Hokkaido","Celé Japonsko / neurčeno":""}

# manual precise queries for verified places (best geocoding)
MANUAL={
 "https://www.instagram.com/reel/Db9_s31yx_Q/":"Ginza Okeya Kyujiro, Ginza, Tokyo",
 "https://www.instagram.com/reel/Dagy4FzPg1s/":"Ginza Happo, Ginza, Tokyo",
 "https://www.instagram.com/reel/DaF8xw2t8Wf/":"Suzuka Circuit, Mie, Japan",
 "https://www.instagram.com/reel/C9-lVf7yuY5/":"Suzuka Circuit, Mie, Japan",
 "https://www.instagram.com/reel/DEct_87T8Sp/":"RURU Cafe Shibuya, Tokyo",
 "https://www.instagram.com/reel/C53R4gASfUZ/":"teamLab Planets TOKYO, Toyosu",
 "https://www.instagram.com/reel/Da8lEYhxWpp/":"Mandarake Complex, Akihabara, Tokyo",
 "https://www.instagram.com/reel/C54sBTtNz_d/":"Nintendo Museum, Uji, Kyoto",
 "https://www.instagram.com/reel/C6Jyhz8RYJ-/":"Nintendo Kyoto, Takashimaya, Kyoto",
 "https://www.instagram.com/reel/C8cQ7C-v3ue/":"Nintendo Kyoto, Takashimaya, Kyoto",
 "https://www.instagram.com/reel/C6oFQ2JPgzj/":"Ghibli Park, Aichi, Japan",
 "https://www.instagram.com/reel/Da5nlyHza6K/":"Pari Shokudo, Japan",
 "https://www.instagram.com/reel/C7ZX9wDP_-g/":"Shimogofukumachi ramen, Hakata, Fukuoka",
 "https://www.instagram.com/reel/C57c3wKrSFa/":"Note Azabu-juban wagyu, Tokyo",
 "https://www.instagram.com/reel/DZPoAGrTnUH/":"Shinjuku Sushi Hatsume, Nishi-Shinjuku, Tokyo",
 "https://www.instagram.com/reel/C7WBc2dvnGZ/":"Kyo Train Garaku, Kyoto",
 "https://www.instagram.com/reel/DIqriTCPwbd/":"Kyo Train Garaku, Kyoto",
 "https://www.instagram.com/reel/C5Lcz-PPpUG/":"Kyoto Railway Museum, Kyoto",
 "https://www.instagram.com/reel/DHmg_ABTwEe/":"The Railway Museum, Omiya, Saitama",
 "https://www.instagram.com/reel/DafD2APoR6I/":"Otsuka Lotec, Japan",
 "https://www.instagram.com/reel/C7wGPN6Sh_C/":"Mofusand store, Tokyo",
 "https://www.instagram.com/reel/DZhteMYBPi7/":"Akihabara Game Boy modding workshop, Tokyo",
 "https://www.instagram.com/reel/DJtrgkfy5y6/":"スパイスカレー コフトアルコ, 3-41-16 Imaike, Chikusa Ward, Nagoya, Aichi",
 # extra common named places
 "https://www.instagram.com/reel/C5igoKPhJEF/":"Tonkatsu Shimizu, Kyoto",
 "https://www.instagram.com/reel/DB3_9TxvNtw/":"Nara Park, Nara",
 "https://www.instagram.com/reel/DYzZxEbMK4b/":"Ichiraku Dotonbori, Osaka",
 "https://www.instagram.com/reel/DLp4anWJg-U/":"The Munch cafe, Osaka",
 "https://www.instagram.com/reel/C_6psNute4H/":"Model Garage ROM, Osaka",
 "https://www.instagram.com/reel/DAhOafoITfY/":"Shinsaibashisuji, Osaka",
 "https://www.instagram.com/reel/DAmX9zPBeJN/":"Liberty Walk, Nagoya",
 "https://www.instagram.com/reel/C61LxMHxCu8/":"Tsuzuki cafe, Nagoya",
 "https://www.instagram.com/reel/C--BJtzS_aA/":"Yanagawa River Cruise, Fukuoka",
 "https://www.instagram.com/reel/C4k7x6LStJL/":"Takayama Inari Shrine, Aomori",
 "https://www.instagram.com/reel/DamSR71JRt9/":"Kanazawa, Ishikawa",
 "https://www.instagram.com/reel/C9ITiDFJ-Kr/":"Tamiya Plamodel Factory Shimbashi, Tokyo",
 "https://www.instagram.com/reel/C6ooJFyLy1O/":"Tsutaya Books Ginza, Tokyo",
 "https://www.instagram.com/reel/DFfWkXVtatl/":"Gotokuji Temple, Tokyo",
 "https://www.instagram.com/reel/DF83MM1SO3B/":"Subaru STI Gallery, Mitaka, Tokyo",
 "https://www.instagram.com/reel/C4VvutnPHfm/":"Daikoku Parking Area, Yokohama",
}

STOP=re.compile(r'^(address|hours|location|about|open|tel|phone|recommended|save|comment|follow|use|book|check)\b',re.I)
FILLER=['which','please',' dm','comment','follow','save ','link','code','just ','literally','next to','isn','you ','your ','here ','this ','more info','check ','tag ','http','www.','store details','access','highlight','available','svoje','tipy','mezi ','former','details','situated']
VENUE_TOK=['cafe','coffee','sushi','ramen','izakaya','garage','museum','kissa','restaurant','diner','shrine','temple','autobacs','tamiya','mandarake','dotonbori','yakiniku','tonkatsu','bakery','patisserie']

def bad(seg):
    low=seg.lower()
    if len(seg)<3 or len(seg)>55: return True
    return any(f in low for f in FILLER)

def clean(s):
    s=re.sub(r'[#@].*$','',s)  # drop trailing hashtags/handles
    s=re.sub(r'[぀-ヿ一-鿿]+',' ',s)  # drop CJK for the query (keep latin name)
    s=re.sub(r'[^A-Za-z0-9 ,\.\-&\']',' ',s)
    s=re.sub(r'\s+',' ',s).strip(' ,.-')
    return s

def handle_name(h):
    h=h.strip().lstrip('@')
    h=re.sub(r'[._]+',' ',h)
    return h.strip()

def extract(o):
    cap=o['cap'] or ''
    # 1) after pin emoji
    for pin in ['📍','📌']:
        i=cap.find(pin)
        if i>=0:
            seg=clean(cap[i+len(pin):].split('\n')[0])
            if not STOP.match(seg) and not bad(seg):
                return seg
    # 2) 'Location:'/'Address' line
    m=re.search(r'(?:location|address)\s*[:\-]?\s*(.+)',cap,re.I)
    if m:
        seg=clean(m.group(1).split('\n')[0])
        if not bad(seg): return seg
    # 3) @venue handle only if it clearly looks like a venue
    for m in re.finditer(r'@([a-z0-9._]{4,30})',cap.lower()):
        h=m.group(1)
        if any(b in h for b in ['klook','airalo','jetpac','official','subject','usa','_au','anz']): continue
        if any(v in h for v in VENUE_TOK):
            nm=handle_name(h)
            if not bad(nm): return nm
    return ''

out=0
for r,o in zip(rows,data):
    url=o['url']
    if url in MANUAL:
        q=MANUAL[url]
    else:
        place=extract(o)
        cityh=CITY_HINT.get(r['city'],'')
        if place:
            q=place
            if cityh and cityh.lower() not in q.lower(): q+=', '+cityh
            if 'japan' not in q.lower(): q+=', Japan'
        elif cityh:
            q=''  # generic reel with only a city -> no precise place; skip maps
        else:
            q=''
    if q:
        r['gmap']='https://www.google.com/maps/search/?api=1&query='+urllib.parse.quote(q)
        r['mq']=q
        out+=1
    else:
        r['gmap']=''; r['mq']=''

json.dump(rows,open(_p('reels_rated.json'),'w'),ensure_ascii=False)
print('reels with maps link:',out,'/',len(rows))
# show a sample
for r in rows[:14]:
    print(('Y' if r['gmap'] else '-'),r['city'][:12].ljust(12),'|',(r['mq'] or '(zadny)')[:50])
