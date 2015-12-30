VK Dialog Photos Downloader
===========================

_ver.: **0.1.1**

## Что это?

Это скрипт, который позволяет скачать все фотографии в максимально доступном
качестве из конкретного диолога из [VKontakte](http://vk.com)

![vk_dpd_2](https://raw.githubusercontent.com/Egregors/vk_dialog_photos_downloader/master/docs/img/vk_dpd_2.png)

## Зачем это?

Это для того, чтобы, например, собрать все фотографии, которые присылал тебе фотограф с сесии,
или собрать в одном месте все _смищные_ картинки твоего самого веселого друга.

## Что там внутри?

Скприт написан на `Python3` и имеет некоторые зависимости, указанные в `requirements.txt`

## Ну и как это запустить?
### Требования

* Python 3.5.x
* [click](http://click.pocoo.org/5/)
* [requests](http://docs.python-requests.org/en/latest/)

### Запуск

0. Скачать репозиторий: `git clone https://github.com/Egregors/vk_dialog_photos_downloader.git`
1. Установить и активировать виртуальное окружение (рекомендуется \ не обязательно):
```
pyvenv env
source env/bin/activate
```
2. Установить зависимоти: `pip install -r requirements.txt`
3. Запустить скрипт, указав необходимые параметры:
```
python vk_dpd.py -r <remixsid> -d <dialog_id>
```

Где **remixsid** — ключ из cookies, который можно посмотреть в консоли для отладки в хроме:

![vk_dpd_0](https://raw.githubusercontent.com/Egregors/vk_dialog_photos_downloader/master/docs/img/vk_dpd_0.png)

Само собой, в это время нужно быть авторизованным в VK.

Где **dialog_id** — уникальный номер диалога, который можно взять из ссылки:

![vk_dpd_1](https://raw.githubusercontent.com/Egregors/vk_dialog_photos_downloader/master/docs/img/vk_dpd_1.png)

### Дополнительные параметры

* `-u` `--username` — название папки, в которую будут скачиваться фотографии, если отсутствует,
название папки генерируется автоматически
* `-v` — флаг, для работы в режиме _debug_, выводит список необработанных ссылок, после завершения
работы