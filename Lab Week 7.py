class Fractional_number:
  def __init__(self, numerator, denominator):
    self.numerator = numerator
    self.denominator = denominator
  
  def __str__(self):
    return f"{self.numerator}/{self.denominator}"
  
  def floating_number(self):
    return f"{self.numerator / self.denominator}"

fraction1 = Fractional_number(1,3)

print(fraction1)
print(fraction1.floating_number())  
