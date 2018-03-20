import os
import io
from PIL import Image
from .models import *

# import glob, os
# from IPython.core.display import Image
def check_login(username,Password):
    import sqlite3
    import pandas as pd
    file = "../SRS/db.sqlite3"
    conn = sqlite3.connect(file)
    user = pd.read_sql_query("SELECT user_name,password FROM SRS_user", conn, index_col=None)
    k=user.loc[(user.user_name==username) & (user.password==Password)]
    print(k)
    if k.empty:
        return 0
    return 1





def assure_path_exists(path):
    dir = os.path.dirname(path)
    dir = dir + "/sihimages"
    if not os.path.exists(dir):
        print
        "I am creating directory"
        os.makedirs(dir)


def uploaded_aadhar(username):
    if dicto[username][0] == 1:
        return 1
    else:
        return 0


def uploaded_pancard(username):
    if dicto[username][1] == 1:
        return 1
    else:
        return 0


def uploaded_otherdocs(username):
    if dicto[username][2] == 1:
        return 1
    else:
        return 0


# global dictionary having variables to check whether uploaded or not
dicto = {}


# [a,p,o,cnt]
def sign_up(username,password,mobile):
    import sqlite3
    import pandas as pd
    file = '/home/super--user/PycharmProjects/SRS/db.sqlite3'
    conn = sqlite3.connect(file)
    # conn.row_factory = sqlite3.Row  # This is the important part, here we are setting row_factory property of connection object to sqlite3.Row(sqlite3.Row is an implementation of row_factory)
    user = pd.read_sql_query("SELECT * FROM SRS_user", conn, index_col=None)
    an=pd.DataFrame([[username,password,mobile]],columns=['user_name','password','mobile_no'])
    print(an)
    ann=an.append(user,ignore_index=True)
    print(ann)
    ann.to_sql('SRS_user', conn,if_exists='replace', index=False)

def savedetails(request):
    s=10


def upload(username, doc, image_path):
    import sqlite3
    import os
    import pandas as pd
    file = '/home/super--user/PycharmProjects/SRS/db.sqlite3'
    conn = sqlite3.connect(file)
    # conn.row_factory = sqlite3.Row  # This is the important part, here we are setting row_factory property of connection object to sqlite3.Row(sqlite3.Row is an implementation of row_factory)
    user = pd.read_sql_query("SELECT * FROM SRS_user", conn, index_col=None)

    my_image = Image.open(image_path)
    add_ad = "aadhaar"
    add_pn = "pancard"
    add_hsc = "hsc"
    add_ssc = "ssc"
    add_caste = "caste"

    abs_path = os.path.join(os.getcwd())
    abs_path = abs_path + "/sihimages"

    my_image = Image.open(image_path)
    filename, extension = os.path.splitext(image_path)
    # check directory created

    assure_path_exists(abs_path)
    if (doc == 1):  # aadhar
        my_image.save('/home/super--user/PycharmProjects/SRS/sihimages/{}_{}{}'.format(username, add_ad, extension))

        path = "/home/super--user/PycharmProjects/SRS/sihimages/" + username + "_" + add_ad + extension

        user.loc[user['user_name'] == username, 'aadhaar'] = path

    if (doc == 2):  # pancard
        my_image.save('/home/super--user/PycharmProjects/SRS/sihimages/{}_{}{}'.format(username, add_pn, extension))

        path = "/home/super--user/PycharmProjects/SRS/sihimages/" + username + "_" + add_pn + extension

        user.loc[user['user_name'] == username, 'pancard'] = path

    if (doc == 3):  # hsc
        my_image.save('/home/super--user/PycharmProjects/SRS/sihimages/{}_{}{}'.format(username, add_hsc, extension))

        path = "/home/super--user/PycharmProjects/SRS/sihimages/" + username + "_" + add_hsc + extension

        user.loc[user['user_name'] == username, 'hsc'] = path

    if (doc == 4):  # ssc
        my_image.save('/home/super--user/PycharmProjects/SRS/sihimages/{}_{}{}'.format(username, add_ssc, extension))

        path = "/home/super--user/PycharmProjects/SRS/sihimages/" + username + "_" + add_ssc + extension

        user.loc[user['user_name'] == username, 'ssc'] = path

    if (doc == 5):  # caste_certificate
        my_image.save('/home/super--user/PycharmProjects/SRS/sihimages/{}_{}{}'.format(username, add_caste, extension))

        path = "/home/super--user/PycharmProjects/SRS/sihimages/" + username + "_" + add_caste + extension

        user.loc[user['user_name'] == username, 'caste_certificate'] = path
    print(user)
    user.to_sql('SRS_user', conn, if_exists='replace', index=False)


