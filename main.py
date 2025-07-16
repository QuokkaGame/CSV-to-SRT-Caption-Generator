import csv
import sys

def csv_to_srt(csv_file, srt_file):
    with open(csv_file, 'r', encoding='utf-8') as infile, open(srt_file, 'w', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        for i, row in enumerate(reader, start=1):
            start = row['start_time'].replace('.', ',')
            end = row['end_time'].replace('.', ',')
            text = row['text']
            outfile.write(f"{i}\n{start} --> {end}\n{text}\n\n")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("使い方: \n1. ターミナルを開く \n2. CSV-to-SRT-Caption-Generator.exe 入力csvファイル 出力srtファイル")
        sys.exit()

csv_to_srt(sys.argv[1], sys.argv[2])