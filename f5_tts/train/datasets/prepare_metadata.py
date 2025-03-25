import glob
from tqdm import tqdm

wavs_path = glob.glob("data/datasetVN/mc/mc1/*.wav")

with open("data/vnTTS__char/metadata.csv", "w", encoding="utf8") as fw:
    fw.write("audio_file|text\n")
    for wav_path in tqdm(wavs_path):
        wav_name = wav_path.split("/")[-1]
        with open(wav_path.replace(".wav", ".lab"), "r", encoding="utf8") as fr:
            text = fr.readlines()[0].replace("\n", "")
        fw.write("wavs/" + wav_name + "|" + text + "\n")