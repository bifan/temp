"双引号是注释

"模拟Ctrl+Shift+Enter 在当前行的上一行插入空白行
nmap <C-S-CR> O
imap <C-S-CR> <ESC>O

"模拟Ctrl+Enter 在当前行的下一行插入空白行
nmap <C-CR> o
imap <C-CR> <ESC>o

"模拟Alt+↓ 与下一行交换位置
nmap <A-Down> ddp
imap <A-Down> <ESC>ddp

"模拟Alt+↑ 与上一行交换位置 (思路，把上一行的内容剪切到当前行的下一行)
nmap <A-Up> kddpk
imap <A-Up> <ESC>kddpk

"模拟Ctrl+Alt+↑ 复制当当前行内容到上一行
nmap <C-A-Down> yyp
imap <C-A-Up> <Esc>yyP

"模拟Ctrl+Alt+↓ 复制当前行内容到下一行
nmap <C-A-Down> yyp
imap <C-A-Down> <Esc>yyp

"一串命令中有一个执行失败则后面的都会被vim忽略
"要在 vim 的插入、普通两个模式中都有效果, 在插入模式使用快捷键后维持插入模式状态,在普通模式使用快捷键后进入插入模式状态.
"nmap表示在普通模式下执行的快捷键(经测试与map效果相同)
"imap表示在插入模式下执行的快捷键
"<C-S-CR> 即 Ctrl+Shift+Enter
"<C-c> 即 Ctrl+c
