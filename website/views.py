from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegistrationForm, AddRecordForm
from .models import Record
from django.views.generic import (  DetailView,
                                    DeleteView,
                                    CreateView,
                                    UpdateView
                                    )





def home(request):
    records = Record.objects.all()

    #check if logged in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome back {username}. It's nice to see you again!")
            return redirect('home')
        else:
            messages.info(request, "There was an error with your login information. Please try again.")
            return redirect('home')
    else: 
        return render(request, 'home.html', {'records': records})

#here i made a little mistake by naming function logout(same as built in function) so i got error maximum reccursion depth exceeded. Probably
#meaning that i can't name my custom function like built in function and then use built in function inside of it.
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully completed your registration.")
            return redirect('home')            
    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form":form})


# def customer_record(request, pk):
#     if request.user.is_authenticated:
#         customer_record = Record.objects.get(id=pk)
#         return render(request,'record.html', {'customer_record':customer_record})
#     else:
            # messages.warning(request, "You must be logged in to see this page!")
#         return redirect('home')

class CustomerRecordView(DetailView):
    model = Record 
    context_object_name = 'crecord'
    template_name = 'record.html'



class RecordDeleteView(DeleteView):
    model = Record 
    context_object_name = 'crecord'
    template_name = 'delete_record.html'
    success_url = reverse_lazy('home')


    def form_valid(self, form):
        messages.success(self.request, "Record deleted successfully.")
        return super().form_valid(form)
    #way to add popup msg with class based views.

class RecordAddView(CreateView):
    model = Record 
    form_class = AddRecordForm
    template_name = "add_record.html"
    
    def form_valid(self, form):
        messages.success(self.request, "Record created successfully.")
        return super().form_valid(form)
    

# def update_record(request, pk):
#     if request.user.is_authenticated:
#         current_record = Record.objects.get(id=pk)
#         form = AddRecordForm(request.POST or None, instance=current_record)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Record has been updated.")
#             return redirect('home')
        
#         return render(request, "update_record.html", {'form': form})
#     else:
#         messages.warning(request, "You must be logged in...")
#         return redirect('home')


class UpdateRecordView(UpdateView):
    model = Record 
    form_class = AddRecordForm
    context_object_name = 'crecord'
    template_name = "update_record.html"
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Record has been successfully updated.")
        return super().form_valid(form)