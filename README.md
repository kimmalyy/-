
#계산기를 만듦,"""표시는 여러개를 한번에 무시하게 만들수 있는기능.처음과끝에 표시함.
"""
print("계산기를 실행합니다.")

Calculation = True

while Calculation:
  number = int(input("계산할숫자: "))
  number2 = int(input("다른숫자: "))

  Operator = input("어떤 계산을 하실건가요?끝내시려면 '멈춤'을 입력해 주세요. (+, -, *, /):")
  
  if Operator == "+":
     print("결과" , number + number2)
     
  elif Operator == "-":
     print("결과" , number - number2)
    
  elif Operator == '*' :
      print("결과" , number * number2)
      
  elif Operator == "/":
     print("결과" , number / number2)
     
  else:
     print("계산기를 종료합니다.")
     Calculation = False
"""