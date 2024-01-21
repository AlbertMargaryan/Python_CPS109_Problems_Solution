def isCyclops(num):
  listNum = list(str(num))
  if(len(listNum)%2==0):
    return False
  else:
    if int(listNum[len(listNum)//2]) == 0:
      for i,v in enumerate(listNum):
        if i!=len(listNum)//2 and int(v)==0:
          return False
      return True
    else:
      return False  
