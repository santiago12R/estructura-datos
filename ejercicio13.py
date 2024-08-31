def celsius_a_fath(celsius):
    fahre =(celsius * 9/5)+32
    return fahre 
tem_celsius = int(input("introduce el celsius "))
tem_fath = celsius_a_fath(tem_celsius)
print(f"temperatura a celsua es igual a" ,tem_fath)