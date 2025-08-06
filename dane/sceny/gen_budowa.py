counter = [-1]

def generate_objects(name):
    global counter
    counter[0] += 1
    return rf'''OBJECT=ITEM_INV_{name}
ITEM_INV_{name}:TYPE=IMAGE
ITEM_INV_{name}:VISIBLE=FALSE
ITEM_INV_{name}:FILENAME=$COMMON\BUDOWA\INV_{name}.IMG
ITEM_INV_{name}:TOCANVAS=TRUE
ITEM_INV_{name}:PRIORITY=300

OBJECT=ITEM_PICK_{name}
ITEM_PICK_{name}:TYPE=ANIMO
ITEM_PICK_{name}:VISIBLE=TRUE
ITEM_PICK_{name}:FILENAME=$COMMON\BUDOWA\PICK_{name}.ANN
ITEM_PICK_{name}:TOCANVAS=TRUE
ITEM_PICK_{name}:PRIORITY={200+counter[0]}
ITEM_PICK_{name}:ONFOCUSON={{;}}
ITEM_PICK_{name}:ONINIT={{THIS^SETASBUTTON(TRUE, TRUE);}}
ITEM_PICK_{name}:ONCLICK=BEHADDITEMTOMENU("{name}")

OBJECT=ITEM_USED_{name}
ITEM_USED_{name}:TYPE=ANIMO
ITEM_USED_{name}:VISIBLE=FALSE
ITEM_USED_{name}:FILENAME=$COMMON\BUDUOWA\USED_{name}.ANN
ITEM_USED_{name}:TOCANVAS=TRUE
ITEM_USED_{name}:PRIORITY={200+counter[0]}

'''

items = [
    'PRALKA',
    'BUTELKA3',
    'BECZKA',
    'BALIA',
    'OPONA',
    'PIECYK',
    'KOLOWROTEK',
    'RURASPUSTOWA',
    'OGRODOWAZ',
    'RURAODKURA',
    'ANTENA',
    'LEJEK',
    'BUTELKA1',
    'BUTELKA2',
    'RADYJKO',
    'SZPULA',
    'PULPIT',
    'GRABIE',
    'SZNUR',
    'KATOMIERZ',
    'DRABINA',
    'KONEWKA',
    'PRZETYKACZKA',
    'WIOSLO',
    'WIADRO',
    'KOTWICA',
]

with open('episode.cnv', 'a', encoding='cp1250') as f:
    for item in items:
        f.write(generate_objects(item))
