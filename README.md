# ワークスペースジェネレータ

リポジトリ: <https://github.com/toshio-nakayama/sandbox-workspace-tool.git>

テンプレートファイルから固定フォルダにファイルを一括生成・リセットするツール。
PHP／SQL／Markdown／HTML／トラブルシュートログの雛形を素早く作成できる。

## 動作環境

- Python 3.x がインストールされていて `python` コマンドが使える
- Windows では同梱の `run-generate.bat` をダブルクリックして実行可能

## ディレクトリ構成

```plaintext
MySandbox/                    ← プロジェクトルート
├─ generate-workspace.py     ← ワークスペース生成スクリプト
├─ run-generate.bat          ← Windows用バッチ（任意）
└─ workspace-templates/      ← 雛形テンプレート置き場
    ├─ sandbox.tpl.php
    ├─ query.tpl.sql
    ├─ document.tpl.md
    ├─ example.tpl.html
    └─ trouble-shooting.tpl.txt
```

- **generate-workspace.py**
  - 実行すると直下に `generated-workspace/` をリセット＆生成
- **run-generate.bat**
  - Windowsでダブルクリック実行するためのバッチ
- **workspace-templates/**
  - コピー元のテンプレートファイル群

## 仕組み

1. `generated-workspace/` があれば丸ごと削除
2. テンプレートを指定回数コピーして生成
   - PHP: `PHP-001-gen.php`～`PHP-003-gen.php`
   - SQL: `SQL-001-tmp.sql`～`SQL-003-tmp.sql`
   - MD:  `MD-001-sample.md`～`MD-002-sample.md`
   - HTML: `HTML-001.html`
   - TXT: `TXT-001-log.txt`
3. 出力先はすべて `generated-workspace/` にフラット配置

## 使い方

### コマンド

```bash
cd C:\Users\user\Projects\MySandbox
python generate-workspace.py
```

### Windowsダブルクリック

- エクスプローラで `run-generate.bat` をダブルクリック

実行後、`generated-workspace/` フォルダ内に生成ファイルが揃う。

## カスタマイズ

- テンプレート追加・編集は `workspace-templates/` 配下の `*.tpl.*` を編集
- 生成数やファイル名形式は `generate-workspace.py` 内の `TYPES` を変更

## ライセンス／作者

- ライセンス: MITライセンス
  - 商用・非商用問わず、利用・複製・改変・再配布が自由
  - 著作権表示とライセンス文を残せばOK
  - 保証なし、責任放棄

- Author: Toshio Nakayama
