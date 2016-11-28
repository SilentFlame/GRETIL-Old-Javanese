import urllib2
url = ""
req= urllib2.urlopen(url)

file_path = ""
fle_name = ".htm"


f = open(file_path+file_name, 'w+')
data = req.read()
f.write(data)
f.close()



