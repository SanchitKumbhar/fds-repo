#include <iostream>
#include <queue>
#include <string>

class JobQueue {
private:
    std :: queue<std::string> jobs; 

public:
    //Function to add Job
    void addJob(const std::string& job){
        jobs.push(job);
        std::cout << "Job Added : " << job << std::endl;
    }

    //Function to delete Job
    void deleteJob(){
        if (!jobs.empty()){
            std::cout << "Jobs Deleted : " << jobs.front() << std::endl;
            jobs.pop();
        } else {
            std :: cout << "No Jobs to Delete " << std::endl;
        }
    }

    //Function to Display Jobs
    void displayJobs(){
        if(jobs.empty()){
            std :: cout << "No Jobs in the queue" << std :: endl;
            return;
        }

        std :: cout << "Current jobs in the queue : " << std::endl;
        std :: queue <std::string> temp = jobs;
        while (!temp.empty()){
            std :: cout << "- " << temp.front() << std :: endl;
            temp.pop();
        }
    }
};

int main () {
    JobQueue jobqueue;
    int choice;
    std :: string job;

    do{
        std :: cout << "Job Queue Menu : " << std::endl;
        std :: cout << "1. Add job" << std::endl;
        std :: cout << "2. Delete job" << std::endl;
        std :: cout << "3. Display jobs"<< std::endl;
        std :: cout << "4. Exit" << std::endl;
        std :: cout << "Enter your choice";
        std :: cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter job name: ";
                std::cin >> job;
                jobqueue.addJob(job);
                break;
            case 2:
                jobqueue.deleteJob();
                break;
            case 3:
                jobqueue.displayJobs();
                break;
            case 4:
                std::cout << "Exiting..." << std::endl;
                break;
            default:
                std::cout << "Invalid choice. Please try again." << std::endl;
        }
    } while (choice != 4);
    return 0;
}
