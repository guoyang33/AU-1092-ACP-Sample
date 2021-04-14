@ git add ./

@ IF "%~1" == "" GOTO EmptyMsg

@ git commit -m "%~1"
@ GOTO :end

:EmptyMsg
@ git commit -m "Pushed by .LazyPush.bat"

:end
@ git push
@ ECHO Push finished.