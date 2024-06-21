#Extra practice problem
#Problem description : 
'''
Given an array of jobs, where each job is associated with its profit and deadline, find an ordering of all jobs that maximizes the profit. A job
generates a profit only if it is completed before the deadline

INPUT : 
An array of jobs, where each job Job is associated with its profit (denoted as profit(Job))
and deadline (denoted as deadline(Job)). Each job takes a single unit of time and no two
jobs can be performed at the same time. Given an ordering of all jobs, we say that the i-th job Job
in this ordering is well-scheduled if i ≤ deadline(Job), i.e., if it is finished before the deadline.
The profit of this ordering is defined as the total profit of all well-scheduled jobs. We assume
that the first job starts at time 0
'''

#Approach : Greedy Algorithm
'''
Will sort an array in descending order so we don't need to go thru each of them for our greedy choice
We choose max profit ones job, that way we will have max profit out of jobs we choose
We choose max and we will perform it on max deadline we can use : 
That way, we have choices available for other deadlines, in which we can maximize our profit
'''

def ordering_jobs(jobs) :
    #converting keys into list so we can sort it
    profits =  list(jobs.keys())
    profits.sort(reverse = True)

    #we also need a slot to store our greedy choice, so max slots capacity would be max deadline
    deadlines = list(jobs.values())
    slots = [None] * max(deadlines)

    for profit in profits :
        deadline = jobs[profit]
        index = deadline - 1

        if slots[index] == None : 
            slots[index] = profit

        else : 
            #find the slot if its deadline > index
            while(index > -1) : 
                if (slots[index] == None) :
                    slots[index] = profit
                    break

                index -= 1

    return slots
if __name__ == '__main__' :
    #we can give input for jobs as dictionary with key as profit and deadline as value
    jobs = {20 : 1, 25 : 1, 50 : 2, 30 : 2, 15 : 3} #profit : deadline
    jobs_2 = {60: 2, 100: 1, 20: 3, 30: 2, 40: 4}

    print(ordering_jobs(jobs_2))
