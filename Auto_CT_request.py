import requests

print "1. Enter the Parameters For Downloading Data Directly "
print "2. Be Precise With The Parameters "
print "3. Use %20 Instead Of Space Also Use \"&\" Between Multiple Parameters"
print "e.g: term=Diabetic%20Foot&strd_s=31%2012%202016 {for term and start date}"

arguments = raw_input()
file_url = ('https://clinicaltrials.gov/ct2/download_studies?'+ arguments )
 
r = requests.get(file_url, stream = True)
 
with open("file266.zip","wb") as zip:
    for chunk in r.iter_content(chunk_size=1024):
 
         # writing one chunk at a time to zip.
         if chunk:
             zip.write(chunk)