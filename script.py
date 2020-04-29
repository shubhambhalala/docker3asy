import os
print("\t\t\t----------------")
print("\t\t\t  Docker3asy    ")
print("\t\t\t----------------")

input("Press Enter: To automatically launch Wordpress site, nextcloud, kali-linux, ubuntu 14.04")

os.system("docker container run -dit -p 8083:443 --name kalios shubhambhalala/kali-nmap-metasploit-shellinabox")
os.system("docker container run -dit -p 8084:4200 --name ubuntu14.04os shubhambhalala/ubuntu14.04-shellinabox")
os.system("docker-compose up")

