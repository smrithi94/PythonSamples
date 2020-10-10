#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import sys 


# In[3]:


def print_char(option,domain=None,class_ABC=None):
    #result_a=[]
    if(os.access('C:/Users/vvs87/Desktop/host_files.txt',os.R_OK)):
        with open("C:/Users/vvs87/Desktop/host_files.txt") as fp:
            filesize = os.path.getsize('C:/Users/vvs87/Desktop/host_files.txt')
            result_a=[]
            result_d=[]
            result_ip=[]
            if filesize==0:
                return 'File is empty'
        
            elif option =='-a':
                for line in enumerate(fp):
                    lines=line[1].split(' ')
                    result_a.append(lines[1]) 
                return result_a
            
            elif option =='-d' and domain:
                
                for line in enumerate(fp):
                    lines=line[1].split(' ')
                    if (lines[1].split('.')[-1]==domain):
                        result_d.append(line[1])
                
                if len(result_d) == 0: 
                    return 'No hosts in the given domain'  
                else: 
                    return result_d
            
            elif option =='-c' and class_ABC:
                for line in enumerate(fp):
                    #print(line)
                    lines=line[1].split(' ')
                    Ip_number=lines[0].split('.')[0]
                    if class_ABC=='A':
                        if(int(Ip_number)>0 and int(Ip_number)<128): 
                            result_ip.append(line[1])
                        #return result_ip #Not Working 
                    elif class_ABC=='B':
                        if(int(Ip_number)>=128 and int(Ip_number)<=191): 
                            result_ip.append(line[1])
                        #return result_ip # Not Working 
                    elif class_ABC=='C':
                        if(int(Ip_number)>=192 and int(Ip_number)<255): 
                            result_ip.append(line[1])
                    #return result_ip
                    else:
                        return 'Improper input'

                if len(result_ip)==0:
                    return 'No Such domain' 
                else: 
                    return result_ip
            elif option=='-v':
                    print('Student_id')
                    print('Name')
                    print('Date')
    else: 
        return 'File is not present'

def main():
    opt=sys.argv[1]
    #print(sys.argv[-1])
    #print(sys.argv[-1])
    if ((opt== '-a') and (sys.argv[-1]=='hosts_files')):
        result=print_char(opt,None,None)
        print(result)
    elif opt=='-d' and sys.argv[-1]=='hosts_files':
        result=print_char(opt,sys.argv[2])
        print(result)
    elif opt=='-c' and sys.argv[-1]=='hosts_files':
        result=print_char(opt,None,sys.argv[2])
        print(sys.argv[2])
        print(result)

    else:
        print('Improper input')

if __name__ == "__main__":
    main()

# In[4]:and sys.argv[-1]=='hosts_file'


#result=print_char('-c',None,'C')
#print(result)
#print(sys.argv)
#print(sys.argv[1])

# In[6]:

#def main():
    
    #if (option== '-a'):
        #result=print_char(option)
        #print(result)
    #elif (sys.argv[1] =='-d'):
        #result=print_char(option,sys.argsv[2])
        #print(result)



# In[ ]:




