import requests
import pandas as pd
import os


# Establish url for data upload
url = 'http://localhost:8888/api/v1/IrevResult/push-result-data-model'

# Establish excel file path
dataPath = 'C:/Users/akand/Documents/Chithub/INEC ERMS/Senate&House_of_Rep_Result_Data.xlsx'

# convert excel to Dataframe
df = pd.read_excel(dataPath, sheet_name='Sheet1')


# define function to upload result with details
def ProcessData():
        body = {
            "Data.Election": Election,
            "Data.PoolingUnit": PoolingUnit,
            "Data.PoolingUnitCode": PoolingUnitCode,
            # "Data.Location"
            "Data.Address": "Unknown",
            "Data.Latitude": "Unknown",
            "Data.longitude": "Unknown",
            "Data.Ward": Ward,
            "Data.LocalGovernment": LocalGovernment,
            "Data.State": State,
            "Data.GeoZone": GeoZone,
            "Data.zone": Zone,
            "Data.presidingOfficer.id": "1",
            "Data.presidingOfficer.name": "System Autogenerator",
            "Data.DocumentUrl": DocumentUrl,
            "Data.votersOnRegister": 0,
            "Data.accreditedVoters": 0,
            "Data.ballotPapersIssuedToPoolingUnit": 0,
            "Data.unusedBallotPapers": 0,
            "Data.rejectedBallot": 0,
            "Data.totalValidVotes": 0,
            "Data.totalUsedBallotPapers": 0,
            "Data.status": "Approved",
            "Data.approvedBy": "System Autogenerator"
        }

        print('Attempting to upload data')
        print(body)

        data_upload = requests.post(url, data=body)
        response = data_upload.status_code
        print(response)
        # print(data_upload.request.body)

        if response == 202:
            print('Data Upload Successful')
            print(data_upload.json())

        else:
            print(response)
            print(data_upload.json())
            print('Data Upload Failed')






for i, row in df.iterrows():
    if i >= 0:
        print('-------------------------------------------')
        print(i)
        Election = row['Election']
        print(Election)
        PoolingUnit = row['PoolingUnit']
        PoolingUnitCode = row['PoolingUnitCode']
        print(PoolingUnitCode)
        Ward = row['Ward']
        State = row['State']
        print(State)
        LocalGovernment = row['LocalGovernment']
        GeoZone = row['GeoZone']
        Zone = row['Zone']
        DocumentUrl = row['DocumentUrl']
        print(DocumentUrl)
        print('-------------------------------------------')


        # Triggering function to upload result
        ProcessData(row)








print('Processing Completed')








