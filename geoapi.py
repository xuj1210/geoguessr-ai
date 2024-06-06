import requests

# GeoGuessr API
# [!] All Endpoints extracted from Android app version 2.8.2
#   API Endpoints:
#       v3/accounts/delete
#       v3/accounts/signin
#       v3/apple/signin
#       v3/experiments
#       v3/facebook/signin
#       v3/games
#       v3/games/streak
#       v3/googleplus/signin
#       v3/likes
#       v3/profiles
#       v3/profiles/maps
#       v3/profiles/pin
#       v3/profiles/resetpassword
#       v3/profiles/setpassword
#       v3/scores/maps
#       v3/search/user
#       v3/social/badges/claim
#       v3/social/badges/unclaimed
#       v3/social/events/unfinishedgames
#       v3/social/friends
#       v3/social/friends/received
#       v3/social/maps/browse/featured
#       v3/social/maps/browse/popular/all
#       v3/social/maps/browse/popular/official
#       v3/subscriptions
#       v3/subscriptions/google
#       v3/subscriptions/plans
#       v3/version/update
#       v4/app/ads/reward
#       v4/app/features/android
#       v4/app/logs
#       v4/app/onboarding/completed
#       v4/app/state
#       v4/chat/emotes
#       v4/feed/friends
#       v4/feed/private
#       v4/games/infinity
#       v4/games/infinity/challenge/new
#       v4/games/infinity/challenge/random
#       v4/games/infinity/challenges
#       v4/games/infinity/guess
#       v4/games/infinity/history
#       v4/games/infinity/inbox
#       v4/games/infinity/location-overview
#       v4/games/infinity/next
#       v4/games/infinity/outbox
#       v4/games/infinity/share
#       v4/games/infinity/shared-location
#       v4/parties
#       v4/pushnotification/register
#       v4/search/map

referrer = "u9bj8ejMnj9scDPB"

# obtain through response.token
gameid = "afxpT3L9v8QKMzXt"

BASE_URL = (
    f"https://www.geoguessr.com/api/v3/games/{gameid}"  # Base URL for all endpoints
)
# _ncfa_TOKEN = f"AlcrsINTVGvLqaiyJZPTuai9Gyqa3X6yARuOwO%2Fm2a8%3DfigXGpM2GISqHcgN74oPi0F4ASnwoKmeBA3KA9hjrzcg99FGx3yQiXaSnyOHGbiy1XFly4gcnsOqu%2FMwiLiQPbF2dTH%2B9Baw2NRG1aC3fpk%3D"  # Insert your _ncfa token here

# # Create a session object and set the _ncfa cookie
# session = requests.Session()
# session.cookies.set("_ncfa", _ncfa_TOKEN, domain="www.geoguessr.com")


headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "content-type": "application/json",
    "priority": "u=1, i",
    "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-client": "web",
    "cookie": "_ncfa=hRTndHvPP9OI1p5Ak1rBkxYGBdNHO8ji6I4HR5ZYbAI%3DfigXGpM2GISqHcgN74oPi0F4ASnwoKmeBA3KA9hjrzcg99FGx3yQiXaSnyOHGbiy1XFly4gcnsOqu%2FMwiLiQPWRCf0HOEA7kOfUcgHxJ%2FOI%3D",
    # "Referer": "https://www.geoguessr.com/challenge/Ywz6chjYnHbU3Ooo",
    "Referrer-Policy": "strict-origin-when-cross-origin",
}


# fetch(
#     "https://www.geoguessr.com/api/v3/games/FYMmVY4MHg5G99Xd",
#     {
#         "headers": {
#             "accept": "*/*",
#             "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
#             "content-type": "application/json",
#             "priority": "u=1, i",
#             "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
#             "sec-ch-ua-mobile": "?0",
#             "sec-ch-ua-platform": '"Windows"',
#             "sec-fetch-dest": "empty",
#             "sec-fetch-mode": "cors",
#             "sec-fetch-site": "same-origin",
#             "x-client": "web",
#             "cookie": '_cfuvid=WPyB4LPagK9m_QSbW1xXflrDwhrw_FWGMdwfd9FMEsk-1717567959504-0.0.1.1-604800000; g_state={"i_l":0}; devicetoken=E136E637FD; session=eyJTZXNzaW9uSWQiOiIyMHd6MTlmaHEyNHRuaG0zb212ZXFtNWV5MGw0bDFiYyIsIkV4cGlyZXMiOiIyMDI0LTA2LTA1VDE5OjE2OjM1LjgzOTUyMTVaIn0%3D; _ncfa=hRTndHvPP9OI1p5Ak1rBkxYGBdNHO8ji6I4HR5ZYbAI%3DfigXGpM2GISqHcgN74oPi0F4ASnwoKmeBA3KA9hjrzcg99FGx3yQiXaSnyOHGbiy1XFly4gcnsOqu%2FMwiLiQPWRCf0HOEA7kOfUcgHxJ%2FOI%3D',
#             "Referer": "https://www.geoguessr.com/challenge/Ywz6chjYnHbU3Ooo",
#             "Referrer-Policy": "strict-origin-when-cross-origin",
#         },
#         "body": '{"token":"FYMmVY4MHg5G99Xd","lat":50.59719607324223,"lng":-104.28635223807014,"timedOut":false}',
#         "method": "POST",
#     },
# )

