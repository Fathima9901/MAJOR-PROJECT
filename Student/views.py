from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from .models import Register

# Create your views here.

def home(request):
    return render(request, 'Student/home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        DOB = request.POST['date_of_birth']
        print('first_name: ', first_name, '\nDOB: ', DOB)
        form = RegisterForm(request.POST)
        if form.is_valid():
            enrollment_no = form.cleaned_data['enrollment_no']
            print(enrollment_no)
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            date_of_birth = form.cleaned_data['date_of_birth']
            gender = form.cleaned_data['gender']
            branch = form.cleaned_data['branch']
            mail_id = form.cleaned_data['mail_id']
            college_mail = form.cleaned_data['college_mail']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            current_cgpa = form.cleaned_data['current_cgpa']
            tenth = form.cleaned_data['tenth']
            twelfth = form.cleaned_data['twelfth']
            address_name = form.cleaned_data['address_name']
            post_office = form.cleaned_data['post_office']
            city = form.cleaned_data['city']
            district = form.cleaned_data['district']
            pincode = form.cleaned_data['pincode']
            father_name = form.cleaned_data['father_name']
            mother_name = form.cleaned_data['mother_name']

            data = Register(enrollment_no=enrollment_no, first_name=first_name, middle_name=middle_name,
                            last_name=last_name, date_of_birth=DOB, gender=gender, branch=branch,
                            mail_id=mail_id, college_mail=college_mail, phone_number=phone_number,
                            password=password, current_cgpa=current_cgpa, tenth=tenth, twelfth=twelfth,
                            address_name=address_name, post_office=post_office, city=city, district=district,
                            pincode=pincode, father_name=father_name, mother_name=mother_name)
            data.save()
            print('inside if')
            return redirect('/')
        else:
            print('inner if not working')
            for field, errors in form.errors.items():
                print(field, errors)
            return HttpResponse(form.errors)
    else:
        print('outer else')
        form = RegisterForm()
    return render(request, 'Student/student_registration.html', {'form': form})


def sign_up(request):
    return render(request, 'Student/student_registration.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if Register.objects.filter(mail_id=email, password=password).exists():
            user = Register.objects.get(mail_id=email)
            request.session['email'] = email
            print(email)
            return redirect('student')
        error = "Credentials not match!.."
        return render(request, 'Student/login.html', {'error': error})
    else:
        return render(request, 'Student/login.html')


def student_dashboard(request):
    session = request.session.get('email')
    if session:
        return render(request, 'Student/student dashboard.html', {'session': session})
    else:
        return redirect('login')