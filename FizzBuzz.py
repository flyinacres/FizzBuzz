for i in range(1,101):
 f,b,s,j='Fizz','Buzz',str(i),i%3
 s=str(i) if j else f
 print s if i%5 else s+b if not j else b