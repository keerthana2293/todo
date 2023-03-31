from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import todoform
from . models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class tasklist(ListView):
    model = task
    template_name='home.html'
    context_object_name = 'task1'

class taskdetail(DetailView):
     model = task
     template_name ='details.html'
     context_object_name ='td'


class taskupdate(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name ='task'
    fields=('name','prority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class taskdelete(DeleteView):
    model=task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
# Create your views here.
def add(request):
    taskse=task.objects.all()
    if request.method == 'POST':
        name= request.POST.get('task','')
        prio= request.POST.get('priority','')
        date1=request.POST.get('date','')
        tasks = task(name=name,prority=prio,date=date1)
        tasks.save()

    return render(request,'home.html',{'task':taskse})

def delete(request,taskid):
    task1=task.objects.get(id=taskid)
    if request.method == 'POST':
        task1.delete()
        return redirect('/')
    return render (request,'delete.html')
def update(request,id):
    taskup=task.objects.get(id=id)
    fom=todoform(request.POST or None,instance=taskup )
    if fom.is_valid():
        fom.save()
        return redirect('/')
    return render(request,'edit.html',{'fo':fom,
                                       'td':taskup})
