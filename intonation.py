import kaldi.feat.pitch as pitch
import kaldi.util.table as table
import kaldi.matrix as matrix
import os
from numpy import mean


def extract_f0_files(dir):
    directory = os.listdir(dir)
    freqs=[]
    for f in directory:
        freq=get_pitch(rspec="scp:data/Lei/"+f, wspec= "ark,t:output/Lei/"+f.replace('.wav', '.ark'))
        freqs.append(freq)
    return freqs



def get_pitch(rspec,wspec):
    #Kaldi pitch options
    pitch_opts = pitch.PitchExtractionOptions ()
    pitch_opts.samp_freq = 44100.0
    pitch_opts.max_f0 = 800

    with table.SequentialWaveReader (rspec) as reader, table.MatrixWriter(wspec) as writer:

        for key, wav in reader:
            assert (wav.samp_freq >= pitch_opts.samp_freq)
            assert (wav.samp_freq % pitch_opts.samp_freq == 0)

            s = wav.data()

            # downsample
            #s = s[:, ::int (wav.samp_freq / pitch_opts.samp_freq)]

            # mix-down stereo to mono
            m = matrix.SubVector(mean(s, axis=0))

            # Extract pitch
            f0 = pitch.compute_kaldi_pitch(pitch_opts,m)
            # standardize features
            #f = matrix.SubMatrix (scale (f0))

            #Write to file
            #writer[key] = f0
    return f0

