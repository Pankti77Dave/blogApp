from django.db.models import Q
from gc import get_objects

from django.shortcuts import get_object_or_404, render, redirect
from .forms import BlogForm, CommentForm, UpdateForm
from .models import Post, Tag, Comment, User

def detail(request, id):
    post = Post.objects.get(id=id)
    comment = Comment.objects.filter(post_id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', id=id)
    else:
        form = CommentForm()
    if 'uname' in request.session:
        return render(request, 'blog/detail.html', {'post': post, 'form': form, 'comments': comment,'uname':request.session['uname']})
    return render(request, 'blog/detail.html', {'post': post, 'form': form, 'comments': comment})
def tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)

    return render(request, 'blog/tag.html', {'tag': tag})


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'blog/search.html', {'posts': posts, 'query': query})

def add(request):
    if 'uname' in request.session:
        return render(request, 'blog/add.html', { 'BlogForm': BlogForm,'uname':request.session['uname']})
    return render(request, 'blog/add.html', { 'BlogForm': BlogForm})

def create(request):
    form = BlogForm(request.POST)
    obj = form.save(commit=False)
    obj.slug = 'text' 
    obj.save()

    return redirect( '/')

def update(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=post)
        form.save()
        return redirect('/')
    else:
        form = UpdateForm(initial= {'title': post.title, 'body': post.body, 'intro': post.intro, 'tag': post.tag})
        if 'uname' in request.session:
            return render(request, 'blog/update.html', { 'UpdateForm': form,'uname':request.session['uname']})
        return render(request, 'blog/update.html', { 'UpdateForm': form})

def delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')

def comment_delete(request,post_id, id):
    comment = Comment.objects.get(id=id)
    comment.delete()
    return redirect('/{}/'.format(post_id))

def comment_add(request, post_id):
    form = CommentForm(request.POST)
    obj = form.save(commit=False)
    user = User.objects.get(id=request.user.id)
    post = Post.objects.get(id=post_id)
    obj.user = user 
    obj.post = post
    obj.save()
    return redirect('/{}/'.format(post_id))
