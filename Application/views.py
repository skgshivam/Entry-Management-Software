from django.shortcuts import render
from .models import Visitor, Host
from .forms import *
# Create your views here.
def add_visitor(request):
    if request.method=="POST":
        form=Add_Visitor(request.POST)
        if form.is_valid():
            visitor_item=form.save(commit=False)
            visitor_item.save()
            print(visitor_item)
            return redirect('/profile/show_profile/'+str(profile_item.doctor_id))
    else:
        form=Add_Visitor(request.POST or None, request.FILES or None)
    return render(request,'new_file.html',{'form':form})

class HostAutocomplete(autocomplete.Select2QuerySetView):
    print('**')
    def get_queryset(self):
        qs = Host.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        print(qs)
        return qs    
