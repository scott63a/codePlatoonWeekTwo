sequence = [4, 3, 5, 0, 1]
sequence2 = [4, 3, 5, 0, 1]
sequence3 = [5, 3,4 , 1, 0]

def bubble_sort(list):
  swaps = 0
  counter = len(list)
  while counter > 0:
    for index in range(len(list) -1):
        previous = list[index]
        current = list[index + 1]
        if previous > current:
          list[index], list[index+1] = current, previous
    counter -= 1
    swaps += 1
  print(f"Swaps: {swaps}")
  return list

print(f"Final result: {bubble_sort(sequence3)}")
