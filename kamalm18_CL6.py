#!/usr/bin/env python
# coding: utf-8

# # Computing 6 Assignment
# 
# 

# ---
# ## Background
# 
# In this assignment you will be implementing a portion of a Geographic Information System (GIS). A GIS is a computer system used to organize, categorize, and analyze geographical data in order to produce accurate depiction of the real world. The system uses multiple layers of information to achieve this task. The data layers are split into a grid and represented as a matrix with **m** rows and **n** columns where each entry in the matrix contains the type of land at that point on the map. An entry **A<sub>ij</sub>** is the *i*th row and *j*th column in our map matrix. We assume that **A<sub>00</sub>** is the first element in our matrix. The graphic below will assist in visualizing the process:
# 
# ![Comp6.png](attachment:Comp6.png)
# \begin{align}
#   \texttt{Figure 1}
# \end{align}
# 
# 
# As seen in the previous example, our GIS utilizes **6** different data layers. We call these layers the **map types** as they classify regions of different land on our map. Thus, each entry in our map matrix can be **one** of the 6 map types.
# 
# -	Transportation (T)
# -	Agricultural (A)
# -	Residential (R)
# -	Commercial (C)
# -	Water (W)
# -	Undeveloped land (U)
# 
# Our GIS will store the map information as a list of lists. If we have a list named **map**, then map[i][j] will store the map type at row i, column j. Each entry will contain a string that corresponds to 1 of the 6 possible map types listed above. The list representation of the map in **Figure 1** is shown below:

# ```
# [['A','A','A','A','U','U','U','U'],    
#  ['A','A','A','A','U','R','R','R'],    
#  ['W','W','W','W','T','T','T','T'],    
#  ['W','W','W','W','T','R','R','R'], 
#  ['C','C','U','U','T','R','U','U'],    
#  ['T','T','T','T','T','T','U','U'],    
#  ['U','U','U','U','T','R','U','U']]
# 
# ```
# 

# One usage of the system is to be able to easily identify whether or not a piece of land (entry in the map matrix) is deemed **commercially buildable**. A piece of land at **A<sub>ij</sub>** is deemed commercially buildable if the following conditions hold:
# -	The entry at **A<sub>ij</sub>** has map type **U**
# -	The entry **A<sub>ij</sub>** is not on the edges of the map (the first and last rows and columns).
# -	The entry **A<sub>ij</sub>** is not adjacent with an entry of map type **R** or map type **A**. Note that adjacent entries are entries to the top, bottom, left, and right of the current cell.
# 
# Based on the criteria and the map representation of **Figure 1**, it can be seen that **A<sub>4,2</sub>** is commercially buildable and **A<sub>1,4</sub>** is not commercially buildable.

# ---
# ## Additional Information (Important!)
# When using a 2D list, we can access elements around a specific index. Let's define a 3x3 2D list, **x**, seen below:

# <center>x =[[1,2,3], <br>
#      &nbsp; &nbsp; &nbsp;[4,5,6], <br>
#      &nbsp; &nbsp; &nbsp;[7,8,9]]</center>

# If we define variables **i**, and **j**, to both equal 1 for example, then **x[ i ][ j ]** would be **x[ 1 ][ 1 ]**, which in this 2D list is the integer _5_. We can access elements around this specific index by modifying our **i** and **j** variables. We can subtract or add 1 from **i** to access the elements above or below the original index. Addtionally, we can subtract or add 1 from **j** to access the elements to the left or right of the original index. To summarize:
#  
# - **x[ i-1 ][ j ]** would access the element <u>above</u> the original index. which here is _2_
# - **x[ i+1 ][ j ]** would access the element <u>below</u> the original index, which here is _8_
# - **x[ i ][ j-1 ]** would access the element <u>left</u> of the original index, which here is _4_
# - **x[ i ][ j+1 ]** would access the element <u>right</u> of the original index, which here is _6_

# ---
# Be careful when accessing adjacent elements - if you try to access an element that doesn't exist, you might receive an unexpected output, or an error! For example:

# - **x[ i-2 ][ j ]** which is equivalent to **x[ -1 ][ 1 ]**, would wrap around and give us the middle element in row **-1**, which here is the last row.
# - **x[ i ][ j+2 ]** Would try to access the element at **x[ 1 ][ 3 ]**, or in the nonexistent colum 3, which would produce an <u>error seen below!</u>
# 
# ```
# ----> 2 print(x[i][j+2])
# IndexError: list index out of range
# ```

