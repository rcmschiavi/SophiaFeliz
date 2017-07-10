'''Código utilizando o selenium para realizar a automação por WebDriver'''

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class ScriptSelenium(unittest.TestCase):
    def setUp(self):
        #Define o webdriver como o firefox
        #É necessário baixar o geckodriver e colocar em alguma path e alterar abaixo
        self.driver = webdriver.Firefox(executable_path='C:/geckodriver.exe')
        #self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(5)
        self.base_url = "http://biblioteca.ifsc.edu.br/asp/login.asp?modo_busca=rapida&content=mensagens&iBanner=0&iEscondeMenu=0&iSomenteLegislacao=0&iIdioma=0"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_scrbiblio(self):
        driver = self.driver
        #Utiliza a página de login separado do restante do site da biblioteca para o selenium não se perder nos elementos
        driver.get("http://biblioteca.ifsc.edu.br/asp/login.asp?modo_busca=rapida&content=mensagens&iBanner=0&iEscondeMenu=0&iSomenteLegislacao=0&iIdioma=0")
        #busca o elemento código para poder prosseguir as etapas e não dar crash
        for i in range(5):
            try:
                print(("Achando elemento codigo {0}").format(i))
                if self.is_element_present(By.NAME, "codigo"): break
            except: pass
            time.sleep(1)
        driver.find_element_by_name("codigo").clear()
        #Substitua o número 666 pelo número de matrícula
        driver.find_element_by_name("codigo").send_keys("666")
        driver.find_element_by_name("senha").clear()
        #Substitua o número 666 pela senha
        driver.find_element_by_name("senha").send_keys("666")
        driver.find_element_by_id("button1").click()
        driver.find_element_by_css_selector("input.button_login").click()
        #Troca de página para fazer o processo de renovação
        driver.get("http://biblioteca.ifsc.edu.br/")
        time.sleep(5)
        #Seleciona o frame certo para realizar as operações
        driver.switch_to.frame("mainFrame")
        #Realiza as operações necessárias e o logout
        driver.find_element_by_link_text("Serviços").click()
        driver.find_element_by_link_text(u"Circ./Renovação").click()
        driver.find_element_by_name("selTudo").click()
        driver.find_element_by_link_text("Renovar itens selecionados").click()
        driver.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
