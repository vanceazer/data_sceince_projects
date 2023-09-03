import requests
import pandas as pd
import numpy as np
import schedule
import threading
import time



# function to schedule the whole process to run at intervals
# def total_process():
def trd():

    # Define urls
    BASE_URL = 'https://prod-etraffika.azurewebsites.net'
    INSTANCE_LOGGER_NEW_ENTRY = f'{BASE_URL}/api/instancelogger/batch?statusId=6&newStatusId=7&pageSize=2'
    # INSTANCE_UPDATE = f'{BASE_URL}/api/instancelogger/update/status/id'

    # Synchronizer API
    API_SYNCHRONIZER = f'{BASE_URL}/api/synchronizer'

    # picking instance log that the violation scheduler has processed
    # Convert Instance log to dataframe
    instance_data = requests.get(INSTANCE_LOGGER_NEW_ENTRY)
    if instance_data.status_code == 200:
        instance_df = pd.DataFrame(instance_data.json()['lprLog'])
        # Accounting for if the dataframe is empty
        if instance_df.empty is True:
            print('Dataframe is empty')
            print('--------------------------------------')
        else:
            instance_needed = instance_df
            instance_plateno = instance_needed['plateNumber']
            instance_ids = instance_needed['id']
            # print(instance_df)
            # print(instance_plateno)

            # function to convert list to strings
            def listToString(s):
                # initialize an empty string
                str1 = ""

                # traverse in the string
                for ele in s:
                    str1 = ele

                    # return string
                return str1
            # function to change instance log id to api processing

            # function to synchronize instance log using the synchronization API
            def api_synchronization(id):
                body = {
                    "id": instance_id,
                    "CreatedATime": time_created,
                    "PlateNumber": plates,
                    "ImageUrl": image_url,
                    "PublicId": public_id,
                    "Latitude": latitude_string,
                    "Longitude": longitude_string,
                    "CarModel": car_model,
                    "CarMake": car_make,
                    "CarColor": car_color,
                    "Classification": classification_plate,
                    "Code": code_plate,
                    "StatusId": status_id,
                    "IsTaxi": is_taxi,
                    "CameraId": camera_id,
                    "Orientation": orientation
                }
                r_synchronize = requests.post(API_SYNCHRONIZER, json=body)
                print(r_synchronize.status_code)
                if r_synchronize.status_code == 200:
                    print('Synchronization Successful for', plates)

                else:
                    print('Synchronization failed')

            # picking each id in the instance log and processing it
            for ids in instance_ids.values:
                # extracting the needed values corresponding to the id being processed
                plate_compare = instance_needed[instance_needed['id'] == ids]
                plates = listToString(plate_compare['plateNumber'])
                # print(plates)
                longitude_string = listToString(plate_compare['longitude'])
                # print(longitude_string)
                latitude_string = listToString(plate_compare['latitude'])
                # print(latitude_string)
                instance_id = int(plate_compare['id'].values)
                print(instance_id, plates)
                time_created = listToString(plate_compare['createdATime'])
                # print(time_created)
                image_url = listToString(plate_compare['imageUrl'])
                # print(image_url)
                public_id = listToString(plate_compare['publicId'])
                # print(public_id)
                car_model = listToString(plate_compare['carModel'])
                # print(car_model)
                car_make = listToString(plate_compare['carMake'])
                # print(car_make)
                car_color = listToString(plate_compare['carColor'])
                # print(car_color)
                classification_plate = listToString(plate_compare['classification'])
                # print(classification_plate)
                code_plate = listToString(plate_compare['code'])
                # print(code_plate)
                status_id = int(plate_compare['statusId'])
                # print(status_id)
                is_taxi = bool(plate_compare['isTaxi'].values)
                # print(is_taxi)
                camera_id = listToString(plate_compare['cameraId'])
                # print(camera_id)
                orientation = listToString(plate_compare['orientation'])
                # print(orientation)

                # synchronizing the instance log using the synchronizing API
                api_synchronization(ids)
                time.sleep(1)

    else:
        print('Unable to pull instance from instance log')




t1 = threading.Thread(target=trd)
t2 = threading.Thread(target=trd)
t3 = threading.Thread(target=trd)
t4 = threading.Thread(target=trd)
t5 = threading.Thread(target=trd)

t1.start()
# time.sleep(3)
# t2.start()
# time.sleep(3)
# t3.start()
# time.sleep(3)
# t4.start()
# time.sleep(3)
# t5.start()


#
# t1.join()
# t2.join()
# t3.join()
# t4.join()
# t5.join()







# scheduling the app to run at the specified intervals
# schedule.every(10).seconds.do(total_process)
#
# while True:
#     schedule.run_pending()
#     time.sleep(2)
