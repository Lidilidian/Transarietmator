#!/usr/bin/python

import base64, sys, os.path, polib, msti, argparse
from lxml import etree

token = msti.get_access_token(base64.standard_b64decode('bGlkaWxpZGlhbl90cmFuc2xhdG9y'), base64.standard_b64decode('ODlZaHNTdk50WDVac0pxU0NRcy9yRitSZHdzNVNLUE5oVTdjL2FrbnRwUT0='))

parser = argparse.ArgumentParser()
parser.add_argument("-i", type=str, required=True, dest='file',help='location of fo file [ex: /path/to/file.po]')
parser.add_argument('-m', required=True, action='store', dest='metode', help='Available method : CheckTranslate, CheckFalseTranslate')
parser.add_argument('-s', required=True, action='store', dest='source_lang', help='Source Language [ex: en]')
parser.add_argument('-t', required=True, action='store', dest='translate_to', help='Translate to language [ex: id]')
parser.add_argument("-v","--version", action='version', version='%(prog)s 1.0')
args = parser.parse_args()

po = polib.pofile(args.file)

def parse_msti_output(xml):
    """Parse output from Micorosoft machine translation API, and return it into string, in case TEXT"""
    text = []
    doc = etree.fromstring(xml)
    for elem in doc.xpath('/foo:string', namespaces={'foo': 'http://schemas.microsoft.com/2003/10/Serialization/'}):
        if elem.text:
            elem_text = ' '.join(elem.text.split())
        if len(elem_text) > 0:
            text.append(elem_text)
    return ' '.join(text)

def checkTranslation():
    translateNo = 0
    valid_entries = [e for e in po if not e.obsolete]
    for entry in valid_entries:
        translation_output = msti.translate(token, entry.msgid, args.translate_to, args.source_lang)
        if translation_output:
            translateNo += 1
            print("\n")
            print("String Number\t\t: {}".format(translateNo))
            print("Source word's\t\t: {}".format(entry.msgid))
            print("Suggestions's\t\t: {}".format(parse_msti_output(translation_output)))
        else:
            print("Done !")

def missTranslation():
    error_no = 0
    valid_entries = [e for e in po if not e.obsolete]
    for entry in valid_entries:
        translation_output = msti.translate(token, entry.msgid, args.translate_to, args.source_lang)
        if translation_output != entry.msgstr:
            error_no += 1
            print("\n")
            print("False Number\t\t: {}".format(error_no))
            print("Source word's\t\t: {}".format(entry.msgid))
            print("Alleged mistranslation\t: {}".format(entry.msgstr))
            print("Suggestions's\t\t: {}".format(parse_msti_output(translation_output)))
        else:
            print("Done !")

def main():
       
    if args.metode == 'CheckTranslate':
        checkTranslation()
    elif args.metode == 'CheckFalseTranslate':
        missTranslation()
    else:
        print('Your not selecting available method, available method ; CheckTranslate and CheckFalseTranslate')

if __name__ == "__main__":
    main()