import json,re
src=open('/mnt/user-data/outputs/layers-research/LAYERS-research-prompt.md',encoding='utf-8').read()
sec2=src[src.index('## 2. Coordinates'):src.index('## 3. Do not duplicate')]
sec4=src[src.index('## 4. Output format'):src.index('## 5. Writing rules')]
sec5=src[src.index('## 5. Writing rules'):].split('\n# Appendix')[0]
sec4=sec4.replace('"region": "province / governorate / emirate",','"region": "first-level region exactly as named in Appendix B",\n  "must_have": "the Part A item number (e.g. \\"SA-A12\\"), or null for a Part B place",')
CN={'sa':'Saudi Arabia','om':'Oman','ae':'United Arab Emirates','qa':'Qatar','bh':'Bahrain'}
Q=json.load(open('quotas.json')); P=json.load(open('plan2.json'))
THEMES={'sa':"Geology first: the harrat volcanic fields (Rahat, Khaybar, Uwayrid, Lunayyir, Kishb, Hutaymah), Red Sea and Farasan coral reefs and islands, the Asir highlands and escarpment, the Rub' al Khali dunes and sabkhas, Tuwaiq escarpment sections, salt domes and Arabian Shield outcrops.",
 'om':"Oman is a world-class geology region: Semail ophiolite sections (Moho transition, pillow lavas, sheeted dykes, peridotite carbonation), Jebel Akhdar and Saih Hatat, Wahiba/Sharqiya Sands, karst and sinkholes, Musandam drowned coast, Huqf outcrops, Masirah ophiolite, wadi fossil sites.",
 'ae':"Geology of Ras Al Khaimah, Fujairah, Ajman and Umm Al Quwain (Hajar Mountains, ophiolite, wadi gorges, exotic limestones, coastal sabkhas and lagoons).",
 'qa':"Geology of Qatar's dome and coast (Dukhan anticline, mesas, sabkhas, dahl sinkholes, Zekreet), and documented sites in Doha, Al Khor, Al Wakrah, Umm Salal and Al Daayen.",
 'bh':"Bahrain is nearly complete; add the few missing must-haves and one or two geological places in the Capital and Muharraq governorates."}
L=[]
A=L.append
A('# Research brief v2 — LAYERS: complete, balanced coverage of the Arab Gulf countries\n\n')
A('You are a research assistant building a dataset for **LAYERS**, a bilingual (English/Arabic) map of the geology, archaeology and ecology of the Arab Gulf countries. Each country must be **complete and defensible**: every officially listed site is on the map, every region has its share of places, and the three layers are balanced.\n\n')
A('Work **country by country**: Saudi Arabia, Oman, United Arab Emirates, Qatar, Bahrain. Do not research Kuwait. Send results in batches of 10–20 places.\n\n')
A('## 1. Two jobs per country\n\n')
A('**Part A — must-have places (do these first).** Appendix B lists, for each country, officially designated sites that are **not yet on the map**: World Heritage sites and components, Tentative List entries, protected areas, Ramsar sites, biosphere reserves, geoparks and recognised geosites, identified from UNESCO, Ramsar, IUGS and national authority pages. For each, return a full record (section 4) with a checkable reference and the best published coordinates, and put its item number in `must_have`. If an item turns out not to be real, not designated, or the same as an Appendix A place, return it with `confidence: "low"` and explain in `distinct_from`.\n\n')
A('**Grouped reserves.** Where Part A says "Protected areas of <region> (grouped)", return ONE record for the group: name it like "Dubai\'s protected areas", put the member reserves with their designation years in `description`, use the coordinates of the largest or best-known member, and cite the authority list.\n\n')
A('**Part B — fill the regional quotas.** Appendix B gives, for each region, how many **extra** places are needed and in which layer. Choose the most significant documented places in that region and layer. If a region truly has fewer documented places, return what exists and say so; never pad with weak sites.\n\n')
A('**Balance target per country** (after both parts): about **40% archaeological, 25–30% geological, 20–25% ecological**. The quotas already produce this.\n\n')
A('**What counts as one place.** One designated site = one place. A serial World Heritage or Tentative property becomes separate places only when its components are distinct places at least ~5 km apart (Part A already lists them that way). A geopark gets one place plus at most its 5 best-documented geosites.\n\n')
A('**Never invent** a site, reference, DOI, coordinate or number. If unsure, leave it out.\n\n')
A(sec2)
A('## 3. Do not duplicate\n\nThe places in **Appendix A** are already on the map. Do not return them under any name, spelling or sub-part. Merge two papers about the same place into one entry with both references.\n\n')
A(sec4); A(sec5.rstrip()+'\n- Always fill `region` with one of the region names used in Appendix B.\n')
A('\n# Appendix A — places already on the map (do not return)\n')
for cc in CN:
    S=[s for s in json.load(open(f'/tmp/w/gulf/{cc}/data.json',encoding='utf-8'))['sites'] if s['c']!='speculative']
    A(f'\n## {CN[cc]} ({len(S)})\n\n'+'; '.join(f"{s['n']} ({s['lat']:.3f}, {s['lng']:.3f})" for s in sorted(S,key=lambda s:s['n']))+'\n')
A('\n# Appendix B — what to find, per country\n')
for cc in CN:
    U=json.load(open(f'missing_units_{cc}.json',encoding='utf-8')); p=P[cc]
    A(f"\n## {CN[cc]}\n\nNow on the map: {p['now']}. Part A must-haves: {p['musthave']}. Part B extras: {p['extra']}. Target total: about {p['final']} "
      f"(archaeological {p['layers_final']['archaeological']}, geological {p['layers_final']['geological']}, ecological {p['layers_final']['ecology']}).\n\n**Focus:** {THEMES[cc]}\n\n")
    A(f'### Part A — must-have places missing from the map ({len(U)})\n\n| # | Name | Layer | Region | Designation | Known coordinates | Source |\n|---|---|---|---|---|---|---|\n')
    for i,u in enumerate(sorted(U,key=lambda u:(u['group'],u.get('region') or '',u['name'])),1):
        co=f"{u['lat']:.4f}, {u['lng']:.4f}" if u.get('lat') else '—'
        des=(u.get('designation') or '').replace('|','/')
        des=des if u['group']=='Protected area (grouped)' else des[:140]
        nm=u['name'].replace('|','/')+(f" ({u['name_ar']})" if u.get('name_ar') else '')
        A(f"| {cc.upper()}-A{i} | {nm} | {u['layer']} | {u.get('region') or '—'} | {des} | {co} | {u.get('source_url') or '—'} |\n")
    A('\n### Part B — extra places per region\n\n| Region | Places after Part A | Extra geological | Extra archaeological | Extra (any layer) |\n|---|---|---|---|---|\n')
    for r,v in Q[cc].items():
        a=v['add']; A(f"| {r} | {sum(v['now'].values())} | {a.get('geological',0) or ''} | {a.get('archaeological',0) or ''} | {a.get('any',0) or ''} |\n")
open('/mnt/user-data/outputs/layers-research/LAYERS-research-prompt-v2.md','w',encoding='utf-8').write(''.join(L))
print(len(''.join(L)))
