from django.shortcuts import render,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (ListView
								 ,DetailView
								 ,CreateView
								 ,UpdateView
								 ,DeleteView)



# def home(request):
# 	context = {
# 		'posts': Post.objects.all()
# 	}

# 	return render(request,'blog/home.html',context)

# classviews for post
class PostListView(ListView):
	model = Post
	context_object_name = 'posts'
	ordering = ['-post_date']
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):
		user = get_object_or_404(User, username = self.kwargs.get('username'))
		return Post.objects.filter(author = user).order_by('-post_date')



class PostDetailView(DetailView):
	model = Post
	context_object_name = 'post'


class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	context_object_name = 'post'
	fields = ['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	context_object_name = 'post'
	fields = ['title','content']

	def form_valid(self,form):
		form.instance.author = self.request.user #setting the user currently logged in to  author of the post that ant to be updated
		return super().form_valid(form)

	#usertest
	def test_func(self): 
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	context_object_name = 'post'
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	return render(request,'blog/about.html',{'title': 'About'})