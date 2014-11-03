from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
import traceback
import simplejson,datetime
import models

# Create your views here.
def index(request):
	return HttpResponse('hello world')

def passive(request):
	try:
		info = request.GET['req']
		print info
		remote_addr = request.META['REMOTE_ADDR']
		print 'remote_addr', remote_addr
		dict_info = simplejson.loads(info)
		cpu_info = dict_info['cpu']
		mem_info =  dict_info['mem']
		df_info = dict_info['df'] 
		dt = datetime.datetime.now()
		ip = models.IP.objects.get(ip=remote_addr)
		models.Item.objects.create(cpu_info=cpu_info,mem_info=mem_info,df_info=df_info,dt=dt,ip=ip)
		return HttpResponse('ok')
	except:
		print traceback.format_exc()
		return HttpResponse('error')  

def regip(request):
	try:
		ip = request.GET.get('ip')
		hostname = request.GET.get('hostname')
		models.IP.objects.create(ip=ip,hostname=hostname)
		print '%s\t%s saved' % (ip,hostname)
		return HttpResponse('%s saved' % ip)
	except:
		return HttpResponse('error') 

def regipbatch(request)
	try:
		json_req = request.GET.get('req')
		list_ip = simplejson.loads(json_req)
		for ip in list_ip:
			models.IP.objects.create(ip=ip[0],hostname=ip[1])
			len_ip += 1
			except:
				print traceback.format_exc()

		return HttpResponse('' % len_ip)







