# Falla

A search-engine-cli-scraper for more than 15 search engines, including Google. duckduckgo, Bing, Ask, etc...

## Requirements
- Python (3.x)
- Pip3
- Docker (Not required for all search-engine)

## How to install

- You need to install all requirements :
```shell-script
pip3 install -r requirements.txt
```
- Install geckodriver :
```shell-script
# For linux users
# cd /home/your-user-name
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
export PATH=$PATH:/path-to-extracted-file/.
```

- Pull and run the splash-scrap module (Some of search engine need this):
```shell-script
docker run -p 8050:8050 scrapinghub/splash
```

- Replace `example.config.txt` by `config.txt` and provide the running IP for the splash-scrap

## How to launch

How to use Falla:
```shell-script
usage: main.py [-h] [-e ENGINE] [-q QUERY]

optional arguments:
  -h, --help            show this help message and exit
  -e ENGINE, --engine ENGINE
                        The search engine
  -q QUERY, --query QUERY
                        The query text
```

- To list all search-engine:
```shell-script
python3 -m app.main
```

- To search something:
```shell-script
$ python3 -m app.main -e google -q "sanix darker"
# output
[+] Falla [the search-engine-scraper]
[+] Searching results for 'sanix darker' on 'Google' :

|> Sanix-Darker (S@n1X) · GitHub
|  https://github.com/Sanix-Darker
|  github.com › Sanix-Darker

|> Sanix Darker (@sanix_code) • Photos et vidéos Instagram
|  https://www.instagram.com/sanix_code/?hl=fr
|  www.instagram.com › sanix_code

|> Antiddos System
|  https://awesomeopensource.com/project/Sanix-Darker/AntiDDOS-system
|  awesomeopensource.com › project

|> Sanix Darker - YouTube
|  https://www.youtube.com/channel/UClEW-2tqT3Z9puUDbTSouXA
|  www.youtube.com › channel

|> Sanix Darker - Speaker Profile @ Sessionize.com
|  https://sessionize.com/sanix-darker/
|  sessionize.com › sanix-darker

|> User Sanix darker - Stack Overflow
|  https://stackoverflow.com/users/6858775/sanix-darker
|  stackoverflow.com › users › sanix-d...

|> User Sanix Darker - Stack Overflow
|  https://stackoverflow.com/users/8633733/sanix-darker
|  stackoverflow.com › users › sanix-d...

|> Php in Cameroon | Git Awards
|  http://git-awards.com/users?country=cameroon&language=php&type=country
|  git-awards.com › users

|> Projects · Sanix-Darker/API_SMS · GitHub
|  https://gh-dark.rauchg.now.sh/Sanix-Darker/API_SMS/projects
|  gh-dark.rauchg.now.sh › projects

```

## Author

- Sanix-darker