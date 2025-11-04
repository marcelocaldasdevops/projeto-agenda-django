from django.shortcuts import render


def create(request):
    post = request.POST
    context = {

    }

    return render(

        request,
        'contact/create.html',
        context
    )