from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import MyForms, FormCompany, FormCompanyModels
# Create your views here.


def index(requests: HttpRequest):
    form = FormCompanyModels(requests.POST or None)
    if requests.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
        return HttpResponse('error')
    return render(requests, 'base.html', {'form': form})


# def data_form(requests: HttpRequest):
#     line = f"name = {requests.POST.get('name')} " \
#         f"surname = {requests.POST.get('surname')} " \
#         f"salary = {requests.POST.get('salary')} "
#     return HttpResponse(line)