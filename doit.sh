URL[0]="http://data.riksdagen.se/dataset/votering/votering-200203.csv.zip"
URL[1]="http://data.riksdagen.se/dataset/votering/votering-200304.csv.zip"
URL[2]="http://data.riksdagen.se/dataset/votering/votering-200405.csv.zip"
URL[3]="http://data.riksdagen.se/dataset/votering/votering-200506.csv.zip"
URL[4]="http://data.riksdagen.se/dataset/votering/votering-200607.csv.zip"
URL[5]="http://data.riksdagen.se/dataset/votering/votering-200708.csv.zip"
URL[6]="http://data.riksdagen.se/dataset/votering/votering-200809.csv.zip"
URL[7]="http://data.riksdagen.se/dataset/votering/votering-200910.csv.zip"
URL[8]="http://data.riksdagen.se/dataset/votering/votering-201011.csv.zip"
URL[9]="http://data.riksdagen.se/dataset/votering/votering-201112.csv.zip"
URL[10]="http://data.riksdagen.se/dataset/votering/votering-201213.csv.zip"
URL[11]="http://data.riksdagen.se/dataset/votering/votering-201314.csv.zip"
URLS=${URL[@]}

for url in $URLS ; do
  wget $url
  zipfile=${url##*/}
  unzip $zipfile 
  filename=${zipfile%.*}
  filename_prepared=${filename}_prepared
  python prepare_data.py $filename > $filename_prepared
  python plot_data.py $filename_prepared
done