# ---
# ## Program Requirements (12 Marks)
# 
# Your GIS system will be comprised of a set of functions used to analyze the information of any given map. In addition, you will be creating a function used to determine whether or not a piece of land is commercially buildable. The requirements of the system are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks.
# 
# 1. Define a function **count_type**(*map_data*, *map_type*):
#   - ***map_data***: A *list of lists* representing the data for a given map.
#   - ***map_type***: A *string* representing a map type ('T','A','R','C','W', or 'U')
#   - **Return:** An *integer* representing the number of times *map_type* occurs in *map_data*.
#   
#   
# 2.	Define a function **classify_map**(*map_data*):
#   -	***map_data***: A *list of lists* representing the data for a given map.
#   -	**Return**: A map classification according to the following rules:
#           -	The *string* **Suburban** if the number of <u>'R' cells is greater than 50% of all cells.</u>
#           - The *string* **Farmland** if the number of <u>'A' cells is greater than 50% of all cells.</u>
#           - The *string* **Conservation** if the number of <u>'U' cells plus the number of 'W' cells is greater than 50% of all cells.</u>
#           - The *string* **City** if the number of <u>'C' cells is greater than 50% of all cells **and** the number of 'U' cells plus the number of 'A' cells is between 10% and 20% of all cells (inclusive).</u>
#           - The *string* **Mixed** if none of the above criteria are met.  
#           _(Hint, use your count_type function coupled with the fact that the total cells in map\_data is given by m*n)_
#           
# 
# 3.	Define a function **isolate_type**(*map_data*, *map_type*):
#   -	***map_data***: A *list of lists* representing the data for a given map.
#   -	***map_type***: A *string* representing a map type (‘T’, ‘A’, ‘R’, ‘C’, ‘W’, or ‘U’)
#   -	**Return**: A <u>new</u> *list of lists* that represent *map_data* as a matrix but all entries that **are not** equal to *map_type* are replaced with a string containing only a space (" ").   
#   _(Hint, review the In-Lab Notebook <u>Nested Loops to Process Lists of Lists</u> demo on how to process 2D lists)_
#   
#   
# 
# 4.	Define a function **commercially_buildable**(*map_data*, *i*, *j*):
#   -	***map_data***: A *list of lists* representing the data for a given map.
#   -	***i***: An *integer* representing a given row in *map_data*.
#   -	***j***: An *integer* representing a given column in *map_data*.
#   -	**Return**: **True** if *map_data[i][j]* ( **A<sub>ij</sub>**) is commercially buildable, otherwise **False**, according to the following rules from our background information:
#             -	First, ensure that the entry **A<sub>ij</sub>** is not at the edge of the map (the first and last rows and columns). If it is, return **False**. _(Hint, you will need to find the amount of rows and columns in the map for this step)_
#             -   Ensure that the entry **A<sub>ij</sub>** has map type **U**, otherwise return **False**.
#             -   Ensure the entry **A<sub>ij</sub>** is not adjacent with an entry of map type **R** or map type **A**. Note that adjacent entries are entries to the top, bottom, left, and right of the current cell. _(Hint, review the additional information section for this step)_

# ---
# ## Implementation
# Please define all functions in the cell below

# In[34]:


#********************************************
# Write your count_type function below: (2 marks)
#********************************************
def count_type(map_data, map_type):
    count = 0
    for i in map_data: # iterates through the rows and columns of the list and adds each entry to the total if it corresponds with the type inputted
        for j in i:
            if j == map_type:
                count += 1
    return count

#********************************************
# Write your classify_map function below: (4 marks)
#********************************************
def classify_map(map_data):
    total = 0
    for i in map_data:
        total += len(i)
    if count_type(map_data, 'R') > (total/2): # checks if >50% of list is 'R'
        return "Suburban"
    elif count_type(map_data, 'A') > (total/2): # checks if >50% of list is 'A'
        return "Farmland"
    elif (count_type(map_data, 'U') + count_type(map_data, 'W')) > (total/2): # checks if >50% of list is 'U' and 'W'
        return "Conservation"
    elif (count_type(map_data, 'C') > (total/2)) and (count_type(map_data, 'U') + count_type(map_data, 'A')) >= (total/10) and (count_type(map_data, 'U') + count_type(map_data, 'A')) <= (total/5): # checks if >50% of list is 'C' and between 10-20% is 'A' and 'U'
        return "City"
    else:
        return "Mixed"

