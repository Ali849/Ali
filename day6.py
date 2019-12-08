# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
for i in range (t):
  name=str(input())
  print(name[0::2]+" "+name[1::2])
