from math import exp


# calculations for 1.b)
xt_a = 28.254
xa_a = 28.271

err_a = round(abs(xt_a-xa_a), 3)
rel_err_a = err_a/xt_a

print(
  "1.a",
  "\nError: ", err_a,
  "\nRelative Error: ", rel_err_a,
  f"\nSignificant digits of the approximation {xa_a}, of the value {xt_a} is 3"
  )

# calculations for 1.b)
xt_b = 0.028254
xa_b = 0.028271

err_b = round(abs(xt_b-xa_b), 8)
rel_err_b = err_b/xt_b


print(
  "1.b",
  "\nError: ", err_b,
  "\nRelative Error: ", rel_err_b,
  f"\nSignificant digits of the approximation {xa_b}, of the value {xt_b} is 4"
  )

# calculations for 1.b)
xt_c = exp(1)
xa_c = 19/7

err_c = abs(xt_c-xa_c)
rel_err_c = err_c/xt_c


print(
  "1.c",
  "\nError: ", err_c,
  "\nRelative Error: ", rel_err_c,
  f"\nSignificant digits of the approximation {xa_c}, of the value {xt_c} is 4"
  )