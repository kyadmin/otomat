#_*_ coding: UTF-8 _*_
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import  ConfigParser
class files_conf_ssh:
        def __init__(self,filename):
                self.filename = filename
                # 生产config 对象
                self.conf = ConfigParser.ConfigParser()
                # 用config对象读取配置文件
                self.conf.read(self.filename)
                # 以列表的形式返回section
                s = self.conf.sections()


        def username(self):
		o_user = self.conf.get("host_user","user_root")
		return o_user
	def address(self):
		o_address = self.conf.get("host_address","host")
		return o_address
	def password(self):
                # 得到指定的sections, options
                o_password = self.conf.get("host_password","password")
		return  o_password

class files_conf_check:
        def __init__(self,filename):
                self.filename = filename
                self.conf = ConfigParser.ConfigParser()
                self.conf.read(self.filename)
                s = self.conf.sections()
        def server_port(self):
                s_port = self.conf.get("server","port")
                return s_port
        def server_host(self):
                s_host = self.conf.get("server","host")
                return s_host
        def server_ip(self):
                s_ip = self.conf.get("server","my_ip")
                return s_ip
        def server_path(self):
                s_path = self.conf.get("server","report_path")
                return s_path
        def server_worker(self):
                s_worker = self.conf.get("server","worker")
                return s_worker

        def client_ip(self):
                c_ip = self.conf.get("client","my_ip")
                return c_ip
        def client_host(self):
                c_host = self.conf.get("client","host")
                return c_host
        def client_port(self):
                c_port = self.conf.get("client","port")
                return c_port
