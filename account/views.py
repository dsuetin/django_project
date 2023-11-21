from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from .forms import RegistrationForm
from .token import account_activation_token
from django.http import HttpResponse


def account_register(request):

    # if request.user.is_authenticated:
    #     return redirect('/')
    print('account_register')
    if request.method == 'POST':
        print('account_register POST')
        registerForm = RegistrationForm(request.POST)
        print('account_register POST2')
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active = False
            user.save()
            # Setup email
            current_site = get_current_site(request)
            subject = 'Activate you Account'
            message = render_to_string('account/registration/account_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # 'token': account_activation_token.make_token(user),
            })
            print('message', message)
            user.email_user(subject=subject, message=message)
            return HttpResponse('register succesfully and activation sent')
        else:
            print('Error: registerForm is not valid')
    else:
        registerForm = RegistrationForm()
        return render(request, 'account/registration/register.html', {'form': registerForm})

