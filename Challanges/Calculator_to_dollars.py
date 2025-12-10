source = int(input('Select your SOURCE currency: 1) soles 2)dollars ')) #it would be more options
#first exchange to pen
if source == 1:
    factor = 1
    ticker_source = "PEN"

elif source == 2:
    factor = 3
    ticker_source = "USD"
else:
    raise ValueError("Doesnt exist this option")

quanti = float(input("How many numbers do you want to enter? "))

target = int(input('Select your TARGET currency: 1) soles 2)dollars ')) #it would be safe with a message error

# Convert whatever target currency 
if source == target:
    print("it's the same currency")

if target == 1:
    factor = factor/1
    ticker_target = "PEN"
elif target == 2:
    factor = factor/3
    ticker_target = "USD"
else:
    raise ValueError("Doesnt exist this option")

print(f" {quanti} {ticker_source} ==> {quanti*factor} {ticker_target}")