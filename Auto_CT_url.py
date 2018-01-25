import urllib2
print "1. Enter the Parameters For Downloading Data Directly "
print "2. Be Precise With The Parameters "
print "3. Use %20 Instead Of Space Also Use \"&\" Operator Between Multiple Parameters"
print "e.g: term=Diabetic%20Foot&strd_s=31%2012%202016 {for term and start date}"

A = raw_input()

response = urllib2.urlopen('https://clinicaltrials.gov/ct2/download_studies?'+ A )
zipcontent= response.read()

with open("CT_ALL.zip", 'w') as f:
    f.write(zipcontent)