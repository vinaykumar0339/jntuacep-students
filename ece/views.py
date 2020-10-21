from django.shortcuts import render
from home.models import PdfUpload

data = {}
data['branch'] = 'Electronics and Communications Engineering'
# Create your views here.
def ece(request):
    return render(request,'branches/branch.html',data)

def eceRegulation(request,regulation):
    data['regulation'] = regulation.split('-')[1]
    return render(request,'branches/regulation.html',data)


def eceYear(request,regulation,year):
    data['regulation'] = regulation.split('-')[1]
    if year == 1:
        data['year'] = 'First Year'
    elif year == 2:
        data['year'] = 'Second Year'
    elif year == 3:
        data['year'] = 'Third Year'
    else:
        data['year'] = 'Fourth Year'
    return render(request,'branches/year.html',data)


def eceSemester(request,regulation,year,semester):
    data['regulation'] = regulation
    if year == 1:
        data['year'] = 'First Year'
        if semester == 1:
            data['semester'] = 'First Semester'
            pdfs = PdfUpload.objects.filter(branch='ece',regulation=regulation.lower(),year='firstyear',semester='firstsemester')
            subjects = []
            for pdf in pdfs:
                subjects.append(pdf.subject)
            data['subjects'] = set(subjects)
            data['pdfs'] = pdfs

        elif semester == 2:
            data['semester'] = 'Second Semester'
            pdfs = PdfUpload.objects.filter(branch='ece',regulation=regulation.lower(),year='firstyear',semester='secondsemester')
            subjects = []
            for pdf in pdfs:
                subjects.append(pdf.subject)
            data['subjects'] = set(subjects)
            data['pdfs'] = pdfs

    elif year == 2:
        data['year'] = 'Second Year'
        if semester == 1:
            data['semester'] = 'First Semester'
            pdfs = PdfUpload.objects.filter(branch='ece',regulation=regulation.lower(),year='secondyear',semester='firstsemester')
            subjects = []
            for pdf in pdfs:
                subjects.append(pdf.subject)
            data['subjects'] = set(subjects)
            data['pdfs'] = pdfs

        elif semester == 2:
            data['semester'] = 'Second Semester'
            pdfs = PdfUpload.objects.filter(branch='ece',regulation=regulation.lower(),year='secondyear',semester='secondsemester')
            subjects = []
            for pdf in pdfs:
                subjects.append(pdf.subject)
            data['subjects'] = set(subjects)
            data['pdfs'] = pdfs
    
    elif year == 3:
        data['year'] = 'Third Year'
        if semester == 1:
            data['semester'] = 'First Semester'
            pdfs = PdfUpload.objects.filter(branch='ece',regulation=regulation.lower(),year='thirdyear',semester='firstsemester')
            subjects = []
            for pdf in pdfs:
                subjects.append(pdf.subject)
            data['subjects'] = set(subjects)
            data['pdfs'] = pdfs

        elif semester == 2:
            data['semester'] = 'Second Semester'
            pdfs = PdfUpload.objects.filter(branch='ece',regulation=regulation.lower(),year='thirdyear',semester='secondsemester')
            subjects = []
            for pdf in pdfs:
                subjects.append(pdf.subject)
            data['subjects'] = set(subjects)
            data['pdfs'] = pdfs

    elif year == 4:
        data['year'] = 'Fourth Year'
        if semester == 1:
            data['semester'] = 'First Semester'
            pdfs = PdfUpload.objects.filter(branch='ece',regulation=regulation.lower(),year='fourthyear',semester='firstsemester')
            subjects = []
            for pdf in pdfs:
                subjects.append(pdf.subject)
            data['subjects'] = set(subjects)
            data['pdfs'] = pdfs

        elif semester == 2:
            data['semester'] = 'Second Semester'
            pdfs = PdfUpload.objects.filter(branch='ece',regulation=regulation.lower(),year='fourthyear',semester='secondsemester')
            subjects = []
            for pdf in pdfs:
                subjects.append(pdf.subject)
            data['subjects'] = set(subjects)
            data['pdfs'] = pdfs
    
    return render(request,'branches/subjects.html',data)
