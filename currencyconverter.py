##Simple code for converting Naira(#) to Dollar ($) and vice-versa using a fix conversion rate of 350.

print("This App ONLY converts amount in Naira(#) to Dollar($) and vice-versa.")
print("\n")
a = input("Press ENTER to continue ...  ")
print("\n")
conversion_rate = 350
exchange =  input("Please enter amount to be converted (in this formate: #50, $10) ...   ")
print("\n")

try:
    if (exchange[0]!= "#") and (exchange[0]!= "$"):
        print("CurrencyError: currency must be either '#' or '$'  ")
        print("\n")
    elif exchange[0]== "#":
        print(str(exchange) + " is equivalent to $" + str(int(exchange[1:])/int(conversion_rate)) + "  (Using a fix conversion rate of " +str(conversion_rate) + ")")
        print("\n")
        print("THANKS FOR CHECKING THIS OUT!")
        print("\n")
    else:
        print(str(exchange) + " is equivalent to #" + str(int(exchange[1:])*int(conversion_rate)) + "  (Using a fix conversion rate of " +str(conversion_rate) + ")")
        print("\n")
        print("THANKS FOR CHECKING THIS OUT!")
        print("\n")
except ValueError:
    print("ValueError: amount must be valid numbers  ")
    print("\n")