import subprocess,re
import time
import logging
import commands
import urllib2,simplejson

def passivesend(url='http://172.16.209.111:8080/monitor/passive?'):
	dictres = run()
	url = url+'?req=%s' % urllib2.quote(simplejson.dumps(dictres))
	res = urllib2.urlopen(url).read()
	if res == 'ok':
		print 'send ok'
	else:
		print 'send error'

def run():
	cpu_info = getcpu()
	mem_info = getmem()
	df_info = getdf()
	#now = time.now()
	return {'cpu':cpu_info,'mem':mem_info,'df':df_info}
	
def getostip():
	pass

def getcpu():
	buf = commands.getstatusoutput('uptime')
	cpu_load = re.search(r'load average:(.*?)',buf[1])
	if cpu_load:
		print cpu_load.groups('\n')
	return '0.0'
	
def getmem():
	mem_info = commands.getstatusoutput('free -m')
	res = mem_info[1].split('\n')[2]
	res = res.split(':')[-1].strip()
	list_res = res.split()
	print list_res
	return list_res

def getdf():
	return 'df'	

if __name__=="__main__":
	run()	
