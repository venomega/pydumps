# precio
p_A = 0.01
p_C = 0.04
p_R = 0.05

# cantidad
c_A = 20  # <- GB HDD
c_C = 1  # <- Cores CPU
c_R = 0.5  # <- GB RAM

# total/h
A = p_A * c_A
C = p_C * c_C
R = p_R * c_R

print("Total a pagar mensual es:", (A+C+R)*24*30, "cup")
