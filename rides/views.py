from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ride
from .forms import RideForm, UpdateForm
from django.urls import reverse_lazy

# Create your views here.
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Ride
    template_name = 'home.html'

class RidesView(ListView):
    model = Ride
    template_name = 'rides.html'
    ordering = ['date', 'grade']

class RideDetailView(DetailView):
    model = Ride
    template_name = 'ride_details.html'

class AddRideView(CreateView):
    model = Ride
    form_class = RideForm
    template_name = 'add_ride.html'
    # when you are using the form_class the fields is deprciated in this class
    # fields = '__all__'
    # Or you could have add then individually as a tuple
    # fields = ('name', 'distance')

class UpdateRideView(UpdateView):
    model = Ride
    form_class = RideForm
    template_name = 'update_ride.html'
    #Again fields commented out as we have 
    #fields = ['name', 'distance', 'speed_mph']

class DeleteRideView(DeleteView):
    model = Ride
    template_name = 'delete_ride.html'
    success_url = reverse_lazy('rides')

class DuplicateRideView(UpdateView):
    model = Ride
    form_class = RideForm
    template_name = 'add_ride.html'

    def form_valid(self, form):
        obj = form.save(commit = False)
        obj.pk = None
        return super(DuplicateRideView, self).form_valid(form)