months = [
 "January",
 "February",
 "March",
 "April",
 "May",
 "June",
 "July",
 "August",
 "September",
 "October",
 "November",
 "December"
]
def convert_format(date_str):
    # check format MM/DD/YYYY
    if "/" in date_str:
        try:
            month, day, year = map(int, date_str.split("/"))
            if 1 <= month <= 12 and 1 <= day <= 31:
                return f"{year:04}-{month:02}-{day:02}"
        except ValueError:
            pass

    # check format "Month DD, YYYY"
    else:
        try:
            parts = date_str.split()
            month_str = parts[0]
            day = int(parts[1].replace(",", ""))
            year = int(parts[2])
            
            if month_str in months and 1 <= day <= 31:
                month = months.index(month_str) + 1
                return f"{year:04}-{month:02}-{day:02}"
        except (ValueError, IndexError):
            pass

    return None

def main():
    while True:
        date = input("Nhập ngày theo định dạng MM/DD/YYYY hoặc 'Month DD, YYYY': ")
        iso_date = convert_format(date)
        if iso_date:
            print(iso_date)
            break
        else:
            print("Dữ liệu không hợp lệ, vui lòng nhập lại.")

if __name__ == "__main__":
    main()