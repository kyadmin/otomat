from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Test(models.Model):
	t = models.CharField(max_length=20)

class IP(models.Model):
	ip = models.IPAddressField(unique=True)
	hostname = models.CharField(max_length=20)
        def __unicode__(self):
                return self.ip


class OpsUser(models.Model):
	user = models.OneToOneField(User)
#	user = models.ForeignKey(User,null=True)
	opsuser = models.CharField(max_length=20)
	opspassword = models.CharField(max_length=20)
	available = models.IntegerField()
	list_ip = models.ManyToManyField(IP)
	def __unicode__(self):
		return self.opsuser
class OpUser(models.Model):
        user = models.ForeignKey(User,null=True)
        opsuser = models.CharField(max_length=20)
        opspassword = models.CharField(max_length=20)
        available = models.IntegerField()
        list_ip = models.ManyToManyField(IP)
        def __unicode__(self):
                return self.opsuser

class Item(models.Model):
	cpu_info = models.CharField(max_length=2000)
	mem_info = models.CharField(max_length=2000)
	df_info = models.CharField(max_length=2000)
	dt = models.DateTimeField()
	ip = models.ForeignKey(IP)
	def __unicode__(self):
        	return '%s\t%s' % (self.ip,'item')
