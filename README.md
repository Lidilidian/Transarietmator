# Transarietmator
------
([Click Here for Indonesian Readme](https://github.com/Lidilidian/Transarietmator/README_ID.md))

Python checker for false translation Gettext (.po) file tool.

When You run this program, the program will run automatically looking for false translation in the po file and provide suggestion's to You on the results of translation, then You can use the result for fixing your untranslated po file whether it's possible to use the weblate and pootle service or even by manual translating.

## How use:
- $ git clone https://github.com/Lidilidian/ceksipo.git
- $ sudo chmod a+x install.sh
- $ ceksipo -i file.po -s en -t id or $ ceksipo -h // for help isntruction 
- [Click here][6] for check all supported langguge code.

>### Library Requierement's :

- [x] [lxml 2.2.8][3] for python2.7
- [x] [msti][4] (include in this repo)
- [x] [polib][5] for python2.7 (also include in this repo)
- [x] json
- [x] urllib and urlllib2

>### a list of which should be further developed :

- [x] Translate suggestion's
- [ ] Auto detect source language
- [x] Create arg for simplify the option
- [ ] Save output to new .po file
- [ ] Improve program interface

[1]: https://www.microsoft.com/en-us/translator/translatorapi.aspx        "Microsoft Translator Text API"
[2]: https://github.com/Bauble                                            "Bauble Project"
[3]: https://pypi.python.org/pypi/lxml/2.2.8                              "lxml v.2.2.8 library for python2.7"
[4]: https://github.com/Lidilidian/ceksipo/blob/master/msti.py    		  "Microsoft Translation API connector"
[5]: https://github.com/Lidilidian/ceksipo/blob/master/polib.py  		  "polib library python2.7"
[6]: https://msdn.microsoft.com/en-us/library/hh456380.aspx               "Language Code"

![Microsoft Translation APIlpful even if it's just a warning for a typo, and please don't be shy to contact me at ([hubungi.aja@gmail.com](mailto:hubungi.aja@gmail.com)).

>### Thanks to
- Allah S.W.T and My Family.
- ([@jayvdb](https://github.com/jayvdb) - Mentor of Besutkode who always give support
- ([@edawine](https://github.com/edawine)) & ([@chocochino](https://github.com/chocochino))- which give Me suggestion.
- Every participant of Besutkode and of course all my Friend's in University of Muhammadiyah Jakarta
