from bs4 import BeautifulSoup

read_file_path = "/home/speedy/FLAME/Soc-related/cltk/GRETIL-Old-Javanese/html/"
write_file_path = "/home/speedy/FLAME/Soc-related/cltk/GRETIL-Old-Javanese/text/"

# file to be scraped
html_file_name = "vrhasp_u.htm"

# output file name
text_file_name = "vrhasp_u.txt"

#will be already there
f = open(read_file_path+html_file_name, 'r')

data = f.read().decode('utf-8')
data = BeautifulSoup(data)

# kill all script and style elements
for script in data(["script", "style"]):
    script.extract()    # rip it out


data = data.get_text().encode('utf-8')

f1 = open(write_file_path+text_file_name, "w+")
f1.write(data)
f1.close()

f.close()
