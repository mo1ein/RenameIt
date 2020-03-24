# Rit 
### Rit is a linux command to rename photos to the time as they were taken .
#### You can rename multiple files with strftime , regex and your favourite time format .

### Install 

```
pip install Rit
```
or :
```
git clone https://github.com/mo1ein/RenameIt.git && cd RenameIt
python3 setup.py install
```
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
#### Rename recursively
```
Rit -r /home/moein/mypics/ 
```
#### other ways :
```
Rit /home/moein/lastnight/*jpg photonew.jpeg %c -v -f
```


# TODO
- [x] Creat GUI with PyQt5
- [x] Jalali Date 
- [x] Fix progress bar 
- [x] Rename recursively 
- [ ] Responsive GUI page 
- [ ] Show selected files thumbnail  
- [ ] Window Style 

