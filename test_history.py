from get_post_file import save_history
import os
import json
import pytest

history_file = 'test_upload_history.json'
# def save_history(file_path, download_link):
#     history = []
#     print('NAME_FILE', history_file)
#
#     if os.path.exists(history_file):
#         with open(history_file, 'r') as f:
#             history = json.load(f)
#     history.append({'file_name':os.path.basename(file_path), 'download_link': download_link})
#     with open(history_file, 'w') as f:
#         json.dump(history, f, indent=4)

def test_save_history():
    test_file_path = 'test_file.txt'
    test_download_link = 'https://store1.gofile.io/example'
    save_history(test_file_path, test_download_link)

    with open('test_upload_history.json', 'r') as f:
        history = json.load(f)
        assert len(history) == 1
        assert history[0]['file_name'] == test_file_path
        assert history[0]['download_link'] == test_download_link

    os.remove('test_upload_history.json')

# test_save_history()
