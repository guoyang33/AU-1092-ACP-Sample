@ IF "%~1" == "" GOTO EmptyMsg

@ git add ./
@ git commit -m "%~1"
@ git push
@ GOTO :end

:EmptyMsg
@ git add ./
@ git commit -m "Pushed by .LazyPush.bat"
@ git push


:end
@ ECHO Push finished.