import os


def write_scp_wav(path):
    dir = os.listdir(path)
    num = 0
    for d in dir:
        with open ('data/Lei/' + d.replace('.wav','') + '.scp', 'w') as writer:
            num +=1
            writer.write(d.split('_')[1].replace('.wav',''))
            writer.write(' ')
            writer.write(path+d)
            writer.write('\n')
