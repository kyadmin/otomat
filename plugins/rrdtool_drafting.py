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
    def __init__(self,filename="/etc/otomat/otomat.cnf",graph=None,title="北京壹號車 系統報告"):
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
        self.title = title
        self.time = str(int(time.time()))
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
			'COMMENT:\\n',
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

if __name__ == "__main__":
	t = graph_rrdtool('/etc/otomat/otomat.cnf')
	t.graph_rrdtool()
