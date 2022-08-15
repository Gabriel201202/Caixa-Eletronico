from ast import Str

d = int(input('Deposite: '))

if (d >= 10 and d <= 600):
  c = input('\nDeseja sacar?\ns-sim\nn-não\n')

  if (c == "s"):
    s = int(input('\nSaque: '))
    v = [str(s)]

    if (s >= 100 and d >= s):

      for i in range(0,7):
        for j in range(1,11):
          for k in range(1,11):

            if (v[0][0] == str(i) and v[0][1] == "0" and v[0][2] == "0"):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == str(5+j) and v[0][2] == "0"):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100, 1 de R$50 e {j} de R$10')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == str(5+j) and v[0][2] == str(5+k)):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100, 1 de R$50, {j} de 10R$, 1 de R$5 e {k} de R$1')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == str(5+j) and v[0][2] == "5"):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100, 1 de R$50, {j} de 10R$ e 1 de R$5')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == str(5+j) and v[0][2] == str(k)):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100, 1 de R$50, {j} de 10R$ e {k} de R$1')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == "5" and v[0][2] == "0"):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100 e 1 de R$50')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == "5" and v[0][2] == str(5+k)):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100, 1 de R$50, 1 de R$5 e {k} de R$1' )
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == "5" and v[0][2] == "5"):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100, 1 de R$50 e 1 de R$5')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == "5" and v[0][2] == str(k)):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100, 1 de R$50 e {k} de R$1')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == str(j) and v[0][2] == "0"):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100 e {j} de R$10')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == str(j) and v[0][2] == str(5+k)):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100, {j} de R$10, 1 de R$5 e {k} de R$1')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == str(j) and v[0][2] == "5"):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100, {j} de R$10 e 1 de R$5')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == str(j) and v[0][2] == str(k)):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100, {j} de R$10 e {k} de R$1')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == "0" and v[0][2] == str(5+k)):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100, 1 de R$5 e {k} de R$1')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == "0" and v[0][2] == "5"):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100 e 1 de R$5')
              i = 100
              j = 100
              break
            if  (v[0][0] == str(i) and v[0][1] == "0" and v[0][2] == str(k)):
              print(f'\nSaldo: {d-s}\nNotas: {i} de R$100 e {k} de R$1')
              i = 100
              j = 100
              break
    
    if (s <= 99 and s >= 10 and d >= s):
      
      for i in range(1,11):
        for j in range(1,11):

          if (v[0][0] == str(5+i) and v[0][1] == "0"):
            print(f'\nSaldo: {d-s}\nNotas: 1 de R$50 e {i} de R$10')
            i = 100
            break
          if (v[0][0] == str(5+i) and v[0][1] == str(5+j)):
            print(f'\nSaldo: {d-s}\nNotas: 1 de R$50, {i} de R$10, 1 de R$5 e {j} de R$1')
            i = 100
            break
          if (v[0][0] == str(5+i) and v[0][1] == "5"):
            print(f'\nSaldo: {d-s}\nNotas: 1 de R$50, {i} de R$10 e 1 de R$5')
            i = 100
            break
          if (v[0][0] == str(5+i) and v[0][1] == str(j)):
            print(f'\nSaldo: {d-s}\nNotas: 1 de R$50, {i} de R$10 e {j} de R$1')
            i = 100
            break
          if (v[0][0] == "5" and v[0][1] == "0"):
            print(f'\nSaldo: {d-s}\nNotas: 1 de R$50')
            i = 100
            break
          if (v[0][0] == "5" and v[0][1] == str(5+j)):
            print(f'\nSaldo: {d-s}\nNotas: 1 de R$50, 1 de R$5 e {j} de R$1')
            i = 100
            break
          if (v[0][0] == "5" and v[0][1] == "5"):
            print(f'\nSaldo: {d-s}\nNotas: 1 de R$50 e 1 de R$5')
            i = 100
            break
          if (v[0][0] == "5" and v[0][1] == str(j)):
            print(f'\nSaldo: {d-s}\nNotas: 1 de R$50 e {j} de R$1')
            i = 100
            break
          if (v[0][0] == str(i) and v[0][1] == "0"):
            print(f'\nSaldo: {d-s}\nNotas: {i} de R$10')
            i = 100
            break
          if (v[0][0] == str(i) and v[0][1] == str(5+j)):
            print(f'\nSaldo: {d-s}\nNotas: {i} de R$10, 1 de R$5 e {j} de R$1')
            i = 100
            break
          if (v[0][0] == str(i) and v[0][1] == "5"):
            print(f'\nSaldo: {d-s}\nNotas: {i} de R$10 e 1 de R$5')
            i = 100
            break
          if (v[0][0] == str(i) and v[0][1] == str(j)):
            print(f'\nSaldo: {d-s}\nNotas: {i} de R$10 e {j} de R$1')
            i = 100
            break

    if (s <= 9 and d >= s):

      for i in range(1,11):

        if (v[0][0] == str(5+i)):
          print(f'\nSaldo: {d-s}\nNotas: 1 de R$5 e {i} de R$1')  
          break
        if (v[0][0] == "5"):
          print(f'\nSaldo: {d-s}\nNotas: 1 de R$5')  
          break
        if (v[0][0] == str(i)):
          print(f'\nSaldo: {d-s}\nNotas: {i} de R$1')  
          break