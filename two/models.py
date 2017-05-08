import datetime

from django.db import models




# сколько чего надо по тех. процессу
class NeedStruct(models.Model):
    equipment = models.ForeignKey('Equipment', blank=True, default=None)
    cnt = models.FloatField(default=0)
    completeCnt = models.FloatField(default=0)

    def __str__(self):
        return str(self.equipment) + " " + str(self.cnt)

class Equipment(models.Model):

    # название
    name = models.CharField(max_length=1000, default="")
    # единица измерения
    dimension = models.CharField(max_length=200, default="")
    # шифр
    code = models.CharField(max_length=100, blank=True, default="", null=True)
    # тип
    equipmentType = models.IntegerField(default=0)
    # кол-во по умолчанию
    cntDefault = models.FloatField(default=0)
    # константы оборудования
    needStruct = models.ManyToManyField(NeedStruct, blank=True, default=None,
                                        related_name="needStructStandartWork12")
    TYPE_EQUIPMENT = 0
    TYPE_MATERIAL = 1
    TYPE_DETAIL = 2
    TYPE_ASSEMBLY_UNIT = 3
    TYPE_STANDART_WORK = 4

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def generateDataFromNeedStructs(self, NeedEquipmentType):
        arr = []
        for ns in self.needStruct.all():
            if (ns.equipment != None) and (ns.equipment.equipmentType == NeedEquipmentType):
                arr.append({'equipment': ns.equipment,
                            'cnt': ns.cnt})

        return arr

    def addFromFormset(self, formset, doCrear=False):
        if (doCrear):
            for ns in self.needStruct.all():
                ns.delete()
            self.needStruct.clear()

        if formset.is_valid():
            for form in formset.forms:
                d = form.cleaned_data
                if (len(d) > 0) and \
                        (("equipment" in d) and (not d["equipment"] is None) and (d["equipment"] != self) or (
                                    ("standartWork" in d) and (not d["standartWork"] is None))):
                    print(d)
                    ns = NeedStruct.objects.create(**d)
                    ns.save()
                    self.needStruct.add(ns)


class MoveEquipment(models.Model):
    date = models.DateField(default=datetime.date.today)
    cnt = models.IntegerField(default=0)
    equipment = models.ForeignKey(Equipment)
    flgAcceptance = models.BooleanField(default=True)
    remainCnt = models.IntegerField(default=0)

    def __str__(self):
        return str(self.equipment) + ":" + str(self.cnt)
