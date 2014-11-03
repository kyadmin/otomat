from django.contrib import admin

# Register your models here.
import models

class ItemAdmin(admin.ModelAdmin):
	list_display = ('cpu_info','ip','dt')

admin.site.register(models.IP)
admin.site.register(models.OpsUser)
admin.site.register(models.Item,ItemAdmin)
admin.site.register(models.OpUser)
