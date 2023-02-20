from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *


def processlist(request): # a view used to list the processor that are in the database
    processorlist = Processor.objects.order_by('-ownersNum')
    context = {
        'processorlist': processorlist
    }
    return render(request, 'processlist.html', context)


def oslist(request):  # a view used to list the OS that are in the database
    Osnum = OS.ownersNum
    oslist = OSChoice.objects.order_by('-votes')
    context = {
        'oslist': oslist
    }
    return render(request, 'oslist.html', context)


def endsubmission(request):  # a view used to show the user their choice was succesfully submitted
    return HttpResponseRedirect("/pollputers")


def ondeletin(request):  # a view used to confirm the deletion of an item
    return HttpResponseRedirect("/pollputers")


def create_view_process(request):  # a function used to create a web page with the 'ProcessForm'
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = Processform(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('thank/')

    context['form'] = form
    return render(request, "submit_process.html", context)


def delete_view(request, id):  # a simple delete function
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Processor, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()

    #redirect to the page
    return render(request, "delete_page.html", context)


def update_view(request, id): # a simple update function
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Processor, id=id)

    # pass the object as instance in form
    form = Processform(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/pollputers")

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_process.html", context)
