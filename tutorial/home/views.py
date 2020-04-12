#from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.

#def home(request):
#    return HttpResponse('it works!')


# here we will be using cclass based views

from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from home.forms import HomeForm
from home.models import Post

class HomeView(TemplateView):
    template_name = 'home/home.html'


    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.all()
        
        args = {'form': form, 'posts': posts, 'users': users}
        return render(request, self.template_name, args)


    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # since we have mentioned one extra field user but we have not using it because we wanted the logged in user's name in that
            post.user = request.user
            post.save()
            
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect('home:home') # to avoid multiple submission we are just redirecting to home page 

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
