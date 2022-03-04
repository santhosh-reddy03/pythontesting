import re

array=[{'name':'ABC','notify':'Warning','value':'100'},
{'name':'DEF','notify':'Info','value':'100'},
{'name':'ABC','notify':'Info','value':'50'},
{'name':'ABC','notify':'Critical','value':'150'},
{'name':'GHI','notify':'Info','value':'40'},
{'name':'DEF','notify':'Warning','value':'170'}]


results = []

for i in array:
  if results:
    # print(results)
    for j in results:
      # print("this is j", j)
      if i['name'] == j['name']:
        if i['notify'] == 'Critical':
          j['notify'] = 'Critical'
          j['value'] = i['value']
          break
        elif i['notify'] == 'Warning' and j['notify'] == 'Info':
          j['notify'] = 'Warning'
          j['value'] = i['value']
          break
        else:
          break
      elif results.index(j) == len(results) - 1:
        # print("this is i ", i)
        results.append(i)
  else:
    results.append(i)

# print(results)


class Range(object):
  def __init__(self, last, first=0):
    self.first = first
    self.last = last

  def advance(self):
    self.first +=1

  def __next__(self):
    if self.first == self.last:
      raise StopIteration
    else:
      answer = self.first
      self.advance()
      return answer

  def __iter__(self):
    return self

def pi(n):
  # when you use arrays they take up lot of space in ram, as the list increases
  sum_ = 0
  prev = 0
  present = 0
  diff = 0
  while abs(diff) <= 0.00000000005:
    try:
      range_obj = Range(n)
      k = next(range_obj) # getting the first value
      while k < n:
        if k==0:
          sum_ += -((-1)**(k+1))*(1/(2*k+1))
          prev = 4 * sum_
        else:
          sum_ += -((-1)**(k+1))*(1/(2*k+1))
          present = 4*sum_
          diff = present - prev
        print("k value", k)
        print(diff)
        k = next(range_obj)
    except StopIteration:
      pass
  if present:
    # where k>0
    return present
  else:
    # only one value k = 0 
    return prev


print("final", pi(10))


a = {"January": 31, "Febraury":29, "March": 31, "April":30, "May":31, "June":30,"July":31,"August":31,"September":30,"October":31,"Novemeber":30, "December":31}
# dt = int(input("dt"))
# mn = input("month")
# days = 183
# co = a[mn] - dt
# while co < days:
#   ke = list(a.keys())
#   mn = ke.index(mn) + 1
#   co += a[ke[mn]]
#   if co > days:
#     dt = co - days
#     print(a[ke[mn]] - dt, ke[mn])
#   mn = ke[mn]

text = "This is a sentence. (RMVE) (Once a day) [twice a day] [RMV]"
text = re.sub('(\(|\[)[a-zA-Z]{1,4}(\)|\])', '', text)
# print(text)
print(re.sub('\[|\]|\(|\)', '', text))

# print(re.sub('(\(|\[)[a-z]{1,4}(\)|\])', '', '(abcd)[abcde][cba]'))