# -*- coding: utf-8 -*-
"""Untitled49.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_t8HSi-MFxxCkuiafI81d1MUItl4dejQ
"""

import pandas as pd
baza={
    "FISH":[ "Qadamova Zulayho", "Xalilov Durbek"       ],
    "Fan nomi":[    "Sun'iy intellekt", "Sun'iy intellekt"    ],
"Mashg'ulot turi":["amaliy", "ma'ruza"          ],
    "kafedrasi":[  "Axborot texnologiyalari","Axborot texnologiyalari"]

}
db=pd.DataFrame(baza)
print(db)

db.to_excel("oqituvchilar.xlsx")