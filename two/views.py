from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.


# редактировать оборудование
from two.forms import MoveEquipmentForm, MoveMaterialForm, MoveDetailForm, EquipmentForm
from two.models import Equipment

def subdict(form,keyset):
    return dict((k, form.cleaned_data[k]) for k in keyset)


def index(request):

    c = {'eqs':Equipment.objects.all()
    }
    return render(request, "two/index.html", c)

def detail(request,equipment_id):
    MaterialFormset = formset_factory(MoveMaterialForm)
    DetailFormset = formset_factory(MoveDetailForm)

    eq = Equipment.objects.get(pk=equipment_id)

    if request.method == 'POST':
        material_formset = MaterialFormset(request.POST, request.FILES, prefix='material')
        detail_formset = DetailFormset(request.POST, request.FILES, prefix='detail')
        eq.addFromFormset(material_formset)
        eq.addFromFormset(detail_formset)
        return HttpResponseRedirect('/')

    c = {'material_formset': MaterialFormset(initial=eq.generateDataFromNeedStructs(
            NeedEquipmentType=Equipment.TYPE_MATERIAL), prefix='material'),
        'detail_formset': DetailFormset(initial=eq.generateDataFromNeedStructs(
            NeedEquipmentType=Equipment.TYPE_DETAIL), prefix='detail', ),
    }
    return render(request, "two/detail.html", c)
