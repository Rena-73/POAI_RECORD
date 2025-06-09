% Rule to find the minimum of two numbers  
minimum(X, Y, X) :- X =< Y. % If X is less than or equal to Y, X is the minimum. 
minimum(X, Y, Y) :- X > Y. % If X is greater than Y, Y is the minimum. 
 
% Rule to find the maximum of two numbers 
maximum(X, Y, X) :- X >= Y. % If X is greater than or equal to Y, X is the maximum. 
maximum(X, Y, Y) :- X < Y. % If X is less than Y, Y is the maximum.
