from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Suggestion, Comment
from .forms import SuggestionForm, CommentForm

# Create your views here.
@require_safe
def index(request):
    suggestions = Suggestion.objects.order_by('-pk')
    context = {
        'suggestions': suggestions,
    }
    print(dir(suggestions))
    return render(request, 'suggestions/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.user = request.user
            suggestion.save()
            return redirect('suggestions:detail', suggestion.pk)
    else:
        form = SuggestionForm()
    context = {
        'form': form,
    }
    return render(request, 'suggestions/create.html', context)


@require_safe
def detail(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk)
    comment_form = CommentForm()
    context = {
        'suggestion': suggestion,
        'comment_form': comment_form,
    }
    return render(request, 'suggestions/detail.html', context)


@require_POST
def delete(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk)
    if request.user.is_authenticated:
        if request.user == suggestion.user:
            suggestion.delete()
    return redirect('suggestions:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    suggestion = get_object_or_404(Suggestion, pk=pk)
    if request.user == suggestion.user:
        if request.method == 'POST':
            form = SuggestionForm(request.POST, instance=suggestion)
            if form.is_valid():
                suggestion = form.save()
                return redirect('suggestions:detail', suggestion.pk)
        else:
            form = SuggestionForm(instance=suggestion)
    else:
        return redirect('suggestions:index')
    context = {
        'suggestion': suggestion,
        'form': form,
    }
    return render(request, 'suggestions/update.html', context)


@require_POST
def comment_create(request, pk):
    if request.user.is_authenticated:
        suggestion = get_object_or_404(Suggestion, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.suggestion = suggestion
            comment.user = request.user
            comment.save()
        return redirect('suggestions:detail', suggestion.pk)
    return redirect('accounts:login')


@require_POST
def comment_delete(request, suggestion_pk ,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('suggestions:detail', suggestion_pk)

