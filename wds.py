#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import json

class Device:
    def __init__(self, device):
        try:
            self.fields = {}
            for key in sorted(device.keys()):
                if key != 'attributes':
                    self.fields[key] = device[key]
            self.attributes = device['attributes']
        except:
            pass

    def __str__(self):
        str = ''
        for key in self.fields.keys():
            str += "%s => %s\n" % ( key, self.fields[key] )
        for a in self.attributes:
            if a.has_key('name') and a.has_key('value'):
                str += "attribute: %s => %s\n" % ( a['name'], a['value'] )
        return str

    def match(self, name, value):
        result = False
        try:
            result = (self.fields[name] == value)
        except:
            pass
        return result

    def get_id(self):
        return self.fields['brand'] + ' ' + self.fields['model']

    def validate_brand(self):
        return len(self.fields['brand']) > 0 and len(self.fields['brand']) <= 50
        
    def validate_model(self):
        return len(self.fields['model']) > 0 and len(self.fields['model']) <= 50
        
    def validate_form_factor(self):
        form_factors = [ "CANDYBAR", "SMARTPHONE", "PHABLET", "CLAMSHELL" ]
        return self.fields['formFactor'] in form_factors

    def validate_attributes(self):
        fail = False
        for attr in self.attributes:
            if not attr.has_key('name'):
                fail = True
                break
            name = attr['name']
            if len(name) < 1 or len(name) > 20:
                fail = True
                break
            if not attr.has_key('value'):
                fail = True
                break
            value = attr['value']
            if len(value) < 1 or len(value) > 100:
                fail = True
                break
        return not fail

class Wds:
    def __init__(self, filename):
        fp = open(filename, "r")
	self.data = json.load(fp)

        self.devices = []
        self.valid_devices = []
        self.invalid_devices = []
        for i in self.data:
            device = Device(i)
            self.devices.append(device)

    def validate(self):
        self.valid_devices = []
        self.invalid_devices = []
        dups = set()
        result = True

        for i in self.data:
            device = Device(i)

            ok = not device.get_id() in dups

            if ok:
                ok = device.validate_brand()

            if ok:
                ok = device.validate_model()

            if ok:
                ok = device.validate_form_factor()

            if ok:
                ok = device.validate_attributes()

            if ok:
                self.valid_devices.append(device)
                dups.add(device.get_id())
            else:
                self.invalid_devices.append(device)
                result = False
        return result

    def find(self, query):
        """
        Find a list of devices matching the query, where query is expected to be
        a string '<name>:<value>'
        """
        result = []
        (name, value) = query.split(':')
        for device in self.valid_devices:
            if device.match(name, value):
                result.append(device)
        return result

    def story1(self):
        """
        Produce output for Story 1
        """
        for device in self.devices:
            print "\n---- Device ----"
            print device

    def story2(self, full_name):
        """
        Produce output for Story 2
        """
        for device in self.devices:
            if device.get_id() == full_name:
                print "\n---- Matching Device ----"
                print device

    def story3(self):
        """
        Produce output for Story 3
        """
        self.validate()
        for device in self.valid_devices:
            print "\n---- Valid Device ----"
            print device
        for device in self.invalid_devices:
            print "\n---- Invalid Device ----"
            print device

    def story4(self, brand, model):
        """
        Produce output for Story 4
        """
        self.validate()

        brand_query = 'brand:' + brand
        model_query = 'model:' + model
        brands = self.find(brand_query)
        models = self.find(model_query)

        for device in brands:
            print "\n---- Matching brand: %s ----" % brand
            print device

        for device in models:
            print "\n---- Matching model: %s ----" % model
            print device

if __name__ == "__main__":
    wds = Wds('devices.json')
    print "------------ Story 1 -----------------"
    wds.story1()

    print "\n------------ Story 2 -----------------"
    wds.story2('Phony X11')

    print "\n------------ Story 3 -----------------"
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
    wds_bad = Wds('bad.json')
    wds_bad.story3()

    print "\n------------ Story 4 -----------------"
    wds.story4('Phony', 'Universe A1')
