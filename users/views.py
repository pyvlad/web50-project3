from django.shortcuts import render
from .forms import RegistrationForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)          # create new user object but don't save
            user.set_password(form.cleaned_data['password'])    # set password
            user.save()                             # now save
            return render(request, 'users/register_done.html', {'user': user})
    else:
        form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})
