import requests
import xmltodict

# reads public steam profiles as xml and writes all owned games into .txt file 
def scrape(url):
    f = open("steamgames.txt", "w")
    try:
        response = requests.get(url)
        xml_raw = xmltodict.parse(response.content)
        for game in xml_raw['gamesList']['games']['game']:
            f.write(game['name'] + '\n')
        print('Finished! Games list was written to "steamgames.txt" in this directory.')

    except requests.exceptions.RequestException as e:
        print(f'Request error: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')
        print('Note: please ensure your Steam profile is public and that you entered the correct URL.')
    f.close()

print('Enter your Steam profile URL: ')
# format: https://steamcommunity.com/id/[USERNAME]/
id = input()
full_url = id + 'games?tab=all&xml=1'
scrape(full_url)

# to do:
# export to cvs 
# support more data (hours played, etc.)
# rewrite for js/ts?
# input leniency?