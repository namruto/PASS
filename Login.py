# import tkinter as tk

# root = tk.Tk()
# root.geometry("400x300")
# root.title("My Beautiful GUI")

# # Create title label
# title_label = tk.Label(root, text="Welcome to PASS", font=("Arial", 20))
# title_label.pack(pady=10)

# # Create username label and entry
# username_label = tk.Label(root, text="Username:", font=("Arial", 12))
# username_label.pack()
# username_entry = tk.Entry(root, font=("Arial", 12))
# username_entry.pack(pady=5)

# # Create password label and entry
# password_label = tk.Label(root, text="Password:", font=("Arial", 12))
# password_label.pack()
# password_entry = tk.Entry(root, show="*", font=("Arial", 12))
# password_entry.pack(pady=5)

# # Create login button
# login_button = tk.Button(root, text="Login", font=("Arial", 12), bg="blue", fg="white", padx=10, pady=5)
# login_button.pack(pady=10)

# # Create message label
# message_label = tk.Label(root, text="", font=("Arial", 12))
# message_label.pack()

# root.mainloop()
import tkinter as tk

# Tạo ứng dụng
root = tk.Tk()

# Cấu hình kích thước và tên của ứng dụng
root.geometry("800x600")
root.title("Ứng dụng của tôi")

# Tạo màn hình chào mừng
splash_screen = tk.Frame(root)
splash_screen.pack(fill=tk.BOTH, expand=True)
splash_image = tk.PhotoImage(file="logo.png")
splash_label = tk.Label(splash_screen, image=splash_image)
splash_label.pack(fill=tk.BOTH, expand=True)

# Tạo màn hình đăng nhập/đăng ký
login_screen = tk.Frame(root)
login_screen.pack(fill=tk.BOTH, expand=True)
login_label = tk.Label(login_screen, text="Đăng nhập/Đăng ký")
login_label.pack()
login_username = tk.Entry(login_screen)
login_username.pack()
login_password = tk.Entry(login_screen, show="*")
login_password.pack()
login_button = tk.Button(login_screen, text="Đăng nhập")
login_button.pack()

# Tạo màn hình chính
dashboard_screen = tk.Frame(root)
dashboard_screen.pack(fill=tk.BOTH, expand=True)

# Tạo chức năng thông báo
notifications_screen = tk.Frame(dashboard_screen)
notifications_screen.pack(fill=tk.BOTH, expand=True)
notifications_label = tk.Label(notifications_screen, text="Thông báo")
notifications_label.pack()

# Tạo chức năng thông tin và tình trạng xe tải
truck_screen = tk.Frame(dashboard_screen)
truck_screen.pack(fill=tk.BOTH, expand=True)
truck_label = tk.Label(truck_screen, text="Thông tin và tình trạng xe tải")
truck_label.pack()

# Tạo chức năng bản đồ và trạm dừng
map_screen = tk.Frame(dashboard_screen)
map_screen.pack(fill=tk.BOTH, expand=True)
map_label = tk.Label(map_screen, text="Bản đồ và trạm dừng")
map_label.pack()

# Tạo menu điều hướng
menu_screen = tk.Frame(root)
menu_screen.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
settings_button = tk.Button(menu_screen, text="Thiết lập")
settings_button.pack()
support_button = tk.Button(menu_screen, text="Hỗ trợ")
support_button.pack()
logout_button = tk.Button(menu_screen, text="Đăng xuất")
logout_button.pack()

# Hiển thị màn hình chào mừng
root.after(3000, lambda: splash_screen.pack_forget())
root.mainloop()
