# writing a  valid email address code 
 
email =input("Enter a Email address: ")
k,j,d=0,0,0
if len(email)>=7:  # example          k@k.com       or  kedra@gmail.com
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-3]==".") ^ (email[-4]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Wrong emial address 5")
                else:
                    print("Valid Email Address...........")
            else:
                print("Wrong Email Address 4")
        else:
            print("Wrong Email Address 3")
    else:
        print("Wrong Email Address 2")
    
else:
    print("Wrong Email Address 1  ")