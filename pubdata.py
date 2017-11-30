from __future__ import unicode_literals
import xml.etree.ElementTree as ET 
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')



tree = ET.parse("medline17n0001.xml")
root = tree.getroot()
Article_data = open('A PubmedData.csv','w')


csvwriter = csv.writer(Article_data)
article_head = []
article_row=[]

tags = root.findall('PubmedArticle')


count = 0
for member in tags:
	article_row=[]
	
	if count == 0: 
		citation = member.find('MedlineCitation')
	
		pmid = citation.find('PMID').tag
		article_head.append(pmid)
		article = citation.find('Article')
		articleTitle = article.find('ArticleTitle').tag
		article_head.append("Title")
		createddate = citation.find('DateCreated').tag
		article_head.append(createddate)
		completeddate = citation.find('DateCompleted').tag
		article_head.append(completeddate)
		datemodified = citation.find('DateRevised').tag
		article_head.append(datemodified)
		AuthorList = article.find('AuthorList')
		Author = AuthorList.find('Author').tag
		article_head.append(Author)
		
		MeshHeadingList = citation.find('MeshHeadingList')
		MeshHeading = MeshHeadingList.find('MeshHeading')
		DescriptorName = MeshHeading.find('DescriptorName').tag
		article_head.append(DescriptorName)
		QualifierName = MeshHeading.find('QualifierName').tag
		article_head.append(QualifierName)

		article_head.append("Abstract")

		csvwriter.writerow(article_head)	 
		count+=1

	citation = member.find('MedlineCitation')
	
	pmid = citation.find('PMID').text
	article_row.append(pmid)
	
	article = citation.find('Article')
	articleTitle = article.find('ArticleTitle').text
	article_row.append(articleTitle)
	
	createddate = citation.find('DateCreated')
	article_row.append(createddate[2].text + "/" + createddate[1].text +"/"+ createddate[0].text)
	
	completeddate = citation.find('DateCompleted')
	article_row.append(completeddate[2].text + "/" + completeddate[1].text +"/"+ completeddate[0].text)
	
	datemodified = citation.find('DateRevised')
	article_row.append(datemodified[2].text + "/" + datemodified[1].text +"/"+ datemodified[0].text)
	
	auths=[]
	AuthorList = article.find('AuthorList')
	try:
		for Author in AuthorList.findall('Author'):
			auths.append(Author[0].text+ " " + Author[1].text)
	except Exception:
		pass
	article_row.append(auths)

	
	MeshHeadingList = citation.find('MeshHeadingList')
	MeshHeading = MeshHeadingList.find('MeshHeading')
	DescriptorName = MeshHeading.find('DescriptorName').text
	article_row.append(DescriptorName)


	Mesh=[]
	MeshHeadingList = citation.find('MeshHeadingList')
	try:
		for QualifierName in MeshHeading.findall('QualifierName'):
			Mesh.append(QualifierName.text)
	except Exception:
		pass
	
	article_row.append(Mesh)


	Text = []
	Abstract = article.find('Abstract')
	try:
		for AbstractText in Abstract.findall('AbstractText'):
			Text.append(AbstractText.text)
	except Exception:
		pass

	article_row.append(Text)

	
	csvwriter.writerow(article_row)

Article_data.close()