__author__ = 'siddiqui'
import urllib2
import  json
import webbrowser
response = urllib2.urlopen('http://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=20&format=json').read()
jsonvalues = json.loads(response)

for i in range(1, 20):
    print "Would you like to read an article on : " + jsonvalues['query']['random'][i]['title'] + "\n" + "Enter yes to read, no to move to next article"

    reply = raw_input()
    if reply == "yes" :
        id = str(jsonvalues['query']['random'][i]['id'])
        webbrowser.open_new_tab('http://en.wikipedia.org/wiki?curid='+id)
        break

#TODO implement a GUI to the script