from selenium import webdriver

baseurl = "http://ifc-challenge.appspot.com/steps/adjunct"
disable_style = "el = document.getElementsByName('program'); el[0].setAttribute('style', '')"

profile = webdriver.FirefoxProfile()
user_agent_string = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
profile.set_preference("general.useragent.override", user_agent_string)
mydriver = webdriver.Firefox(profile)

import itertools

variables = ['l1 = ','l2 = ','l3 = ', 'l4 = ', 'l5 = ', 'l6 = ']
values = ['true;', 'false;']

mydriver.get(baseurl)
mydriver.maximize_window()
for comb in list(itertools.product(values, repeat=6)):

    # First form element in the HTML
    #driver.find_element_by_xpath("//form[@id='progForm']")
    prog_form = mydriver.find_element_by_xpath("//form[1]")
    elem = mydriver.find_element_by_name("program")

    mydriver.execute_script(disable_style);
    # elem.clear()
    pgm = "".join("%s%s" % tup for tup in zip(variables, comb))
    elem.send_keys(pgm)
    prog_form.submit()
    if "Congrats" in mydriver.page_source:
        print("Solution program:\n%s" % pgm)
        break

mydriver.quit()

mydriver.close()

