from thirdai import licensing
licensing.activate("389C76-A6CCC7-BA2CAE-02A467-313084-V3")
from thirdai import neural_db as ndb

db = ndb.NeuralDB(user_id="my_user")
db.from_scratch()
from utils import CSV

csv_files = ['UpdatedResumeDataSet.csv' ]
csv_docs = []

for file in csv_files:
    csv_doc = CSV(
        path=file,
        id_column='DOC_ID',
        strong_columns=['Resume'],
        weak_columns=['Category'],  
        reference_columns=['Resume'])

    csv_docs.append(csv_doc)
source_ids = db.insert(csv_docs, train=True)

search_results = db.search(
    query="what is the keywords related to Software Developer",
    top_k=2,
    on_error=lambda error_msg: print(f"Error! {error_msg}"))

for result in search_results:
    print(result.text())
    # print(result.context(radius=3))
    # print(result.source())
    # print(result.metadata())
    # result.show()
    print('************')