data = f'{{"token":"{gameid}","lat":19.472139102492733,"lng":27.954903911028065,"timedOut":false}}'


# Send a GET request to the profiles endpoint
profiles = requests.post(BASE_URL, headers=headers, data=data)

# Check if the request was successful
if profiles.status_code == 200:
    # Print the response as text
    print(profiles.text)
else:
    # Print an error message
    print(f"Error: {profiles.status_code}")

# fetch("https://www.geoguessr.com/api/v3/games/OyGYuNS1S9mRHyEU", {
#   "headers": {
#     "accept": "*/*",
#     "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
#     "content-type": "application/json",
#     "priority": "u=1, i",
#     "sec-ch-ua": "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "x-client": "web",
#     "cookie": "_cfuvid=WPyB4LPagK9m_QSbW1xXflrDwhrw_FWGMdwfd9FMEsk-1717567959504-0.0.1.1-604800000; g_state={\"i_l\":0}; devicetoken=E136E637FD; session=eyJTZXNzaW9uSWQiOiIyMHd6MTlmaHEyNHRuaG0zb212ZXFtNWV5MGw0bDFiYyIsIkV4cGlyZXMiOiIyMDI0LTA2LTA1VDE5OjE2OjM1LjgzOTUyMTVaIn0%3D; _ncfa=hRTndHvPP9OI1p5Ak1rBkxYGBdNHO8ji6I4HR5ZYbAI%3DfigXGpM2GISqHcgN74oPi0F4ASnwoKmeBA3KA9hjrzcg99FGx3yQiXaSnyOHGbiy1XFly4gcnsOqu%2FMwiLiQPWRCf0HOEA7kOfUcgHxJ%2FOI%3D",
#     "Referer": "https://www.geoguessr.com/challenge/7NBTWRGzWBTQY5Td",
#     "Referrer-Policy": "strict-origin-when-cross-origin"
#   },
#   "body": "{\"token\":\"OyGYuNS1S9mRHyEU\",\"lat\":19.472139102492733,\"lng\":27.954903911028065,\"timedOut\":false}",
#   "method": "POST"
# });

# curl 'https://www.geoguessr.com/api/v3/games/OyGYuNS1S9mRHyEU' \
#   -H 'accept: */*' \
#   -H 'accept-language: en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7' \
#   -H 'content-type: application/json' \
#   -H 'cookie: _cfuvid=WPyB4LPagK9m_QSbW1xXflrDwhrw_FWGMdwfd9FMEsk-1717567959504-0.0.1.1-604800000; g_state={"i_l":0}; devicetoken=E136E637FD; session=eyJTZXNzaW9uSWQiOiIyMHd6MTlmaHEyNHRuaG0zb212ZXFtNWV5MGw0bDFiYyIsIkV4cGlyZXMiOiIyMDI0LTA2LTA1VDE5OjE2OjM1LjgzOTUyMTVaIn0%3D; _ncfa=hRTndHvPP9OI1p5Ak1rBkxYGBdNHO8ji6I4HR5ZYbAI%3DfigXGpM2GISqHcgN74oPi0F4ASnwoKmeBA3KA9hjrzcg99FGx3yQiXaSnyOHGbiy1XFly4gcnsOqu%2FMwiLiQPWRCf0HOEA7kOfUcgHxJ%2FOI%3D' \
#   -H 'origin: https://www.geoguessr.com' \
#   -H 'priority: u=1, i' \
#   -H 'referer: https://www.geoguessr.com/challenge/7NBTWRGzWBTQY5Td' \
#   -H 'sec-ch-ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"' \
#   -H 'sec-fetch-dest: empty' \
#   -H 'sec-fetch-mode: cors' \
#   -H 'sec-fetch-site: same-origin' \
#   -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36' \
#   -H 'x-client: web' \
#   --data-raw '{"token":"OyGYuNS1S9mRHyEU","lat":19.472139102492733,"lng":27.954903911028065,"timedOut":false}'
