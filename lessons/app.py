import tkinter
import tkinter.messagebox
import customtkinter
from main import run
import threading
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

import os

# Get the current folder
current_folder = os.getcwd()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.load_data()
        self.exist_info = False
        # configure window
        self.title("Tool Check Credit")
        self.geometry(f"{1100}x{640}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="TOOL CHECK", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="RUN", command=self.run_thread)
        self.main_button_1.grid(row=3, column=1,columnspan=3, padx=(0, 0), pady=(20, 20), sticky="ns")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")

        # create radiobutton frame
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radiobutton_frame.grid_columnconfigure(0, weight=1)
        self.radiobutton_frame.grid_columnconfigure(1, weight=2)
        self.radiobutton_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Chọn chế độ")
        self.label_radio_group.grid(row=0, column=0,columnspan = 2)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0,text="Đăng nhập")
        self.radio_button_1.grid(row=1, column=1, pady=10, padx=20, sticky="W")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1,text="Tự động đăng ký")
        self.radio_button_2.grid(row=2, column=1, pady=10, padx=20, sticky="W")

        # create account
        self.account_frame = customtkinter.CTkFrame(self)
        self.account_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.account_frame.grid_columnconfigure(0, weight=1)
        self.account_frame.grid_columnconfigure(1, weight=2)
        self.account_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.label_radio_group = customtkinter.CTkLabel(master=self.account_frame, text="Tài khoản")
        self.label_radio_group.grid(row=0, column=0 ,columnspan = 2)
        self.label_email = customtkinter.CTkLabel(master=self.account_frame, text="Email :")
        self.label_email.grid(row=1, column=0, padx=10, pady=10, sticky="W")
        
        self.entry_email = customtkinter.CTkEntry(self.account_frame, placeholder_text="user@gmail.com",textvariable=self.email)
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)
        self.label_password = customtkinter.CTkLabel(master=self.account_frame, text="Password :")
        self.label_password.grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.entry_password = customtkinter.CTkEntry(self.account_frame, placeholder_text="password",textvariable=self.password)
        self.entry_password.grid(row=2, column=1, padx=20, pady=(10, 10))
        self.save_account_button = customtkinter.CTkButton(self.account_frame, text="Save",
                                                         command=self.save_account)
        self.save_account_button.grid(row=3, column=0,columnspan = 2)


        # create thông tin tài khoản frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self)
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_columnconfigure(1, weight=2)
        
        self.slider_progressbar_frame.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
        self.label_radio_group = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="Thông tin tài khoản")
        self.label_radio_group.grid(row=0, column=0 ,columnspan = 2)
        self.label_firstname = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="First Name :")
        self.label_firstname.grid(row=1, column=0,padx=10, pady=(10, 10), sticky="W")
        self.entry_firstname = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="first name",textvariable=self.first_name)
        self.entry_firstname.grid(row=1, column=1,padx=10, pady=(10, 10), sticky="WE")

        self.label_lastname = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="Last Name :")
        self.label_lastname.grid(row=2, column=0,padx=10, pady=(5, 5), sticky="W")
        self.entry_lastname = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Last name",textvariable=self.last_name)
        self.entry_lastname.grid(row=2, column=1,padx=10, pady=(5, 5), sticky="WE")

        self.label_address = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="Address :")
        self.label_address.grid(row=3, column=0,padx=10, pady=(5, 5), sticky="W")
        self.entry_address = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Address",textvariable=self.address)
        self.entry_address.grid(row=3, column=1,padx=10, pady=(5, 5), sticky="WE")

        self.label_city = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="City :")
        self.label_city.grid(row=4, column=0,padx=10, pady=(5, 5), sticky="W")
        self.entry_city = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="City",textvariable=self.city)
        self.entry_city.grid(row=4, column=1,padx=10, pady=(5, 5), sticky="WE")

        self.label_state = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="State :")
        self.label_state.grid(row=5, column=0,padx=10, pady=(5, 5), sticky="W")
        self.entry_state = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="State",textvariable=self.state_city)
        self.entry_state.grid(row=5, column=1,padx=10, pady=(5, 5), sticky="WE")

        self.label_state = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="Zip Code :")
        self.label_state.grid(row=6, column=0,padx=10, pady=(5, 5), sticky="W")
        self.entry_state = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Zip Code",textvariable=self.zip_code)
        self.entry_state.grid(row=6, column=1,padx=10, pady=(5, 5), sticky="WE")


        self.label_phone = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="Phone :")
        self.label_phone.grid(row=7, column=0,padx=10, pady=(5, 5), sticky="W")
        self.entry_phone = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Phone ",textvariable=self.phone)
        self.entry_phone.grid(row=7, column=1,padx=10, pady=(5, 5), sticky="WE")

        self.string_input_button = customtkinter.CTkButton(self.slider_progressbar_frame, text="Save Info",
                                                           command=self.save_info)
        self.string_input_button.grid(row=8, column=0,columnspan = 2,pady=(10,10))
        
        self.radio_var_exist_info = tkinter.IntVar(value=0)
       
        # self.check_box_exist_info = customtkinter.CTkCheckBox(master=self.slider_progressbar_frame,checkbox_width=18,checkbox_height=18)

        # self.check_box_exist_info.grid(row=9, column=0,columnspan = 2 ,pady=(10,10))
        # create url_product and result frame

        self.url_product_frame = customtkinter.CTkFrame(self)
        self.url_product_frame.grid(row=1, column=2,columnspan = 2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.url_product_frame.grid_columnconfigure(0, weight=1)
        
        self.url_product_frame.grid_rowconfigure((0,2,3), weight=1)
        self.url_product_frame.grid_rowconfigure(1, weight=3)
        self.url_product_frame.grid_rowconfigure(3, weight=6)
        self.label_url_product = customtkinter.CTkLabel(master=self.url_product_frame, text="URL Product")
        self.label_url_product.grid(row=0, column=0,padx=(0, 0), pady=(0, 0), sticky="WE" )
        self.textbox_product = customtkinter.CTkTextbox(self.url_product_frame,height=100)
        self.textbox_product.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="WE")
        self.string_input_button = customtkinter.CTkButton(self.url_product_frame, text="Save URL",
                                                           command=self.save_url_product)
        self.string_input_button.grid(row=2, column=0,pady=(5,10))

        
        self.url_proxy_frame = customtkinter.CTkFrame(self.url_product_frame)
        self.url_proxy_frame.grid(row=3, column=0, sticky="nsew")

        self.radio_button_proxy = customtkinter.CTkCheckBox(master=self.url_proxy_frame, variable=self.radio_var_proxy,text="Sử dụng Proxy")
        self.radio_button_proxy.grid(row=1, column=0, pady=10, padx=20, sticky="nsew")
        # self.radio_button_proxy_user = customtkinter.CTkCheckBox(master=self.url_proxy_frame, variable=self.radio_var_proxy_user,text="Proxy có User")
        # self.radio_button_proxy_user.grid(row=1, column=1, pady=10, padx=20, sticky="nsew")
        # self.textbox_result = customtkinter.CTkTextbox(self.url_proxy_frame)
        # self.textbox_result.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="WE")

        self.label_proxy = customtkinter.CTkLabel(master=self.url_proxy_frame, text="Proxy :")
        self.label_proxy.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        self.entry_proxy = customtkinter.CTkEntry(self.url_proxy_frame, placeholder_text="http://149.215.113.110:70",textvariable=self.proxy)
        self.entry_proxy.grid(row=2, column=1, padx=10, pady=10)

        self.save_proxy_button = customtkinter.CTkButton(self.url_proxy_frame, text="Save Proxy",
                                                           command=self.save_proxy)
        self.save_proxy_button.grid(row=3, column=1,columnspan = 2,pady=(10,10))

        # #setup 
        # if self.box_exist_info ==1 or self.box_exist_info =="1":
        #     self.check_box_exist_info.select()
        # else:
        #     self.check_box_exist_info.deselect()
        self.entry_email.bind(command=self.change_account)
        # self.textbox_result.configure(state="disabled")
        self.textbox_product.insert("0.0",self.string_url_product)

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

        self.textbox.insert("0.0", "Hướng dẫn sử dụng\n\n" + "1. Chọn Chế độ : đăng nhập sẽ đăng nhập theo tài khoản đã nhập nếu fail sẽ tự động đăng ký.\n" +"2.Kiểm tra và chỉnh sửa thông tin tài khoản ( Save Info để lưu ).\n"+"3.Kiểm tra và chỉnh sửa url product ( Save URL để lưu ).\n" +"4.RUN\n"+"5.Xem kết quả (fail - pass).")
        
        self.textbox.configure(state="disabled")

    def load_data(self):
        self.urls_list = []

        # Read each line of the file and append to the urls array
        url_product_list= open(current_folder+'/url_product.txt', 'r') 
        for line in url_product_list:
            url = line.strip()
            self.urls_list.append(url)
        print(self.urls_list)
        self.string_url_product = ''
        for i in  range(len(self.urls_list)):
           self.string_url_product += str(self.urls_list[i])+ "\n" 
        
        # Load the first URL using the webdriver object
        account =  open(current_folder+'/account.txt', 'r')
        for line in account:
            self.email, self.password = line.strip().split('|')
            self.email = customtkinter.StringVar(value=self.email.replace(' ',''))
            self.password= customtkinter.StringVar(value=self.password.replace(' ',''))

        proxy =  open(current_folder+'/proxy.txt', 'r')
        for line in proxy:
            radio_button_proxy, proxy = line.strip().split('|')
            self.radio_var_proxy = tkinter.IntVar(value=radio_button_proxy)
            self.proxy = customtkinter.StringVar(value=proxy)

        form_ship_address = []
        ship_address =  open(current_folder+'/ship_address.txt', 'r')
        for line in ship_address:
            # Split the line into separate fields
            raw = line.strip()
            form_ship_address.append(raw)
            # Extract the individual fields
        print(form_ship_address)
    
        self.first_name = customtkinter.StringVar(value=form_ship_address[0])
        self.last_name = customtkinter.StringVar(value=form_ship_address[1])
        self.address = customtkinter.StringVar(value=form_ship_address[2])
        self.city = customtkinter.StringVar(value=form_ship_address[3])
        self.state_city = customtkinter.StringVar(value=form_ship_address[4])
        self.zip_code = customtkinter.StringVar(value=form_ship_address[5])
        self.phone = customtkinter.StringVar(value=form_ship_address[6])
        # self.box_exist_info = form_ship_address[7]
        self.list_creadit = []
        credit =  open(current_folder+'/credit.txt', 'r')
        for line in credit:
            number, month, year = line.strip().split('|')
            self.list_creadit.append([number, month, year])
    def save_account(self):
        with open(current_folder+'/account.txt', 'w') as f :
            account = str(self.email.get())+'|'+str(self.password.get())
            f.write(account)
            # self.save_account_button.configure(state="disabled",text="Saved")
    def save_info(self):
        with open(current_folder+'/ship_address.txt', 'w') as f :
            ship_adress_form = str(self.first_name.get()) +"\n" +str(self.last_name.get()) +"\n" +str(self.address.get()) +"\n" +str(self.city.get()) +"\n"+str(self.state_city.get()) +"\n" +str(self.zip_code.get()) +"\n" +str(self.phone.get())
            print(ship_adress_form)
            f.write(ship_adress_form)
    def save_url_product(self):
        with open(current_folder+'/url_product.txt', 'w') as f :
            url_product = self.textbox_product.get('0.0','end-1c')
            f.write(url_product)
    def save_proxy(self):
         with open(current_folder+'/proxy.txt', 'w') as f :
            proxy = str(self.radio_button_proxy.get()) +'|'+str(self.proxy.get()) 
            f.write(proxy)
    def change_account(self):
        print('Change ok')
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
    def run_thread(self):
    # Start a new thread that runs your Selenium code
        thread = threading.Thread(target=run)
        thread.start()

app = App()
app.mainloop()