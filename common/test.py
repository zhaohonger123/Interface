import requests
import json

# accessToken = '2ba63418-d13b-49cd-91ba-ce146857efac'
#
# headers = {
#     'Authorization': 'Bearer {}'.format(accessToken),
#     'Content-Type': 'application/json'
# }
# url = "http://gateway.fxdd6678.cc/game-server/game/api/v1/lobby/getBannerList"
# rq_content = requests.get(url, headers=headers)
# # print(rq_content.text)


data = {
    "resp_code": 0,
    "resp_msg": "succeed"
}

new_data = str(data).replace(" ", "")
print(new_data)
print(type(new_data))
