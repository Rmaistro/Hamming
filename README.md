# Hamming
Hamming (7,4) by Jelle, Nena, Xander
## What is this?
This is a schoolproject, made by three students at Utrecht University in the Netherlands.
It is part of a Programming Course for Mathematics. While writing, we are all in our first year of the
Mathematics Bachelor. We implemented the Hamming (7,4) code and analyzed different
implementations of the algorithm.
## Code features:
Both the ”Hamming 7 4 code.py” (the matrix implementation) and ”Hamming 7 4 bitwise.py”
(the bitwise implementation) have a print statement that is called, every time one
runs the document. This block of code can be found on the lines 229-242 and the
lines 207-220 respectively. The input function gives the following question:
”Type ’analysis’ if you want to perform an complexity analysis, type
’codecheck’ if you want to check wether or not the code works, type
’encrypt’ if you want to encrypt a message or ’decrypt’ if you want to
decrypt and if needed correct a message: ”In other words, there are four choises 
that the user can make. If a correctly spelledanswer is provided, the program will 
run the code that, as said in the message, a follow-up question might be presented.
There is also a Matrix and Vector class in the repository, which was used during the project, but
could by used individualy. Finally, there is a short Hamming (15,11) implementation, which could be
used, but has not been developped properly. 
## In- and output:
With the ”encrypt” function one can convert a string of character into a
list of seven bit long, secured strings, presented in a list. The ”decrypt” 
function can change a list, as produced by the "encypt" function back to the original 
message, even when up to one bit per element of the list is flipped. The ”codecheck” 
generates a random string and checks whether or not the function 
still works, by running the encrypt and decrypt function back to back. 
Further more: it randomly flips a bit in the produced string. 
With the ”analysis” function the user can initiate 30.000 random checks which are presented
in a plot in your Python editor "plots"-window.
## Contribution:
Contributions to this project are not (yet) possible since it is a schoolproject, that has yet
to be grated. 