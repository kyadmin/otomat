#_*_ coding: UTF-8 _*_
import sys,time,os
reload(sys)
sys.setdefaultencoding('utf8')
import rrdtool
import random,datetime
import time,shutil
from otomat.conf import conf
from  otomat.logs  import log as logging

config =conf.otomat_conf('/etc/otomat/otomat.cnf')
logfile = config.report_log()
logdir = config.server_logdir()

if not os.path.exists(logdir):
        os.makedirs(logdir,0o755)

os.chdir(logdir)
logging.set_logger(filename =logfile, mode = 'a')

class graph_rrdtool:
    """
    rrdtool 绘图过程一共有四步：
    1.创建rrdtool数据库
    2.插入rrdtool所需的数据
    3.更新rrdtool数据库
    4.进行rrdtool绘图。
    """
    def __init__(self,filename="/etc/otomat/otomat.cnf",start_time="-1d"):
        self.filename = filename
	config = conf.otomat_conf(self.filename)
	self.host = config.rrdtool_host()
	self.rrdtool_dir = config.rrdtool_dir()
	# graph
	self.graph_cpu = config.graph_cpu()
	self.graph_mem = config.graph_mem()
	self.graph_disk = config.graph_disk()
	self.graph_network = config.graph_network()
        self.graph_login = config.graph_login() 
	self.graph_dir = config.graph_dir()
        #self.time = str(int(time.time()))
        self.time = start_time
	self.graph_list = [self.graph_cpu,self.graph_mem,self.graph_disk,self.graph_network,self.graph_login]
	
    def graph_rrdtool(self):
	host = self.host
	ISOFORMAT='%Y%m%d'
	today = datetime.date.today()
	today_dir = today.strftime(ISOFORMAT)
	date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	if not os.path.exists(self.graph_dir):
		os.mkdir(self.graph_dir)
	for i in list(host.split(',')):
		os.chdir(self.graph_dir)
		if not os.path.exists(i):
			os.mkdir(i)
		os.chdir(i)
		if not os.path.exists(today_dir):
			os.mkdir(today_dir)
	
	for j in list(host.split(',')):
		os.chdir(self.rrdtool_dir)
		os.chdir(j)
		#os.chdir(today_dir)
		### nic.png
		title = "Network Traffic Flow ("+date+")"
         	rrdtool.graphv(self.graph_network,'--start',"-1d",
			'--vertical-label=Bytes/s',
			'--x-grid','MINUTE:12:HOUR:1:HOUR:1:0:%H',
			'--width','650','--height','230',
			'--title',title,
            		'DEF:input=nic.rrd:input:AVERAGE',
            		'DEF:output=nic.rrd:output:AVERAGE',
            		'DEF:ine=nic.rrd:input_err:AVERAGE',
            		'DEF:oute=nic.rrd:output_err:AVERAGE',
            		'CDEF:inp=input,8,*',
            		'CDEF:inerr=ine,8,*',
            		'CDEF:outp=output,8,*',
            		'CDEF:outerr=oute,8,*',
            		'COMMENT:\\r',
            		'COMMENT:\\r',
			'AREA:inp#FFC125:Network Input',
            		'GPRINT:inp:LAST:Currnet\:%8.2lf %Sbps',
            		'GPRINT:inp:AVERAGE:Average\:%8.2lf %Sbps',
            		'GPRINT:inp:MAX:Maxnum\:%8.2lf %Sbps\\n',
			'LINE3:inerr#CD2626:Network Output',
            		'GPRINT:inerr:LAST:Currnet\:%8.2lf %Sbps',
            		'GPRINT:inerr:AVERAGE:Average\:%8.2lf %Sbps',
            		'GPRINT:inerr:MAX:Maxnum\:%8.2lf %Sbps\\n',
			'LINE3:outp#00FF00:Network Output',
			'GPRINT:outp:LAST:Current\:%8.2lf %Sbps',
            		'GPRINT:outp:AVERAGE:Average\:%8.2lf %Sbps',
            		'GPRINT:outp:MAX:Maxnum\:%8.2lf %Sbps\\n',
			'LINE3:outerr#0000FF:Network Out err',
            		'GPRINT:outerr:LAST:Current\:%8.2lf %Sbps',
            		'GPRINT:outerr:AVERAGE:Average\:%8.2lf %Sbps',
            		'GPRINT:outerr:MAX:Maxnum\:%8.2lf %Sbps\\n')

		if not os.path.exists(self.graph_network):
			logging.error('Network png not found. PNG file generated failure.')
		else:
			k = '/'
			dst = self.graph_dir+k+j+k+today_dir
			dst_file = dst+k+self.graph_network
			print dst_file
			if not os.path.exists(dst_file):
				shutil.move(self.graph_network,dst)
			else:
				logging.warning("Network png already exists.To be convered.")
				os.remove(dst_file)
				shutil.move(self.graph_network,dst)
			
		### cpu.png
		title = "CPU Utilzation rate  ("+date+")"
         	rrdtool.graphv(self.graph_cpu,'--start',"-1d",
			'--vertical-label=Bytes/s',
			'--x-grid','MINUTE:12:HOUR:1:HOUR:1:0:%H',
			'--width','650','--height','230',
			'--title',title,
            		'DEF:a=cpu.rrd:cpu_loadavg_1:AVERAGE',
            		'DEF:b=cpu.rrd:cpu_loadavg_5:AVERAGE',
            		'DEF:c=cpu.rrd:cpu_loadavg_15:AVERAGE',
			'DEF:user=cpu.rrd:cpu_user:AVERAGE', 
			'DEF:nic=cpu.rrd:cpu_nice:AVERAGE',
			'DEF:system=cpu.rrd:cpu_system:AVERAGE',
			'DEF:iowait=cpu.rrd:cpu_iowait:AVERAGE',
			'DEF:steal=cpu.rrd:cpu_steal:AVERAGE',
			'DEF:idel=cpu.rrd:cpu_idel:AVERAGE',
			'COMMENT:\\r',
			'COMMENT:\\r',
			'LINE3:a#FFC125:Loadavg 1',
			'GPRINT:a:LAST:Currnet\:%8.2lf %s',
			'GPRINT:a:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:a:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:b#EE7600:Loadavg 5',
			'GPRINT:b:LAST:Currnet\:%8.2lf %s',
			'GPRINT:b:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:b:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:c#FF0000:Loadavg 15',
			'GPRINT:c:LAST:Currnet\:%8.2lf %s',
			'GPRINT:c:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:c:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:user#0000FF:CPU User', 
			'GPRINT:user:LAST:Currnet\:%8.2lf %s',
			'GPRINT:user:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:user:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:nic#9AC0CD:CPU Nice',
			'GPRINT:nic:LAST:Currnet\:%8.2lf %s',
			'GPRINT:nic:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:nic:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:system#9A32CD:CPU System', 
			'GPRINT:system:LAST:Currnet\:%8.2lf %s',
			'GPRINT:system:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:system:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:iowait#999999:CPU Iowait',
			'GPRINT:iowait:LAST:Currnet\:%8.2lf %s',
			'GPRINT:iowait:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:iowait:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:steal#9AC0CD:CPU Steal',
			'GPRINT:steal:LAST:Currnet\:%8.2lf %s',
			'GPRINT:steal:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:steal:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:idel#00CD00:CPU Idel',
			'GPRINT:idel:LAST:Currnet\:%8.2lf %s',
			'GPRINT:idel:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:idel:MAX:Maximum\:%8.2lf %s\\n')

		if not os.path.exists(self.graph_cpu):
			logging.error('CPU png not found. PNG file generated failure.')
		else:
			k = '/'
			dst = self.graph_dir+k+j+k+today_dir
			dst_file = dst+k+self.graph_cpu
			print dst
			print dst_file
			if not os.path.exists(dst_file):
				shutil.move(self.graph_cpu,dst)
			else:
				logging.warning("CPU png already exists.To be convered.")
				os.remove(dst_file)
				shutil.move(self.graph_cpu,dst)
		
		
		### mem.png
		title = "Mem Utilzation   ("+date+")"
         	rrdtool.graphv(self.graph_mem,'--start',"-1d",
			'--vertical-label=Bytes',
			'--x-grid','MINUTE:12:HOUR:1:HOUR:1:0:%H',
			'--width','650','--height','230',
			'--title',title,
			'DEF:memtotal=mem.rrd:mem_total:AVERAGE',
			'DEF:memfreed=mem.rrd:mem_freed:AVERAGE',
			'DEF:memused=mem.rrd:mem_used:AVERAGE',
			'DEF:buffersfreed=mem.rrd:mem_buffers_freed:AVERAGE',
			'DEF:buffersused=mem.rrd:mem_buffers_used:AVERAGE',
			'DEF:mempercent=mem.rrd:mem_used_percent:AVERAGE',
			'DEF:swaptotal=mem.rrd:swap_total:AVERAGE',
			'DEF:swapfreed=mem.rrd:swap_freed:AVERAGE',
			'DEF:swapused=mem.rrd:swap_used:AVERAGE',
			'DEF:swappercent=mem.rrd:swap_used_percnet:AVERAGE',
			'COMMENT:\\r',
			'COMMENT:\\r',
			'LINE3:memtotal#FFC125:Mem Total',
			'GPRINT:memtotal:LAST:Currnet\:%8.2lf %s',
			'GPRINT:memtotal:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:memtotal:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:memused#CD2626:Mem Used',
			'GPRINT:memused:LAST:Currnet\:%8.2lf %s',
			'GPRINT:memused:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:memused:MAX:Maximum\:%8.2lf %s\\n',
			'LINE2:memfreed#00FF00:Mem Freed',
			'GPRINT:memfreed:LAST:Currnet\:%8.2lf %s',
			'GPRINT:memfreed:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:memfreed:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:buffersfreed#0000FF:Mem Buffers Freed',
			'GPRINT:buffersfreed:LAST:Currnet\:%8.2lf %s',
			'GPRINT:buffersfreed:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:buffersfreed:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:buffersused#EEEE00:Mem Buffers Used',
			'GPRINT:buffersused:LAST:Currnet\:%8.2lf %s',
			'GPRINT:buffersused:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:buffersused:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:mempercent#EE9A49:Mem Used Percent',
			'GPRINT:mempercent:LAST:Currnet\:%8.2lf %s',
			'GPRINT:mempercent:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:mempercent:MAX:Maximum\:%8.2lf %s\\n', 
			'LINE3:swaptotal#B4EEB4:SWAP Total',
			'GPRINT:swaptotal:LAST:Currnet\:%8.2lf %s',
			'GPRINT:swaptotal:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:swaptotal:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:swapfreed#B4EEB4:SWAP Freed',
			'GPRINT:swapfreed:LAST:Currnet\:%8.2lf %s',
			'GPRINT:swapfreed:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:swapfreed:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:swapused#B4EEB4:SWAP Used',
			'GPRINT:swapused:LAST:Currnet\:%8.2lf %s',
			'GPRINT:swapused:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:swapused:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:swappercent#AAAAAA:SWAP Used Percent',
			'GPRINT:swappercent:LAST:Currnet\:%8.2lf %s',
			'GPRINT:swappercent:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:swappercent:MAX:Maximum\:%8.2lf %s\\n')


		if not os.path.exists(self.graph_mem):
			logging.error('MEM png not found. PNG file generated failure.')
		else:
			k = '/'
			dst = self.graph_dir+k+j+k+today_dir
			dst_file = dst+k+self.graph_mem
			print dst
			print dst_file
			if not os.path.exists(dst_file):
				shutil.move(self.graph_mem,dst)
			else:
				logging.warning("MEM png already exists.To be convered.")
				os.remove(dst_file)
				shutil.move(self.graph_mem,dst)

		### disk.png
		title = "Disk Utilzation   ("+date+")"
         	rrdtool.graphv(self.graph_disk,'--start',"-1d",
			'--vertical-label=Bytes',
			'--x-grid','MINUTE:12:HOUR:1:HOUR:1:0:%H',
			'--width','650','--height','230',
			'--title',title,
			'DEF:percent=disk.rrd:disk_used_percnet:AVERAGE',
			'DEF:used=disk.rrd:disk_used:AVERAGE',
			'DEF:freed=disk.rrd:disk_freed:AVERAGE',
			'DEF:total=disk.rrd:disk_total:AVERAGE',
			'COMMENT:\\r',
			'COMMENT:\\r',
			'AREA:percent#FFC125:Percent',
			'GPRINT:percent:LAST:Currnet\:%8.2lf %s',
			'GPRINT:percent:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:percent:MAX:Maximum\:%8.2lf %s\\n',
			'AREA:used#CD2626:Used',
			'GPRINT:used:LAST:Currnet\:%8.2lf %s',
			'GPRINT:used:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:used:MAX:Maximum\:%8.2lf %s\\n',
			'LINE2:freed#00FF00:Freed',
			'GPRINT:freed:LAST:Currnet\:%8.2lf %s',
			'GPRINT:freed:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:freed:MAX:Maximum\:%8.2lf %s\\n',
			'LINE3:total#0000FF:Total',
			'GPRINT:total:LAST:Currnet\:%8.2lf %s',
			'GPRINT:total:AVERAGE:Average\:%8.2lf %s',
			'GPRINT:total:MAX:Maximum\:%8.2lf %s\\n')

		if not os.path.exists(self.graph_disk):
			logging.error('DISK png not found. PNG file generated failure.')
		else:
			k = '/'
			dst = self.graph_dir+k+j+k+today_dir
			dst_file = dst+k+self.graph_disk
			print dst
			print dst_file
			if not os.path.exists(dst_file):
				shutil.move(self.graph_disk,dst)
			else:
				logging.warning("DISK png already exists.To be convered.")
				os.remove(dst_file)
				shutil.move(self.graph_disk,dst)

		### login_user.png
		title = "Lonin User Num   ("+date+")"
         	rrdtool.graphv(self.graph_login,'--start',"-1d",
			'--vertical-label=Bytes',
			'--x-grid','MINUTE:12:HOUR:1:HOUR:1:0:%H',
			'--width','650','--height','230',
			'--title',title,
			'DEF:o=login_user.rrd:login_user_num:AVERAGE',
			'COMMENT:\\r',
			'COMMENT:\\r',
			'AREA:o#00FF00:Users',
			'COMMENT: ',
			'GPRINT:o:LAST:Currnet\:%8.0lf',
			'COMMENT: ',
			'GPRINT:o:AVERAGE:Avg login user num\:%8.0lf',
			'COMMENT: ',
			'GPRINT:o:MAX:Maximum\:%8.0lf\\n')


		if not os.path.exists(self.graph_login):
			logging.error('login png not found. PNG file generated failure.')
		else:
			k = '/'
			dst = self.graph_dir+k+j+k+today_dir
			dst_file = dst+k+self.graph_login
			print dst
			print dst_file
			if not os.path.exists(dst_file):
				shutil.move(self.graph_login,dst)
			else:
				logging.warning("Login png already exists.To be convered.")
				os.remove(dst_file)
				shutil.move(self.graph_login,dst)
