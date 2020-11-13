from scraping import actions
from selenium import webdriver
import time
import Levenshtein as lev
import os
from cryptography.fernet import Fernet



email = "sk4196485@gmail.com"
password = "P@ssword9803"
path = os.path.dirname(os.path.realpath(__file__))
print("path", path)


class Linkedin:

    def __init__(self, linkdin_url):
        print("os current directory", os.curdir)
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        options.add_argument("--start-maximized")
        path = os.path.dirname(os.path.realpath(__file__))
        print("path", path)
        # os.chmod(f'{path}\chromedriver', 755)
        self.driver = webdriver.Chrome(r"C:\Users\Sudha\Downloads\linkedin_skills-master\linkedin_scraper\chromedriver", chrome_options=options)

        actions.login(self.driver, self.decrypted_email, self.decrypted_password)
        self.driver.get("https://www.linkedin.com/in/pratyusha-anne-b3aa4968/")
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Scrolled to Bottom")

    def deccrypted_creds(self):
        key = Fernet.generate_key()
        f = Fernet(key)
        self.decrypted_email = f.decrypt(email)
        self.decrypted_password = f.decrypt(password)

    def get_score(self, employee_skills):
        max_wait = 1
        while max_wait <= 200:
            try:
                print("checking skills ")
                self.driver.execute_script("window.scrollBy(0,500)")
                self.driver.find_element_by_xpath('//h2[text()="Skills & endorsements"]')
                print("Skills and Endorsements attached to Dom")
                break
            except Exception as e:
                time.sleep(1)
                max_wait += 1

        skills_lst = []
        total_skills = len(
            self.driver.find_elements_by_xpath("//ol[starts-with(@class,'pv-skill-categories-section')]/li"))
        for skill in range(1, total_skills + 1):
            skill_prefix_xpath = f"//ol[starts-with(@class,'pv-skill-categories-section')]/li[{skill}]/div//p"
            try:
                skill = self.driver.find_element_by_xpath(f"{skill_prefix_xpath}/span").text
                print(f"Skill: {skill}")
            except:
                skill = self.driver.find_element_by_xpath(f"{skill_prefix_xpath}/a/span").text
                print(f"Skill: {skill}")
            skills_lst.append(skill)
        max_wait = 1
        while max_wait <= 10:
            try:
                print("clicking show more")
                self.driver.execute_script("window.scrollBy(0,500)")
                self.driver.find_element_by_xpath('//button[@data-control-name="skill_details"]').click()
                time.sleep(1)
                print("clicked show more")

                break
            except Exception as e:
                time.sleep(1)
                max_wait += 1

        max_wait = 1
        while max_wait <= 10:
            try:
                print("checking Tools & Technologies")
                self.driver.execute_script("window.scrollBy(0,500)")
                self.driver.find_element_by_xpath('//h3[text()="Tools & Technologies"]')
                print("Tools & Technologies attached to Dom")

                break
            except Exception as e:
                time.sleep(1)
                max_wait += 1

        total_section = len(
            self.driver.find_elements_by_xpath("//ol[@class='pv-skill-category-list__skills_list list-style-none']"))

        for section in range(1, total_section + 1):
            sub_skills_prefix_xpath = f"(//ol[@class='pv-skill-category-list__skills_list list-style-none'])[{section}]/li"
            total_tools_and_tech = len(self.driver.find_elements_by_xpath(sub_skills_prefix_xpath))
            for tools_and_tech in range(1, total_tools_and_tech + 1):
                sub_skill_prefix_xpath = f"{sub_skills_prefix_xpath}[{tools_and_tech}]/div/div[2]/p"
                try:
                    tools_and_tech_text = self.driver.find_element_by_xpath(f"{sub_skill_prefix_xpath}/a/span").text
                    print(f"sub skill: {tools_and_tech_text}")
                except:
                    tools_and_tech_text = self.driver.find_element_by_xpath(f"{sub_skill_prefix_xpath}/span").text
                    print(f"sub skill: {tools_and_tech_text}")
                skills_lst.append(tools_and_tech_text)
        print("linkdin skills_lst", skills_lst)
        print("employeer skills_lst", employee_skills)
        # skills_lst = ['Java', 'Python', 'Selenium WebDriver']
        score_list = []
        if employee_skills:
            print("splitted employee skills ", employee_skills.split(','))
            for employee_skill in employee_skills.split(","):
                for linkedin_skill in skills_lst:
                    emp_skill_format = employee_skill.strip().lower()
                    link_skill_format = linkedin_skill.strip().lower()
                    if (emp_skill_format in link_skill_format) or (emp_skill_format == link_skill_format):
                        print(linkedin_skill)
                        score = lev.ratio(emp_skill_format, link_skill_format) * 100
                        score_list.append(score)
            print("score_list", score_list)
            return sum(score_list) / len(score_list)
        else:
            return 0

# lnk= Linkedin("google.com")
# print(lnk.get_score([]))

# l =Linkedin("https://www.linkedin.com/in/sudhaguda/")
# l.get_score(["python"])
