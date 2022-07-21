from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.
from django.http import HttpResponse
from .models import Racquet
from .forms import RestringForm

# Define the home view
def home(request):
    # return HttpResponse('<h1> Hello Tennis Nerds! </h1>')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def racquets_index(request):
  racquets = Racquet.objects.all()
  return render(request, 'racquets/index.html', { 'racquets': racquets })

def racquets_detail(request, racquet_id):
  racquet = Racquet.objects.get(id=racquet_id)
  restring_form = RestringForm()
  return render(request, 'racquets/detail.html', { 
    'racquet': racquet, 'restring_form': restring_form 
    })

def add_restring(request, racquet_id):
      # create a ModelForm instance using the data in request.POST
  form = RestringForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_restring = form.save(commit=False)
    new_restring.racquet_id = racquet_id
    new_restring.save()
  return redirect('detail', racquet_id=racquet_id)   

class RacquetCreate(CreateView):
  model = Racquet
  fields = '__all__'
  success_url = '/racquets/'

class RacquetUpdate(UpdateView,):
  model = Racquet
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['brand', 'description']
  

class RacquetDelete(DeleteView):
  model = Racquet
  success_url = '/racquets/'