# GitHub MCP Server API ドキュメント

このドキュメントでは、GitHub MCP Serverの主要なAPI機能について説明します。

## リポジトリ操作

### リポジトリの作成

```javascript
create_repository({
  name: "リポジトリ名",
  description: "リポジトリの説明",
  private: false,  // true=プライベート, false=パブリック
  autoInit: true   // README.mdファイルで初期化
})
```

### リポジトリの検索

```javascript
search_repositories({
  query: "検索キーワード",
  perPage: 10,  // 1ページあたりの結果数
  page: 1       // ページ番号
})
```

## ファイル操作

### ファイルの取得

```javascript
get_file_contents({
  owner: "リポジトリオーナー",
  repo: "リポジトリ名",
  path: "ファイルパス"
})
```

### ファイルの作成/更新

```javascript
create_or_update_file({
  owner: "リポジトリオーナー",
  repo: "リポジトリ名",
  path: "ファイルパス",
  message: "コミットメッセージ",
  content: "ファイルの内容",
  branch: "ブランチ名",
  sha: "更新する場合は既存ファイルのSHA"
})
```

## イシュー操作

### イシューの作成

```javascript
create_issue({
  owner: "リポジトリオーナー",
  repo: "リポジトリ名",
  title: "イシュータイトル",
  body: "イシューの内容",
  labels: ["ラベル1", "ラベル2"]
})
```

### イシューへのコメント追加

```javascript
add_issue_comment({
  owner: "リポジトリオーナー",
  repo: "リポジトリ名",
  issue_number: イシュー番号,
  body: "コメント内容"
})
```

## その他の機能

このAPIドキュメントは随時更新されます。さらに詳しい情報やその他の機能については、公式ドキュメントを参照してください。