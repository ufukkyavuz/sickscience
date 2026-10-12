"""ElevenLabs voiceover for video-01. Reads the key from the ELEVENLABS_API_KEY environment variable (never stored in files).
Generates one clip per scene line, writes vo.mp3 (lines placed at scene starts) and timings.json, then render.py uses them."""
import json, os, subprocess, urllib.request
import imageio_ffmpeg

HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.environ.get('ELEVENLABS_API_KEY')
if not KEY: raise SystemExit('ELEVENLABS_API_KEY is not set')
VOICE = os.environ.get('ELEVENLABS_VOICE_ID', '21m00Tcm4TlvDq8ikWAM')  # default: premade "Rachel" — calm US female
LINES = [  # scene key, text (US English, site-safe claims only)
    ('phone', 'This October, add one step to your routine.'),
    ('set', 'Your monthly self-check.'),
    ('pair', "Because it's a pair worth checking."),
    ('donation', 'And this October, twenty percent of NetWork sales on SickScienceLabs dot com go to The Breast Cancer Research Foundation.'),
]
ff = imageio_ffmpeg.get_ffmpeg_exe()
os.makedirs(os.path.join(HERE, 'vo'), exist_ok=True)

def tts(text, path):
    body = json.dumps({'text': text, 'model_id': 'eleven_multilingual_v2',
                       'voice_settings': {'stability': 0.55, 'similarity_boost': 0.8, 'style': 0.15, 'use_speaker_boost': True}}).encode()
    req = urllib.request.Request(f'https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128', data=body,
                                 headers={'xi-api-key': KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    open(path, 'wb').write(urllib.request.urlopen(req).read())

def duration(path):
    out = subprocess.run([ff, '-i', path], capture_output=True, text=True).stderr
    h, m, s = out.split('Duration: ')[1].split(',')[0].split(':'); return int(h) * 3600 + int(m) * 60 + float(s)

T, clips = {}, []
for k, text in LINES:
    p = os.path.join(HERE, 'vo', f'{k}.mp3'); tts(text, p); d = duration(p)
    T[k] = round(max(d + 0.7, 2.6), 2); clips.append((k, p))
T['end'] = 2.6
json.dump(T, open(os.path.join(HERE, 'timings.json'), 'w'), indent=1)
# place each line 0.25 s after its scene start
starts, t = {}, 0.0
for k in ['phone', 'set', 'pair', 'donation', 'end']: starts[k] = t; t += T[k]
inputs, filt = [], []
for i, (k, p) in enumerate(clips):
    inputs += ['-i', p]; ms = int((starts[k] + 0.25) * 1000); filt.append(f'[{i}]adelay={ms}|{ms}[a{i}]')
mix = ''.join(f'[a{i}]' for i in range(len(clips)))
subprocess.run([ff, '-y', *inputs, '-filter_complex', ';'.join(filt) + f';{mix}amix=inputs={len(clips)}:normalize=0,apad=pad_dur=1[out]',
                '-map', '[out]', '-t', str(t), os.path.join(HERE, 'vo.mp3')], check=True, stderr=subprocess.DEVNULL)
print('timings', T, 'total', round(t, 2))
