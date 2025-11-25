from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

#docstrings """ """-> documentation for any coding part (functions, classes, interfaces,etc)

class PostListView(ListView): #ListView is a GET request
    """
    PostListView retrieves all objects from the posts table in the database
    """
    # template_name renders a specific html file
    template_name = "posts/list.html"

    # model attribute lest Django know from which table (model) we want to retrieve the data
    model = Post

    #context_object_name attribute allows us to change the variable where all the data is stored
    context_object_name = "posts"

class PostDetailView(DetailView): #DetailView is a GET request
    """
    PostListView retrieves one object from the posts table in the database
    """
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView): #CreateView is a POST request
    """
    Render a from with the specified fields to create a new post object 
    """
    template_name = "posts/new.html"
    model = Post
    #fields attribute is a list and lets us enable/disable the inputs to render in the html form and depends on the model
    fields = ["title", "subtitle", "body", "image"]

    def form_valid(self, form):
        print(form.data)
        # print(form.instance)
        print(User.objects.all())
        form.instance.author = User.objects.filter(is_superuser=True).first()
        return super().form_valid(form)

class PostUpdateView(UpdateView): 
    """
    Render a form that will allow the user to update certain fields of their post
    """
    template_name = "posts/update.html"
    context_object_name = "single_post"
    model = Post
    fields = ["title", "subtitle", "body", "image"]

class PostDeleteView(DeleteView):
    """
    View used to delete a post
    """
    template_name = "posts/delete.html"
    model = Post
    context_object_name = "single_post"
    success_url = reverse_lazy("post_list")
