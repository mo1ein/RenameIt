# Rit 
### Rit is a linux command to rename photos to the time as they were taken .
### You can rename multiple files with strftime ,regex and your favourite time format .

### Install 

```
git clone https://github.com/mo1ein/RenameIt.git && cd RenameIt
```
then :
```python3 setup.py install```

and enjoy it :)
### Usage
```
Rit [path] [strftime] [switches]
```
### Example
```
Rit /home/moein/pics/photo1.jpg ./photo2.jpg
```
#### Jalali time
```
Rit /home/moein/Pictires/photo.JPG %c -v -j
```
output : 
```
Renamed: /home/moein/Pictures/photo.JPG -> Yekshanbeh 20 Ordibehesht 1399 23:12:25.JPG
[ 1 : Files Renamed]
```
#### other ways :
```
Rit /home/moein/lastnight/*jpg photonew.jpeg %c -v -f
```
output : 
```
Renamed: /home/moein/lastnight/2019_1.jpg -> Thu Mar 10 05:41:04 2018.jpg
Renamed: /home/moein/lastnight/2019_1.jpg -> Wed Jan 25 08:41:14 2019.jpg
Renamed: /home/moein/lastnight/2019_1.jpg -> Sun Dec 01 02:33:16 2020.jpg
Renamed: /home/moein/pics/photonew.jpeg -> Mon Feb 01 22:41:16 2020.jpeg
[ 5 : Files Renamed]
```


# TODO
- [x] Creat GUI with PyQt5
- [x] Jalali Date 
- [ ] Responsive GUI page 
- [x] Fix progress bar 
- [ ] Show selected files  
- [ ] Window Style 

