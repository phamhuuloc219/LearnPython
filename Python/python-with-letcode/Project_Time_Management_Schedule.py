class Event:
    event_id_counter = 1

    def __init__(self, month, week, day, start_time, end_time, event_name, details, is_important):
        self.event_id = Event.event_id_counter
        Event.event_id_counter += 1
        self.month = month
        self.week = week
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.event_name = event_name
        self.details = details
        self.is_important = is_important

class ScheduleManager:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def view_schedule(self, month, week):
        print(f"\nThời khóa biểu cho tháng {month}, tuần {week}:\n")
        for event in self.events:
            if event.month == month and event.week == week:
                self.display_event(event)

    def display_event(self, event):
        print(f"ID: {event.event_id}")
        print(f"Sự kiện: {event.event_name}")
        print(f"Ngày: Tuần {event.week}, Thứ {event.day}")
        print(f"Thời gian: {event.start_time} - {event.end_time}")
        print(f"Chi tiết: {event.details}")
        print(f"Quan trọng: {'Có' if event.is_important else 'Không'}")

    def edit_event(self, event_id):
        event = self.find_event_by_id(event_id)
        if event:
            new_month = input("Nhập tháng mới: ")
            new_week = input("Nhập tuần mới: ")
            new_day = input("Nhập thứ mới: ")
            new_start_time = input("Nhập thời gian bắt đầu mới: ")
            new_end_time = input("Nhập thời gian kết thúc mới: ")
            new_event_name = input("Nhập tên sự kiện mới: ")
            new_details = input("Nhập chi tiết mới: ")
            new_is_important = input("Sự kiện có quan trọng không? (Có/Không): ").lower() == "có"

            event.month = new_month
            event.week = new_week
            event.day = new_day
            event.start_time = new_start_time
            event.end_time = new_end_time
            event.event_name = new_event_name
            event.details = new_details
            event.is_important = new_is_important
            print("Sự kiện đã được cập nhật.")
        else:
            print("Sự kiện không được tìm thấy.")

    def delete_event(self, event_id):
        event = self.find_event_by_id(event_id)
        if event:
            self.events.remove(event)
            print("Sự kiện đã được xóa.")
        else:
            print("Sự kiện không được tìm thấy.")

    def find_event_by_id(self, event_id):
        for event in self.events:
            if event.event_id == event_id:
                return event
        return None

# Hàm chính
def main():
    schedule_manager = ScheduleManager()

    while True:
        print("\n1. Thêm sự kiện\n2. Xem thời khóa biểu\n3. Chỉnh sửa sự kiện\n4. Xóa sự kiện\n5. Thoát")
        choice = int(input("Chọn một lựa chọn (1-5): "))

        if choice == 1:
            month = input("Nhập tháng: ")
            week = input("Nhập tuần: ")
            day = input("Nhập thứ: ")
            start_time = input("Nhập thời gian bắt đầu: ")
            end_time = input("Nhập thời gian kết thúc: ")
            event_name = input("Nhập tên sự kiện: ")
            details = input("Nhập chi tiết: ")
            is_important = input("Sự kiện có quan trọng không? (Có/Không): ").lower() == "có"

            new_event = Event(month, week, day, start_time, end_time, event_name, details, is_important)
            schedule_manager.add_event(new_event)
            print("Sự kiện đã được thêm.")

        elif choice == 2:
            month = input("Nhập tháng: ")
            week = input("Nhập tuần: ")
            schedule_manager.view_schedule(month, week)

        elif choice == 3:
            event_id = int(input("Nhập ID sự kiện: "))
            schedule_manager.edit_event(event_id)

        elif choice == 4:
            event_id = int(input("Nhập ID sự kiện: "))
            schedule_manager.delete_event(event_id)

        elif choice == 5:
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()