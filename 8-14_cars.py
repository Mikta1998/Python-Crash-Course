def car_info(manufacturer, model_name, **further_info):
    further_info["manufacturer"] = manufacturer
    further_info["model name"] = model_name
    return further_info


my_car = car_info("Porsche","PoscheGT",
                  PS=700,
                  Production_year="2025")

print(my_car)