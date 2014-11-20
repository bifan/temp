"双引号是注释

"要在 vim 的插入、普通两个模式中都有效果
"在插入模式使用快捷键后维持插入模式状态
"在普通模式使用快捷键后进入插入模式状态

"模拟Ctrl+Shift+Enter
" nmap表示在普通模式下执行的快捷键(经测试与map效果相同)
" imap表示在插入模式下执行的快捷键
" <C-S-CR> 即 Ctrl+Shift+Enter
" <C-c> 即 Ctrl+c
nmap <C-S-CR> O
imap <C-S-CR> <ESC>O

"模拟Ctrl+Enter
nmap <C-CR> o
imap <C-CR> <ESC>o

"模拟Alt+↓ 与下一行交换位置 esc进入普通模式 dd剪切当前行 p在当前行的下一行粘贴
nmap <A-Down> <ESC>ddp
imap <A-Down> <ESC>ddp

"模拟Alt+↑ 与上一行交换位置 (思路，把上一行的内容剪切到当前行的下一行)
imap <A-Up> <ESC>kddpk
nmap <A-Up> <ESC>kddpk

"模拟Ctrl+Alt+↑ 复制当当前行内容到上一行
imap <C-A-Up> <Esc>yyP
nmap <C-A-Up> <Esc>yyP

"模拟Ctrl+Alt+↓ 复制当前行内容到下一行
imap <C-A-Down> <Esc>yyp
nmap <C-A-Down> <Esc>yyp
