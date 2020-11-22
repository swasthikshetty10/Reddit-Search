from django.shortcuts import render
from . import models
import praw
import random
reddit = praw.Reddit(client_id = "gUJfYY0AI_ZIng", 
                    client_secret = "02D7j0I_adTS8iI4xTbpUoxDnYeU-Q",
                    username = "admin_10902",
                    password = "@Admin_10902",
                    user_agent = 'web')

def search_reddit(name):
    post = reddit.subreddit(name)
    top = post.top(limit = 100)
    all_post_subs = []
    
    for submission  in top:
        all_post_subs.append([submission.title , submission.url])
        
    return all_post_subs





# Create your views here.
def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    try :
        posts = search_reddit(search)

        stuff_for_frontend = {
            'search': search,
            'posts': posts
        }
        return render(request, 'new_search.html' , stuff_for_frontend)
    except :
        return render(request , 'no_result.html')
    

