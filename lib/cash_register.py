#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total= total
    self.items = []

  def add_item(self, title, price, quantity = 1):
    transaction_amount = price * quantity
    self.last_transaction_amount = transaction_amount
    self.total += transaction_amount
    for _ in range(quantity):
      self.items.append(title)
    return self.items
  
  def apply_discount(self):
    self.total = self.total - (self.total * (self.discount/100))
    if self.discount != 0:
      print(f"After the discount, the total comes to ${int(self.total)}.")
      return self.total
    else:
      print("There is no discount to apply.")
    
  def void_last_transaction(self):
    if self.last_transaction_amount != 0:
      self.total -= self.last_transaction_amount  
      self.last_transaction_amount = 0 