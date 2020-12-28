    ##### Helper methods #######
import requests
from bs4 import BeautifulSoup

##### For multiple files ######

def download_file(link, filename):
    mid_file_request = requests.get(link, stream=True)
    if (mid_file_request.status_code != 200):
        raise Exception("Failed to download {0}".format(url))
        
    with open(filename, 'wb+') as saveMidFile:
        saveMidFile.write(mid_file_request.content)

def download_midi(midi_url, path):
    """
    For single MIDI files.
    """
    !wget $midi_url --directory-prefix "$path" > download_midi.log

def download_midi_files(url, output_path):
    def get_file_name(link):
        filename = link.split('/')[::-1][0]
        return filename
    
    site_request = requests.get(url)
    if (site_request.status_code != 200):
        raise Exception("Failed to access {0}".format(url))
    
    soup = BeautifulSoup(site_request.content, 'html.parser')
    link_urls = soup.find_all('a')
        # Because midi files are stored as <a> in html.

    for link in link_urls:
        href = link['href']
        if (href.endswith(".mid")):
            file_name = get_file_name(href)
            download_path = output_path + "/" + file_name
            midi_request = download_file(href, download_path)

def start_midis_download(folder, url):
    !mkdir $folder # It is fine if this command fails when the directory already exists.
    download_midi_files(url, folder)

    
