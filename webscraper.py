import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/" 
page = requests.get(URL) #gets the site

print(page.text) 

soup = BeautifulSoup(page.content, "html.parser") 
results = soup.find(id="ResultsContainer")
print(results.prettify()) #prints the div id we are scraping

job_elements = results.find_all("div", class_="card-content") #finds all the jobs

for job_element in job_elements: #finds specific details to each job
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip()) #text removes the HTML tags
    print(company_element.text.strip()) #strip method removes whitespace
    print(location_element.text.strip())
    print()

engineer_jobs = results.find_all( 
    "h2", string=lambda text: "engineer" in text.lower()) #finds all engineer jobs, using lambda function to get it all to lower case
for engineer_job in engineer_jobs: #runs through each result, printing it 
    print(engineer_job.text.strip())
print(len(engineer_jobs), " results found") #number of results


