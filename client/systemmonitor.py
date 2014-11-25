#_*_ coding: UTF-8 _*_
import sys,os
import psutil
reload(sys)
sys.setdefaultencoding('utf8')


class Monitor_systeminfo:
    def __init__(self):
        pass
    def Mem_info(self):
        mem = psutil.virtual_memory()
        print '內存总数: % s ;内存空闲 %s,' % (mem.total,mem.free)
        swap = psutil.swap_memory()
        print "swap总数 : %s;swap空闲: %s" % (swap.total,swap.free)
    def Cpu_info(self):
        cpu = psutil.cpu_times()
        print "User使用的cputimes详细信息: %s;\n Iowait的cputimes详细信息: %s;\nSystem使用的cputimes详细信息: %s;\nCPU的idel详细信息: %s\n" % (cpu.user,cpu.iowait,cpu.system,cpu.idle)
    def disk_info(self):
        disk = psutil.disk_partitions()
	print "服务器的磁盘分区: %s" % str(disk)
        disk_io = psutil.disk_io_counters("/")
	print "服务器的磁盘IO: %s" % str(disk_io)
        disk_usage = psutil.disk_usage("/")
	print "服务器的磁盘使用: %s" % str(disk_usage)
        #return disk,disk_io,disk_usage
    def network_info(self):
        network_io = psutil.network_io_counters(pernic=True)
	print "服务器网络IO: %s" %  str(network_io)
        #return network_io
if __name__ == "__main__":
	m = Monitor_systeminfo()
	print  m.Mem_info()
	print  m.Cpu_info()
	print  m.network_info()
	print  m.disk_info()
	
