

# Derivative function
def f(x:float) -> float:
   x**4 - 3*x**3 + 2

def df(x: float) -> float:
  return 4*x**3 - 9*x**2



def gradient_desent(df, func= None):
    next_x = 6            # Starting point.
    gamma = 0.01          # Step size multiplier
    precision = 0.001     # Desired precision of result
    max_iters = 1000      # Maximum number of iterations
    for _ in range(max_iters):
        current_x = next_x
        next_x = current_x - gamma * df(current_x)

        step = next_x - current_x  # Deffirence to decreace the function.
        if abs(step) <= precision:
            break

    return next_x


def main():
    print(gradient_desent(df, f))

if __name__ == "__main__":
   main()

