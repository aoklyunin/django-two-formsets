from django.contrib import admin

# Register your models here.
from two.models import Equipment, MoveEquipment, NeedStruct

admin.site.register(Equipment)
admin.site.register(MoveEquipment)
admin.site.register(NeedStruct)
