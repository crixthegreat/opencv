step1

pre many neg images



step2

gen positive images from neg images

```
opencv_createsamples -img target.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 557
```

step3

gen the vec file

```
opencv_createsamples -info info/info.lst -num 502 -w 50 -h 50 -vec positives.vec
```

step3 

train the model

```
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 500 -numNeg 250 -numStages 10 -w 50 -h 50
```

