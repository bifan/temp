"双引号是注释

"要在 vim 的插入、命令两个模式中都有效果
"插入模式使用快捷键后维持插入模式状态
"命令模式使用快捷键后进入插入模式状态

"模拟Ctrl+Shift+Enter
" map表示在命令模式下执行的快捷键
" imap表示在插入模式下执行的快捷键
" <C-S-CR> 即 Ctrl+Shift+Enter
" <C-c> 即 Ctrl+c
:map <C-S-CR> O
:imap <C-S-CR> <C-c>O
