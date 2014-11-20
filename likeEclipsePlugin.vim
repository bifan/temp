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
