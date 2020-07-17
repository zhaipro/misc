from xml.etree import ElementTree

import requests


def issuetoken(secret_key):
    url = f'https://chinaeast2.api.cognitive.azure.cn/sts/v1.0/issuetoken'
    headers = {'Ocp-Apim-Subscription-Key': secret_key}
    r = requests.post(url, headers=headers)
    return r.text


def _microsoft_to_audio(body, token):
    url = 'https://chinaeast2.tts.speech.azure.cn/cognitiveservices/v1'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-type': 'application/ssml+xml',
        'X-Microsoft-OutputFormat': 'audio-16khz-32kbitrate-mono-mp3',
        'User-Agent': 'tests'
    }
    r = requests.post(url, data=body, headers=headers)
    return r


def microsoft_to_audio(text, name, token):
    xml_body = ElementTree.Element('speak', version='1.0')
    xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'zh-CN')
    xml_body.set('xmlns:mstts', 'https://www.w3.org/2001/mstts')
    voice = ElementTree.SubElement(xml_body, 'voice')
    voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'zh-CN')
    voice.set('name', f'Microsoft Server Speech Text to Speech Voice ({name})')
    voice.text = text
    body = ElementTree.tostring(xml_body)
    r = _microsoft_to_audio(body, token)
    return r


def microsoft_to_text(audio, token):
    url = 'https://chinaeast2.stt.speech.azure.cn/speech/recognition/conversation/cognitiveservices/v1?language=zh-CN'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-type': 'audio/wav; codecs=audio/pcm; samplerate=16000',
        'Accept': 'application/json',
    }
    r = requests.post(url, audio, headers=headers)
    return r


if __name__ == '__main__':
    key = 'unknown'
    token = issuetoken(key)
    text = '今天天气晴朗。'
    name = 'zh-CN, XiaoxiaoNeural'
    r = microsoft_to_audio(text, name, token)
    with open(f'a.mp3', 'wb') as fp:
        fp.write(r.content)

    r = microsoft_to_text(open('test2.wav', 'rb'), token)
    print(r.json())
