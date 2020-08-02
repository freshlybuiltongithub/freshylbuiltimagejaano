from requests import get
from os import mkdir,path,remove
from tqdm import tqdm
from hashlib import md5
from colorama import init,deinit,Fore

"""
freshlybuiltimagejaanolibrary tokenizer file
status_code for checking the execution status
code   meaning
2000 - token already exist
2001 - token file corrupted
2002 - successful download
2003 - http error
2004 - connection error
2005 - timeout error
2006 - miscellanious error
2007 - building models directory
2008 - signature mismatch 

class token - intiate coroutine check for available tokenizer file
function __init__ : initiate instance of class token
function check_token : checks availability of tokenizer file and intiate other functions according to the need
function get_token : get tokens start downloading in case of absence of tokenizer file 
function token_check : token_check implements md5 hash checksum for checking the corruption of tokenizer file

"""

class token:
    status_code=0
    token_checksum='b8bc863c36b0c5ea638fdb75ea86e1bc'
    curr_dir=path.dirname(path.realpath(__file__))

    def __init__(self):
        self.check_token(self.status_code,self.curr_dir)

    def check_token(self,status_code,curr_dir):
        if path.isfile(curr_dir+"/tokenizer.p"):
            print("tokenizer found")
            self.token_check(self.token_checksum)  
        else:
            print("downloading tokenizer")    
            self.get_token()

    def get_token(self):
        token_url= "https://raw.githubusercontent.com/freshlybuiltongithub/freshylbuiltimagejaano/master/freshlybuiltimagejaano/tokenizer.p"
        response = get(token_url, stream=True)
        try:
            response.raise_for_status()   
        except response.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
            self.status_code=2003
            return self.status_code
        except response.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
            self.status_code=2004
            return self.status_code
        except response.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
            self.status_code=2005
            return self.status_code
        except response.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            self.status_code=2006
            return self.status_code
        with open(self.curr_dir+"/"+"tokenizer.p", "wb") as f:
            total_length = int(response.headers.get('content-length'))
            if total_length is None:
                f.write(response.content)
            else:
                chunk_size=512
                for data in tqdm(iterable = response.iter_content(chunk_size),total=total_length/chunk_size, unit = 'KB'):
                    try:
                        f.write(data)
                    except:
                        pass
        self.status_code=2002
        return self.status_code             
    
    def token_check(self,token_checksum):
        model_checksum="tokenizer.p"
        md5_hash=md5()
        model_handler=open(model_checksum,"rb").read()
        md5_hash.update(model_handler)
        hash_code=md5_hash.hexdigest()
        if hash_code==token_checksum:
            init(autoreset=True)
            print("tokenizer signature matched")
            deinit()
            self.status_code=2000
            return self.status_code

        else:
            init(autoreset=True)
            print("tokenizer signature mismatched")
            deinit()
            self.status_code=2001
            print("restarting download")
            remove(self.curr_dir+"/"+"tokenizer.p")
            self.get_token()


#print(token().status_code)
