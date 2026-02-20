#Assigning `import_file` to the name of the file 
import_file = "allow_list.txt"
#Assigning `remove_list` to a list of IP addresses that are no longer allowed to access restricted information 
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]
# Display `import_file`
print(import_file)
# Display `remove_list`
print(remove_list)

#Results
['192.168.97.225', '192.168.158.170', '192.168.201.40', '192.168.58.57']

# Building the `with` statement to read in the initial contents of the file
with open(import_file, "r") as file:

  # Using the `.read()` to read the imported file and store it in a variable named `ip_addresses`
 ip_addresses = file.read()
# Display `ip_addresses`
print(ip_addresses)

'''Results
ip_address
192.168.25.60
192.168.205.12
192.168.97.225
192.168.6.9
192.168.52.90
192.168.158.170
192.168.90.124
192.168.186.176
192.168.133.188
192.168.203.198
192.168.201.40
192.168.218.219
192.168.52.37
192.168.156.224
192.168.60.153
192.168.58.57
192.168.69.116'''

# Using `.split()` method to convert `ip_addresses` from a string to a list
ip_addresses = ip_addresses.split()
# Display `ip_addresses`
print(ip_addresses)

# Results
['ip_address', '192.168.25.60', '192.168.205.12', '192.168.97.225', '192.168.6.9', '192.168.52.90', '192.168.158.170', '192.168.90.124', '192.168.186.176', '192.168.133.188', '192.168.203.198', '192.168.201.40', '192.168.218.219', '192.168.52.37', '192.168.156.224', '192.168.60.153', '192.168.58.57', '192.168.69.116']

# Building an iterative statement,conditional statement,naming loop variable `element` and Looping through `ip_addresses`  
for element in ip_addresses:
  
  if element in remove_list:
    ip_addresses.remove(element)
# Display `ip_addresses` 
print(ip_addresses)

# Results
['ip_address', '192.168.25.60', '192.168.205.12', '192.168.6.9', '192.168.52.90', '192.168.90.124', '192.168.186.176', '192.168.133.188', '192.168.203.198', '192.168.218.219', '192.168.52.37', '192.168.156.224', '192.168.60.153', '192.168.69.116']

# Converting `ip_addresses` back to a string so that it can be written into the text file 
ip_addresses = " ".join(ip_addresses)    
# Using `with` statement to rewrite the original file
with open(import_file, "w") as file:
  # Rewriting the file, replacing its contents with `ip_addresses`
  file.write(ip_addresses)

# Building `with` statement to read the updated file
with open(ip_addresses, "r") as file:
    # Reading the updated file and storing the contents in `text`
    text = file.read()
# Displaying the contents of `text`
print(text)

'''Results
ip_address 192.168.25.60 192.168.205.12 192.168.6.9 192.168.52.90 192.168.90.124 192.168.186.176 192.168.133.188 192.168.203.198 192.168.218.219 192.168.52.37 192.168.156.224 192.168.60.153 192.168.69.116'''

'''Defining a function named `update_file` that takes in two parameters: `import_file` and `remove_list` 
and combines all the steps written above in this algorithm leading up to this'''

def update_file(import_file, remove_list):
  
# Calling `update_file()` function and passing in "allow_list.txt" and a list of IP addresses to be removed
 update_file ("allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])
# Using `with` statement to read in the updated file
with open("allow_list.txt", "r") as file:
  # Reading the updated file and storing the contents in `text`
  text = file.read()
# Display the contents of `text`

print(text)

'''Results
ip_address 192.168.205.12 192.168.6.9 192.168.52.90 192.168.90.124 192.168.186.176 192.168.133.188 192.168.218.219 192.168.52.37 192.168.156.224 192.168.60.153 192.168.69.116'''