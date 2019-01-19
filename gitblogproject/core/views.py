from django.shortcuts import render
from core.models import Post
from django.core.paginator import Paginator

def home(request):
	return render(request, 'core/index.html')

def lista(request):
	#lista = Post.objects.all().order_by('-id')
	lista = Post.objects.all()
	paginator = Paginator(lista, 3)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request,'core/lista.html',{'posts': posts,'lista_post': posts})
	#return render(request,'core/lista.html',{'lista_post': posts})
