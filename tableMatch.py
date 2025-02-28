
def verify_waiters(dictionary_time):
   previous_time_exceed = 0
   waiters = 1
   new_time_exceed = 0
   """
   1. VERIFY IF THE KEY EXCEED THE PREVIOUS TIME > THAN NEW KEY: YES ?
      (1 3) (2 5, 6). I NEED TO ENSURE THAT VALUE'S NEW KEY OF THE ELEMENT IS < = 1, OTHERWISE I NEED TO ADD WAITERS 
      AND SETUP NEW TIME EXCEED VARIABLE
   2. NO ? I DO NOT NEED NEW WAITERS IN THIS CONDITION (1 3) (3 5, 6). IN THE CONDITION THAT THE PREVIOUS EXPIRATION TIME
      IS NOT MAJOR  THAT THE KEY. HOWEVER I NEED TO ADD WAITERS ONLY WHEN EXIST VALUE'S ELEMENT > 1 
      AND SETUP ONE AGAIN THE TIME EXCEED VARIABLE WITH THE NEW ONE
   """
   for i in dictionary_time.keys():

    if previous_time_exceed > i:
        for p in dictionary_time[i]:
          waiters += 1
          new_time_exceed = p
    else:
        count = 0
        new_time_exceed = 0
        for p in dictionary_time[i]:
            count+=1
            if count >1:
              waiters += 1
            new_time_exceed = p
    if new_time_exceed > previous_time_exceed:
        previous_time_exceed = new_time_exceed

   print(f'The number of waiters necessary is {waiters}')








def read_input():
    dictionary_time = { }
    list_times = []
    waiters = 1
    # UNPACKING
    n, r = (input("Enter the number of table and reservation\n").split())
    for n in range(int(r)):
      i, j = (input("Enter the reservation time\n").split())
      j = int(j) + 1
      i = int(i)
        # VERIFY KEY IS PRESENT https://www.geeksforgeeks.org/python-check-given-key-already-exists-in-a-dictionary
      if int(i) in dictionary_time.keys():
          # VERIFY KEY IS PRESENT / EXTRACT THE LIST INSIDE IF IT IS ALREADY PRESENT THE VALUE CREATE A NEW LIST
          for values in dictionary_time.keys():
              list_verify = dictionary_time [values]
              list_verify.append(j)
              break
      else:
          new_from_Time = list_times.copy()
          new_from_Time.append(int(j))
          dictionary_time[int(i)] = new_from_Time

    verify_waiters(dictionary_time)



















if __name__ == "__main__":
  a  = 5
  b = 10
  c = a+b
  n = hash(c)
  print(n)
  read_input()