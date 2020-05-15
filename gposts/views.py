from django.shortcuts import render
from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect

from gposts.models import BoastsAndRoasts
from gposts.forms import AddPostForm

# Create your views here.


def index(request):
    data = BoastsAndRoasts.objects.all().order_by('-date')
    return render(request, 'index.html', {'data': data})


def upvote_view(request, post_id):
    post = BoastsAndRoasts.objects.get(id=post_id)
    post.votescore += 1
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def downvote_view(request, post_id):
    post = BoastsAndRoasts.objects.get(id=post_id)
    post.votescore -= 1
    post.downvotes -= 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))


def boasts(request):
    data = BoastsAndRoasts.objects.filter(is_boast=True).order_by('-date')
    return render(request, 'boasts.html', {'data': data})


def roasts(request):
    data = BoastsAndRoasts.objects.filter(is_boast=False).order_by('-date')
    return render(request, 'roasts.html', {'data': data})


def most_popular(request):
    data = BoastsAndRoasts.objects.all().order_by('-votescore')
    return render(request, 'index.html', {'data': data})


def least_popular(request):
    data = BoastsAndRoasts.objects.all().order_by('votescore')
    return render(request, 'index.html', {'data': data})


def add_post(request):
    html = 'form.html'
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BoastsAndRoasts.objects.create(
                is_boast=data['is_boast'],
                content=data['content']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddPostForm()
    return render(request, html, {'form': form})
