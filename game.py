import add as a
import subtract as s
import multiplication as u
import division as d
import power as p
import module as m
def game():
  score = 0
  while True:
    print('======== Menu ========'
          '\n1. Add'
          '\n2. Subtract'
          '\n3. Multiplication'
          '\n4. Division'
          '\n5. Power'
          '\n6. Module'
          '\n0. Exit')
    option = int(input('\nChoice an option: '))
    
    if option == 0:
      break
      
    num_1 = eval(input('Enter first number: '))
    num_2 = eval(input('Enter second number: '))
    answer = int(input('Enter you answer: '))
  
    if option == 1:
      result =a.add(num_1, num_2)
      if result == answer:
        score += 1
        print('Correct!!')
      else:
        print('Incorrect')
    elif option==2:
      result=s.subtract(num_1, num_2)
      if result== answer:
        score+=1
        print("  Correct!!")
      else:
        print("Incorrect")
    elif option==3:
      result=u.multiplication(num_1, num_2)
      if result== answer:
        score+=2
        print("  Correct!!")
      else:
        print("Incorrect")
    elif option==4:
      result=d.division(num_1, num_2)
      if result== answer:
        score+=2
        print("  Correct!!")
      else:
        print("Incorrect")
    elif option==5:
      result=p.power(num_1, num_2)
      if result== answer:
        score+=4
        print("  Correct!!")
      else:
        print("Incorrect")
    elif option==6:
      result=m.module(num_1, num_2)
      if result== answer:
        score+=4
        print("  Correct!!")
      else:
        print("Incorrect")
      
  print(f'======== Game Over ========'
        f'\nYou score is {score}'
        '\nKeep going!')
game()
