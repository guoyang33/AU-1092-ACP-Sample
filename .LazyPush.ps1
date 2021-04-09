$count=1
for(;;)
{
    git pull
    git add .
    git commit -m "Push by .LazyPush.ps1"
    git push
    echo count=$count
    $count++
    start-sleep(5)
}