#********************************************
# Write your isolate_type function below: (2 marks)
#********************************************
def isolate_type(map_data, map_type):
        new_map = map_data
        for i in range(len(new_map)): # iterates through rows and columns of the new list
            for j in range(len(new_map[0])):
                if new_map[i][j] != map_type: # checks if list element is equal to the type inputted, replaces with ' ' otherwise
                    new_map[i][j] = " "
        return new_map

#********************************************
# Write your commercially_buildable function below: (2 marks)
#********************************************
def commercially_buildable(map_data, i, j):
    rows = len(map_data)
    columns = len(map_data[0])
    if i == 0 or i == (rows-1) or j == 0 or j == (columns-1): # checks if list index is in the first/last row/column
        return False
    elif map_data[i][j] != 'U': # checks if list element is of type 'U'
        return False
    elif map_data[i+1][j] == 'R' or map_data[i+1][j] == 'A' or map_data[i-1][j] == 'R' or map_data[i-1][j] == 'A' or map_data[i][j+1] == 'R' or map_data[i][j+1] == 'A' or map_data[i][j-1] == 'R' or map_data[i][j-1] == 'A': # checks if any adjacent indexes in the list are 'A' or 'R'
        return False
    else:
        return True
    


# ---
# ## Testing
# 
# Unlike the other computing labs that required you to run main() to validate your code, these functions can act as stand-alone functions. You have been provided with some test cases, but you are encouraged to create more to thoroughly test your code.
# 
# ### Important
# 
# Run the cell where you implemented your functions first and ensure it outputs with no errors. Then, run the testing cell to verify that your code works correctly with the provided input. The following message should be printed after the testing cell is run:
# 
# ```
# The number of U spaces in MAP = 17  
# The number of T spaces in MAP2 = 12 
# MAP Type = Mixed 
# MAP2 Type = City  
# -----------------
# Isolated MAP: U
# [' ', ' ', ' ', ' ', 'U', 'U', 'U', 'U']
# [' ', ' ', ' ', ' ', 'U', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', 'U', 'U', ' ', ' ', 'U', 'U']
# [' ', ' ', ' ', ' ', ' ', ' ', 'U', 'U']
# ['U', 'U', 'U', 'U', ' ', ' ', 'U', 'U']
# -----------------
# Isolated MAP2: T
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# ['T', 'T', 'T', 'T', 'T', ' ', ' ']
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# [' ', ' ', ' ', ' ', ' ', 'T', ' ']
# [' ', ' ', ' ', ' ', ' ', ' ', ' ']
# [' ', ' ', ' ', 'T', ' ', ' ', ' ']
# [' ', 'T', ' ', 'T', ' ', ' ', ' ']
# -----------------
# Is MAP commercially buildable at (4,2): True  
# Is MAP2 commercially buildable at (2,2): False
# ```
# 
# Again, note that your code is not necessarily correct if your output matches the expected output. Your code will be checked against multiple inputs for correctness. The cell below is not graded, so feel free to modify the code as you wish!

# In[35]:


MAP = [['A','A','A','A','U','U','U','U'],
       ['A','A','A','A','U','R','R','R'],
       ['W','W','W','W','T','T','T','T'],
       ['W','W','W','W','T','R','R','R'],
       ['C','C','U','U','T','R','U','U'],
       ['T','T','T','T','T','T','U','U'],
       ['U','U','U','U','T','R','U','U']]

MAP2 = [['C','C','C','C','R','T','C'],
        ['T','T','T','T','T','C','C'],
        ['C','C','W','C','R','T','C'],
        ['C','C','C','W','U','T','C'],
        ['C','C','C','U','U','T','C'],
        ['C','C','C','C','C','U','C'],
        ['C','C','C','T','U','U','C'],
        ['C','T','C','T','U','A','C']]


# count_type() and classify_map() functions
print("The number of U spaces in MAP =",count_type(MAP, 'U'))
print("The number of T spaces in MAP2 =",count_type(MAP2, 'T'))
print("MAP Type =",classify_map(MAP))
print("MAP2 Type =",classify_map(MAP2))

# isolate_type() function
print("-----------------")
print("Isolated MAP: U")
MA = isolate_type(MAP,'U')
for row in MA:
    print(row)
print("-----------------")
print("Isolated MAP2: T")
MB = isolate_type(MAP2,'T')
for row in MB:
    print(row)
print("-----------------")

