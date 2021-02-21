from math import atan, cos, log

def f1(x):
  return cos(x)

def f2(x):
  return atan(x)

def f3(x):
  return log(x)

# 5.a) f(xa) = cos(1.473)

fa_a = round(f1(1.473), 4)

# doing some arithmetic to find
# the lower & upper bounds
fa_a_min = round(fa_a - 0.0005, 4)
fa_a_max = round(fa_a + 0.0005, 4)


min_a = round(fa_a_min - fa_a, 4)
max_a = round(fa_a_max - fa_a, 4)

print(
  f"5.a)\n f(xa) = {fa_a}",
  "\nerror bound: ",
  f"{min_a} <= f(xt) - f(xa) <= {max_a}",
  "\nRelative error bound: ",
  f"{round(min_a/fa_a_min, 8)} <= f(xt) - f(xa) <= {round(max_a/fa_a_max, 8)}"
)

# 5.b) f(xa) = arctan(2.62)

fa_b = round(f2(2.62), 3)

# doing some arithmetic to find
# the lower & upper bounds
fa_b_min = round(fa_b - 0.005, 3)
fa_b_max = round(fa_b + 0.005, 3)

min_b = round(fa_b_min - fa_b, 3)
max_b = round(fa_b_max - fa_b, 3)

print(
  f"5.b)\n f(xa) = {fa_b}",
  "\nerror bound: ",
  f"{min_b} <= f(xt) - f(xa) <= {max_b}",
  "\nRelative error bound: ",
  f"{round(min_b/fa_b_min, 6)} <= f(xt) - f(xa) <= {round(max_b/fa_b_max, 6)}"
)


# 5.c) f(xa) = ln(1.4712)

fa_c = round(log(1.4712), 5)

# doing some arithmetic to find
# the lower & upper bounds
fa_c_min = round(fa_c - 0.00005, 5)
fa_c_max = round(fa_c + 0.00005, 5)

min_c = round(fa_c_min - fa_c, 5)
max_c = round(fa_c_max - fa_c, 5)

print(
  f"5.b)\n f(xa) = {fa_c}",
  "\nerror bound: ",
  f"{min_c} <= f(xt) - f(xa) <= {max_c}",
  "\nRelative error bound: ",
  f"{round(min_c/fa_c_min, 10)} <= f(xt) - f(xa) <= {round(max_c/fa_c_max, 10)}"
)
