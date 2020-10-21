from django.shortcuts import render

data = {}
data['branch'] = 'Electrical and Electronics Engineering'
# Create your views here.
def eee(request):
    return render(request,'branches/branch.html',data)

def eeeRegulation(request,regulation):
    data['regulation'] = regulation.split('-')[1]
    return render(request,'branches/regulation.html',data)


def eeeYear(request,regulation,year):
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


def eeeSemester(request,regulation,year,semester):
    data = {}
    data['branch'] = 'Mechanical Engineering'
    if year == 1:
        data['year'] = 'First Year'
        if semester == 1:
            data['semester'] = 'First Semester'

        elif semester == 2:
            data['semester'] = 'Second Semester'

    elif year == 2:
        data['year'] = 'Second Year'
        if semester == 1:
            data['semester'] = 'First Semester'

        elif semester == 2:
            data['semester'] = 'Second Semester'
    
    elif year == 3:
        data['year'] = 'Third Year'
        if semester == 1:
            data['semester'] = 'First Semester'

        elif semester == 2:
            data['semester'] = 'Second Semester'

    elif year == 4:
        data['year'] = 'Fourth Year'
        if semester == 1:
            data['semester'] = 'First Semester'

        elif semester == 2:
            data['semester'] = 'Second Semester'
    
    return render(request,'branches/subjects.html',data)
