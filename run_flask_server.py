from flask import Flask
from flask import send_file
from matplotlib import pyplot as plt
import logging
import requests
import time
import httpx
from datetime import datetime
from flask import render_template


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
pool = httpx.Client()



@app.route('/github/<user_name>')
def handle_get(user_name):
    response = pool.get(f'https://api.github.com/users/{user_name}/repos')

    now = datetime.now()
    logging.info(f'Request to server : https://api.github.com/users/{user_name}/repos time: {now.strftime("%Y-%m-%d %H:%M:%S")}')
    logging.info(f'Response : {response.status_code}')

    repo_list_len = list()
    dict_to_display = dict()
    counter = 1
    for item in response.json():
        repo_list_len.append(len(item['name']))
        dict_to_display[counter] = '* ' * len(item['name'])
        counter += 1

    # plt.hist(repo_list_len)
    # plt.title('Histogram of length repo ')
    # plt.savefig('histogram.png')
    # send_file('histogram.png', mimetype='image/png')
    return render_template('histogram.html', dictionary=dict_to_display)


if __name__ == '__main__':
    app.run()
