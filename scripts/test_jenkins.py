import allure


class TestJenkins(object):
    @allure.step('测试步骤')
    def test_jenkins(self):
        allure.attach('附件名字','附件内容')
        print('测试')
        assert True