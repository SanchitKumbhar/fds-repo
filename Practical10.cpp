#include <iostream>
#include <stack>
#include <string>
using namespace std;

//Check the precedence of the operator
int precedence (char op){
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

//Converting the infix expression to postfix
string infixToPostfix(const string& infix){
    stack <char> s;
    string postfix;

    for (char ch : infix){
        if(isalnum(ch)){
            postfix += ch;
        } else if (ch == '('){
            s.push(ch);
        } else if (ch == ')'){
            while (!s.empty() && s.top() != '('){
                postfix += s.top();
                s.pop();
            }
            s.pop();
        } else {
            while (!s.empty() && precedence(s.top()) >= precedence(ch)){
                postfix += s.top();
                s.pop();
            }
            s.push(ch);
        }
    }
    while (!s.empty()){
        postfix += s.top();
        s.pop();
    }
    return postfix;
} 

//Evaluating the postfix expression
int evaluatePostfix (const string& postfix){
    stack <int> s;

    for (char ch : postfix){
        if (isdigit(ch)){
            s.push(ch - '0');
        } else {
            int right = s.top(); s.pop();
            int left = s.top(); s.pop();
            switch (ch){
                case '+': s.push(left + right); break;
                case '-': s.push(left - right); break;
                case '*': s.push(left * right); break;
                case '/': s.push(left / right); break;
            }
        }
    }
    return s.top();
}

int main(){
    string infix;
    cout << "Enter an infix expression : ";
    cin >> infix;

    string postfix = infixToPostfix(infix);
    cout << "Postfix Expression = "<< postfix << endl;

    int result = evaluatePostfix(postfix);
    cout << "Result of Evaluation = " << result << endl;

    return 0;
}