from django.shortcuts import redirect
from django.urls import resolve
from django.contrib.auth import get_user_model, login

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
     
        resolver_match = resolve(request.path)

       
        public_views = ['login', 'logout']

        if resolver_match.app_name == 'admin':
            return self.get_response(request)

        if not request.user.is_authenticated and resolver_match.url_name not in public_views:
            return redirect('login')

        return self.get_response(request)

class AdminAutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Autenticar automaticamente apenas no Django Admin
        if request.path.startswith('/admin'):
            User = get_user_model()
            admin_user = User.objects.filter(is_superuser=True).first()
            if admin_user and not request.user.is_authenticated:
                login(request, admin_user)
        return self.get_response(request)