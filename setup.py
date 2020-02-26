
import os 

#install Rit :))
os.system('sudo dpkg -i Rit_1.0.0_all.deb')

# finding current directory
cwd = os.path.abspath(__file__)
setup_dir = os.path.dirname(cwd)

# Creating man page file
Rit_man_page = os.path.join(setup_dir, 'man', 'Rit.1')
os.system('gzip -f -k -9 "' + Rit_man_page + '"')
cp = Rit_man_page + '.gz'
os.system('sudo cp %s /usr/share/man/man1/'%(cp))

print('man page is generated!')

