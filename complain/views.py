from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Complain, ComplainComment
from .forms import ComplainForm, ComplainCommentForm

# Create your views here.
@require_safe
def index(request):
    complains = Complain.objects.order_by('-pk')
    context = {
        'complains': complains,
    }
    return render(request, 'complains/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ComplainForm(request.POST)
        if form.is_valid():
            complain = form.save(commit=False)
            complain.user = request.user
            complain.save()
            return redirect('complain:detail', complain.pk)
    else:
        form = ComplainForm()
    context = {
        'form': form,
    }
    return render(request, 'complains/create.html', context)


@require_safe
def detail(request, pk):
    complain = get_object_or_404(Complain, pk=pk)
    comment_form = ComplainCommentForm()
    context = {
        'complain': complain,
        'comment_form': comment_form,
    }
    return render(request, 'complains/detail.html', context)


@require_POST
def delete(request, pk):
    complain = get_object_or_404(Complain, pk=pk)
    if request.user.is_authenticated:
        if request.user == complain.user:
            complain.delete()
    return redirect('complain:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    complain = get_object_or_404(Complain, pk=pk)
    if request.user == complain.user:
        if request.method == 'POST':
            form = ComplainForm(request.POST, instance=complain)
            if form.is_valid():
                complain = form.save()
                return redirect('complain:detail', complain.pk)
        else:
            form = ComplainForm(instance=complain)
    else:
        return redirect('complain:index')
    context = {
        'complain': complain,
        'form': form,
    }
    return render(request, 'complains/update.html', context)


@require_POST
def comment_create(request, pk):
    if request.user.is_authenticated:
        complain = get_object_or_404(Complain, pk=pk)
        comment_form = ComplainCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.complain = complain
            comment.user = request.user
            comment.save()
        return redirect('complain:detail', complain.pk)
    return redirect('accounts:login')


@require_POST
def comment_delete(request, complain_pk ,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(ComplainComment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('complain:detail', complain_pk)

