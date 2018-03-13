from django.shortcuts import render, HttpResponse, redirect
from ..app_one.models import User
from .models import Idea
from django.contrib import messages
from django.db.models import Count


# renders index.html
def index(request):
    if 'user_id' not in request.session:
        return redirect('app1:index')
    else:
        print("This is index function in app2 views.py")
        all_ideas = Idea.objects.all()
        context = {
            'all_ideas': all_ideas,
        }
        return render(request, 'app_two/index.html', context)


# renders likes.html
def all_likes(request, post_id):
    print("This is all_likes function in app2 views.py")
    this_idea = Idea.objects.get(id=post_id)
    users_like_idea = User.objects.filter(liked_by=Idea.objects.get(id=post_id))
    context = {
        'idea': this_idea,
        'users': users_like_idea,
    }
    return render(request, 'app_two/all_likes.html', context)


# renders users.html, with id
# still haven't figured out how to get the total number of user likes
def users(request, user_id):
    print("This is users function in app2 views.py")
    this_user = User.objects.get(id=user_id)
    # all Idea objects created by the session user
    this_user_ideas = Idea.objects.filter(adds_idea=this_user)
    likes_count = 0
    for idea in this_user_ideas:
        likes_count = likes_count + idea.times_liked
    context = {
        'user': this_user,
        'likes_count': likes_count,
    }
    return render(request, 'app_two/users.html', context)


# session user creates an Idea object (post)
def create_idea(request):
    print("This is create_idea function in app2 views.py")
    if request.method == 'POST':
        this_post = request.POST['post']
        this_poster = User.objects.get(id=request.session['user_id'])
        this_idea = Idea.objects.create(post=this_post, adds_idea=this_poster)
        print(this_idea.post, this_idea.adds_idea.name)
        return redirect('app2:index')
    return redirect('app2:index')


# session user likes an Idea object (post)
def like_idea(request, post_id):
    print("This is like_idea function in app2 views.py")
    this_user = User.objects.get(id=request.session['user_id'])
    this_idea = Idea.objects.get(id=post_id)
    this_idea.likes_idea.add(this_user)
    # increments like count
    this_idea.times_liked = this_idea.times_liked + 1
    this_idea.save()
    print("Total times idea liked:", this_idea.times_liked)

    return redirect('app2:index')


# lets session user delete own posts
def delete_post(request, post_id):
    print("This is delete_post function in app2 views.py")
    post_to_delete = Idea.objects.get(id=post_id)
    post_to_delete.delete()
    print(post_to_delete.post, "deleted!")
    return redirect('app2:index')
