from tkinter.tix import Tree 

class Contact_book:
    def __init__(self):
        self.__data={}

    def addContact(self, name=None, address=None, phone_number=None,email=None):
        if name!= None and address!= None and phone_number!= None and email!=  None:
            if phone_number not in self .__data:
                self .__data[phone_number]=[name,address,phone_number,email]
                print("Data Added Successfully")   
            else:
                print("This Number is already  existing")
        else:
            print("Enter the required values")   


    def deleteContact(self,phone_number=None):
        if phone_number!=None:
            if phone_number in self .__data:
                del self .__data[phone_number]
                print("The data is deleted successfully")
            else:
                print("This phone number already exists")
        else:
            print("Enter the phone number")

    def editContact(self, name=None, address=None, phone_number=None,email=None):
        if phone_number!=None and phone_number in self .__data:
            lst_info= self .__data[phone_number]
            if name!=None:
                lst_info[0]=name
            if address != None:
                lst_info[1]=address
            if email != None:
                lst_info[3]=email
            self .__data[phone_number]=lst_info
            print("Data updated succesfully")
        else:
            print("This phone number does not exist")               

    def searchContact(self, query=None,sort_field=None):
        if query != None:
            search_arr=[]
            for key, val in self .__data.items():
                search_arr.append(val+[" ".join(val)])

            result=set()
            for word in query.lower().split():
                for i in range(len(search_arr)):
                    if word in search_arr[i][-1].lower():
                        result.add(i)


            ans =[]
            for i in result:
                ans.append(search_arr[i][:-1])


            indx=0
            if sort_field=='name': 
                indx=0
            if sort_field=='address':
                indx=1
            if sort_field=='phone_nummber':
                indx=2
            if sort_field=='email':
                indx=3   
            ans.sort(key=lambda x:x[indx])
        else:
            return[]

    def console(self):
        while True:
            try:
                print("\n1. Add Contact:\n2. Delete Conatact:\n3. Edit Contact:\n4. Search Contact:\n5 Stop:")
                n=int(input("Enter your choice:"))
                if n==1:
                    name=input("Name: ")
                    address=input("Address: ")
                    phone_number=input("Phone Number: ")
                    email=input("Email: ")
                    if len(name)==0:
                        name==None
                    if len(address)==0:
                        address=None
                    if len(phone_number)==0:
                        phone_address=None       
                    if len(email)==0:
                        email=None
                    self.addContact(name,address,phone_number,email) 

                if n==2:
                    phone_number=input("Phone Number: ")
                    if len(phone_number)==0:
                        phone_number=None
                    self.deleteContact(phone_number)

                if n==3:
                    name=input("Name: ")
                    address=input("Address: ")
                    phone_number=input("Phone Number: ")
                    email=input("Email: ")    
                    if len(name)==0:
                        name=None
                    if len(address)==0:
                        address=None
                    if len(phone_number)==0:
                        address=None
                    if len(email)==0:
                        email=None
                    self.editContact(name,address,phone_number,email)  


                if n==4:
                    query=input("Search: ")
                    sort_by=input("Sort by; ")  
                    if len(query)==0:
                        query=None
                    if len(sort_by)==0:
                        sort_by=None
                    self.searchContact(query,sort_by)

                if n==5:
                    break        

            except Exception as e:
                pass

contact_book=Contact_book()            
contact_book.console()
                                   