from django.shortcuts import render
data = {}
data['branch'] = 'Civil Engineering'
# Create your views here.
def civil(request):
    return render(request,'branches/branch.html',data)

def civilRegulation(request,regulation):
    data['regulation'] = regulation.split('-')[1]
    return render(request,'branches/regulation.html',data)


def civilYear(request,regulation,year):
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

def civilSemester(request,regulation,year,semester):
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
