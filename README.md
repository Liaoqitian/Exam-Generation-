# Exam-Generation Project 
This repo includes the auto-generated problems I wrote during Spring 2020. They are supported by PrairieLearn. The following is a more detailed description of each question's implemenations.  
[Sign and Magnitude](#Sign-and-Magnitude)
[Number Division](#my-multi-word-header)
[Number Multiplication](#my-multi-word-header)
[Speed Up ](#my-multi-word-header)
[Programming Paradigm](#my-multi-word-header) 
***
## Sign and Magnitude (Summer 2019, Question 5)
### Question Description:  
The concept of positive and negative binary numbers is not formally introduced in CS10. However, the question starts with a detailed explanation of the definition. This justifies the question to be present on a CS10 midterm. Meanwhile, the problem can be directly used in a CS61C exam. 
### Solution Form: 
Fill in the blank. 
### Implementation Description: 
For all the questions, solutions will be automatically computed corresponding to the randomized input. This solution will then be compared with the input of the student for checking and grading purposes. 
1. For the first question, a random number in the interval (-100, -50) and (50, 100) is generated. This restricts the variety of difficulty of the question, since the length of the binary number is restricted with no more than 8 digits and no less than 7 digits (including the sign digit). 
2. For the second question, a random number between 5 and 9 is generated. This restricts the variety of difficulty of the question. The number of digits does not significantly affect the difficulty of the question if the student is familiar with the clever method.
3. For the third question, a random number between 5 and 9 is generated. This restricts the variety of difficulty of the question. The number of digits does not significantly affect the difficulty of the question if the student is familiar with the clever method.  

### Demonstration: 
![alt text](https://github.com/Liaoqitian/Exam-Generation-/blob/master/Sign%20Magnitude/Question%20Demo.png "Question Demo")
***
## Number Division (Fall 2019, Question 6)
### Question Description: 
This question focuses on the division of numbers represented in different bases. 
### Solution Form:
Fill in the blank.  
### Implementation Description: 
The numbers I implemented are in binary, octal or hex. The divisor and the dividend are guaranteed to be in different bases. The two numbers are first randomly generated within the range (50, 100). Then they are converted to their base representation depending on their automatically generated bases. 
The solution is generated throughout the process. Student's solutions will be checked up to two significant digits. 
### Demonstration 
![alt text](https://github.com/Liaoqitian/Exam-Generation-/blob/master/Number%20Division/Solution%20Demo.png "Question Demo")
***
## Number Multiplication (Spring 2019, Question 6)
### Question Description: 
This question focuses on the multiplication of numbers represented in different bases. 
### Form:
Multiple Choice. 
### Implementation Details: 
The numbers I implemented are in binary, octal, decimal or hex. The divisor and the dividend are guaranteed to be in different bases. The two numbers are first randomly generated within the range (50, 100). Then they are converted to their base representation depending on their automatically generated bases. The solution is generated throughout the process. Furthermore, numerous incorrect confounding choices are automatically generated. This includes the following: 
1. A total of 7 off-target choices, both on the left and right-hand side of the correct solution with an offset of 2. The distribution of the incorrect choices (i.e. how many are on the left and how many are on the right) is randomized. 
2. Two dummy choices: The first one is generated by directly appending the second input to the first input. The second one has an offset of 2 from the first one. 
3. Two choices with the wrong base: The first one is the correct answer but with a wrong base. The second one is similar to the first one but with another wrong base. 

### Demonstration: 
![alt_text](https://github.com/Liaoqitian/Exam-Generation-/blob/master/Number%20Multiplication/Solution%20Demo.png "Question Demo")
***
## Speed Up (Spring 2019, Question 5)
### Question Description:
This question focuses on the relationship between infinite cores and maximum speedup.  
### Solution Form: 
Multiple Choice. 
### Implementation Details:
The percentage of program which is serial is randomized in the list [5, 10, 20, 25, 50, 100]. Then the corresponding solution is computed by taking its reciprical. 
### Demonstration: 
![alt_text](https://github.com/Liaoqitian/Exam-Generation-/blob/master/Speed%20Up/Solution%20Demo.png "Question Demo")
***
## Programming Paradigm (Fall 2018, Question 8)
### Question Description: 
This question focuses on matching each programming paradigm with a problem best suited to it. 
### Solution Form: 
Multiple Choice. 
### Implementation Details: 
The input of the four texts are stored in strings. The sequence in which they appear and their corresponding solutions is randomized. 
### Demonstration:
![alt_text](https://github.com/Liaoqitian/Exam-Generation-/blob/master/Programming%20Paradigm/Solution%20Demo.png "Question Demo")

