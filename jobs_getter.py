import requests
from bs4 import BeautifulSoup
import pandas as pd

# HTTP request to server
URL = "https://www.ilhabela.sp.gov.br/cidadao/pat-de-ilhabela/"
# URL = "https://realpython.github.io/fake-jobs"
page = requests.get(URL)

# data parsing and getting jobs as list of html table rows
soup = BeautifulSoup(page.content, "html.parser")
jobs = soup.findAll('tr')

# extracting contents from the rows and building a pandas dataframe

# indexes of fields to extract from data rows's contents
# (exploring the data, you finfd out these are the odd ones)
fields_indexes = [ind for ind in range(len(jobs[0])) if ind %2 == 1]

# column names for data frame
columns_for_df = [
    jobs[0].contents[i].contents[0].contents[0] # extracting them from nested html tags
    for i in fields_indexes
]

# data contents for dataframe
jobs_data = []
for job in jobs[1:]:
    jobs_data.append([job.contents[ind].contents[0] for ind in fields_indexes])
jobs_df = pd.DataFrame(data=jobs_data, columns=columns_for_df)

# cleaning sallary string
def filter_sym(s):
    return s.replace('R$','').replace(' ','').replace(',','').replace(',','')

# ordering data by sallary
jobs_df = jobs_df[jobs_df["Faixa Salarial"] != 'A combinar' ]
jobs_df['Faixa Salarial'] = jobs_df['Faixa Salarial'].apply(filter_sym)
jobs_no_exp = jobs_df[jobs_df["Exige experiência"] == 'Não'].sort_values(
    by='Faixa Salarial',
    ascending=False
)

print(jobs_no_exp)