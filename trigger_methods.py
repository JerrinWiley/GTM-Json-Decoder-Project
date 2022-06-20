# Test filters
filter = [
    {
        "type": "CONTAINS",
        "parameter": [
            {
                "type": "TEMPLATE",
                "key": "arg0",
                "value": "{{Page URL}}"
            },
            {
                "type": "TEMPLATE",
                "key": "arg1",
                "value": "docs.couchbase.com"
            }
        ]
    },
    {
        "type": "MATCH_REGEX",
        "parameter": [
            {
                "type": "TEMPLATE",
                "key": "arg0",
                "value": "{{element id}}"
            },
            {
                "type": "TEMPLATE",
                "key": "arg1",
                "value": "(yesBtn)|(noBtn)"
            }
        ]
    }
]

folder = [
    {
        "accountId": "27605728",
        "containerId": "844498",
        "folderId": "68",
        "name": "Global Variables",
        "fingerprint": "1455306776310"
    },
    {
        "accountId": "27605728",
        "containerId": "844498",
        "folderId": "974",
        "name": "Google Analytics Elements",
        "fingerprint": "1574551691519"
    },
    {
        "accountId": "27605728",
        "containerId": "844498",
        "folderId": "975",
        "name": "Third-Party Elements",
        "fingerprint": "1574551002425"
    },
    {
        "accountId": "27605728",
        "containerId": "844498",
        "folderId": "976",
        "name": "Global Triggers",
        "fingerprint": "1574551021799"
    }
]

customEventFilter = [
    {
        "type": "EQUALS",
        "parameter": [
            {
                "type": "TEMPLATE",
                "key": "arg0",
                "value": "{{_event}}"
            },
            {
                "type": "TEMPLATE",
                "key": "arg1",
                "value": "customEvent"
            }
        ]
    }
]

parameter = [
    {
        'type': 'BOOLEAN', 
        'key': 'useOnScreenDuration', 
        'value': 'false'
    }, 
    {
        'type': 'BOOLEAN', 
        'key': 'useDomChangeListener', 
        'value': 'true'
    }, 
    {
        'type': 'TEMPLATE', 
        'key': 'elementSelector', 
        'value': 'div.mktoForm'
    }, 
    {
        'type': 'TEMPLATE', 
        'key': 'firingFrequency', 
        'value': 'ONCE'
    }, 
    {
        'type': 'TEMPLATE', 
        'key': 'selectorType', 
        'value': 'CSS'
    }, 
    {
        'type': 'TEMPLATE', 
        'key': 'onScreenRatio', 
        'value': '50'
    }
]



# Returns list of formatted filter conditions
def filter_parser(filter):
    # print(len(filter))
    list = []
    try:
        for i in filter:
            # print(i)
            variable = i['parameter'][0]['value']
            condition = i['type']
            value = i['parameter'][1]['value']
            # print(type(list))
            string = "%s %s '%s'" % (variable, condition, value)
            # print(string)
            list.append(string)
    except:
        pass

    return list

# Returns list of formatted filter conditions
def event_parser(custom_event_filter, filter_type):
    # print(len(filter))
    list = []
    try:
        for i in custom_event_filter:
            # print(i)
            event = i['parameter'][0]['value']
            condition = i['type']
            value = i['parameter'][1]['value']
            # print(type(list))
            string = "%s %s '%s'" % (event, condition, value)
            # print(string)
            list.append(string)
    except:
        pass
    return list

# Returns string of formatted parameter conditions
def parameter_parser(parameter,type):
    elementVisibility_dict = {
        'selectorType': 'Selection Method: ',
        'elementSelector': 'Element Selector: ',
        'firingFrequency' : 'When to fire this trigger: ',
        'onScreenRatio' : 'Minimum Percent Visible: ',
        'useOnScreenDuration' : 'Set minimum on-screen duration: ',
        'useDomChangeListener' : 'Observe DOM changes: ',
    }

    string = ''
    if type == 'ELEMENT_VISIBILITY':
        try:
            for j, i in enumerate(parameter):
                key = i['key']
                value = i['value']
                try:
                    cat = elementVisibility_dict[key]
                    if j == 0:
                        string += '%s%s' % (cat,value)
                    else:
                        string += '\n%s%s' % (cat,value)
                except:
                    if j == 0:
                        string += '%s EQUALS %s' % (key,value)
                    else:
                        string += '\n%s EQUALS %s' % (key,value)
                # print(value)
        except:
            pass
    else:
        try:
            for i in parameter:
                key = i['key']
                value = i['value']
                # print(value)
                string += '\n%s EQUALS %s' % (key,value)
        except:
            pass
    return string

def folder_dictionary(folder_list):
    new_dict = {}
    try:
        for dict in folder_list:
            # print(type(dict))
            new_dict[dict['folderId']] = dict['name']
    except:
        print('Folder dictionary builder failed')
    return (new_dict)


# # Function tests
# print(parameter_parser(parameter, 'elementVisibility'))
# print(filter_parser(filter)[0])
# print(event_parser(customEventFilter, 'customEvent')[0])
# print(folder_dictionary(folder))
# test_dict = folder_dictionary(folder)
# print(test_dict['974'])
