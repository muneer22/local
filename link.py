from __future__ import unicode_literals
import recordlinkage
import sys
import pandas
#reload(sys)
#sys.setdefaultencoding('utf8')


pd = pandas.read_csv("A PubmedData.csv")
ct = pandas.read_csv("A ClinicalTrialsData.csv")

#print pd


print("\n")
#indexer = recordlinkage.FullIndex()
#pairs = indexer.index(pd, ct)

indexer = recordlinkage.BlockIndex(on='Title')
pairs = indexer.index(pd, ct)
print("RecordLinkage Based on Title Through BlockIndex")
print(len(pd), len(ct), len(pairs))
print("\n")

indexer = recordlinkage.BlockIndex(on='Abstract')
pairs = indexer.index(pd, ct)
print("RecordLinkage Based on Abstract Through BlockIndex")
print(len(pd), len(ct), len(pairs))
print("\n")

indexer = recordlinkage.SortedNeighbourhoodIndex(on="Title")
pairs = indexer.index(pd,ct)
print("RecordLinkage Based on Title Through SortedNeighbourhoodIndex")
print(len(pd), len(ct), len(pairs))
print("\n")


indexer = recordlinkage.SortedNeighbourhoodIndex(on="Abstract")
pairs = indexer.index(pd,ct)
print("RecordLinkage Based on Abstract Through SortedNeighbourhoodIndex")
print (len(pd),len(ct),len(pairs))
print("\n")


compare_cl = recordlinkage.Compare()

compare_cl.string('Title', 'Title', method='jarowinkler',label='Title')

compare_cl.string('Abstract', 'Abstract', method='jarowinkler', label='Abstract')


compare_cl.string('DescriptorName', 'MESH1', method='jarowinkler', label='Mesh')


compare_cl.string('QualifierName', 'MESH1', method='jarowinkler', label='Mesh2')


features = compare_cl.compute(pairs,pd,ct)

#print (features)

print (features.describe())

#print (features.sum(axis=1).value_counts().sort_index(ascending=False))

#print(features[features.sum(axis=1) >0.90])

