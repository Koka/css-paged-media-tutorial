for d in lesson-*
do
	echo $d
    cd $d 
    git rm -fr *pdf images
    git commit -m removed .        
    make git
    make images
    cd ..

done
