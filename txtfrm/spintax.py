'''
Created on 19.03.2019

@author: neumann
'''


import re


def getText():

    original = """
        Ein Web-Shop {etwa|z.B.|zum Beispiel|beispielsweise|per exemplum}
        {bietet|offeriert|zeigt} einen {Mantel|Rock|Schal|Akku-Bohrer|Backofen|Artikel|Gegenstand|Schnapper}
        für {weitaus|weit|ungleich|sehr viel|bei weitem|bedeutend}
        weniger Geld als alle {anderen|üblichen}
        """

    searchpattern = re.compile(r"{.+?}")
    
    color = [('<span style="color: #333300;">','</span>'),
             ('<span style="color: #99cc00;">','</span>'),
             ('<span style="color: #ff0000;">','</span>')
             ]
    
    for item in re.findall(searchpattern, original):
        i = 0
        newitem = []
        for wort in item[1:-1].split("|"):
            newitem.append(color[i%len(color)][0] + wort + color[i%len(color)][1])
            i += 1
        newitem = "{" + "|".join(newitem) + "}"
        original = original.replace(item, newitem)
    
    return original
    

def getHtml():
    return "<pre>" + getText().replace("<", "&lt;").replace(">","&gt;") + "</pre>"
