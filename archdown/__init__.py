import sys
import time
import os


dbs= ["core", "multilib",  "extra", "community" ]
url = "http://download.jovenclub.cu/repos/archlinux/"

def error(string):
    print ("ERROR: " + string ,file=sys.stderr)
    exit (1)

def _help():
    text = "syntax: program <option>\n\noptions:\n -d Daemon mode\n -f Foreground mode\n\n"
    print (text)

def isBin():
    """
    check for necesary binary files
    """
    #w3m
    try:
        fd = open("/bin/w3m", "rb")
        fd.close()
        return 0
    except:
        error("we dont find all necesary binaries: w3m")
    #Aria2c
    try:
        fd = open("/bin/aria2c", "rb")
        fd.close()
        return 0
    except:
        error("we dont find all necesary binaries: aria2")

def fetchList(url):
    #    fd = open("/tmp/webfetch", "w")
    #    os.system("/usr/bin/cat /tmp/webfetch | /usr/bin/grep -e '.pkg.tar.xz' > /tmp/webresult")
    lista = []
    print (f"retriving list of files on {url}")
    
    # fetch the webpage
    stream = os.popen(f"/usr/bin/w3m -dump {url}", "r")
    webpage = stream.read()
    if webpage == '':
        error("Failed to establish a connection")
    
    # put the webpage in a file
    fd = open("/tmp/webpage", "w")
    print (webpage, file=fd)
    fd.close()
    
    # remove garbage from file
    stream = os.popen("cat /tmp/webpage | grep -e 'x86_64' -e 'any' | cut -d ' ' -f 11", 'r')
    text = stream.read()
    fd = open("tmp", "w")
    print (text,file=fd )
    fd.close()
    fd = open("tmp", "r")
    
 
    for i in fd:
        # remove last character on each filename
        i = i[:-1]
        # add to a tmp list each filename
        lista.append(i)
    fd.close()

    return lista
        
def getList():
    global dbs, url
    # We want to put in more :)
    list_core =['core.db', 'core.db.tar.gz', 'core.files', 'core.files.tar.gz']
    list_community =['community.db', 'community.db.tar.gz', 'community.files', 'community.files.tar.gz']
    list_multilib =['multilib.db', 'multilib.db.tar.gz', 'multilib.files', 'multilib.files.tar.gz']
    list_extra =['extra.db', 'extra.db.tar.gz', 'extra.files', 'extra.files.tar.gz']
    arch="x86_64"

    for db in range(len(dbs)):
        new_url = url + dbs[db] + '/os/' + arch + '/'
        test = fetchList(new_url)

        if dbs[db] == "core":
            for i in range(len(test)):
                list_core.append(test[i])
        if dbs[db] == "community":
            for i in range(len(test)):
                list_community.append(test[i])
        if dbs[db] == "extra":
            for i in range(len(test)):
                list_extra.append(test[i])
        if dbs[db] == "multilib":
            for i in range(len(test)):
                list_multilib.append(test[i])

    for db in dbs:
        fd = open(f"{db}.list", "w")
        if db == "core":
            for item in range(len(list_core)):
                print (list_core[item], file=fd)
        if db == "community":
            for item in list_community:
                print (item, file=fd)
                
        if db == "extra":
            for item in list_extra:
                print (item, file=fd)

        if db == "multilib":
            for item in list_multilib:
                print (item, file=fd)

        fd.close()

    
def isCopyTime():
    the_clock = (time.localtime())
    """
    # from `the_clock`
    # [3] =  h
    # [4] =  m
    # [5] =  s
    # [-3]=  week day # start from monday in 0, sunday is 6
    """
    if the_clock[-3] > 4:
        print ("saturday-sunday")
        ## saturday and sunday
        if the_clock[3] > 3 and  the_clock[3] < 10:
            return 0
        else:
            return 1
    else:
        print ("monday-freeday")
        ## from monday to friday
        if the_clock[3] > 2 and  the_clock[3] < 12:
            return 0
        else:
            return 1
    
def check_argv(argv):
    """
    check for invalid arguments, just admit one, -d or -f
    """
    if len (argv) != 2 :
        error("invalid argument, -h for help")
    else:
        if "-h"  in argv:
            _help()
            exit (0)
        else:
            
            if argv[1] == "-d" or argv[1] == "-f":
                return 0
            else:
                error("invalid argument, -h for help")


def prepareDir():
    global dbs,url
    for i in dbs:
        os.system(f"/usr/bin/mkdir -p ./x86_64/{i}")

def prepare_file(file_path, url):
    fd = open(file_path, "r")
    _list = []
    for i in fd:

        _list.append(url + i)
    fd.close()
    fd = open(file_path, "w")
    
    for i in _list:
        print (i,file=fd)
    
    
    fd.close()

        
def onWait():
    # wait for isCopyTime()
    time.sleep(30)
        
def onCopy():
    global dbs,url
    prepareDir()
    for i in dbs:
        os.system(f"/usr/bin/cp ./{i}.list ./x86_64/{i}/{i}.fetch")
        time.sleep (1)
        # start the Download :)

        prepare_file(f"./x86_64/{i}/{i}.fetch", url  + i  + '/os/' + "x86_64"+ "/")
        os.system(f"/usr/bin/aria2c --auto-file-renaming=false -x 4 -j 4 -k 1M -i ./x86_64/{i}/{i}.fetch -d ./x86_64/{i}/")
    

def main_unit():
    while True:
        if not  isCopyTime():
            #copia
            onCopy()
        else:
            onWait()

def daemon_download():
    while True:
        time.sleep(10)
        try:
            # FILE EXIST
            fd=open(".lock", 'r')
            fd.close()
            continue
        except:
            # FILE NOT EXIST

            # check if its actually downloading
            try:
                fd = open("DOWN_PID", "r")
                fd.close()
                continue
            except:
                
                DOWN_PID=os.getpid()
                os.fork()
                if os.getpid()!= DOWN_PID:
                    fd = open("DOWN_PID", "w")
                    print (os.getpid(), file=fd)
                    fd.close()
                    onCopy()
                else:
                    time.sleep(10)

def daemon_clock():
    while True:
        time.sleep(10)
        if not isCopyTime(): # si es horario inicia
            os.system("/usr/bin/rm .lock")


        else:                # si no es horario detiene
        
            os.system("/usr/bin/touch .lock")
            try:
                fd=open("DOWN_PID", "r")
                pid=fd.read()
                fd.close()
                os.system(f"/usr/bin/kill {pid}")
                os.system("/usr/bin/rm DOWN_PID")
            except:
                time.sleep(10)

def daemon_unit():
    MAIN_PID = os.getpid()

    os.fork()
    if os.getpid() == MAIN_PID:
        daemon_clock()

    else:
        daemon_download()
    
def daemon_mode():
    """
    for turn into the background the entire proccess
    """
    PID = os.getpid()
    os.fork()
    if os.getpid() == PID:
        time.sleep(1)
        fd = open("PID", 'r')
        print (f"Turning into background... pid={fd.read()} \nhave a nice day")
        fd.close()
        exit (0)
    else:
        fd = open("PID", 'w')
        print (os.getpid(), file=fd)
        fd.close()
        daemon_unit()

    
def main(argv):
    
    check_argv(argv)
    if not isBin():
        getList()
    
    if  argv[1] == "-d":
        daemon_mode()
    else:
        main_unit()
        
    

if __name__ == "__main__":

    banner="""
    Este programa no verifica errores de descarga, tampoco si hay conexion o no
    Por favor, verifique este hecho antes de usar es script
    """
    print (banner)
    time.sleep(10)
    main(sys.argv)
