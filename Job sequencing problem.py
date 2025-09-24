# Job sequencing problem
# https://www.geeksforgeeks.org/problems/job-sequencing-problem/1



def jobScheduling(deadline, profit):
    n = len(deadline)

    jobs = list(zip(profit, deadline))

    jobs.sort(reverse=True)

    max_deadline = max(deadline)

    slot = [-1] * (max_deadline + 1)
    
    total_profit = 0
    count_jobs = 0
    
    for p, d in jobs:
        for j in range(d, 0, -1):
            if slot[j] == -1:
                slot[j] = 1 
                total_profit += p
                count_jobs += 1
                break
    
    return [count_jobs, total_profit]

deadline1 = [4, 1, 1, 1]
profit1   = [20, 10, 40, 30]
print(jobScheduling(deadline1, profit1))  

deadline2 = [2, 1, 2, 1, 1]
profit2   = [100, 19, 27, 25, 15]
print(jobScheduling(deadline2, profit2))  

deadline3 = [3, 1, 2, 2]
profit3   = [50, 10, 20, 30]
print(jobScheduling(deadline3, profit3))  
