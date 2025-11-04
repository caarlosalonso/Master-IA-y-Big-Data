num_ventas = [20, 30, 40, 50, 60, 70, 80]
high_ventas = [hv for hv in num_ventas if hv >= 50]
print(f"Ventas mayores o iguales a 50: {high_ventas}")

high_ventas = [hv + hv * 0.1 for hv in num_ventas if hv >= 50]
print(f"Ventas mayores o iguales a 50 con aumento del 10%: {high_ventas}")