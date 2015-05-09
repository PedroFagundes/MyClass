from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Areas

# Create your views here.
class AreaListView(ListView):
    model = Areas
    fields = '__all__'
    context_object_name = 'areas'
    template_name = 'areas/areas_list.html'


class AreaCreateView(CreateView):
    model = Areas
    fields = '__all__'
    success_url = reverse_lazy('areas_list')


class AreaUpdateView(UpdateView):
    model = Areas
    fields = '__all__'
    success_url = reverse_lazy('areas_list')



#######################
#					  #
# D E P R E C A T E D #
#                     #
#######################

# def nova(request, id=None):
# 	form = FormArea()

# 	dados = {}
# 	dados['form'] = form

# 	return render(request, 'areas/nova_area.html', dados)

# def salvar(request, id=None):
# 	form = FormArea(request.POST or None)
# 	if form.is_valid():
# 		area = form.save(commit=False)
# 		if id not in (None, '0'):
# 			area.id = id
# 			area.save()
# 			return render(request, 'areas/sucesso_editar_area.html')
# 		area.save()

# 		return render(request, 'areas/sucesso_cadastrar_area.html')

# def editar(request, area_id):
# 	area = get_object_or_404(Areas, pk=area_id)
# 	form = FormArea(instance=area)

# 	dados = {}
# 	dados['area'] = area
# 	dados['form'] = form
# 	return render(request, 'areas/editar_area.html', dados)

# def lista(request):
# 	areas = Areas.objects.all()

# 	dados = {}
# 	dados['areas'] = areas

# 	return render(request, 'areas/lista_areas.html', dados)

# def excluir(request, area_id):
# 	area = get_object_or_404(Areas, pk=area_id)

# 	area.delete()

# 	dados = {}
# 	dados['area'] = area

# 	return render(request, 'areas/sucesso_excluir_area.html')

##############################
#							 #
# E N D  D E P R E C A T E D #
#                            #
##############################