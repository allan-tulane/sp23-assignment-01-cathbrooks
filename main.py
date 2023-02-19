"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
  if x <= 1:
    print(x)
    return x
  else:
    return foo(x-1) + foo(x-2)
    
def longest_run(mylist, key):
  longest_seq = 0
  current_seq = 0
  for num in mylist:
    if num == key:
      current_seq += 1
    else:
      if current_seq > longest_seq:
        longest_seq = current_seq
      current_seq = 0

  return longest_seq
      
      


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
  #base case as to not exceed recurrsion depth
  if not mylist or len(mylist) == 1:
    return 1
    
  #split list in half
  middle_index = len(mylist)//2
  left_half = mylist[:middle_index]  
  right_half = mylist[middle_index:]

  #recursive call
  left_half = longest_run_recursive(left_half, key)
  right_half = longest_run_recursive(right_half, key)

  #find longest run in both halves and if it crosses the middle
  left_half_longest_run = 0
  right_half_longest_run = 0
  for i in range(middle_index-1, -1, -1):
    if mylist[i] == key:
      left_half_longest_run += 1
    else:
      break
  for i in range(middle_index, len(mylist)):
    if mylist[i] == key:
      right_half_longest_run += 1
    else:
      break

  middle_longest_run = left_half_longest_run + right_half_longest_run

  #find longest run
  longest_run = max(left_half_longest_run, right_half_longest_run, middle_longest_run)

  #find if the entire input matches the key
  is_entire_range = False
  if len(mylist) == longest_run:
    is_entire_range = True

  #utilize result class
  result = Result(left_half_longest_run, right_half_longest_run, longest_run, is_entire_range)

  return result

  

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3



