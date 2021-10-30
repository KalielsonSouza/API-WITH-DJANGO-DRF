from django.shortcuts import render
from .resources import PersonResource
from django.contrib import messages
from tablib import Dataset
from .models import Person
from datetime import datetime
from datetime import date

def ageCalculate(bornDate):
    currentDate = date.today()
    age = currentDate.year - bornDate.year -((currentDate.month, currentDate.day) < (bornDate.month, bornDate.day))
    return age

def simple_upload(request):
    if request.method == 'POST':
        personResource = PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']
        if not new_person.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'templates/upload.html')
        imported_data = dataset.load(new_person.read(),format='xlsx')
        for data in imported_data:
            bornDate = datetime.fromtimestamp(data[7]).strftime('%Y-%m-%d')
            value = Person(
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                bornDate,
                data[8],
                data[9],
                data[10],
                data[11],
                ageCalculate(datetime.fromtimestamp(data[7])),
            )
            value.save()
    return render(request,'index.html')
