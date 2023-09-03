# import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
import wget


# declare login credentials
Email = 'tech@eChithub.com'
password = 'chithubtech'

file_path = []

# declare inec url
url = 'https://www.inecelectionresults.ng/'

# import selenium chrome webdriver
# ser = Service(
#     'C:\\Users\\akand\\Documents\\Pycharm\\Chithub Pycharm\\INEC ERMS Pycharm\\chromedriver\\chromedriver.exe')
options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=ser, options=options)

driver = webdriver.Chrome(
    'C:/Users/akand/Documents/Pycharm/Chithub Pycharm/INEC ERMS Pycharm/chromedriver/chromedriver.exe')

root_path = 'C:/Users/akand/Downloads/inecpdf'
combined_data_path = 'C:/Users/akand/Downloads/INECDATAcombined'
election_data_path = 'C:/Users/akand/Downloads/InecElectionData'



def downloadPdf(link, path):
    wget.download(link,path)

def createDirectory(folder_name):
    isExist = os.path.exists(folder_name)
    print(isExist)

    if isExist:
        print('Folder', folder_name, 'exists')
    else:
        print('creating new Folder', folder_name)
        os.makedirs(folder_name)
        print('New Folder', folder_name, 'created')
# load inec url
driver.get(url)

# imput login credentials
driver.find_element(By.NAME, 'email').send_keys(Email)
driver.find_element(By.NAME, 'password').send_keys(password)

#
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary mb-4'][type='submit']").click()

# pause the process to allow for complete page loading
time.sleep(10)

# getting all the links for Election category on first page
elements = driver.find_elements(By.XPATH, '//a[@class="text-medium"]')
# print(elements)

# declare list to put links and name on first layer of page
links = []
name_list = []

# put all list and names of first page into the created list
for i in range(len(elements)):
    links.append(elements[i].get_attribute('href'))
    name_list.append(elements[i].text)

# combine both lists and put them in a dataframe
combined_1 = list(zip(links, name_list))
df = pd.DataFrame(combined_1, columns=['links', 'Elective Category'])
print('printing df')
print(df)

