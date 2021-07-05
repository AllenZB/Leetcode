from queue import PriorityQueue
class Solution:
    def getOrder(self, tasks):
        task = []
        pq = PriorityQueue()

        for i in range(len(tasks)):
            task.append([tasks[i][0], tasks[i][1], i])
        task.sort(reverse=True)
        ans = []
        currenttime = task[-1][0]
        while task:
            print('test')
            while task:
                print('test11')
                if currenttime >= task[-1][0]:
                    pq.put([task[-1][1], task[-1][2]])
                    task.pop()
                else:
                    break
            if pq.empty()==False:
                current = pq.get()
                ans.append(current[1])
                currenttime += current[0]
            else:
                currenttime = task[-1][0]
        while pq.empty()==False:
            ans.append(pq.get()[1])
            print('test1111')
        print('return')
        return ans

a=[[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]
a=[[100,100],[1000000000,1000000000]]
print(Solution().getOrder(a))
