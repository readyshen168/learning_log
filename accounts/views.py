from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def index2(request):
    return render(request, 'accounts/index2.html')


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录，并重定向到主页
            login(request, new_user)
            return redirect('learning_logs:index')

    # 显示新表单或指出表单无效
    context = {'form': form}
    return render(request, 'registration/register.html', context)