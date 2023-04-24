import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

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

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="RUN")
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
        self.entry_email = customtkinter.CTkEntry(self.account_frame, placeholder_text="user@gmail.com")
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)
        self.label_password = customtkinter.CTkLabel(master=self.account_frame, text="Password :")
        self.label_password.grid(row=2, column=0, padx=10, pady=10, sticky="W")
        self.entry_password = customtkinter.CTkEntry(self.account_frame, placeholder_text="password")
        self.entry_password.grid(row=2, column=1, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.account_frame, text="Save",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=3, column=0,columnspan = 2)
        # self.string_input_button.grid_rowconfigure(1, weight=1)
        # self.string_input_button.grid_columnconfigure(1, weight=1)

        

        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self)
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_columnconfigure(1, weight=2)
        
        self.slider_progressbar_frame.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
        self.label_radio_group = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="Thông tin tài khoản")
        self.label_radio_group.grid(row=0, column=0 ,columnspan = 2)
        self.label_firstname = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="First Name :")
        self.label_firstname.grid(row=1, column=0,padx=10, pady=(10, 10), sticky="W")
        self.entry_firstname = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="first name")
        self.entry_firstname.grid(row=1, column=1,padx=10, pady=(10, 10), sticky="WE")

        self.label_lastname = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="Last Name :")
        self.label_lastname.grid(row=2, column=0,padx=10, pady=(5, 5), sticky="W")
        self.entry_lastname = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Last name")
        self.entry_lastname.grid(row=2, column=1,padx=10, pady=(5, 5), sticky="WE")

        self.label_address = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="Address :")
        self.label_address.grid(row=3, column=0,padx=10, pady=(5, 5), sticky="W")
        self.entry_address = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Address")
        self.entry_address.grid(row=3, column=1,padx=10, pady=(5, 5), sticky="WE")

        self.label_city = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="City :")
        self.label_city.grid(row=4, column=0,padx=10, pady=(5, 5), sticky="W")
        self.entry_city = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="City")
        self.entry_city.grid(row=4, column=1,padx=10, pady=(5, 5), sticky="WE")

        self.label_state = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="State :")
        self.label_state.grid(row=5, column=0,padx=10, pady=(5, 5), sticky="W")
        self.entry_state = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="State")
        self.entry_state.grid(row=5, column=1,padx=10, pady=(5, 5), sticky="WE")

        self.label_phone = customtkinter.CTkLabel(master=self.slider_progressbar_frame, text="Phone :")
        self.label_phone.grid(row=6, column=0,padx=10, pady=(5, 5), sticky="W")
        self.entry_phone = customtkinter.CTkEntry(self.slider_progressbar_frame, placeholder_text="Phone ")
        self.entry_phone.grid(row=6, column=1,padx=10, pady=(5, 5), sticky="WE")

        self.string_input_button = customtkinter.CTkButton(self.slider_progressbar_frame, text="Save Info",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=7, column=0,columnspan = 2,pady=(10,10))
        
        # create slider and progressbar frame

        self.url_product_frame = customtkinter.CTkFrame(self)
        self.url_product_frame.grid(row=1, column=2,columnspan = 2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.url_product_frame.grid_columnconfigure(0, weight=1)
        # self.url_product_frame.grid_columnconfigure(1, weight=2)
        
        self.url_product_frame.grid_rowconfigure((0,2,3), weight=1)
        self.url_product_frame.grid_rowconfigure(1, weight=3)
        self.url_product_frame.grid_rowconfigure(3, weight=6)
        self.label_url_product = customtkinter.CTkLabel(master=self.url_product_frame, text="URL Product")
        self.label_url_product.grid(row=0, column=0,padx=(0, 0), pady=(0, 0), sticky="WE" )
        self.textbox_product = customtkinter.CTkTextbox(self.url_product_frame,height=50)
        self.textbox_product.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="WE")
        self.string_input_button = customtkinter.CTkButton(self.url_product_frame, text="Save URL",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=3, column=0,pady=(5,10))

        self.label_url_product = customtkinter.CTkLabel(master=self.url_product_frame, text="Kết quả")
        self.label_url_product.grid(row=4, column=0,padx=(0, 0), pady=(10, 0) , sticky="WE" )
        self.textbox_result = customtkinter.CTkTextbox(self.url_product_frame,height=150)
        self.textbox_result.grid(row=5, column=0, padx=(10, 10), pady=(0, 10), sticky="WE")
        # # create scrollable frame
        # self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
        # self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.scrollable_frame.grid_columnconfigure(0, weight=1)
        # self.scrollable_frame_switches = []
        # for i in range(100):
        #     switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
        #     switch.grid(row=i, column=0, padx=10, pady=(0, 20))
        #     self.scrollable_frame_switches.append(switch)

        # # create checkbox and switch frame
        # self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        # self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # set default values
        # self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        self.textbox_result.configure(state="disabled")
        
        # self.checkbox_1.select()
        # self.scrollable_frame_switches[0].select()
        # self.scrollable_frame_switches[4].select()
        # self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        # self.optionmenu_1.set("CTkOptionmenu")
        # self.combobox_1.set("CTkComboBox")
        self.textbox.insert("0.0", "Hướng dẫn sử dụng\n\n" + "Import data" )
        self.textbox.configure(state="disabled")
        # self.slider_1.configure(command=self.progressbar_2.set)
        # self.slider_2.configure(command=self.progressbar_3.set)
        # self.progressbar_1.configure(mode="indeterminnate")
        # self.progressbar_1.start()
        
        # self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        # self.seg_button_1.set("Value 2")

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


if __name__ == "__main__":
    app = App()
    app.mainloop()