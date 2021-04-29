# Check Temprature of a nuclear power  station core

max_temp = int(input("Enter the max Temprature"))
min_tem = int(input("Enter the min Temprature"))
current_temp = int(input("Enter the current Temprature"))

if current_temp > max_temp:
    print("Core Temprature above safe level . Everyone panic")
elif current_temp < min_tem:
    print("Temprature level low. Please make a fire")
else:
    print("Everything is fine")