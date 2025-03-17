import unittest


import NewTableMatch

class TestReservation(unittest.TestCase):


   def test_input(self):
       list_reservation = list()
       reserv = NewTableMatch.Reservation (4, 1,3, False)
       list_reservation.append(reserv)
       reserv = NewTableMatch.Reservation (3, 2, 4, False)
       list_reservation.append(reserv)
       reserv = NewTableMatch.Reservation (2, 1, 4, False)
       list_reservation.append(reserv)
       reserv = NewTableMatch.Reservation (1, 4, 6, False)
       list_reservation.append(reserv)
       table_list = {i: [] for i in range(1, 4)}
       values = NewTableMatch.assign_table_count_waiters(list_reservation, table_list)
       self.assertEqual(values,3)

   def test_second__input(self):
       list_reservation = list()
       reserv = NewTableMatch.Reservation (4, 1,3, False)
       list_reservation.append(reserv)
       reserv = NewTableMatch.Reservation (3, 2, 4, False)
       list_reservation.append(reserv)
       reserv = NewTableMatch.Reservation (2, 3, 5, False)
       list_reservation.append(reserv)
       reserv = NewTableMatch.Reservation (1, 3, 6, False)
       list_reservation.append(reserv)
       reserv = NewTableMatch.Reservation(5, 5, 7, False)
       list_reservation.append(reserv)
       table_list = {i: [] for i in range(1, 6)}
       values = NewTableMatch.assign_table_count_waiters(list_reservation, table_list)
       self.assertEqual(3,values)

   def test_exceed_table(self):
       list_reservation = list()
       reserv = NewTableMatch.Reservation (4, 1,3, False)
       list_reservation.append(reserv)
       reserv = NewTableMatch.Reservation (3, 1, 3, False)
       list_reservation.append(reserv)
       reserv = NewTableMatch.Reservation (2, 1, 3, False)
       list_reservation.append(reserv)
       reserv = NewTableMatch.Reservation (1, 1, 3, False)
       list_reservation.append(reserv)
       table_list = {i: [] for i in range(1, 4)}
       values = NewTableMatch.assign_table_count_waiters(list_reservation, table_list)
       self.assertEqual(-1,values)