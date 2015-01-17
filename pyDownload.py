#!/usr/bin/python

import urllib 
from optparse import OptionParser
import sys,os
cek = 0 
def main(url=None,x=1,y=1,formatFile=None):
    filenya = None 
    if url == None or formatFile == None :
	sys.exit()
    else :
        nameFolder = url.split("/")
	Daftar = os.listdir(".")
        for folder in Daftar :
		if folder == nameFolder[6] :
			cek = 1
	if cek != 1 :
		os.mkdir(nameFolder[6])

        while x <= y :
            if x < 10 :
               filenya = "00"+str(x)+"."+formatFile
            elif x < 100 :
               filenya = "0"+str(x)+"."+formatFile
            elif x < 100 :
              filenya = str(x)+"."+formatFile

            print "[Download] => "+url+filenya 
            urllib.urlretrieve(url+filenya,filenya) 
	    print "[Move ] => "+nameFolder[6]+filenya
	    os.system("mv "+str(filenya)+" "+str(nameFolder[6])+"/"+str(filenya))
            x += 1
	
if __name__ == "__main__": 
    Op = OptionParser(usage="%prog -u <arg> -s <arg> -e <arg> -f <arg> ")
    Op.add_option("-u","--url", dest="url",type=str,help="Alamat url yang ingin didownload")
    Op.add_option("-s","--start",dest="s",type=int,help="angka memulai")
    Op.add_option("-e","--end",dest="e",type=int,help="angka berakhir")
    Op.add_option("-f","--format",dest="formatfile",type=str,help="Format file yang didownloadnya")
    options, args = Op.parse_args()
    print "Start Program" 
    main(options.url, options.s, options.e, options.formatfile)
    print "End Program"
