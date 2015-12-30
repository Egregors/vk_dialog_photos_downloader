# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#   VK Dialog Photo Downloader
#   ==========================
#   ver.: 0.1.1
#
#   @egregors (2015)
import json
import os
import re
import urllib
import click
import urllib.request
import requests


@click.command()
@click.option('-r', '--remixsid', help='remixsid', required=True)
@click.option('-d', '--dialog_id', help='dialog id ("sel=DIALOG_ID" from URL)', required=True)
@click.option('-u', '--username', help='the name of the interlocutor', default=None)
@click.option('-v', '--debug', is_flag=True, default=False)
def download_photos(remixsid: str, dialog_id: str, username: str, debug: bool):
    """
    Это инфа оп оп

    :param remixsid: уникальный id из cookies
    :param dialog_id: id целевого диалога
    :param username: название папки, в которую будут качаться фотографии
    :param debug: флаг для режима DEBUG
    :return:
    """
    data = {
        'act': 'show',
        'al': 1,
        'loc': 'im',
        'w': 'history' + dialog_id + '_photo',
        'offset': 0,
        'part': 1
    }

    bound = {
        "count": 10000,
        "offset": 0
    }

    url = 'http://vk.com/wkview.php'

    click.secho('Создание папки для загрузок..')
    try:
        if username is None:
            username = 'user_{}'.format(dialog_id)
        os.mkdir(username)
    except OSError:
        click.secho('Папка для загрузок уже существует')

    if os.path.exists(username):
        os.chdir(username)
    else:
        click.echo('OP')
    part = 1
    data_for_download = []

    print('Подготовка ссылок..', end='.')
    while bound['offset'] < bound['count']:
        data['offset'] = bound['offset']
        content = requests.post(
                url, cookies={"remixsid": remixsid}, params=data).text

        json_data_offset = re.compile(
                '\{"count":.+?,"offset":.+?\}').search(content)

        bound = json.loads(
                content[json_data_offset.span()[0]:json_data_offset.span()[1]])

        bound['count'] = int(bound['count'])
        bound['offset'] = int(bound['offset'])

        links = re.compile('&quot;http://cs.+?"').findall(content)

        for link in links:

            vk_link_temp = re.search('http://cs\d+.vk.me.\w\d+/', link)
            if vk_link_temp is not None:
                vk_link = vk_link_temp.group()
                if link.find('z_&') != -1:
                    tail = link[link.find('z_&') + 16:]
                    result_link = vk_link + tail[:tail.find('&quot;,')] + '.jpg'
                    img_link = result_link
                elif link.find('y_&') != -1:
                    tail = link[link.find('y_&') + 16:]
                    result_link = vk_link + tail[:tail.find('&quot;,')] + '.jpg'
                    img_link = result_link
                else:
                    tail = link[link.find('x_&') + 16:]
                    result_link = vk_link + tail[:tail.find('&quot;,')] + '.jpg'
                    img_link = result_link

                data_for_download.append({
                    'raw_link': link,
                    'link': img_link,

                })
            else:
                click.secho('Плохая ссылка: {}'.format(link), bold=True, fg='red')
        print('.', end='.')
        part += 1
    print('.')
    file_count = 0
    bad_urls = []
    click.secho('Начало загрузки..', fg='green')
    with click.progressbar(data_for_download) as data_list:
        for link in data_list:
            # for degub
            if requests.get(link['link'].replace('\n', '')).status_code != 200:
                bad_urls.append(link)
            else:
                urllib.request.urlretrieve(link['link'], str(file_count) + ".jpg")
                file_count += 1

    click.secho('Готово! Скачено {} фото'.format(file_count), fg='green')

    if len(bad_urls) > 0 and debug is True:
        click.secho('Плохие ссылки:')
        for url in bad_urls:
            click.secho('RAW:\n{}\nLINK:\n{}\n'.format(url['raw_link'], url['link']))


if __name__ == '__main__':
    download_photos()
