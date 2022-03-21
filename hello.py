#!/usr/local/bin/python3

# 日本語を扱うために必要な設定 --- (*1)
import os, sys, io, cgi
sys.stdin =  open(sys.stdin.fileno(),  'r', encoding='UTF-8')
sys.stdout = open(sys.stdout.fileno(), 'w', encoding='UTF-8')
sys.stderr = open(sys.stderr.fileno(), 'w', encoding='UTF-8')

out = lambda msg: print(msg, end="\r\n")

# ヘッダの出力 --- (*2)
out("Content-Type: text/html; charset=utf-8")
out("")

# HTMLの出力 --- (*3)
out("<html><meta charset='utf-8'><body>")
out("<h1>こんにちは</h1>")
out("</body></html>")
