import matplotlib.pyplot as plt

def calculate(operation, num1, num2):
  if operation == '+':
    return num1 + num2
  elif operation == '-':
    return num1 - num2
  elif operation == '*':
    return num1 * num2
  elif operation == '/':
    return num1 / num2
  else:
    print("Invalid operation")

def plot_graph(operation, num1, num2):
  x = list(range(num1, num2 + 1))
  y = []
  for i in x:
    y.append(calculate(operation, num1, i))
  plt.plot(x, y)
  plt.xlabel("Input")
  plt.ylabel("Output")
  plt.title(f"{operation} Operation")
  plt.show()

# Get user input
operation = input("Enter the operation (+, -, *, /): ")
num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))

# Calculate and plot the graph
result = calculate(operation, num1, num2)
print(f"The result of {operation} operation between {num1} and {num2} is: {result}")
plot_graph(operation, num1, num2)