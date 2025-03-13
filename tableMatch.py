

def read_input():
    dictionary_time = dict()
    n, r = (input().split())
    n = int(n)
    r = int(r)
    for q in range(int(r)):
      i, j = (input().split())
      j = int(j) + 1
      i = int(i)
      list_from_time = list()
      # HOW TO SORTED   # https: // realpython.com / sort - python - dictionary /
      if i in dictionary_time:
          dictionary_time[i].append(j)
          p = sorted(dictionary_time[i])
          dictionary_time[i] = p
      # SORTED BY KEY
      else:
          list_new = list_from_time.copy()
          list_new.append(j)
          dictionary_time[i] = list_new
      sorted(dictionary_time.items())
    count_waiters(dictionary_time, n)


def count_waiters (dictionary_time, table):
    list_store_free_time = list()
    waiters = 0
    for n in dictionary_time.keys():
        if len(list_store_free_time) < 1:
          for s, v in enumerate(dictionary_time[n]):  # EXTRACT KEY VALUES
             waiters += 1
             list_store_free_time.append(v)  # STORE THE LIST OF FREE TIME WAITERS
        else:
              for s, v in enumerate(dictionary_time[n]): # EXTRACT THE SECOND KEY LIST TIME
                waiters += 1
                for q in list_store_free_time:  # EXTRACT THE FREE TIME AVAILABLE
                  if q <= n: # VERIFY THAT THE SET KEY AS LESS THAN THE TIME FREE AVAILABLE
                     waiters -= 1
                     list_store_free_time.remove(q) # REMOVE FREE TIME
                     list_store_free_time.append(v)
                     break
                  else:
                    list_store_free_time.append(v) # ADD WHEN IS ANOTHER FREE TIME WAITERS
                    break

    if waiters > table:
        print("impossible")
    else:
        print(f'{waiters}')

if __name__ == "__main__":

  read_input()