#!/usr/bin/python3


import os
import sys
import time
import argparse
import PIL.Image
import PIL.ExifTags
from datetime import datetime
from Rit.jalali import JalaliFormat


class Rename :

    def __init__ (self):
        #Defualt time format
        self.format = '%Y-%m-%d'
        self.jalali = False 
        self.Verbos = False
        self.fullpath = '' 
        self.count = 1
        self.path = []
        self.shit = []
        self.args = {}
        self.dic = {}
        self.progress = 0.0

    #read Modified DateTime from exif data 
    def readMeta(self,f) :
        img = PIL.Image.open(f)

        #some photos are damaged and we got error
        #so use exception

        try:
            exif = {
                PIL.ExifTags.TAGS[k]: v
                for k, v in img._getexif().items()
                if k in PIL.ExifTags.TAGS
            }

        except :
            print('image file is damaged !!! im still trying...')

        try :

            realTime = exif['DateTime']
            #because strptime has no str obj ...
            image_time = datetime.strptime(realTime, "%Y:%m:%d %H:%M:%S")
            new = image_time.strftime(self.format)
            alldate = image_time.strftime("%Y%m%d%H%M%S")

            if self.jalali :
                alldate = JalaliFormat(image_time,self.format).jsort()
                new = JalaliFormat(image_time,self.format).jconvert()
        except :
            realTime = time.strftime("%Y:%m:%d %H:%M:%S",time.gmtime(os.path.getmtime(f)))
            image_time = datetime.strptime(realTime, "%Y:%m:%d %H:%M:%S")
            new = image_time.strftime(self.format)
            alldate = image_time.strftime("%Y%m%d%H%M%S")

            if self.jalali :
                alldate = JalaliFormat(image_time,self.format).jsort()
                new = JalaliFormat(image_time,self.format).jconvert()
        
        times = new , alldate
        return times

        

    def Rit (self):

        if not self.path and self.args['help'] is not True and self.args['version'] is not True :
            print ('Rit: missing operand \nTry \'Rit --help\'')
        else :
                #Sort file by erlier Time
                for files in self.path :

                    self.progress += 1.0 / len(self.path)

                    try :
                        # find full path of file (absolutized path)
                        self.fullpath = os.path.abspath(files)
                        Priority = self.readMeta(files)
                        self.dic[Priority[1]] = self.fullpath ,Priority[0]

                    except OSError :
                        print (
                                ' Rit: cannot stat \'%s\': '%files
                                +'No such file or directory'
                        ) 

                        self.shit.append(files)
                for piece_of in self.shit : self.path.remove(piece_of)
                self.dic = dict(sorted(self.dic.items()))

                for item in self.dic :
                        # current name
                        oldname = self.dic[item][0]
                        head = os.path.split(self.dic[item][0])[0] 
                        # split extention of file .
                        ext = os.path.splitext(self.dic[item][0])[1]
                        
                        Time =self.dic[item][1] 
                        newname = head  + '/' + Time + ext

                        # if file with newname is exist , try to change it .
                        while os.path.exists(newname) :
                            if (newname == oldname) : 
                                break
                            newname = head + '/' + Time +'_' + str(self.count) + ext
                            self.count+=1

                        self.count = 1
                        #Renaming...
                        os.rename(self.dic[item][0],newname) 

                        if self.Verbos :
                            print ( ' Renamed:' , 
                                    self.dic[item][0] , 
                                    '->' ,
                                    newname.split('/')[-1]
                            )
                                   
                if self.Verbos :
                    print ("[",len(self.path),": Files Renamed]")

    # add switchs whit argparse
    def get_parser(self) :

        parser = argparse.ArgumentParser(
                add_help = False ,
                prog = 'Rit',
                usage='Rit [-fv] [file[strftime]]'
                )

        # verbos
        parser.add_argument (
                '-v',
                '--verbos',
                action = 'store_true'
                )

        # file argument
        parser.add_argument (
                'path',
                type = str,
                nargs = '*'
                )

        # time format
        parser.add_argument (
                '-f',
                '--format',
                dest = 'format',
                action = 'store_true'
                )

        # jalali time format
        parser.add_argument (
                '-j',
                '--jformat',
                dest = 'jformat',
                action = 'store_true'
                )
        
        # help
        parser.add_argument (
                '-h',
                '-help',
                '--help',
                action = 'store_true'
                )
       
        # version
        parser.add_argument (
                '--version',
                action = 'store_true'
                )

        self.args = vars(parser.parse_args())

        # move path arguments to self.path
        self.path = self.args['path']
        
    # what happen on terminal?! 
    def cli (self) :

        if self.args['verbos'] :
            self.Verbos = True

        if self.args['format'] :
            for item in sys.argv :
                if '%' in item :
                    self.format = item
                    self.path.remove(item)
        
        if self.args['jformat'] :
            self.jalali = True
            for item in sys.argv :
                if '%' in item :
                    self.format = item
                    self.path.remove(item)
                   
        if self.args['help'] :
            print('\nRename It (Version 1.0.0)'
                  '\nusage: Rit [OPTIONS] [FILE|DIR...]'
                '\n\nOptions :'
                  '\n  -h, --help        show this help message and exit '
                  '\n  -v, --verbos      increase output verbosity '
                  '\n  -f, --format      time unix format '
                  '\n  -j, --jformat     jalali time unix format '
                  '\n  --version         show version '
            )
        
        if self.args['version'] :
            print('''
                          ____  _ _   
                         |  _ \(_) |_ 
                         | |_) | | __|
                         |  _ <| | |_ 
                         |_| \_\_|\__|

                        This is : Rename It
                        Version : 1.0.0
                        Built   : comming soon ...
                         Author : Moein Halvaei
                         E-Mail : <moeinn.com@gmail.com>
                      Copyright : (C) 2020  Moein Halvaei
                        License : GNU General Public License, version 3 (gpl3)
                    '''
            )

def main():

    RenameIt = Rename()
    RenameIt.get_parser()  
    RenameIt.cli()
    RenameIt.Rit()

if __name__ == "__main__" :

    main()


