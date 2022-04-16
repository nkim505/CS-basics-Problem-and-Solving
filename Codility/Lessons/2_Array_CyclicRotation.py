# 1st trial

def solution(A, K):
    # write your code in Python 3.6
    new_A = []
    for i in range(K):
        new_A += [A[-1]]
        for j in range(len(A)-1):
            new_A += [A[j]]
        A = new_A
        new_A = []
        
    return A
    pass
    
 # the result: 87%
 # The following issues have been detected: runtime errors.
 # For example, for the input ([], 1) the solution terminated unexpectedly.
 
 # 2nd trial
def solution(A, K):
  new_A = []
  if A != []:
    for i in range(K):
      new_A += [A[-1]]
      for j in range(len(A)-1):
        new_A += [A[j]]
      A = new_A
      new_A = []
    return A

  else: print("Alart: Put an array with elements on the first place")
  pass

# the result: 87%
# K=0 일 때 문제가 생김.


# 3rd trial
