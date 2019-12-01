from django.shortcuts import render, redirect
from blog.models import blog

def index(request):
    return render(request,'blog/index.html')

def blog_list(request):
	blog_list = blog.objects.all()
	data = {'blog_list':blog_list}
	return render(request,'blog/blog_list.html',data)

def blog_item(request,blog_id):
	blog_info = blog.objects.get(id=blog_id)
	data = {'blog_info':blog_info}
	return render(request,'blog/blog_item.html',data)


def blog_post(request):
	data = {'hello':'hello'}
	return render(request,'blog/blog_post.html',data)

def blog_post_submit(request):
	b = blog(title = request.POST['blog_title'],text = request.POST['blog_text'])
	b.save()
	return redirect('/blog/list/')

def blog_edit(request,blog_id):
	blog_info = blog.objects.get(id=blog_id)
	data = {'blog_info':blog_info}
	return render(request,'blog/blog_edit.html',data)

def blog_update(request,blog_id):
	b = blog.objects.get(id=blog_id)
	b.title = request.POST['blog_title']
	b.text = request.POST['blog_text']
	b.save()
	return redirect('/blog/list/')

def blog_delete(request,blog_id):
	b = blog.objects.get(id=blog_id)
	b.delete()
	return redirect('/blog/list/')





