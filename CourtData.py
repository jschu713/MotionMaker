from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

from StateCourt import Case

def get_search_term():
    with open('cause_search_entry.txt', 'r') as infile:
        pending_search_term = json.load(infile)

    return pending_search_term

PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# Opens the Court records page for Galveston County, TX
driver.get("http://publicaccess.co.galveston.tx.us/default.aspx")

# Clicks the criminal case records
driver.find_element_by_link_text("Criminal Case Records").click()

# Clicks the search by case radio button
driver.find_element_by_xpath("//input[@name='SearchBy' and @value='0']").click()

# Enters search term by cause number and hits enter

search_term = get_search_term()
# search_term = "19-CR-1222"


search_by_case = driver.find_element_by_xpath("//input[@name='CaseSearchValue']")
search_by_case.send_keys(search_term)
search_by_case.send_keys(Keys.RETURN)

# Clicks on the corresponding case
try:
    driver.find_element_by_link_text(search_term).click()
except selenium.common.exceptions.NoSuchElementException:
    pass

page_source = driver.page_source

driver.close()

# time.sleep(5)

#BS

soup = BeautifulSoup(page_source, 'html.parser')

class CaseSearch:
    '''the case search class'''

    def __init__(self):

        self._case_args = []

    def to_json(self):
        '''
        method that assists in transforming class obj into json obj
        '''

        return json.dumps(self, default=lambda x: x.__dict__, indent=4)

    def get_cause_number(self):
        try:
            cause_number_search = soup.find(class_='ssCaseDetailCaseNbr')
            cause_number = cause_number_search.find('span').get_text()
        # self._case_args.append(cause_number)
        except AttributeError:
            return ""


        return cause_number

    def get_defendant(self):

        try:
            defendant_name = soup.find(id='PIr11').get_text()

            defendant_name_temp = defendant_name.split()

            if len(defendant_name_temp) == 3:
                defendant_name_temp[0] = defendant_name_temp[0].replace(',', '')
                defendant_swapped = defendant_name_temp[1:] + defendant_name_temp[:-2]
            elif "Jr." in defendant_name_temp:
                defendant_name_temp[2] = defendant_name_temp[2].replace(',', '')
                defendant_swapped = defendant_name_temp[1:3] + defendant_name_temp[:-3] + defendant_name_temp[-1::]
            else:
                defendant_name_temp[0] = defendant_name_temp[0].replace(',', '')
                defendant_swapped = defendant_name_temp[1:] + defendant_name_temp[:-1]

            defendant_final_name = " ".join(defendant_swapped)
        except AttributeError:
            return ""

        # self._case_args.append(defendant_final_name)

        return defendant_final_name

    def get_plaintiff(self):
        try:
            plaintiff_name = soup.find(id='PIr12').get_text()
        # self._case_args.append(plaintiff_name)
        except AttributeError:
            return ""

        return plaintiff_name

    def get_court(self):
        try:
            court_search = soup.find_all(style="padding-left:10px")
            court_search_narrow = court_search[2]
            court = court_search_narrow.b.string
            split = court.split()
            court_number = split[0]
        # self._case_args.append(court)
        except AttributeError:
            return ""

        return court_number

    def get_opposing_counsel(self):
        try:
            opposing_counsel_find = soup.find(headers="PIr01 PIr11 PIc5")
            opposing_counsel_name = opposing_counsel_find.b.string
        except AttributeError:
            return ""

        return opposing_counsel_name
        # self._case_args.append(opposing_counsel_name)


    def get_judge(self):
        try:
            judge_search = soup.find_all(style="padding-left:10px")
            judge_search_narrow = judge_search[3]
            judge = judge_search_narrow.b.string

            judge_name_temp = judge.split()
            judge_name_temp[0] = judge_name_temp[0].replace(',', '')

            judge_swapped = judge_name_temp[1:] + judge_name_temp[:-1]
            judge_final_name = " ".join(judge_swapped)
        except AttributeError:
            return ""

        # self._case_args.append(judge_final_name)

        return judge_final_name

    def save_as_json(self, json_name):
        '''
        method that writes the pets listed in np_members to a json file
        '''

        with open(json_name, 'w') as outfile:
           outfile.write(self.to_json())

    def make_case(self):
        case = Case(self.get_cause_number(), self.get_plaintiff(), self.get_defendant(), self.get_court(), self.get_opposing_counsel(), self.get_judge())

        self._case_args.append(case)

def run():
    cs = CaseSearch()
    cs.make_case()

    # cs.get_cause_number()
    # cs.get_defendant()
    # cs.get_plaintiff()
    # cs.get_court()
    # cs.get_opposing_counsel()
    # cs.get_judge()

    cs.save_as_json('case_data.json')

run()