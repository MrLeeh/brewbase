#!/usr/bin/env python

"""
import_maltlist.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from pyquery import PyQuery as pq

from app.models import Malt
from app import db


doc = pq('http://hobbybrauer.de/forum/wiki/doku.php/malzuebersicht')


def replace(s):
    replace_list = [
        (',', '.'),
        ('~', ''),
        ('?', '')
    ]
    for char in replace_list:
        s = s.replace(char[0], char[1])
    return s


def median(s_val):
    values = [str.strip(s) for s in s_val.split('-')]
    try:
        values = [float(replace(s)) for s in values]
    except ValueError:
        return None
    else:
        return sum(values) / len(values)


def get_malts_from_hobbybrauer():
    for table in doc('table'):
        rows = doc(table).find('tr')
        for row in rows[1:]:
            cells = doc(row).find('td')

            name = cells.eq(0).text()
            english_name = cells.eq(1).text()
            ebc = median(cells.eq(2).text())

            if name == '':
                name = english_name

            if ebc is not None:
                yield(Malt(name=name, ebc=ebc))


Malt.query.delete()
malts = sorted(list(get_malts_from_hobbybrauer()), key=lambda x: x.name)
db.session.add_all(malts)
db.session.commit()
