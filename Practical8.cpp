#include <iostream>
#include <set>
#include <string>
using namespace std;

int main (){
    //Initiallizing three sets
    set<string> vanilla_students = {"A", "B", "C"};                                                                 
    set<string> butterscotch_students = {"B", "D", "E"};
    set<string> both_students;

    //Students who like both Vanilla and Butterscotch
    for (const auto& student : vanilla_students){
        if (butterscotch_students.find(student) != butterscotch_students.end()){
            both_students.insert(student);
        }
    }
    cout << "Students who like both Vanilla and Butterscotch : ";
    for (const auto& student : both_students){
        cout << student << " ";
    }
    cout << endl;

    //Students who like either Vanilla and Butterscotch
    set<string> either_student = vanilla_students;
    either_student.insert(butterscotch_students.begin(), butterscotch_students.end());
    cout << "Students who either like Vanilla or Butterscotch : ";
    for (const auto& student : either_student){
        cout << student << " ";
    }
    cout << endl;

    //Students who like neither of the flavours
    set<string> all_students = {"A", "B", "C", "D", "E", "F", "G"};
    int neitherCount = 0;
    for (const auto& student : all_students){
        if (vanilla_students.find(student) == vanilla_students.end() &&
            butterscotch_students.find(student) == butterscotch_students.end()){
                neitherCount++;
        }
    }
    cout << "Number of students who like neither Vanilla nor Butterscotch = "<< neitherCount << endl;

    return 0;
} 