import datetime

current_datetime = datetime.datetime.now()
format_datetime = current_datetime.strftime("%d-%m-%Y")

print("Thời gian hiện tại: ",current_datetime)
print("Thời gian hiện tại vip: ",format_datetime)