# loop through acquired url of first page details
for i, row in df.iterrows():
    # load link from first page
    if i == 5:
        print(i)
        print('Loading category page:', row['Elective Category'])
        path_1 = os.path.join(root_path, row['Elective Category']).replace("\\", "/")
        print(path_1)
        createDirectory(path_1)
        driver.get(row['links'])
        print('Elective Category page', row['Elective Category'], 'Loaded successfully')
        print('getting links for elections available for', row['Elective Category'])
        time.sleep(10)

        # getting all the links and names for specific Election on second page(Elective category)
        elements_2 = driver.find_elements(By.XPATH, '//a[@class="text-medium"]')
        links_2 = []
        name_list_2 = []
        for i_2 in range(len(elements_2)):
            links_2.append(elements_2[i_2].get_attribute('href'))
            name_list_2.append(elements_2[i_2].text)

        # combine both lists and put them in a dataframe
        combined_2 = list(zip(links_2, name_list_2))
        df_2 = pd.DataFrame(combined_2, columns=['links', 'Election'])
        print('printing df_2 for Specific Election')
        print(df_2)

        # loop through acquired url of second page(Elections)
        for i, row in df_2.iterrows():
            # load link from election page
            if i == 5:
                print(i)
                print('Loading Election page:', row['Election'])
                elec_name = row['Election'].replace('/', '-')
                path_2 = os.path.join(path_1, elec_name).replace("\\", "/")
                print(path_2)
                createDirectory(path_2)
                path_election = os.path.join(election_data_path, elec_name).replace("\\", "/")
                createDirectory(path_election)
                driver.get(row['links'])
                print('Election page', row['Election'], 'Loaded successfully')
                print('getting links for lga involved in', row['Election'])
                time.sleep(10)

                # getting all the links and names for lga involved in specific Election
                elements_3 = driver.find_elements(By.TAG_NAME, 'a')
                print(elements_3)
                links_3 = []
                name_list_3 = []

                for i_3 in range(len(elements_3)):
                    links_3.append(elements_3[i_3].get_attribute('href'))
                    name_list_3.append(elements_3[i_3].text)

                # combine both lists and put them in a dataframe
                combined_3 = list(zip(links_3, name_list_3))
                df_3 = pd.DataFrame(combined_3, columns=['links', 'lga'])
                print('printing df_3 for LGA')
                print(df_3)

                # loop through acquired url of lga page
                for i, row in df_3.iterrows():
                    # load link from lga page i >= 5
                    if i == 5:
                        print('Loading lga page:', row['lga'])
                        lga_1 = row['lga'].replace('/', '-')
                        path_3 = os.path.join(path_2, lga_1).replace("\\", "/")
                        print(path_3)
                        createDirectory(path_3)
                        driver.get(row['links'])
                        print('lga', row['lga'], 'Loaded successfully')
                        print('getting links for wards in LGA', row['lga'])
                        time.sleep(10)

                        # getting all the links and names for ward in lga of interest
                        elements_4 = driver.find_elements(By.TAG_NAME, 'a')
                        links_4 = []
                        name_list_4 = []

                        for i_4 in range(len(elements_4)):
                            links_4.append(elements_4[i_4].get_attribute('href'))
                            name_list_4.append(elements_4[i_4].text)

                        # combine both lists and put them in a dataframe
                        combined_4 = list(zip(links_4, name_list_4))
                        df_4 = pd.DataFrame(combined_4, columns=['links', 'ward'])
                        print('printing df_4 for WARD in LGA', row['lga'])
                        print(df_4)

                        # loop through acquired url of ward page to get to polling unit page
                        for i, row in df_4.iterrows():
                            # load link from ward page i>=5
                            if 6 <= i <= 11:
                                print('Loading ward page:', row['ward'])
                                ward_name_0 = row['ward'].replace('"', '\'')
                                ward_name = ward_name_0.replace('/', '-')
                                path_4 = os.path.join(path_3, ward_name).replace("\\", "/")
                                print('path 4', path_4)
                                createDirectory(path_4)
                                driver.get(row['links'])
                                print('WARD', row['ward'], 'Loaded successfully')
                                time.sleep(10)

                                print('getting links for pu in', row['ward'])

                                # getting all the clicks for pu results in ward of interest
                                # elements_5 = driver.find_elements(By.XPATH, 'button')
                                elements_5 = driver.find_elements(By.CSS_SELECTOR,
                                                                  "button[class='btn btn-success'][tabindex='0']")
                                pu_code_list = driver.find_elements(By.XPATH, '//*[@class="pl-4"]')
                                pu_name_list = driver.find_elements(By.TAG_NAME, 'mdb-icon')
                                # elements_5 = driver.find_elements(By.XPATH, "/html/body/app-root/div/app-activated/div/div/div/div/app-election-lga/div/div/div/div[2]/div[2]/mdb-card/mdb-card-body/div/div/div[8]/div/div[2]/button")

                                # print(elements_5)
                                # elements_5
                                pu_name = []
                                pu_code = []
                                result_page = []

                                print(pu_name_list)
                                print('[[[[[[[[[[[[[[[[[[[[')

                                for i_5 in range(len(elements_5)):
                                    result_page.append(elements_5[i_5])
                                    print(i_5)
                                print(result_page)

                                for code in range(len(pu_code_list)):
                                    pu_code.append(pu_code_list[code].text)
                                print(pu_code)

                                for name in range(len(pu_name_list)):
                                    pu_name.append(pu_name_list[name].text)
                                print(pu_name)

                                # combine both lists and put them in a dataframe
                                combined_5 = list(zip(result_page, pu_code))
                                df_5 = pd.DataFrame(combined_5, columns=['resultLink', 'puCode'])
                                print('printing df_5 of Polling Units for ward', row['ward'])
                                print(df_5)

                                for i, rowz in df_5.iterrows():
                                    # reloading pu ward page
                                    # pulling polling units
                                    if i >= 0:
                                        print(i)
                                        print('Loading ward page:', row['ward'])
                                        puCode = rowz['puCode'].replace('/', '-')
                                        puCode_2 = puCode.replace(':', ' -')
                                        path_5 = os.path.join(path_4, puCode_2).replace("\\", "/")
                                        print(path_5)
                                        createDirectory(path_5)
                                        path_combined = os.path.join(path_election, puCode_2).replace("\\", "/")
                                        createDirectory(path_combined)
                                        driver.get(row['links'])
                                        print('WARD', row['ward'], 'Loaded successfully')
                                        time.sleep(10)
                                        # load link fpr pu result page
                                        print('Loading result page for PU :', rowz['puCode'])
                                        # print(row['resultLink'])
                                        # row['resultLink'].click()
                                        x_Path = "/html/body/app-root/div/app-activated/div/div/div/div/app-election-lga/div/div/div/div[2]/div[2]/mdb-card/mdb-card-body/div/div/div[" + str(
                                            i + 1) + "]/div/div[2]/button"
                                        print(x_Path)
                                        elements_5 = driver.find_elements(By.XPATH, x_Path)
                                        for ele in elements_5:
                                            print(ele)
                                            ele.click()
                                            print('PU result for', rowz['puCode'], 'Loaded successfully')
                                            time.sleep(10)
                                            pdf_url = driver.find_element(By.TAG_NAME, 'iframe').get_attribute('src')
                                            print(pdf_url)
                                            the_url = str(pdf_url)
                                            print(the_url)

                                            # the_path = 'C:/Users/akand/Downloads/inecpdf'
                                            downloadPdf(the_url, path_5)
                                            print('pdf downloaded in nested path')
                                            time.sleep(3)
                                            downloadPdf(the_url, path_combined)
                                            print('pdf downloaded in combined path')




                                            print('pdf download successful')
                                            print('------------------------------------------------------------------')




print('Processing Completed')






