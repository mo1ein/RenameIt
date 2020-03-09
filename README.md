# Rit 
## Rit is a linux command to rename photos to the time as they were taken .
### Getting Started

### Dependencies

```pip install persiantools ```

### Install 

first you must clone :
```
git clone https://github.com/mo1ein/RenameIt.git
```
then :
```
cd RenameIt
python3 setup.py
```
and enjoy it :)
### Usage
```
Rit [path] [strftime] [switch]
```
like :
```
Rit /home/moein/pics/photo1.jpg ./photo2.jpg
```
other ways :
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
- [ ] Fix progress bar 
- [ ] Show selected files  
- [ ] Window Style 

