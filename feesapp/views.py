from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from .models import FeesType, Student
from django.views.generic import View
from feesapp.utils import render_to_pdf #created in step 4


# Create your views here.

def index(request):
    if request:
        return render(request,'index.html')

def search_students(request):
    if request.method == "POST":
        admno_searched = request.POST.get("admno_for_search")
        name_searched = request.POST.get("name_for_search")
        class_searched = request.POST.get("class_for_search")
        section_searched = request.POST.get("section_for_search")
        students_all = Student.objects.all()
        
        if admno_searched:
            students = Student.objects.filter(admno__contains=admno_searched)
            return render(request, 'search_students.html',{'admno_searched':admno_searched,'students':students,'students_all':students_all})
        elif name_searched:
            students = Student.objects.filter(fname__contains=name_searched)
            return render(request, 'search_students.html',{'name_searched':name_searched,'students':students,'students_all':students_all})
        else:
            students = Student.objects.filter(class_student=class_searched , section=section_searched)
            return render(request, 'search_students.html',{'class_searched':class_searched,'section_searched':section_searched,'students':students,'students_all':students_all})
    
    else:
        students_all = Student.objects.all()
        return render(request,"search_students.html",{'students_all':students_all})

def fees_collection(request):
    if request.method =="POST":
        admno = request.POST.get("admno")
        students = Student.objects.filter(admno=admno)
        for student in students:
            class_fees_results = FeesType.objects.filter(class_fees=student.class_student)
        return render(request,"fees_collection.html",{'admno':admno,'students':students,'class_fees_results':class_fees_results})
    else:
        return render(request,"fees_collection.html")



def student_registeration(request):
    if request.method == 'POST':
        # name = request.POST.get('name','')
        admno = request.POST.get('admno','')
        roll = request.POST.get('roll','')
        class_student = request.POST.get('class_student','')
        section = request.POST.get('section','')
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        gender = request.POST.get('gender','')
        dob = request.POST.get('dob','')
        category = request.POST.get('category','')
        religion = request.POST.get('religion','')
        caste = request.POST.get('caste','')
        phno = request.POST.get('phno','')
        email = request.POST.get('email','')
        fathername = request.POST.get('fathername','')
        fatherphone = request.POST.get('fatherphone','')
        motherphone = request.POST.get('motherphone','')
        mothername = request.POST.get('mothername','')
        fatherocc = request.POST.get('fatherocc','')
        motherocc = request.POST.get('motherocc','')
        guardianphone = request.POST.get('guardianphone','')
        guardianname = request.POST.get('guardianname','')
        guardianemail = request.POST.get('guardianemail','')
        guardianrelation = request.POST.get('guardianrelation','')
        guardianocc = request.POST.get('guardianocc','')
        guardianadd = request.POST.get('guardianadd','')
        # if admno and roll and class_student and section and fname and lname and gender and dob and category and religion and caste and phno and email and fathername and fatherphone and motherphone and mothername and fatherocc and motherocc and guardianphone and guardianname and guardianemail and guardianrelation and guardianocc and guardianadd:
        if 1:
            student = Student(admno = admno,roll=roll , class_student=class_student,section=section,fname=fname,
            lname=lname,gender=gender,fathername=fathername,mothername=mothername,
            fatherocc=fatherocc,motherocc = motherocc,
            guardianphone=guardianphone,guardianname=guardianname,guardianemail=guardianemail,category=category,religion=religion,caste=caste,phno=phno,
            email=email,fatherphone=fatherphone,motherphone=motherphone,
            guardianrelation=guardianrelation,guardianocc=guardianocc,guardianadd=guardianadd)
            student.save()
        else:
            return HttpResponse("<alert>Please Enter All The Details</alert>")

    return render(request, 'student_registeration.html')


def invoice(request):
    if request.method == 'POST':
        admno = request.POST.get("admno")
       
        student = Student.objects.filter(admno__contains=admno).first()
        data = {
        'student':student 
        }
       
    pdf = render_to_pdf('pdf/invoice.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def adminpanel(request):
    if request.method == 'POST':
        feestype1 = request.POST.get('feestype','')
        class_fees = request.POST.get('class_fees','')
        fees_value = request.POST.get('fees_value','')
        class_fees_search = request.POST.get('class_fees_search','')
        if feestype1 and class_fees and fees_value:
            feestype = FeesType(feestype=feestype1, class_fees=class_fees,fees_value=fees_value)
            feestype.save()
            return render(request, 'adminpanel.html')

        elif class_fees_search:
            class_fees_results = FeesType.objects.filter(class_fees=class_fees_search)
            return render(request, 'adminpanel.html',{'class_fees_results':class_fees_results})
        else:
            return render(request, 'adminpanel.html')
    return render(request, 'adminpanel.html')

