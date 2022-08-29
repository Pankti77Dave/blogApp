from django.db.models import Q
from gc import get_objects

from django.shortcuts import get_object_or_404, render, redirect
from .forms import BlogForm, CommentForm, UpdateForm
from .models import Post, Tag, Comment, User
from users.models import BlogUser
from django.views.generic import TemplateView, ListView

class BlogDetail(TemplateView):
    template_name = 'blog/detail.html'
    def get(self, request, id):
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

class BlogSearch(ListView):
    template_name = 'blog/search.html'
    model = Post
    def get(self, request, *args, **kwargs):
            # <process form cleaned data>
        blogquery=request.GET.get("query")
        print(f"\n\n\n\n\n{blogquery}\n\n\n\n\n")
        posts = Post.objects.filter(Q(title__icontains=blogquery) | Q(intro__icontains=blogquery) | Q(body__icontains=blogquery))
        print(f"\n\n\n\n\n{posts}\n\n\n\n\n")
        if 'uname' in request.session:
            return render(request, self.template_name, {'posts': posts, 'query': blogquery,'uname':request.session['uname'] })
        return render(request, self.template_name, {'posts': posts, 'query': blogquery})




def add(request):
    if 'uname' in request.session:
        return render(request, 'blog/add.html', { 'BlogForm': BlogForm,'uname':request.session['uname']})
    return render(request, 'blog/add.html', { 'BlogForm': BlogForm})

def create(request):
    if request.method=="POST" and ('uname' in request.session):
        form = BlogForm(request.POST) 
        if form.is_valid():
            tag=form.cleaned_data['tag']
            title=form.cleaned_data['title']
            intro=form.cleaned_data['intro']
            body=form.cleaned_data['body']
            uname=BlogUser.objects.get(uname=request.session['uname'])
            add=Post(tag=tag,title=title,intro=intro,body=body,slug=title,uname=uname) 
            add.save()
            return redirect( '/')
        else:
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
