
from pygitgrab.__main__ import *

if __name__ == '__main__':

    main()

def _dmy():
    print( "-" *7 )
    githuburl = "https://github.com/kr-g/pygitgrab/sub/web.pygg?ref="

    url = get_owner_repo(githuburl)
    print(url)
    
    regex = r"http[s]?:\/\/github\.com\/([^/]+)\/([^/]+)\/([^?:]*)([?:]ref=(.+))?"

    match = re.search(regex,githuburl)
    for i in range(0,5+1):
        print(i,match.group(i))