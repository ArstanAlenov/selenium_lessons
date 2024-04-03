
from selenium import webdriver
from selenium.webdriver import Remote
import selenium


class TestCalc:
    def srtUp(self):
        dc = {'app': 'C"/windows/system32/calc.exe'}
        self.driver = Remote(command_executor='http://localhost:9999',
                             desired_capabilities=dc)

    def test_power(self):
        window = self.driver.find_element_by_class_name()