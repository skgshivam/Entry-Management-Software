from django.shortcuts import render
from .models import Visitor, Host
from .forms import *
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime

# Create your views here.
def add_visitor(request):
    if request.method=="POST":
        form=Add_Visitor(request.POST)
        if form.is_valid():
            visitor_item=form.save(commit=False)
            host=form.cleaned_data.get("host")
            host_instance= get_object_or_404(Host, name=host)
            visitor_item.host=host_instance
            visitor_item.save()
            print(visitor_item.host.__dict__)
            context={
                'visitor':visitor_item,
                'host':visitor_item.host,
            }
            return render(request, 'visiting.html',context)
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


def end_visit(request,visitor_id):
    visitor = get_object_or_404(Visitor, pk=visitor_id)
    visitor.checkout_out_time=datetime.now()
    visitor.save()
    print(visitor.__init__)
    return render(request, 'checkout.html')

