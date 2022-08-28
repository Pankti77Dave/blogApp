from django.shortcuts import render

from blog.models import Post

def frontpage(request):
    post = Post.objects.all()
    
    if 'uname' in request.session:
        return render(request, 'core/frontpage.html', { 'posts': post,'uname':request.session['uname']})
    return render(request, 'core/frontpage.html',{'posts':post})
def about(request):
    return render(request, 'core/about.html')

