#Extrating epwc and pwc dataset from CWI and SeCoDa datasets
import pandas as pd


def create_extended_pwc:
extendedcw = pd.read_csv ('data/extendedcw.csv')
traindf = pd.read_csv ('data/traindf.csv')

print(extendedcw.shape)
print(traindf.shape)

merged_df = pd.DataFrame

merged_df = pd.merge(extendedcw, traindf, on=["Keyword", "Context", 'Offset', 'Offset.1' ])
merged_df = merged_df.drop_duplicates()

filename = "data/extendedWSDDataset.csv"
merged_df.to_csv(filename)



def create_pwc:
	cwdataset = pd.read_csv ('data/cwdataset.csv')
traindf = pd.read_csv ('data/traindf.csv')

print(cwdataset.shape)
print(traindf.shape)

merged_df = pd.DataFrame

merged_df = pd.merge(cwdataset, traindf, on=["Keyword", "Context", 'Offset', 'Offset.1' ])
merged_df = merged_df.drop_duplicates()

merged_df.head()

filename = "data/cwdatasetwithcomplexity.csv"
merged_df.to_csv(filename)
