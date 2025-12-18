from django.shortcuts import render, redirect, get_object_or_404
from .models import X
from .forms import XForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.http import require_POST
from datetime import datetime

def xlistview(request):
    Xs = X.objects.order_by('created_at').reverse().all()[:20]
    return render(request, 'x/x_list.html', {'Xs': Xs})

def xaddview(request):
    if request.method == 'POST':
        form = XForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return redirect('post1')

def xdelete(request, x_id):
    x_to_delete = get_object_or_404(X, id = x_id)
    x_to_delete.delete()
    return redirect('post1')

def xedit(request, x_id):
    x = X.objects.get(id = x_id)
    if request.method == 'POST':
        form = XForm(request.POST, request.FILES, instance = x)
        if form.is_valid():
            form.save()
            return redirect('post1')
        else:
            print(form.errors)
    else:
        form = XForm
    return render(request, 'x/x_edit.html', {'x': x, 'form': form})

@require_POST 
def xlikeadd(request, x_id):
    x = get_object_or_404(x, id = x_id)
    x.like_count +=1
    x.save()
    return JsonResponse({'like_count': x.like_count})


def xlikesubtract(request, x_id):
    x = get_object_or_404(x, id = x_id)
    if x.like_count >0:
        x.like_count -= 1
        x.save()
    return JsonResponse({'like_count': x.like_count})

 



    




    




