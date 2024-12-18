#include <iostream>
#include <stack>
#include <string>

bool isWellParenthesized (const std::string& expression){ //created an input "expression"
    std :: stack<char> s; //created a stack 's'

    for (char ch : expression){
        if (ch == '(' || ch == '{' || ch == '[') {
            s.push (ch);
        }
        else if (ch == ')' || ch == '}' || ch == '}'){
            if (s.empty()){
                return false;
            }
            char top = s.top();
            s.pop();
            if ((ch == ')' && top != '(') ||
                (ch == '}' && top != '{') ||
                (ch == ']' && top != '[')){
                    return false;
            }
        }
    }
    return s.empty();
}

int main(){
    std :: string expression;
    std :: cout << "Enter an expression : ";
    std :: getline (std::cin, expression);

    if (isWellParenthesized(expression)){
        std::cout << "The expression is well parentesized." << std :: endl;
    } else {
        std::cout << "The expression is not well parenthesized." << std :: endl;
    }
    return 0;
}