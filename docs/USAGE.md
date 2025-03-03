# GitHub MCP Server 使用ガイド

このガイドでは、GitHub MCP Serverの基本的な使い方を説明します。

## 前提条件

- Node.js または Python の基本的な知識
- GitHub アカウント
- GitHub Personal Access Token (PAT)

## 初期設定

1. リポジトリをクローンします
   ```bash
   git clone https://github.com/yourusername/yourrepo.git
   cd yourrepo
   ```

2. 必要なパッケージをインストールします
   ```bash
   npm install
   # または
   pip install -r requirements.txt
   ```

3. 環境変数を設定します
   ```bash
   export GITHUB_TOKEN=your_personal_access_token
   ```

## 基本的な使い方

### リポジトリの作成

```javascript
// JavaScriptの例
const result = await createRepository({
  name: "my-new-repo",
  description: "This is a new repository",
  private: false
});
console.log(result);
```

```python
# Pythonの例
result = create_repository(
  name="my-new-repo",
  description="This is a new repository",
  private=False
)
print(result)
```

### ファイルの追加

```javascript
// JavaScriptの例
const result = await createOrUpdateFile({
  owner: "username",
  repo: "my-new-repo",
  path: "README.md",
  content: "# My New Repository\n\nThis is a new repository.",
  message: "Add README file",
  branch: "main"
});
console.log(result);
```

```python
# Pythonの例
result = create_or_update_file(
  owner="username",
  repo="my-new-repo",
  path="README.md",
  content="# My New Repository\n\nThis is a new repository.",
  message="Add README file",
  branch="main"
)
print(result)
```

## 高度な使い方

### 複数ファイルの一括コミット

```javascript
// JavaScriptの例
const result = await pushFiles({
  owner: "username",
  repo: "my-new-repo",
  branch: "main",
  message: "Add multiple files",
  files: [
    { path: "file1.txt", content: "Content of file 1" },
    { path: "file2.txt", content: "Content of file 2" },
    { path: "dir/file3.txt", content: "Content of file 3" }
  ]
});
console.log(result);
```

```python
# Pythonの例
result = push_files(
  owner="username",
  repo="my-new-repo",
  branch="main",
  message="Add multiple files",
  files=[
    { "path": "file1.txt", "content": "Content of file 1" },
    { "path": "file2.txt", "content": "Content of file 2" },
    { "path": "dir/file3.txt", "content": "Content of file 3" }
  ]
)
print(result)
```

## トラブルシューティング

一般的な問題とその解決策：

1. **認証エラー**: Personal Access Tokenが正しく設定されているか確認してください。
2. **パーミッションエラー**: トークンに必要な権限が付与されているか確認してください。
3. **レート制限**: GitHub APIのレート制限に達した場合は、しばらく待ってから再試行してください。

## さらなる情報

さらに詳しい情報は、[公式ドキュメント](https://docs.github.com/en/rest)を参照してください。