# Vytvořte pole, které bude mít 5 stringových hodnot.
pocasi = ["dešt", "mlha", "mrak", "snih", "bouře"]

# Přidejte pomocí metody append() jeden prvek. - "vítr"
pocasi.append("vítr")

# Odstraňte pomocí metody remove() druhý prvek z pole.
pocasi.remove("dešt")
print(pocasi)

# Zaměňte 5 hodnotu z pole za: "slunce"
pocasi[5] = "slunce"
print(pocasi)

# Přidejte 2 stringové hodnoty pole pomocí metody extend().
nove_polozky = ["noc", "den"]

pocasi.extend(nove_polozky)
print(pocasi)

# Vypište základní vytvořené pole a potom každé pole, ve kterém uděláte změnu.
print(pocasi)
print(pocasi.append)
print(pocasi.remove)
print(pocasi[5])
print(pocasi.extend)
