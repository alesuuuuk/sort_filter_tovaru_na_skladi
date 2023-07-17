import json
if __name__ == "__main__":
    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)

        # sort by price
        # sorted_by_price = [sorted(products, key=lambda x: x["price"])]
        # print(sorted_by_price)
        # filter
        # minimal_price = int(input("Введіть від якої ціни ви хочете побачити товари: "))
        # filter_by_price_products = []
        #
        # for product in products:
        #     price = product["price"].replace(" ", "")  # Remove spaces from the price string
        #     if int(price) > minimal_price:
        #         filter_by_price_products.append(product)
        #
        # for product in filter_by_price_products:
        #     print(product)



# товари на складі
    tovaru_na_skladi = {
        "Банан": 35,
        "Яблуко": 5,
        "Слива": 12,
        "киві": 9
    }

    tovaru_na_skladi = {
        "Банан": 35,
        "Яблуко": 5,
        "Слива": 12,
        "киві": 9
    }

    while True:

        continue_ = input("Чи хочете ви зробити оновлення данних?")
        if continue_ == "1":
            for product, quantity in tovaru_na_skladi.items():
                if quantity < 10:
                    print(f"{product}: {quantity}")

        elif continue_ == "2":
            break

        else:
            print("ви ввели неправильне значення, спробуйте ще раз")