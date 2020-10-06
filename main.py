import random
x=[]
def sorter(nums:list):
  check=False
  for i in range(len(nums)-1):
    if nums[i+1]<nums[i]:
      temp=nums[i]
      nums[i]=nums[i+1]
      nums[i+1]=temp
      check=True
  
  if check:
    check=False
    return sorter(nums)
  
  return nums

for i in range(50):
  x.append(random.randint(0,100))

print(sorter(x))
