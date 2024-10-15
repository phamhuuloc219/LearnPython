import inflect 
# inflect được sử dụng để định dạng danh sách tên 
# một cách đúng ngữ pháp, thêm dấu phẩy và từ "and" ở vị trí phù hợp.
def main():
    p = inflect.engine()

    names = []

    try:
        while True:
            name = input("Nhập tên: ")
            names.append(name)
    except EOFError:
        print()
        
    goodbye = f"Adieu, adieu, to {p.join(names)}"
    print(goodbye)

if __name__ == "__main__":
    main()
