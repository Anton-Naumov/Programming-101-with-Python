import requests
from models import session
from models import BgServers
from sqlalchemy import func


register_url = 'http://register.start.bg/'


def craw_bg_servers(id_start, id_end):
    for id in range(id_start, id_end):
        url = f'{register_url}link.php?id={id}'
        try:
            request = requests.get(url, timeout=1)

            if request.status_code == 200 and 'Server' in request.headers:
                # send_request(request.headers['Server'].split('/')[0], id, request.url)
                add_in_database(id, request.headers['Server'].split('/')[0], request.url)
        except Exception:
            pass


def add_in_database(page_id, server, url):
    print(server)
    session.add(BgServers(page_id=page_id, server=server, url=url))
    session.commit()


def get_server_histogram():
    servers = session.query(BgServers.server, func.count(BgServers.id))\
        .group_by(BgServers.server).all()

    print({r[0]: r[1] for r in servers})


# def send_request(server, id, url):
#     requests.post(
#         'http://192.168.0.14:5000/',
#         data={
#             'server': server,
#             'id': id,
#             'url': url
#         }
#     )
#     print(
#         {
#             'server': server,
#             'id': id,
#             'url': url
#         }
#     )


if __name__ == '__main__':
    craw_bg_servers(15000, 16000)
