from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':200,'b':56,'c':98}
    return render(request,'conditions.html',d)
def looping(request):
    d={'dish':'whitesausepasta'}
    return render(request,'looping.html',d)