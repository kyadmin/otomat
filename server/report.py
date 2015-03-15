#_*_ coding: UTF-8 _*_
import sys,time,os
reload(sys)
sys.setdefaultencoding('utf8')
import time
from otomat.conf import conf
from  otomat.logs  import log as logging
from  otomat.plugins  import rrdtool_data_collector
from  otomat.plugins  import rrdtool_drafting

config =conf.otomat_conf('/etc/otomat/otomat.cnf')
logfile = config.report_log()
logdir = config.server_logdir()

if not os.path.exists(logdir):
        os.makedirs(logdir,0o755)

os.chdir(logdir)
logging.set_logger(filename =logfile, mode = 'a')

def main(argv=sys.argv[1:]):
	t = rrdtool_data_collector.rrdtool_collector(argv)
	logging.info(("The otomat-report-server has been launched successfully !!!"))
	while True:
		t.rrdb()
		t.rrdb_update()
		time.sleep(300)
		continue
if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
