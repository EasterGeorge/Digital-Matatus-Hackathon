from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Post , Resources , Reports
from .forms import PostForm,  CommentForm, ReportForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from bokeh.plotting import figure, output_file, show 
from bokeh.embed import components

from django.http import HttpResponseRedirect

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:4]
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_resources(request):
    resources = Resources.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'blog/post_list.html', {'resources': resources})
    return render(request, 'blog/post_list.html', {'resources': resources})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post,'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

def about_page_view(request):
    resources = Resources.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'about.html',{'resources': resources})


def contact_us(request):
    reports = Reports.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    new_report = None
    if request.method == 'POST':
        report_form = ReportForm(data=request.POST)
        if report_form.is_valid():

            new_report = report_form.save(commit=False)
            new_report.save()
    else:
        report_form = ReportForm()
    return render(request, 'contactus.html' , {'reports': reports , 'new_report': new_report,'report_form': report_form})


