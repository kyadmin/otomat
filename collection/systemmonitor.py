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
        disk_io = psutil.disk_io_counters("/")
        disk_usage = psutil.disk_usage("/")
        return disk,disk_io,disk_usage
    def network_info(self):
        network_io = psutil.net_io_counters(pernic=True)
        return network_io
