
# 1.a) uses addition

# xa_a - xt_a <= 0.00005
xa_a = 1.1062

# ya_a - yt_a <=  0.0005
ya_a = 0.947

# doing some arithmetic to find
# the lower & upper bounds
xa_a_min = round(xa_a - 0.00005, 5)
xa_a_max = round(xa_a + 0.00005, 5)

ya_a_min = round(ya_a - 0.0005, 4)
ya_a_max = round(ya_a + 0.0005, 4)

min_temp_a = ya_a_min + xa_a_min
max_temp_a = ya_a_max + xa_a_max

min_a = round(min_temp_a - (ya_a + xa_a), 5)
max_a = round(max_temp_a - (ya_a + xa_a), 5)

print(
  f"1.a)\n xa = {xa_a}, ya = {ya_a}",
  "\nPropogated error bound: ",
  f"{min_a} <= (xt+yt) - (xa+ya) <= {max_a}"
)


# 1.b) uses subtraction

# xa_b - xt_b <= 0.005
xa_b = 23.46

# ya_b - yt_b <=  0.0005
ya_b = 12.753

# doing some min arithmetic to find
# the lower & upper bounds
xa_b_min = round(xa_b - 0.005, 3)
xa_b_max = round(xa_b + 0.005, 3)

ya_b_min = round(ya_b - 0.0005, 4)
ya_b_max = round(ya_b + 0.0005, 4)

min_temp_b = ya_b_min - xa_b_min
max_temp_b = ya_b_max - xa_b_max

max_b = round(min_temp_b - (ya_b - xa_b), 4)
min_b = round(max_temp_b - (ya_b - xa_b), 4)

print(
  f"1.b)\n xa = {xa_b}, ya = {ya_b}",
  "\nPropogated error bound: ",
  f"{min_b} <= (xt-yt) - (xa-ya) <= {max_b}"
)


# 1.c) uses multiplication

# xa_c - xt_c <= 0.0005
xa_c = 2.747

# ya_c - yt_c <=  0.005
ya_c = 6.83

# doing some min arithmetic to find
# the lower & upper bounds
xa_c_min = round(xa_c - 0.0005, 4)
xa_c_max = round(xa_c + 0.0005, 4)

ya_c_min = round(ya_c - 0.005, 3)
ya_c_max = round(ya_c + 0.005, 3)

min_temp_c = ya_c_min * xa_c_min
max_temp_c = ya_c_max * xa_c_max

min_c = round(min_temp_c - (ya_c * xa_c), 7)
max_c = round(max_temp_c - (ya_c * xa_c), 7)

print(
  f"1.c)\n xa = {xa_c}, ya = {ya_c}",
  "\nPropogated error bound: ",
  f"{min_c} <= (xt*yt) - (xa*ya) <= {max_c}"
)


# xa_d - xt_d <= 0.0005
xa_d = 8.473

# ya_d - yt_d <=  0.0005
ya_d = 0.064

# doing some min arithmetic to find
# the lower & upper bounds
xa_d_min = round(xa_d - 0.0005, 4)
xa_d_max = round(xa_d + 0.0005, 4)

ya_d_min = round(ya_d - 0.0005, 4)
ya_d_max = round(ya_d + 0.0005, 4)

min_temp_d = xa_d_min / ya_d_min
max_temp_d = xa_d_max / ya_d_max

max_d = round(min_temp_d - (xa_d / ya_d), 8)
min_d = round(max_temp_d - (xa_d / ya_d), 8)

print(
  f"1.d)\n xa = {xa_d}, ya = {ya_d}",
  "\nPropogated error bound: ",
  f"{min_d} <= (xt/yt) - (xa/ya) <= {max_d}"
)