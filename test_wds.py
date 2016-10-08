#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import unittest
from wds import Wds

class TestWds(unittest.TestCase):

    def test_validate1(self):
        str = '[{\t"brand":"Mockia",\n\
\t"model":"5800",\n\
\t"formFactor":"CANDYBARZ",\n\
\t"attributes":[\n\
\t\t{"name":"Screen Size","value":"128mm"}\n\
\t]},\n\
{\t\n\
\t"brand":"Phony",\n\
\t"model":"X11",\n\
\t"formFactor":"SMARTPHONE",\n\
\t"attributes":[\n\
\t\t{"name":"Bluetooth","value":"0.1"},\n\
\t\t{"name":"Raspberry","value":"Pi"}\n\
\t]},\n\
{\n\
\t"brand":"Samwrong",\n\
\t"model":"Universe A1",\n\
\t"formFactor":"PHABLET",\n\
\t"attributes":[\n\
\t\t{"name":"Frequencies","value":"GSM,LTE,Kenneth"},\n\
\t\t{"name":"Memory","value":"333Mb"},\n\
\t\t{"name":"Teasmaid","value":"true"}\n\
\t]}\n\
]\n'        
        f = open('bad.json', 'w')
        f.write(str)
        f.close()

        wds = Wds('devices.json')
        result = wds.validate()
        self.assertEqual(result, True)

        wds = Wds('bad.json')
        result = wds.validate()
        self.assertEqual(result, False)

    def test_validate2(self):
        str = '[{\t"brand":"Mockia",\n\
\t"model":"5800",\n\
\t"formFactor":"CANDYBAR",\n\
\t"attributes":[\n\
\t\t{"name":"Screen Size","value":"128mm"}\n\
\t]},\n\
{\t\n\
\t"brand":"Phony",\n\
\t"model":"X11",\n\
\t"formFactor":"SMARTPHONE",\n\
\t"attributes":[\n\
\t\t{"nm":"Bluetooth","value":"0.1"},\n\
\t\t{"name":"Raspberry","value":"Pi"}\n\
\t]},\n\
{\n\
\t"brand":"Samwrong",\n\
\t"model":"Universe A1",\n\
\t"formFactor":"PHABLET",\n\
\t"attributes":[\n\
\t\t{"name":"Frequencies","value":"GSM,LTE,Kenneth"},\n\
\t\t{"name":"Memory","value":"333Mb"},\n\
\t\t{"name":"Teasmaid","value":"true"}\n\
\t]}\n\
]\n'        
        f = open('bad.json', 'w')
        f.write(str)
        f.close()

        wds = Wds('bad.json')
        result = wds.validate()
        self.assertEqual(result, False)

    def test_validate3(self):
        str = '[{\t"brand":"Mockia++++++++++++++++++++++++++++++++++++++++++++++++++++++++",\n\
\t"model":"5800",\n\
\t"formFactor":"CANDYBAR",\n\
\t"attributes":[\n\
\t\t{"name":"Screen Size","value":"128mm"}\n\
\t]},\n\
{\t\n\
\t"brand":"Phony",\n\
\t"model":"X11",\n\
\t"formFactor":"SMARTPHONE",\n\
\t"attributes":[\n\
\t\t{"name":"Bluetooth","value":"0.1"},\n\
\t\t{"name":"Raspberry","value":"Pi"}\n\
\t]},\n\
{\n\
\t"brand":"Samwrong",\n\
\t"model":"Universe A1",\n\
\t"formFactor":"PHABLET",\n\
\t"attributes":[\n\
\t\t{"name":"Frequencies","value":"GSM,LTE,Kenneth"},\n\
\t\t{"name":"Memory","value":"333Mb"},\n\
\t\t{"name":"Teasmaid","value":"true"}\n\
\t]}\n\
]\n'        
        f = open('bad.json', 'w')
        f.write(str)
        f.close()

        wds = Wds('bad.json')
        result = wds.validate()
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()
