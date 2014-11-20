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

"模拟Alt+↑ 与上一行交换位置
"bug1 首行的时候变成了删除效果，貌似没有执行P, 手动执行<ESC>ddkP是没有问题的.
"bug2 末行会和上一行的上一行交换位置，由于dd剪切后当前行已经消失，光标自动跑到上一行，此时再执行k，光标总计两次向上
imap <A-Up> <ESC>ddkP
nmap <A-Up> <ESC>ddkP