def replace(username, doc, image_path):
    import sqlite3
    import pandas as pd
    import os
    file = '/home/super--user/PycharmProjects/SRS/db.sqlite3'
    conn = sqlite3.connect(file)
    # conn.row_factory = sqlite3.Row  # This is the important part, here we are setting row_factory property of connection object to sqlite3.Row(sqlite3.Row is an implementation of row_factory)
    user = pd.read_sql_query("SELECT * FROM SRS_user", conn, index_col=None)

    my_image = Image.open(image_path)
    add_ad = "aadhaar"
    add_pn = "pancard"
    add_hsc = "hsc"
    add_ssc = "ssc"
    add_caste = "caste"

    # stuffs all the images from the image directory

    abs_path = os.path.join(os.getcwd())
    abs_path = abs_path + "/sihimages"
    ll = []
    for file in os.listdir(abs_path):
        if file.endswith(".png"):
            ll.append(os.path.join(abs_path, file))

    for file in os.listdir(abs_path):
        if file.endswith(".jpg"):
            ll.append(os.path.join(abs_path, file))

    print(ll)

    # ll contains the image directory files

    my_image = Image.open(image_path)
    filename, extension = os.path.splitext(image_path)
    # check directory created

    final_extension = ""

    # verifies that the name of the file matches with the other file image .

    for i in ll:
        f, extension = os.path.splitext(i)
        temp = []
        temp = f.split('/')
        if temp[-1] == username + "_" + add_ad:
            final_extension = extension
            break

    print(filename)
    assure_path_exists(abs_path)

    if (doc == 1):  # aadhar
        file_to_be_deleted = username + "_" + add_ad + final_extension
        os.remove(abs_path + "/" + file_to_be_deleted)
        my_image = Image.open(image_path)
        my_image.save('/home/super--user/PycharmProjects/SRS/sihimages/{}_{}{}'.format(username, add_ad, extension))
        path = "/home/super--user/PycharmProjects/SRS/sihimages/" + username + "_" + add_ad + extension

    if (doc == 2):  # pancard
        file_to_be_deleted = username + "_" + add_pn + final_extension
        print(file_to_be_deleted)
        os.remove(abs_path + "/" + file_to_be_deleted)
        my_image = Image.open(image_path)
        my_image.save('/home/super--user/PycharmProjects/SRS/sihimages/{}_{}{}'.format(username, add_pn, extension))
        path = "/home/super--user/PycharmProjects/SRS/sihimages/" + username + "_" + add_pn + extension

    if (doc == 3):  # hsc
        file_to_be_deleted = username + "_" + add_hsc + final_extension
        os.remove(abs_path + "/" + file_to_be_deleted)
        my_image = Image.open(image_path)
        my_image.save('/home/super--user/PycharmProjects/SRS/sihimages/{}_{}{}'.format(username, add_hsc, extension))
        path = "/home/super--user/PycharmProjects/SRS/sihimages/" + username + "_" + add_hsc + extension

    if (doc == 4):  # ssc
        file_to_be_deleted = username + "_" + add_ssc + final_extension
        os.remove(abs_path + "/" + file_to_be_deleted)
        my_image = Image.open(image_path)
        my_image.save('/home/super--user/PycharmProjects/SRS/sihimages/{}_{}{}'.format(username, add_ssc, extension))
        path = "/home/super--user/PycharmProjects/SRS/sihimages/" + username + "_" + add_ssc + extension

    if (doc == 5):  # caste_certificate
        file_to_be_deleted = username + "_" + add_caste + final_extension
        os.remove(abs_path + "/" + file_to_be_deleted)
        my_image = Image.open(image_path)
        my_image.save('/home/super--user/PycharmProjects/SRS/sihimages/{}_{}{}'.format(username, add_caste, extension))
        path = "/home/super--user/PycharmProjects/SRS/sihimages/" + username + "_" + add_caste + extension


def call(username, replac, doctype):
    # if username not in dicto.keys():
    # dicto[username] = [0, 0, 0, 0]
    upload(username)
