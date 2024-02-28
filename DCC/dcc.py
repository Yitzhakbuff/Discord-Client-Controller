import requests
import os
import socket
import deb

def msgsend(headers):
    texto=deb.inputx("[Discord] pon el mensaje:")
    canal_id=deb.inputx("[Discord] pon el id del canal:")
    r=requests.post(f"https://discord.com/api/v9/channels/{canal_id}/messages", headers=headers, data={"content":texto})
    deb.debug(response=r)
    input()
    main_commands()
def typing(headers):
    canal_id=deb.inputx("[Discord] pon el id del canal:")
    r=requests.post(f"https://discord.com/api/v9/channels/{canal_id}/typing", headers=headers)
    deb.debug(response=r)
    input()
    main_commands()
def pinmsg(headers):
    canal_id=deb.inputx("[Discord] pon el id del canal:")
    msg_id=deb.inputx("[Discord] pon el id del mensaje:")
    r=requests.put(f"https://discord.com/api/v9/channels/{canal_id}/pins/{msg_id}", headers=headers)
    deb.debug(response=r)
    input()
    main_commands()
def callring(headers):
    canal_id=deb.inputx("[Discord] pon el id del canal:")
    r=requests.post(f"https://discord.com/api/v9/channels/{canal_id}/call/ring", headers=headers)
    deb.debug(response=r)
    input()
    main_commands()
def silencefriends(headers):
    r=requests.get(f"https://discord.com/api/v9/users/@me/relationships", headers=headers)
    deb.debug(response=r)
    #usuarios=r.json()
    #for usuario in usuarios:
    #
    r=requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers)
    for usuario in r.json():
        requests.delete(f"https://discord.com/api/v9/channels/{usuario['id']}?silent=false", headers=headers)
    input()
    main_commands(headers=headers)


def main_commands(headers):
    deb.clear()
    print("\033[1;36;40m Lista de Comandos \033[0m")
    print("\033[1;35;40m-------------------\033[0m")
    comandos = ["msgsend", "typing", "pingmsg", "callring", "silencefriends"]
    for i, comando in enumerate(comandos, start=1):
        print(f"\033[1;33;40m{i}. \033[1;34;40m{comando}")
    entrada = input(f"\n\033[1;36;40m{socket.gethostname()}\033[0m \033[1;33;40m=>\033[0m ")
    if entrada == "1":
        msgsend(headers=headers)
    if entrada == "2":
        typing(headers=headers)
    if entrada == "3":
        pinmsg(headers=headers)
    if entrada == "4":
        callring(headers=headers)
    if entrada == "5":
        silencefriends(headers=headers)
        
def main():
    deb.clear()
    token = deb.inputx("[Discord] pon el token: ")
    deb.info("Conectandose al cliente...")
    client = {'Authorization': f"{token}"}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=client)
    deb.debug(response=response)
    if response.status_code == 200:
        data = response.json()
        deb.info(f"Conectado al cliente: \033[1;36;40m{data.get('global_name')}\033[0m (\033[1;35;40m{data.get('username')}\033[0m)")
        deb.info("Haga click para entrar a la sala de comandos \033[1;36;10m[Presiona cualquier tecla]")
        input()
        main_commands(headers=client)
    else:
        deb.error("No se pudo conectar.")
