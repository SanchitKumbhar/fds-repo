#include <iostream>
using namespace std;

class Node{
public:
  string prn;
  string name;
  Node* next;

  Node(string gprn, string gname){
    prn = gprn;
    name = gname;
  }
};

Node* head = NULL;

void addPresident(Node* head, string prn, string name){
    Node* gnode = new Node(prn, name);
    if (head == NULL){
        head->next = gnode;
        return;
    }

    gnode->next = head->next;
    head->next = gnode;
}

void displayLL(Node* head){
    Node* cur = head;
    while(cur != NULL){
        cout << cur -> prn <<" "<< cur -> name << endl; 
        cur = cur -> next;
    }
}

int main(){
    addPresident(head,"1", "abc");
    addPresident(head,"2", "xyz");
    displayLL(head);
}