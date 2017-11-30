from __future__ import unicode_literals
import xml.etree.ElementTree as ET 
import json
import xmltodict
import csv
import os
import glob
import sys
reload(sys)
sys.setdefaultencoding('utf8')

Months={
	"January" : 1,
	"February" : 2,
	"March" : 3,
	"April":4,
	"May":5,
	"June":6,
	"July":7,
	"August":8,
	"September":9,
	"October":10,
	"November":11,
	"December":12
}

path = os.getcwd();
files =  [file for file in glob.glob('*.xml')]

Ct_data = open('A ClinicalTrialsData.csv','w')


csvwriter = csv.writer(Ct_data)
ct_head = []
ct_row=[]

count = 0





for file in files:
	print "Processing File: " , file
	ct_row=[]
	tree = ET.parse(file)
	root = tree.getroot()

	if count == 0: 
		

		
		ct_head.append("Title")
		
		ct_head.append("DateCreated")

		ct_head.append("DateCompleted")

		ct_head.append("DateRevised")

		ct_head.append("MESH1")

		ct_head.append("Abstract")

		
		csvwriter.writerow(ct_head)	 
		count+=1



	breifTitle = root.find('brief_title').text
	ct_row.append(breifTitle)

	created = root.find('study_first_submitted').text
	date , year = created.split(",")

	date = date.split()

	month = Months[date[0]]

	newdate = date[1] + "/" + str(month) + "/" + year.strip()
	ct_row.append(newdate)

	updated = root.find('last_update_submitted').text


	date , year = updated.split(",")

	date = date.split()

	month = Months[date[0]]

	newdate = date[1] + "/" + str(month) + "/" + year.strip()
	ct_row.append(newdate)

	revised = root.find('lastchanged_date').text
	date , year = revised.split(",")

	date = date.split()

	month = Months[date[0]]

	newdate = date[1] + "/" + str(month) + "/" + year.strip()
	ct_row.append(newdate)

	
	MESH1 = []
	condition_browse = root.find('condition_browse')
	try:
		for mesh_term in condition_browse.findall('mesh_term'):
			MESH1.append(mesh_term.text)
	except Exception:
		pass
	ct_row.append(MESH1)



	Abs = []
	brief_summary = root.find('brief_summary')
	try:
		for textblock in brief_summary.findall('textblock'):
			Abs.append(textblock.text)
	except Exception:
		pass

	ct_row.append(Abs)	


	csvwriter.writerow(ct_row)

Ct_data.close()