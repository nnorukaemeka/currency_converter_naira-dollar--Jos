##Simple code for converting Naira(#) to Dollar ($) and vice-versa using a fix conversion rate of 350.


def nairaDollar_converter (response):
    print("This App ONLY converts amount in Naira(#) to Dollar($) and vice-versa.\n")
    a = input("Press ENTER to continue ...  \n")
    conversion_rate = 350

    try:
        if (response[0]!= "#") and (response[0]!= "$"):
            print("CurrencyError: currency must be either '#' or '$'  \n")

        elif response[0]== "#":
            print(str(response) + " is equivalent to $" + str(int(response[1:])/int(conversion_rate)) + "  (Using a fix conversion rate of " +str(conversion_rate) + ")\n")
            print("THANKS FOR CHECKING THIS OUT!\n")
    
        else:
            print(str(response) + " is equivalent to #" + str(int(response[1:])*int(conversion_rate)) + "  (Using a fix conversion rate of " +str(conversion_rate) + ")\n")
            print("THANKS FOR CHECKING THIS OUT!\n")
          
    except ValueError:
        print("ValueError: amount must be valid numbers  \n")      



#with a global scope:
amount =  input("Please enter amount to be converted (in this formate: #50, $10) ...   \n")

#execute this way:
nairaDollar_converter(amount)
