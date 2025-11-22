from .models import Post
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
    fields = ["title", "subtitle", "body", "author"]
