def apply_vat(price, percent):
    new_percent = None
    new_price = None

    if isinstance(float(price), str):  #
        raise ValueError(f"{price} is not a number.")  # To change to a try catch
    elif isinstance(float(percent), str):
        raise ValueError(f"{percent} is not a percentage.")  # To change to a try catch
    elif float(price) <= 0:
        return f'The price ($ {price}) is inferior or equal to 0.'
    elif float(percent) <= 0:
        return f"The percentage ({percent}) is inferior or equal to 0."
    elif float(percent) >= 100:
        return f"The percentage ({percent}) is superior to 100."
    elif 0 < float(percent) < 100 and 0 < float(price):
        new_percent = 1 + float(percent) / 100
        new_price = float(price) * new_percent
        return new_price
    else:
        return "error"


# print(apply_vat('hello', 20))

# print(apply_vat(0,5.2))

