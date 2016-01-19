for d in lesson-*
do
	echo $d
    cd $d 
    make git
    make images
    cd ..

done
