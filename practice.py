import urllib.request as req
import urllib
def main():
	data=urllib.request.urlopen('http://www.baidu.com')
	print(data.getcode())
	print(data.geturl())
	data_read=data.read()
	fhandle=open("E:/1.html","wb")
	fhandle.write(data_read)
	#另一种方法
	req.urlcleanup()
	filename=req.urlretrieve("http://edu.51cto.com","E:/2.html")
if __name__ == '__main__':
    main()