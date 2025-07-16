# CSV to SRT Converter

このツールはCSV形式の字幕ファイルをSRT形式に変換するための簡単なツールです。  
PythonとPyInstallerを使って作成しました。

## 使い方

1. 事前に表計算ソフトなどで、start_time, end_time, textという列を作り、それに対応する内容を書きます。例↓<img width="1100" height="288" alt="image" src="https://github.com/user-attachments/assets/2597d7b1-bb1c-48d2-bd8c-ad53cf04a086" />
3. `csv-to-srt.exe` をダウンロード
4. ターミナルを開く
5. `CSV-to-SRT-Caption-Generator.exe xxx.csv xxx.srt` のようにターミナルから入力と出力を指定して実行
6. `xxx.srt` が生成されます

## セキュリティについて

- ソースコードはこのリポジトリで全て公開しています
- 実行ファイル（exe）は `PyInstaller` を使って生成されています
- ご不安な場合は、ソースコードから自分でビルドしてご利用ください

## ビルドのやり方
1. `pip install pyinstaller`でPyinstallerをインストールします。
2. `pyinstaller --onefile --icon=icon.ico --name=CSV-to-SRT-Caption-Generator main.py`というコマンドを実行します。(引数は変更可能です。)
3. `dist/CSV-to-SRT-Caption-Generator.exe`というファイルが出力されます。
