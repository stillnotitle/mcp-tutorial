/**
 * GitHub MCP Serverのテスト用関数
 */
function helloWorld() {
  console.log('Hello from GitHub MCP Server!');
  return 'Success';
}

/**
 * サンプルクラス
 */
class ExampleClass {
  constructor(name) {
    this.name = name;
  }
  
  greet() {
    return `Hello, ${this.name}!`;
  }
}

// 実行例
helloWorld();
const example = new ExampleClass('GitHub');
console.log(example.greet());