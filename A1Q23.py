#To convert temperature from Celsius to Fahrenheitand vice versa based on user input.
scale = input("Enter the temperature scale (C or F): ")

temperature = float(input("Enter the temperature: "))
if scale.upper() == "C":
    new_temp = (temperature * 1.8) + 32
    newscale="F"
    print(temperature,scale,"to",newscale,"=",new_temp)
    print(new_temp,newscale,"to",scale,"=",temperature)

elif scale.upper() == "F":
    # Convert Fahrenheit to Celsius
    new_temp = (temperature - 32) / 1.8
    newscale="C"
    print(temperature,scale,"to",newscale,"=",new_temp)
    print(new_temp,newscale,"to",scale,"=",temperature)

    
