from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('안녕하세요')
    return render(request, 'demos/index.html')

def calculator(request):
  # return HttpResponse('계산기 기능 구현 시작입니다. 이게 맞나요?')
  
  # 1. 데이터 확인
  num1 = request.GET.get('num1')
  num2 = request.GET.get('num2')
  operators = request.GET.get('operators')
  
  # 2. 계산
  if operators == '+':
    result = int(num1) + int(num2)
  elif operators == '-':
    result = int(num1) - int(num2)
  elif operators == '*':
    result = int(num1) * int(num2)
  elif operators == '/':
    result = int(num1) / int(num2)
  else:
    result = 0
    
  # 3. 응답
  return render(request, 'calculator.html', {'result': result})