from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path = 'Social_Network_Ads.csv')
document = loader.load()

print(len(document))  # Number of rows
print(document[0].page_content)  # Content of the first row
print(document[0].metadata)  # Metadata of the first row