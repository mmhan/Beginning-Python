from subprocess import Popen, PIPE

def tidyMess():
    '''
    Requires tidy to be installed to be able to run this.
    http://www.paehl.com/open_source/?HTML_Tidy_for_Windows
    '''
    text = open('messy.html').read()
    tidy = Popen('tidy', stdin = PIPE, stdout = PIPE, stderr = PIPE)
    
    tidy.stdin.write(text)
    tidy.stdin.close()
    
    print tidy.stdout.read()
    
tidyMess()