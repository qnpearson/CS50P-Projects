# QP Bank
### Video Demo: https://www.youtube.com/watch?v=LmIMwQe0Ats&ab_channel=QuinnPearson
### Description: A prototype stage banking application, allowing users to create an account, privately access their information, make deposits, withdrawals, and transfers to other users on the platform. Includes a UI designed with the rich library, unique account creation with associated pins, names, balances, routing numbers, and account numbers. Data is organized and updated in a dataframe using the pandas library.

# Introduction

QP Bank is a prototype banking application that serves to provide an easily usable interface for customers and owners alike. Upon opening the application users are prompted with
8 different options including: creating an account, accessing personal account data, making deposits, making withdrawals, making transfers, closing accounts,
accessing "administrative mode", and exiting the program. Each of these functions contains features to safeguard against user input error, and ensure the program runs smoothly.
This application is primarily intended for company side usage as opposed to customer side usage to safeguard against any potential security risks. Although many more features could
have been added to ensure security, correct user input, and enchanced user-interface time restraints have limited the current state of this application to a simple prototype
providing adequate use of essential features, and adequate safeguards against user error. The libraries used include the following: sys, pandas, rich and random. The usage of these
libraries will be described in further detail later in this description.

# Functions

## Main Function
The main function is way in which users interact with the program interface. Everytime the main function is initialized it displays the user interface created using the rich library.
Rich is a library used for displaying text and tabular data. The UI is displayed as a table where users have the ability to call 8 different functions as listed in the introduction.
Rich helps enable a better user experience and better clarity in options to decrease potential for user error and generally help the aesthetics and clarity of the application. Further,
all functions access data using the pandas library, and all functions call upon the corresponding dataframe called "customers" to alter, display, or append customer data. The dataframe customers contains the following information: "Name", "Pin", "Balance", "Routing Number" and "Account Number".

### [1] Create an Account
This function is called by inputting "1" into the main function and was created using the pandas library, and random and takes the arguments: customers, name, and pin. Upon providing this information this function checks for correctness of inputs, and if successful generates a 5 digit routing number, and 6 digit account number associated with the account. This new customer information is then appended to the customers dataframe providing a new row with the associated information. Further, the new customer is given an initial balance of $0. If I was to add more features to this function I would also have the function check the dataframe that no other account has the same routing number or account number before appending the dataframe. This could prevent serious errors in accessing the correct customer data.

### [2] Access Account Information
This function was created using the pandas library and takes the arguments: name and pin. Upon inputting name and pin this function checks the name and pin to make sure it matches the dataframe. If one of these values does not correspond correctly it returns an error message "Incorrect name or pin." and returns you to the main menu. If the information corresponds correctly, it greets the customer by name, and returns their corresponding account information which is a slice of the customers dataframe corresponding to that customer. Then it returns you to the main menu.

### [3] Make Deposit
This function was created using the pandas library and takes arguments: name, pin, and deposit. It was created using the same vetting method as the prior function "Access Account Information", but has the additional feature of vetting the deposit amount. The function checks that the deposit amount is a positive integer with no decimals. If the deposit does not meet the criteria the user is provided with an error message and returned to the main menu. If the arguments are entered correctly, it returns the users updated balance and returns user to the main menu.

### [4] Make Withdrawal
This function was created using the pandas library and takes arguments: name, pin, and withdrawal. It was created using the same vetting method as the prior function "Make Deposit", but has the additional feature of vetting the withdrawal amount as well as ensuring the withdrawal amount is less equal to the user's balance. If the withdrawal amount is greater than the user's balance, they are given an error message "Withdrawal exceeds available balance. Please try again." and are then returned to the main menu.

### [5] Make Transfer
This function was created using the pandas library and takes arguments: name, pin, transfer, and routing number. It was created using the same vetting method as the prior function "Make Withdrawal", but has the additional feature of vetting another user's routing number to find the corresponding account to transfer to. Similarly to making withdrawals, if the transfer amount exceeds the account balance the user is met with an error message. If the user inputs another user's routing number, and a vetted transfer amount, that amount will be transferred to the account of that user's balance to the other user's with the corresponding routing number. If a user tries to transfer to theirself, their balance will remain unchanged but will not be provided with an error message. Upon successful completion of a transfer, the function will return a greeting "Transfer successfully completed." and the user's updated balance following the transfer.

### [6] Close Account
This function uses the pandas library and takes the arguments: name and pin. It uses the same vetting process as "Access Account Information" and upon correct user input the function will ask the user if they are sure they would like to close their account (Yes/No). If the user inputs yes, the function will return the message "Account closed. Here is the remaining balanced returned." followed by the remaining account balance returned to the customer. Then the function will remove the customer's account from the customers dataframe.

### [7] Administrative View
This function uses the pandas library and prompts the user for the "Administrative Password". Upon inputting the administrative password "CS50" the function displays the entire customers dataframe and all account information.

### [8] Quit System
This function uses the sys library and provides the only means of exiting the application. Upon pressing "8" this function will run sys.exit() and display the quitting system message and close the entire application.

# Future Updates
In the future, I would like to be able to save the customers dataframe when closing the application and be able to access that information next time the application is opened. Furthermore, security measures and additional checking of user inputs is needed. For example, although the pin number asks the user for a 4 digit pin, it accepts any type of characters and any length of the string. Additionally, I think a 4-digit pin and username is not secure enough in providing distinction between user accounts because it is possible users of the same name could enter the same 4-digit pin. Furthermore, the UI could be improved especially when displaying the customers dataframe or it's elements.

# Design Choices
Initially I intended to program this application using OOP and did so unsuccessfully. I do believe the pandas dataframe provided an adequate alternative method in saving this data. I do think using OOP with an account/customer class could help in organizing this application or perhaps using some hybrid of the pandas library with OOP. Furthermore, a more legitimate UI would be nice.

# Conclusion
Although this application could be improved upon and some of the design choices were debatable. I believe I did provide a sufficient prototype banking application. Additional features are certainly needed to legitimize it for use, but these functions could also be extended to a variety of other applications that require account creation, and the saving of unique customer data. In the future I hope to develop this application more, and add the features it needs.