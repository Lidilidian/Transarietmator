# Transarietmator
------
Python checker for Untranslated Gettext (.po) file and recommendation for the unstranslated `msgstr` tool.

this program using Python v.2.7 and [Microsoft Translator Text API][1] as backend translation. when You run this program, the program will run automatically looking for untranslated `msgstr` in the po file and provide recommendation's to You on the results of translation then You can use the result for fixing your untranslated po file whether it's possible to use the weblate and pootle service or even by manual translating.

## How use:
- $ git clone https://github.com/Lidilidian/Transarietmator.git
- $ cd Transariemator
- $ python2.7 transariemator.py 
- Insert Source Language : en // Insert the language code of Your source po file.
- Insert Your translation language : id // insert the language you want to be your translate recommendation
- [Click here][6] for check all supported langguge code.

note : this program default is use `administration.po` from [Bauble Project][2] , You should change it in `transarietmator.py` with your own .po file

>### Library Requierement's :

- [x] [lxml 2.2.8][3] for python2.7
- [x] [msti][4] (include in this repo)
- [x] [polib][5] for python2.7 (also include in this repo)
- [x] json
- [x] urllib and urlllib2

>### a list of which should be further developedDeveloping :

- [x] Translate suggestion's
- [ ] Auto detect source language
- [ ] Create argparse for simplify the option
- [ ] Save output to new .po file
- [ ] Improve program interface

[1]: https://www.microsoft.com/en-us/translator/translatorapi.aspx        "Microsoft Translator Text API"
[2]: https://github.com/Bauble                                            "Bauble Project"
[3]: https://pypi.python.org/pypi/lxml/2.2.8                              "lxml v.2.2.8 library for python2.7"
[4]: https://github.com/Lidilidian/Transarietmator/blob/master/msti.py    "Microsoft Translation API connector"
[5]: https://github.com/Lidilidian/Transarietmator/blob/master/polib.py   "polib library python2.7"
[6]: https://msdn.microsoft.com/en-us/library/hh456380.aspx               "Language Code"

>### License
This program using the MIT License - https://github.com/Lidilidian/Transarietmator/blob/master/LICENSE
