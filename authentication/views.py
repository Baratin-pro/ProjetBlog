from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import View
from . import forms


class LoginView(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForms

    def get(self, request):
        form = self.form_class
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect(settings.LOGIN_REDIRECT_URL)
        message = f"Votre nom d'utilisateur et/ou votre mot de passe ne correspondent pas, veuillez réessayer."
        return render(request, self.template_name, context={'form': form, 'message': message})
