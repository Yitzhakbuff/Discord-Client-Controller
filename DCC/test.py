import requests
import datetime

def get_user_info(user_id):
    response = requests.get(
        f"https://discord.com/api/v9/users/{user_id}",
        headers={"Authorization": "MTIxMTQ2ODk2MTYyMzk2NTcyNw.GAwfmt.MvHoAKVPRlLtufbpMVo6QyN8lp2zWE-OanW2Ws"}
    )
    user_data = response.json()
    xd = "✅" if user_data['premium_type'] == 2 else "❌"
    timestamp = int(user_id) // 4194304 + 1420070400000
    creation_date = datetime.datetime.fromtimestamp(timestamp / 1000)
    print(f"\033[1;34mName:\033[0m {user_data['global_name']}")
    print(f"\033[1;34mUsername:\033[0m {user_data['username']}")
    print(f"\033[1;34mAvatar:\033[0m https://cdn.discordapp.com/avatars/{user_id}/{user_data['avatar']}.png?size=2048")
    print(f"\033[1;34mCreation Date:\033[0m {creation_date}")
    print(f"\033[1;34mNitro:\033[0m {xd}")
user_id = input("\033[1;32mColoca el id del usuario:\033[0m ")
get_user_info(user_id)
