#!/usr/bin/env python3

# Python script for getting bar codes of bills

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://site.sabesp.com.br/site/Default.aspx")
elem = driver.find_element_by_partial_link_text('Segunda via de conta')
elem.click()

driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(3)
rgiElement = driver.find_element_by_xpath('/html/body/form/div[4]/div/div[3]/table/tbody/tr[1]/td/input')
rgiElement.send_keys('01072224/69')

driver.find_element_by_xpath('/html/body/form/div[4]/div/div[4]/span/ul/li/a').click()

driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="frmhome:j_id206"]').click()

driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="frmhome:table:0:j_id185"]').click()
driver.find_element_by_xpath('//*[@id="frmhome:j_id356"]/table/tbody/tr[4]/td/label').click()
driver.find_element_by_xpath('//*[@id="frmhome:j_id380"]').click()

driver.implicitly_wait(5)
CodBarraH20 = driver.find_element_by_xpath('//*[@id="frmhome:table1:0:j_id168"]').text
driver.find_element_by_xpath('//*[@id="frmhome:j_id206"]').click()
driver.find_element_by_xpath('//*[@id="frmhome:j_id386"]').click()
driver.quit()

print('Seu codigo de barras é: {}'.format(CodBarraH20))

driver = webdriver.Chrome()
driver.get('https://atendimentolivetim.tim.com.br/portal/site/timfiber/template.LOGIN?utm_source=btl&utm_medium=email&utm_term=regua-conta-online&utm_content=parametrizada-antes-vencimento&utm_campaign=btl-email-regua-conta-online-parametrizada-antes-vencimento-live')

TimElement = driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div[2]/div[2]/div/input[1]')
print('Entre com o CPF:\n')
user = input()
TimElement.send_keys(user)

TimPass = driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div[2]/div[2]/div/input[2]')
print('Entre com senha:\n')
ppass = input()
TimPass.send_keys(ppass)

driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div[2]/div[2]/div/div[1]/button').click()
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[2]/div/table[1]/tbody/tr[1]/td[4]/a/img').click()
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="main"]/div[1]/ul/li[8]/a').click()
driver.quit()

