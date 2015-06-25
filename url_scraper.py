import requests
from codecs import open

f1=r"c:\tmp\units\weblist.tsv"
f2=r"c:\tmp\units\units.js"
with open(f1, 'r', encoding="utf-8") as infile, open(f2, 'w', encoding="utf-8") as outfile:
    outfile.write('var units = {\n')
    firstline = True
#    fullname = 'Testing'
#    testunits = ['cech','frwa','mlkm','mall','inau','chva','xrds']
#    for unit in testunits:
    for line in infile:
        unit,fullname = [f.strip() for f in line.split('\t')]
        try:
            try:
                resp = requests.get('http://www.nps.gov/'+unit)
            except Exception as e:
                resp = e
            if resp:
                if resp.status_code == 200:
                    lines = resp.text.split('\n')
                    start = -1
                    for num, line in enumerate(lines):
                        if 'bapTitleBox' in line:
                            start = num
                            break
                    if start > 0:
                        gotname,gotextra = False,False
                        for line in lines[start:(start+10)]:
                            if not gotname and '<h1>' in line:
                                gotname = True
                                name = line.replace('<h1>','').replace('</h1>','').strip()
                            if not gotextra and '<span class="location">' in line:
                                gotextra = True
                                typ,loc  = line.replace('<h3>','').replace('</span></h3>','').split('<span class="location">')
                                typ,loc = typ.strip(),loc.strip()
                        if not gotname:
                            name = u'*Name line not found'
                        if not gotextra:
                            msg = u'*Location line not found'
                            typ,loc = msg,msg
                        outline = u'"{0}":{{"name":"{1}","type":"{2}","state":"{3}"}}'.format(unit.upper(),name,typ,loc)
                    else:
                        outline = u'"{0}":{{"name":"{1}","type":"*Desktop header not found","state":""}}'.format(unit.upper(),fullname)
                else:
                    outline = u'"{0}":{{"name":"{1}","type":"*Bad request: {2}","state":""}}'.format(unit.upper(),fullname,resp.status_code)
            else:
                outline = u'"{0}":{{"name":"{1}","type":"*Request Exception: {2}","state":""}}'.format(unit.upper(),fullname,resp)
            if firstline:
                firstline = False
            else:
                outfile.write(u',\n')
            outfile.write(outline)
        except Exception as e:
            outfile.write(unit + ' ' + str(e))
    outfile.write(u'\n};\n')
