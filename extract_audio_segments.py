import os
from pydub import AudioSegment
import tgt

#Helper function to extract audio segments from Praat Textgrids.

def segment_textgrid_audio(textgrid_path, tier):
    directory = os.listdir(textgrid_path)
    try:
        os.mkdir(textgrid_path + '/segments')
    except:
        print("Path already exists")
    for f in directory:
        if '.TextGrid' in f:
            text_grid = tgt.read_textgrid(os.path.join(textgrid_path, f))
            wav = os.path.join(textgrid_path, f.replace('TextGrid', 'wav'))
            interval_num = 0
            for interval in text_grid.tiers[tier].intervals:
                interval_num +=1
                if interval.text != '':
                    start_audio = interval.start_time * 1000
                    end_audio = interval.end_time * 1000
                    audio_segment = AudioSegment.from_file(wav)
                    audio_segment = audio_segment[start_audio:end_audio]
                    audio_segment.export(textgrid_path + '/segments/'+f.replace('.TextGrid', '_')+'_'+str(interval_num)+'.wav', format="wav")