from django.shortcuts import render, redirect
from .models import Tenant
from .forms import TenantForm

def tenant_list(request):
    tenants = Tenant.objects.all()
    return render(request, 'rental/tenant_list.html', {'tenants': tenants})

def add_tenant(request):
    if request.method == 'POST':
        form = TenantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tenant_list')
    else:
        form = TenantForm()
    return render(request, 'rental/add_tenant.html', {'form': form})


