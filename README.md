# hbty

hbtyは簡単にバースデーカードを作成するツールです。

## デモ

以下のように使用することができます。

```bash
$ hbty sea
画像を生成しました。
```

画像はカレントディレクトリに作成されます。

![output](https://user-images.githubusercontent.com/50062855/79682353-759c4880-825c-11ea-9b8d-36debb3e3596.png)

## インストール

```bash
pip install hbty
```

## 使用方法

基本的には`hbty <キーワード>`で画像が生成されます。

```bash
$ hbty happy
画像を生成しました。
```

以下のようなオプションをつけることもできます。

* -C, --color <テキスト>

このオプションはテキストの色を一色に指定することができます。対応している色は白、赤、青、緑、黄色です。

<テキスト>のところに以下のいずれかの文字を入れてください。

white, red, blue, green, yellow

* --to <テキスト>

画像にのるHappy Birthday to の後の文字を指定することができます。デフォルトでは You になっています。

英語以外使用できません。文字化けします。

* --help

ヘルプを見ることができます。

<!-- ## 注意点 -->

## 依存パッケージ

* click 7.1.1
* Pillow 7.1.1
* requests 2.23.0

## 作者

* 作成者: minguu
* minguu42@gmail.com

## ライセンス

[MIT license](https://en.wikipedia.org/wiki/MIT_License)
