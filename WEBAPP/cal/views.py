from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'cal/input.html')

def addition(request):
    num1 = request.POST['num1']
    num2 = request.POST['num2']
    if num1.isdigit() and num2.isdigit():
       res = int(num1)+int(num2)
    else:
        res= "Please enter the numbers"

    return render(request, 'cal/results.html', {'result':res})

def substraction(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1-num2
    return render(request, 'cal/results.html', {'result':res})


def multiplication(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    res = num1*num2
    return render(request, 'cal/results.html', {'result':res})

def division(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    try:
        res = num1/num2
    except:
        res = "num2 should not be a zero"
    return render(request, 'cal/results.html', {'result':res})