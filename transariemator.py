#!/usr/bin/python

import sys
import os.path
import polib
import msti
from lxml import etree

token = msti.get_access_token('lidilidian_translator', '89YhsSvNtX5ZsJqSCQs/rF+Rdws5SKPNhU7c/akntpQ=')

def get_text_from_msmt_xml(xml):
    """Parse the xml string returned by the MS machine translation API, and return just the text"""
    text = []
    doc = etree.fromstring(xml)
    for elem in doc.xpath('/foo:string', namespaces={'foo': 'http://schemas.microsoft.com/2003/10/Serialization/'}):
        if elem.text:
            elem_text = ' '.join(elem.text.split())
            if len(elem_text) > 0:
                text.append(elem_text)
	return ' '.join(text)

source_language = raw_input("Insert Your source language: ")
translate_language = raw_input("Insert Your translation language: ")

po = polib.pofile('administration.po')
#po_valid_entries = [e for e in po if not e.obsolete] // if you want to make entries obsolete

UNTRANSLATED = 0
for untr in po.untranslated_entries():
	UNTRANSLATED += 1
	print("\n")
	print("{} Untranslated words found".format(UNTRANSLATED))
	print("UNTRANSLATED   : {}".format(untr.msgid))
	translation_process = msti.translate(token, untr.msgid, translate_language, source_language)
	print("RECOMMENDATION : {}".format(get_text_from_msmt_xml(translation_process)))
	print("\n")

if UNTRANSLATED == 0:
	print("Process Complete!")