# commercially_buildable() function
print("Is MAP commercially buildable at (4,2):",commercially_buildable(MAP,4,2))
print("Is MAP2 commercially buildable at (2,2):",commercially_buildable(MAP2,2,2))


# ----------
# ## Code Legibility (6 Marks)
# Your code will be marked on commenting and code legibility.<br>
# The mark breakdown is as follows:<br>
# > - 2 marks for using **appropriate variable names** that indicate what is being stored in that variable<br>
# >- 2 marks for leaving **comments on major parts of your code** such as where you read the file or calculate a summation<br>
# >- 2 marks for **general legibility**. The TA's should be able to understand your code without spending hours reading it. For example do not put your code in one very long line as this is hard for someone else reading your code to understand

# ---
# ## Test Plan
# Develop a test plan for your program. Your test plan should have at least three test cases: one normal case, one boundary case, and one abnormal case. You can test any function but you must test **at least two different** functions. Please use the following format for your test cases:
# 
# **Function:**   
# **Input:**  
# **Output:**  
# **Expected Output:**  
# **Pass/Fail:**  
# 
# An example test case is shown below:  
# ```
# Function: count_type(map_data,map_type)
# Input: map_data = [['U','T','U','A'],
#                     ['R','T','W','A'],
#                     ['U','T','A','W']]  
#        map_type = 'U'
# Output: 3
# Expected Output: 3
# Pass/Fail: Pass
# ```
# 
# Implement your testing plan in the cell below! 

# ```
# Normal case:
#     Function: count_type(map_data,map_type)
#     Input: map_data = [['U','T','U','A'],
#                         ['R','T','W','A'],
#                         ['U','T','A','W']]  
#            map_type = 'R'
#     Output: 1
#     Expected Output: 1
#     Pass/Fail: Pass
# 
# Boundary case:
#     Function: classify_map(map_data)
#     Input: map_data = [['U','T','A','A'],
#                         ['R','T','A','A'],
#                         ['U','T','A','A']]
#     Output: "Mixed"
#     Expected Output: "Mixed"
#     Pass/Fail: Pass
# 
# Abnormal case:
#     Function: commercially_buildable(map_data, i, j)
#     Input: map_data = [['U','T','U','A'],
#                         ['R','T','U','A'],
#                         ['U','T','T','W']]  
#            i = 'ksdjalkshda'
#            j = 2
#     Output: Type error
#     Expected Output: Type error
#     Pass/Fail: Pass
# ```

# ---
# ## Reflective Questions (6 Marks)
# 
# 1. Which functions did you use a nested structure (nested loops, nested conditionals, etc) to implement the requirements? Would it have been possible to implement them without using a nested structure? Which functions did you *not* use a nested structure? Would it have been possible to implement them *with* a nested structure?  
# 
# 
# 2. Suppose we wanted to create an additional map classification called 'Urban City' which is indicated by the number of 'R' cells plus the number of 'C' cells being between 60% and 80%. Can we do this? How might this affect our classify_map() function?
# 
# 
# 3. How many test cases would you need to confirm that your classify_map() function correctly identifies a "Farmland" map? Explain what your test cases would be.

# ```
# 1) I used nested loops in count_type() and isolate_type(). Yes, its possible to create those functions without nested structures by using another method such as recursion to iterate through both rows and columns in a nested list. the functions classify_map() and commercially_buildable() didn't use any nested structures. However, it's possible to implement them when eg. checking conditions to classify the map or see if a plot is commercially buildable. I used regular if/elif/else statements, but I could have used nested conditionals instead.
# 
# 2) We can create it by adding another elif statement in classify_map() that checks if the number of 'R' cells plus the number of 'C' cells being between 60% and 80%. If that statement is true, then the function will return "Urban city".
# 
# 3) 3 test cases:
# - one where less than 50% the land has 'A'
# - one where exactly 50% of the land is 'A'
# - one where more than 50% of the land is 'A'
# ```

# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 6 dropbox on avenue with the naming convention: macID_CL6.py
# 
# #### NOTE: YOU WILL BE MARKED ON MULTIPLE ITEMS IN THIS LAB IN ADDITION TO THE FUNCTIONALITY OF YOUR CODE
#  - Variable Names
#  - Commenting
#  - General Legibility
#  - Reflective Questions
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely receive zero.**
# 
# This assignment is due the day of your Lab section at 11:59 PM EST
# 
# Late labs will not be accepted
