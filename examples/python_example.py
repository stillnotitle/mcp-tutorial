#!/usr/bin/env python

def hello_world():
    """
    GitHub MCP Serverのテスト用関数
    """
    print("Hello from GitHub MCP Server!")
    return "Success"

class ExampleClass:
    """
    サンプルクラス
    """
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"

if __name__ == "__main__":
    hello_world()
    example = ExampleClass("GitHub")
    print(example.greet())