"""
For the table match the main issue was to understand how to order the time.
I decided to create sorted the time for the reservation_until
This allows to reduce the time complexity  and decrease the
amount of time.

"""

class Waiters:
    def __init__(self, busy_from, busy_until, list_reservation_table):
        self.busy_from = busy_from
        self.busy_until = busy_until
        self.list_reservation_table = list_reservation_table

class Reservation:
  def __init__(self,reservation_id, reservation_from, reservation_until, waiters_supply):
    self.reservation_id = reservation_id
    self.reservation_from = reservation_from
    self.reservation_until = reservation_until
    self.waiters_supply = waiters_supply

def assign_table_count_waiters(list_reservation, table_list)-> int:
    # SORT THE LIST
    list_reservation.sort(key=lambda r: r.reservation_until)
    index = -1
    waiters = Waiters(0, 0, 0)
    # INCREASE ON PURPOSE THE NUMBER OF WAITERS TO DISCOVER AN IMPOSSIBLE ASSIGN
    max_waiters = {s: [] for s in range(1, len(table_list) + 2)}
    set_count_waiters = set()
    # CREATE A FAKE WAITERS
    for t in max_waiters.keys():
        max_waiters[t].append(waiters)
    while index < len(list_reservation)-1:
      index += 1
      first_check = list_reservation[index]
      # VERIFY IF THERE IS TOO MANY ORDER

      # EXTRACT WAITERS
      for k in max_waiters.keys():
          # THEY ARE ORDER THEREFORE I DO NOT NEED TO USE THE FOR ( STACK CONCEPT)
          s = max_waiters[k][0]
          if first_check.reservation_from >= s.busy_until:
             waiters = Waiters(first_check.reservation_from, first_check.reservation_until, first_check.reservation_id)
             max_waiters[k].append(waiters)
             max_waiters[k].sort(key=lambda r: r.busy_until, reverse=True)
             set_count_waiters.add(k)
             if len(set_count_waiters) > len(table_list):
                 return -1
             break
    return len(set_count_waiters)

def read_input():
    num_table, reservation = (input().split())
    convert_num_table = int(num_table)
    convert_reservation = int(reservation)
    list_reservation = list()
    table_list = [t for t in range(1, convert_num_table+1)]
    while  convert_reservation > 0:
      time_from, to_time = (input().split())
      convert_time_from = int(time_from)
      convert_to_time = int(to_time) + 1
      table_reservation = Reservation(convert_reservation, convert_time_from, convert_to_time, 0)
      # STORE RESERVATION WITH TABLE INFO WITH A PRIORITY FOR START TIME
      list_reservation.append(table_reservation)
      convert_reservation -= 1

    values = assign_table_count_waiters(list_reservation, table_list)
    if values == -1:
        print("impossible")
    else:
        print(values)

if __name__ == "__main__":

  read_input()