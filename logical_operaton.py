#10진수 -> 2진수 변환 모듈
def ten2two(num, length):
  bin = list(format(num,'b'))

  if len(bin) > length :
    print("오류발생")
    return -1
  if len(bin) < length:
    while len(bin) < length:
      bin.insert(0,'0')

  return bin

#단순반복연산
def cal(text):
  text = text.replace('(0)','0')  #parentheses
  text = text.replace('(1)','1')

  text = text.replace('~0','1')
  text = text.replace('~1','0')   #not

  text = text.replace('0n0','0')  #and
  text = text.replace('0n1','0')
  text = text.replace('1n0','0')
  text = text.replace('1n1','1')

  text = text.replace('0v0','0')  #or
  text = text.replace('0v1','1')
  text = text.replace('1v0','1')
  text = text.replace('1v1','1')

  text = text.replace('0+0','0')  #xor
  text = text.replace('0+1','1')
  text = text.replace('1+0','1')
  text = text.replace('1+1','0')

  text = text.replace('0-0','1')  #if and only if
  text = text.replace('0-1','0')
  text = text.replace('1-0','0')
  text = text.replace('1-1','1')

  text = text.replace('0>0','1')  #if..then..
  text = text.replace('0>1','1')
  text = text.replace('1>0','0')
  text = text.replace('1>1','1')





  if len(text) != 1:
    return cal(text)

  if len(text) == 1:
    return text


#변수마다 TF 루프, 입력은 문자열, 사용되는 문자 리스트->집합->리스트로 변환, (), ~, v,n, >(->), -(<->), +(xor) 은 제외
def var_TF(text) :
  del_list = {'(',')','~','v','n','>','-','+'}
  settext = set(text)
  var_list = list(settext - del_list)
  var_list.sort()

  satisfied_list = []
  for i in range(2**(len(var_list))):
    var_num = ten2two(i, len(var_list))
    new_text = text.translate(str.maketrans('?'+str(var_list),'?'+str(var_num)))
    #print(new_text)
    for j in range(len(var_list)):
      print(f"{var_list[j]}:{'T' if var_num[j]=='1' else 'F'}",end=' ')
    tf_of_text = cal(new_text)
    print(f"명제:{'T' if tf_of_text=='1' else 'F'}")
    if tf_of_text =='1':
      satisfied_list.append([var_list,var_num])

  print("===============================\n 명제가 T가 되도록 하는 진리값 목록\n")
  for a,b in satisfied_list:
    for k in range(len(a)):
      print(f"{a[k]}:{'T' if b[k] == '1' else 'F'}", end=' ')
    print('')

# 메인부분, var_TF(명제),  (), ~(not), v(or),n(and), >(->), -(<->), +(xor) 사용바람
var_TF('((pvq)>~(qv~r)n(rv~p)+~(pvqvr)n(~pv~qv~r))') #예시