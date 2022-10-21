
while [ 1 -gt 0 ]
do
  eval $(xdotool getmouselocation --shell)
  echo $X $Y
done

