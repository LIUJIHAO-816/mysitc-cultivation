import menu
from action import btn_action as ba

class Ui_extension(menu.Ui_Form):

    def listener(self):
        self.btn_test_1.clicked.connect(self.test)

    def test(self):
        print("test_1")
        ba.ButtonAction().prop_test_1(self)
