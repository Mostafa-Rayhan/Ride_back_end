from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, HelpForm, ProfileForm
from django.contrib.auth import authenticate, login
from .models import Review
from .models import Help
from .forms import ProfileForm
from .models import profileForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# Create your views here.

from django.contrib import messages
from django.views import View

def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User Created!!! ')
            # msg = 'user created'
            return redirect('login_view')
        else:
            # msg = 'form is not valid'
            messages.info(request, 'Username OR Password is incorrect')
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('/admin')
            elif user is not None and user.is_rider:
                login(request, user)
                messages.success(request, 'You login successfully!!! ')
                return redirect('home')

            elif user is not None and user.is_driver:
                login(request, user)
                messages.success(request, 'You login successfully!!! ')
                return redirect('home')

            else:
                # msg= 'invalid credentials'
                messages.info(request, 'Username OR Password is incorrect')
        else:
            # msg = 'error validating form'
            messages.info(request, 'error validating form')
    return render(request, 'login.html', {'form': form, 'msg': msg})

# @login_required(login_url='login')
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            current = request.POST["cpwd"]
            new_pas = request.POST["npwd"]

            user = User.objects.get(id=request.user.id)
            # un = user.username
            # check = user.check_password(current)
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Update Password successfully!!! ')
                return redirect('home')
        else:
            fm = PasswordChangeForm(user=request.user)
            context = {'form':fm}
            return render(request, "passwordChange.html", context)
    else:
        return redirect('login')

def forgotPass(request):
    context = {}
    if request.method == "POST":
        un = request.POST["username"]
        pwd = request.POST["npass"]

        user = get_object_or_404(User,username=un)
        user.set_password(pwd)
        user.save()

        login(request,user)
        if user.is_superuser:
            return redirect("/admin")
        else:
            return redirect("home")
        # context["status"] = "Password Changed Successfully!!!"

    return render(request, "Forget_Password.html", context)

def logout(request):
    return render(request, 'index.html')

def home(request):
    form = HelpForm
    if request.method == "POST":
        help = HelpForm(request.POST)
        if help.is_valid():
            help.save()
            messages.success(request, 'Comment successfully Submitted!!! ')
            return redirect("home")
    return render(request, 'home.html', {'form':form})

# def admin(request):
#     return render(request,'admin.html')


def rider(request):
    return render(request, 'home.html')


def driver(request):
    return render(request, 'home.html')

def settings(request):
    return render(request, "settings.html")

def ratting(request):
    return render(request, "ratting.html")

def wallet(request):
    return render(request, "wallet.html")

def profile(request):
    form = ProfileForm
    if request.method == "POST":
        pro = ProfileForm(request.POST)
        if pro.is_valid():
            pro.save()
            messages.success(request, 'Form Created successfully!!! ')
            return redirect("home")
    return render(request, "profile.html", {'form':form})

def review(request):
    if request.method == "GET":
        id = request.POST.get('id')
        comment = request.POST.get('comment')
        rate = request.POST.get('rate')
        user = account.models.User(username=username)
        Review(user=user, comment=comment, rate=rate, id=id).save()
        return redirect('home.html')
    return render(request, "ratting.html")



def profile_view(request):
    if request.method == "GET":
        data = profileForm.objects.all()
        context = {
            'data': data
        }
        # return redirect("profile_view")
        return render(request, "profileView.html", context)


#  def get(self, request):
#   form = ProfileForm()
#   candidates = profileForm.objects.all()
#   return render(request, 'profile.html', {'candidates':candidates, 'form':form})
#
#  def post(self, request):
#   form = ProfileForm(request.POST, request.FILES)
#   if form.is_valid():
#    form.save()
#    return render(request, 'profile.html', {'form':form})
#
# class CandidateView(View):
#  def get(self, request, pk):
#   candidate = profileForm.objects.get(pk=pk)
#   return render(request, 'candidate.html', {'candidate':candidate})





    # context = {}
    # data = profileForm.objects.get(user__id=request.user.id)
    # context["data"]=data
    # if request.method=="POST":
    #     # print(request.POST)
    #     fn = request.POST["fristName"]
    #     ln = request.POST["lastName"]
    #     em = request.POST["email"]
    #     phn = request.POST["phoneNumber"]
    #     ad = request.POST["address"]
    #     lc = request.POST["licence"]
    #     nid = request.POST["nidNo"]
    #     img = request.POST["photo"]
    #
    #     usr = User.objects.get(id=request.user.id)
    #     usr.email = em
    #     usr.save()
    #
    #     data.firstName = fn
    #     data.lastName = ln
    #     data.phoneNumber = phn
    #     data.address = ad
    #     data.licence = lc
    #     data.nidNo = nid
    #     data.photo = img
    #     data.save()
    #     if "images" in request.FILES:
    #         img = request.FILES["image"]
    #         data.photo = img
    #         data.save()
    #     context["status"] = "Changes Saved Successfully!!!"
    #
    # return render(request, "profile.html", context)



