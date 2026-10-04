def celsius_to_fahrenheit(celsius):
  """Convert Celsius to Fahrenheit."""
  return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
  """Convert Fahrenheit to Celsius."""
  return (fahrenheit - 32) * 5 / 9

c_val = 25
f_val = celsius_to_fahrenheit(c_val)
print(f'{c_val}°C is equal to {f_val}°F') 

back_to_c = fahrenheit_to_celsius(f_val)
print(f'{f_val}°F is equal to {back_to_c}°C')
