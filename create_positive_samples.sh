rm positivas_finales/*
for file in positivas_seleccionadas/*
do
  opencv_createsamples -img $file -bg negativas.txt -inv -randinv -num 2000 -info positivas_finales/$(basename "$file").txt  -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5
done

#opencv_createsamples -info positivas_finales/positivas_finales.txt -num 10000 -w 100 -h 100 -vec positives.vec
