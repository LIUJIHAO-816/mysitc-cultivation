import menu
from action import btn_action as ba


class UiExtension(menu.Ui_Form):

    def listen_all(self):
        self.listener()
        self.listen_btn_map_1()
        self.listen_btn_map_2()
        self.listen_btn_map_3()
        self.listen_map_lst_sub_map()

    def ui_init_extension(self):
        self.hide_btn_do()

    def hide_btn_do(self):
        self.btn_do_1_times.setVisible(False)
        self.btn_do_5_times.setVisible(False)

    def show_btn_do(self):
        self.btn_do_1_times.setVisible(True)
        self.btn_do_5_times.setVisible(True)

    def listener(self):
        self.btn_test_1.clicked.connect(self.test)

    def listen_btn_map_1(self):
        self.btn_map1.clicked.connect(self.active_listen_btn_map_1)

    def listen_btn_map_2(self):
        self.btn_map2.clicked.connect(self.active_listen_btn_map_2)

    def listen_btn_map_3(self):
        self.btn_map3.clicked.connect(self.active_listen_btn_map_3)

    def listen_map_lst_sub_map(self):
        self.lst_sub_map.clicked.connect(self.active_listen_map_lst_sub_map)

    def test(self):
        print("test_1")
        ba.ButtonAction().prop_test_1(self)

    def active_listen_btn_map_1(self):
        print("map1")
        self.hide_btn_do()
        ba.ButtonAction().show_map_A_list(self)

    def active_listen_btn_map_2(self):
        print("map2")
        self.hide_btn_do()
        ba.ButtonAction().show_map_B_list(self)

    def active_listen_btn_map_3(self):
        print("map3")
        self.hide_btn_do()
        ba.ButtonAction().show_map_C_list(self)

    def active_listen_map_lst_sub_map(self):
        self.show_btn_do()
        print("sub_map")
