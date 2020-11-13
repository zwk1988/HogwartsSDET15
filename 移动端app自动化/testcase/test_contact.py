from 作业.移动端app自动化.page.app import App


class TestContact():
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()
        # App().start().goto_main()

    def teardown(self):
        self.app.stop()

    def test_addcontact(self):
        name = "hogwarts001"
        gender = '男'
        phonenum = '18903307481'
        result = self.main.goto_address() \
            .click_addmember() \
            .add_member_menual() \
            .add_contact(name, gender, phonenum).get_toast()
        assert '添加成功' == result

    def test_delcontact(self):
        result = self.main.goto_address() \
            .click_contact() \
            .contactdetailbip() \
            .contactds() \
            .contact_del().search_del_contact()
        assert result is True
