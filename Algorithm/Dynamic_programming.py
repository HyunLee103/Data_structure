# 피보나치_DP
def FibonacciDP(n):
    dic = {}
    dic[0] = 0
    dic[1] = 1
    for itr in range(2, n+1):
        dic[itr] = dic[itr-1] + dic[itr-2]
    return dic[n]

for itr in range(0, 10):
    print(FibonacciDP(itr))


# DP factory scheduling
class Assembly:
    t_station = [[7,9,3,4,8,4],[8,5,6,4,5,7]]
    t_belt = [[2,2,3,1,3,4,3],[4,2,1,2,2,1,2]]

    time_memoization = [list(range(6)),list(range(6))]
    trace = [list(range(6)),list(range(6))]

    def scheduling(self):
        num = len(self.t_station[0])
        self.time_memoization[0][0] = self.t_station[0][0] + self.t_belt[0][0]
        self.time_memoization[1][0] = self.t_station[1][0] + self.t_belt[1][0]

        for i in range(1, num):
            if self.time_memoization[0][i-1] > self.time_memoization[1][i-1] + self.t_belt[1][i]:
                self.time_memoization[0][i] = self.t_station[0][i] + self.time_memoization[1][i-1] + self.t_belt[1][i]
                self.trace[0][i] = 1
            else:
                self.time_memoization[0][i] = self.t_station[0][i] + self.time_memoization[0][i-1]
                self.trace[0][i] = 0

            if self.time_memoization[1][i] > self.time_memoization[0][i-1] + self.t_belt[0][i]:
                self.time_memoization[1][i] = self.t_station[1][i] + self.time_memoization[0][i-1] + self.t_belt[0][i]
                self.trace[1][i] = 0
            else:
                self.time_memoization[1][i] = self.t_station[1][i] + self.time_memoization[0][i-1] 
                self.trace[1][i] = 1

        costline1 = self.time_memoization[0][num-1] + self.t_belt[0][num]
        costline2 = self.time_memoization[1][num-1] + self.t_belt[1][num]
        
        if costline1 > costline2:
            return costline2, 1
        else:
            return costline1, 0

    def tracing(self,trace_line):
        num_statation = len(self.t_station[0])
        print('line :',trace_line,'station :',num_statation)
        for i in range(num_statation-1,0,-1):
            trace_line = self.trace[trace_line][i]
            print('line :',trace_line,'station :',i)

lines = Assembly()
time, trace_line = lines.scheduling()
print('Fastest time : ', time)
lines.tracing(trace_line)