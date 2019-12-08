if __name__ == '__main__':
    list1=[]
    n = int(input())
    for i in range(n):
       comand=input().split()
       first=(comand[0])
       second=(comand[1:])
       if first=="print":
        print(list1)
       else:
        x=",".join(second) 
        eval("list1."+first+"("+x+")")
