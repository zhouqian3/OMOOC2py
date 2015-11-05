# -*- coding: utf-8 -*-
import time


                                                # ----问候----
print "I'm your diary"
print "Anything to share for today?"
print "You can also press ENTER to read the history diary"

diary = raw_input('ε=ε=ε=ε=ε=ε=┌(;￣◇￣)┘')


                                                # ----输入回车键，阅读日记----
if diary == '':
    diaryFile = open('diary.txt')
    diary = diaryFile.read()
    print ">>>>>>日记<<<<<<"
    print diary


                                                # ----输入文字，开始写日记啦 ----   
else:
    diaryFile = open('diary.txt','a')
    
    write='y'
    while write=='y':
        diaryFile.write('\n' + time.strftime('%Y/%m/%d')+ ' ' +diary)

                                                # ----还想继续写日记----        
        print('Continue?(y/n)')
        write=raw_input()
        if write == 'y':
            diary = diary = raw_input('ε=ε=ε=ε=ε=ε=┌(;￣◇￣)┘ what else dude?')
                                                # ----不想写啦----        
        else:
            print "End of Diary"
            diaryFile.close()