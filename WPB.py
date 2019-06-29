# Python script for getting bar codes of bills

from selenium import webdriver

# It will open Chromium. It works better than Firefox.
# I do not know how to solve gecko path problem.
driver = webdriver.Chrome()
