from django.shortcuts import render
from .models import Register, PdfUpload
from django.contrib import messages
from .password import password_hack, password_decrypt
from decimal import Decimal,ROUND_DOWN
import requests
from bs4 import BeautifulSoup
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
def home(request):
    user_data = {}
    if request.method == 'POST':
        roll_number = request.POST['roll_number']
        password = request.POST['password']

        # roll number converting into uppercase
        roll_number = roll_number.upper()

        # decryipting the password
        try:
            user = Register.objects.get(roll_number=roll_number)
            if password_decrypt(password,user.password):
                request.session['username'] = user.username
                request.session['roll_number'] = user.roll_number
                return render(request,'index.html')
            else:
                user_data['error'] = True
                return render(request,'accounts/signin.html',user_data)
        except Register.DoesNotExist:
            user_data['user_exits'] = roll_number
            return render(request,'accounts/signin.html',user_data)
    return render(request,'index.html')

def signup(request):
    return render(request,'accounts/signup.html')

def signin(request):
    user_data = {}
    if request.method == 'POST':
        roll_number = request.POST['roll_number']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        #hashing the password
        password = password_hack(password)
        # roll number converting into uppercase
        roll_number = roll_number.upper()

        try:
            Register.objects.get(roll_number=roll_number)
            user_data['user_exits'] = roll_number
            return render(request,'accounts/signup.html',user_data)
            
                
        except Register.DoesNotExist:
            user = Register(roll_number=roll_number,username=username,email=email,password=password)
            user.save()
            user_data['username'] = username
            

        
    return render(request,'accounts/signin.html',user_data)

def logout(request):
    del request.session['roll_number']
    del request.session['username']
    return render(request,'index.html')

def contactUs(request):
    return render(request,'contactus/contactus.html')

def results(request):
    roll_no = request.POST.get('roll_no')
    dob = request.POST.get('dob')
    sem = request.POST.get('semester')
    grades = {
        'S' : 10,
        'A++' : 9.5,
        'A+' : 9,
        'A' : 8.5,
        'B++' : 8,
        'B+' : 7.5,
        'B' : 7,
        'C++' : 6.5,
        'C+' : 6,
        'C' : 5.5,
        'D' : 5,
        'E' : 4.5,
        'F' : 0,
        'Ab' : 0
    }

    final_result = {}

    try:
        url = "https://jntuacep.ac.in/results/"+sem
        portal = requests.post(url,data={'roll_no':roll_no,'dob':dob})
        soup = BeautifulSoup(portal.content,'lxml')
        result = soup.find('section',{'id':"printResults"})
        # semester name
        semester = result.h6.text
        final_result['semester'] = semester

        # basic info
        basic_info = result.find_all('span')
        for index, tag in enumerate(basic_info):
            if (index == 1):
                final_result['hall_ticket'] = tag.b.text
            if (index == 3):
                final_result['student_name'] = tag.b.text
            if (index == 5):
                final_result['dob'] = tag.b.text

        # column names
        column = result.find_all('th')
        final_result['column_names'] = [] 
        for i in column:
            final_result['column_names'].append(i.text)

            
        # result data
        data = result.find('tbody').find_all('td')
        final_result['data'] = {}
        count = 1
        for i,d in enumerate(data):
            if i%6 == 0:
                sub = 'subject' + str(count)
                count = count + 1
                final_result['data'][sub] = []
            if '\r\n' in d.text or '\r' in d.text:
                final_result['data'][sub].append(d.text[0])
            else:
                final_result['data'][sub].append(d.text) 
        
        for sub in final_result['data']:
            score = final_result['data'][sub][4]
            final_result['data'][sub].append(grades[score])

        # total credits
        credits = []
        for sub in final_result['data']:
            credits.append(int(final_result['data'][sub][5]))


        # pass or fail 
        fail = 0
        absent = 0
        for sub in final_result['data']:
            f = final_result['data'][sub][3]
            ab = final_result['data'][sub][4]
            if f == 'F':
                fail += 1
            if ab == 'Ab':
                absent += 1

        final_result['fail'] = fail
        final_result['absent'] = absent

        sgpa = 0
        for sub in final_result['data']:
            sgpa += (float(final_result['data'][sub][5]) * float(final_result['data'][sub][6]))
            
        final_result['sgpa'] = Decimal(sgpa/sum(credits)).quantize(Decimal('.001'), rounding=ROUND_DOWN)
    except:
        pass
        
    return render(request,'results/result.html',context=final_result)

def profile(request):
    user_data = {}
    try:
        username = request.session['username']
        roll_number = request.session['roll_number']
        user = Register.objects.get(roll_number=roll_number)
        user_data['username'] = username
        user_data['roll_number'] = roll_number
        user_data['email'] = user.email

    except:
        user_data['need_login'] = True
        return render(request,'accounts/signin.html',user_data)

    return render(request,'profile/profile.html',user_data)


def pdfUpload(request):
    user_data = {}
    # to check the user login
    try:
        request.session['roll_number']

    except:
        user_data['need_login'] = True
        return render(request,'accounts/signin.html',user_data)


    if request.method == 'POST':
        branch = request.POST['branch']
        regulation = request.POST['regulation']
        year = request.POST['year']
        semester = request.POST['semester']
        subject = request.POST['subject']
        file = request.FILES['pdf']


        file_path = branch + '/' + regulation + '/' + year + '/' + semester + '/' + subject.lower() +'/' +  file.name
        if os.path.exists("media/" + file_path):
            user_data['file_exists'] = True
            user_data['file_url']= "media/" + file_path

        else:
            fs = FileSystemStorage()
            file_name = fs.save(file_path,file)
            user_data['filename'] = file.name
            user_data['file_exits'] = False
            
            # upload to database to retrive
            book = PdfUpload(branch=branch,
                            regulation=regulation,
                            year=year,
                            semester=semester,
                            subject=subject,
                            file_path=file_name,
                            file_name=str(file),
                            uploaded_by=request.session['username'] + ' ('+ request.session['roll_number'] + ')')
            book.save()


    return render(request,'uploads/pdf_uploads.html',user_data)