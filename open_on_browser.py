import webbrowser

new = 2

inpPage = open('companies_job_pages.csv','r')
for row in inpPage:
				webbrowser.open(row,new=new)
