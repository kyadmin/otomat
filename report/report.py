#_*_ coding: UTF-8 _*_
import sys,time
reload(sys)
sys.setdefaultencoding('utf8')
import rrdtool

class graph_create:
    def __init__(self,filename="default.rrd",insert=None,graph=default.png,title="北京壹號車 系統報告"):
        self.filename = filename
        self.insert = insert
        self.graph = graph
        self.title = title
        self.time = time.time()
    def rrdb (self):
        '''
        创建rrdtool的数据库.
        '''
        db = rrdtool.create(self.filename,'--step','300','--start',self.time,
        'DS:input:GAUGE:600:U:U',
        'DS:output:GAUGE:600:U:U',
        'RRA:LAST:0.5:1:600',
        'RRA:AVERAGE:0.5:5:600',
        'RRA:MAX:0.5:5:600',
        'RRA:MIN:0.5:5:600')
        if db:
            print rrdtool.error()
    def rrdtool_insert(self):
        for keys in self.insert:
            sent = self.insert[keys][0]
            recv = self.insert[keys][1]
            up = rrdtool.updatev(self.filename,'N:%d:%d' % (sent,recv))
            print up
    def rrdtool_graph(self):
         rrdtool.graph(self.graph,'--start',self.time,
            '--title',self.title,
            '--vertical-label','bits',
            'DEF:input=rest.rrd:input:LAST',
            'DEF:output=rest.rrd:output:LAST',
            'LINE1:input#0000FF:In traffic',
            'LINE1:output#00FF00:Out traffic\\r',
            'CDEF:bytes_in=input,8,*',
            'CDEF:bytes_out=output,8,*',
            'COMMENT:\\n',
            'GPRINT:bytes_in:LAST:LAST in traffic\: %6.2lf %Sbps',
            'COMMENT:  ',
            'GPRINT:bytes_out:LAST:LAST out traffic\: %6.2lf %Sbps')  
