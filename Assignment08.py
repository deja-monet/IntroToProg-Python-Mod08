# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# dejam,220829,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
#declare variables and constants
strFileName = 'products.txt'
lstOfProductObjects = []
user_choice = ""

class Errors:
    def user_input():
        print("Something went wrong with the user input...")
    def no_numeric():
        print("You must enter a number!")
    def too_many_characters():
        print("You entered too many characters!")

class Product:
    """
    Stores data about a product:

    properties:
        product_name: (string) with the product's  name

        product_price: (float) with the product's standard price
    methods:
        add_data_to_list(): processes user input data into a temporary array that is then appended a list of arrays
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        dejam,220829:
            - modified code to complete assignment 8
            - created add_data_to_list function
    """
    #product_name and product_price are initialized
    product_name = ""
    product_price = 0.00
    
    #add data to list of product objects
    def add_data_to_list(product_name, product_price):
        
        #add user input data to array
        row = [product_name, product_price]
        
        #add array to list of arrays
        lstOfProductObjects.append(row)
        
        #alert user their data has been successfully processed
        print("Your data has been added to the list!")
        
        #return updated list of rows
        return lstOfProductObjects

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """
    Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        dejam,220829:
            - modified code to complete assignment 8
            - created load_data_to_file and save_data_to_file functions
    """
    #data is loaded from file
    @staticmethod
    def load_data_to_file(strFileName):
        try:
            lstOfProductObjects.clear() #clear current data from list
            file_load = open(strFileName, "r")
            
            #array is loaded as rows into lstOfProductObjects table
            for line_cycle in file_load:
                
                #paired product_name and product_price are identified by the comma between them
                line_split = line_cycle.split(",")
                product_name = line_split[0].strip()
                product_price = line_split[1].strip()
                
                #row is the product name and product price identified above (with any leading/trailing spaces removed)
                row = [product_name, product_price]
                
                #row is appended to lstOfProductObjects
                lstOfProductObjects.append(row)
                
            file_load.close()
            print("Data loaded from file!")
            return lstOfProductObjects
        
        except FileNotFoundError:
            print("No data to load from file!")
                 
    #data is saved to file
    @staticmethod
    def save_data_to_file(strFileName, lstOfProductObjects):
    
        #products.txt is identified as file_obj
        file_obj = open(strFileName, "w")
        
        #write user input to-do items to products.txt
        for row in lstOfProductObjects:
            file_obj.write(row[0] + ", " + str(row[1]) + "\n")
        
        #products.txt is closed
        file_obj.close()
        
        #user is alerted that their data has successfully been saved
        print("Your data has been saved!")

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """
    Receives user input and processes output to user
    
    properties:
        lstOfProductObjects: a list of Python arrays that contain the user's input product_name and product_price
    methods:
        main_menu(): prints main menu to user
        input_menu_choice(): receives the user's choice from the main menu and returns this choice
        output_current_data(): prints the user's current data when the user makes that choice
        input_product_data: receives the user's input product_name and product_price
    changeLog: 
        dejam, 220829:
            - created docString
            - created functions listed above in "methods" to complete assignment
    """

    #show main menu to user
    @staticmethod
    def main_menu():
        print("""
        Menu of Options
        1) See current data in list of product objects
        2) Add data to the list of product objects
        3) Save current data to file and exit program
        """)
        
    #return user's choice from main menu
    @staticmethod
    def input_menu_choice():
        user_choice = str(input("Which option would you like to perform? [1 to 3]: ")).strip()
        return user_choice
    
    #show the current data from the file to user
    @staticmethod
    def output_current_data(lstOfProductObjects):
        if(lstOfProductObjects != []):
            print("Here is the current product data: ")
            for row in lstOfProductObjects:
                print(row[0] + ", " + str(row[1]))
        else:
            print("There is no data to display!")
    
    #get product data from user
    @staticmethod
    def input_product_data():
        #retrieve user input product name
        Product.product_name = input("Enter a product name: ")
        
        #retrieve user input product price
        Product.product_price = float(input("Enter the product's standard price: "))
                                      
        #return user input product name and product price
        return Product.product_name, Product.product_price

# Main Body of Script  ---------------------------------------------------- #

#load data from file into a list of product objects when script starts
FileProcessor.load_data_to_file(strFileName)

#continue to return to main menu until user chooses to save and exit script
while(True):
    #show user a menu of options
    IO.main_menu()
    
    #get user's choice from menu of options
    user_choice = IO.input_menu_choice()
    
    #return to main menu if user does not enter a number
    if(user_choice != "1" and user_choice != "2" and user_choice != "3"):
        Errors.user_input()
        if(user_choice.isnumeric() == False):
            Errors.no_numeric()
        if(len(user_choice) != 1):
            Errors.too_many_characters()
    
    #show user current data in the list of product objects
    if(user_choice.strip() == "1"):
        #show user the current data 
        IO.output_current_data(lstOfProductObjects)
    
    #let user add data to the list of product objects
    if(user_choice.strip() == "2"):
        #ask for user input product name and product price
        product_name, product_price = IO.input_product_data()
        
        #add user input product name and product price to list of product objects
        Product.add_data_to_list(product_name, product_price)
        
    #let user save current data to file and exit program
    if(user_choice.strip() == "3"):
        #save current data to file
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        
        #exit script
        print("Exit script!")
        break
