import pprint
from googleapiclient.discovery import build

service = build("customsearch", "v1",
               developerKey="AIzaSyBNpq5EBgxwYUMGeTmOfYGr8wOlX8B_EeY")

res = service.cse().list(
    q='football',
    cx='006354159737151125162:amidb2ooswc',
    searchType='image',
    num=3,
    imgType='clipart',
    fileType='png',
    safe= 'off'
).execute()

if not 'items' in res:
    print ('No result !!\nres is: {}').format(res)
else:
    for item in res['items']:
        print('{}:\n\t{}'.format(item['title'], item['link']))