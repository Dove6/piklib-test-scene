def generate_objects(name, pick_index, used_index=None):
    ret = rf'''OBJECT=ITEM_INV_{name}
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
ITEM_PICK_{name}:PRIORITY={200 + pick_index}
ITEM_PICK_{name}:ONFOCUSON={{;}}
ITEM_PICK_{name}:ONINIT={{THIS^SETASBUTTON(TRUE, TRUE);}}
ITEM_PICK_{name}:ONCLICK=BEHADDITEMTOMENU("{name}")

'''
    if used_index is not None:
        ret += rf'''OBJECT=ITEM_USED_{name}
ITEM_USED_{name}:TYPE=ANIMO
ITEM_USED_{name}:VISIBLE=FALSE
ITEM_USED_{name}:FILENAME=$COMMON\BUDOWA\USED_{name}.ANN
ITEM_USED_{name}:TOCANVAS=TRUE
ITEM_USED_{name}:PRIORITY={250 + used_index}

'''
    return ret

items = [ #          index
    # name,       pick, used
    ('ANTENA',       0,    0),
    ('BALIA',        2,    0),
    ('BECZKA',       1,    2),
    ('BUTELKA1',     0,    4),
    ('BUTELKA2',     0,    4),
    ('BUTELKA3',     3,    4),
    ('DRABINA',      0,    1),
    ('GRABIE',       0,    0),
    ('LEJEK',        0,    0),
    ('KATOMIERZ',    0,    0),
    ('KOLOWROTEK',   0,    3),
    ('KONEWKA',      0, None),
    ('KOTWICA',      0, None),
    ('OGRODOWAZ',    0,    0),
    ('OPONA',        1,    0),
    ('PIECYK',       2,    2),
    ('PRALKA',       0, None),
    ('PRZETYKACZKA', 0, None),
    ('PULPIT',       0,    0),
    ('RADYJKO',      0,    3),
    ('RURAODKURA',   0,    0),
    ('RURASPUSTOWA', 0,    2),
    ('SZNUR',        0,   10),
    ('SZPULA',       0,    4),
    ('WIADRO',       0, None),
    ('WIOSLO',       4, None),
]

with open('episode.cnv', 'r+', encoding='cp1250') as f:
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        if line.find('### Everything below this point will be truncated') > -1:
            f.truncate(f.tell())
            break

with open('episode.cnv', 'a', encoding='cp1250') as f:
    f.write('\n')
    for (item, pick_index, used_index) in items:
        f.write(generate_objects(item, pick_index, used_index))
