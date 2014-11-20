"双引号是注释

"模拟Ctrl+Shift+Enter 在上一行插入空白行
nmap <C-S-CR> O
imap <C-S-CR> <ESC>O

"模拟Ctrl+Enter 在下一行插入空白行
nmap <C-CR> o
imap <C-CR> <ESC>o

"模拟Alt+↑ 当前行上移一行 (把上一行的内容剪切到当前行的下一行)
nmap <A-up> kddpk
imap <A-up> <ESC>kddpk

"模拟Alt+↓ 当前行下移一行
nmap <A-down> ddp
imap <A-down> <ESC>ddp

"模拟Ctrl+Alt+↑ 复制当前行到上一行
nmap <C-A-down> yyp
imap <C-A-up> <ESC>yyP

"模拟Ctrl+Alt+↓ 复制当前行到下一行
nmap <C-A-down> yyp
imap <C-A-down> <ESC>yyp

"一串命令中有一个执行失败则后面的都会被vim忽略
"nmap表示在普通模式下执行的快捷键(经测试与map效果相同)
"imap表示在插入模式下执行的快捷键
"<C-S-CR> 即 Ctrl+Shift+Enter
"<C-c> 即 Ctrl+c
