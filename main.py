import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random


df = pd.read_csv('studentMarks.csv')
data = df["Math_score"].tolist()
fig = ff.create_distplot([data], ["Math_score"], show_hist=False)
fig.show()

data_mean = statistics.mean(data)
data_std_deviation = statistics.stdev(data)
print(data_mean)
print(data_std_deviation)

def random_set_of_mean(counter):
    data_set = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return mean

# Function to get the mean of 100 data sets
mean_list = []
for i in range(0, 1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)


## calculating mean and standard_deviation of the sampling distribution.

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print('standard deviation: ', std_deviation)
print('mean : ',mean)

## findig the standard deviation starting and ending values
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)


# # finding the mean of THE STUDENTS WHO GAVE EXTRA TIME TO MATH LAB and plotting on graph
df = pd.read_csv('School_1_Sample.csv')
data = df['Math_score'].tolist()

mean_of_sample_1 = statistics.mean(data)
print('mean of sample 1:', mean_of_sample_1)
fig=ff.create_distplot([mean_list], ["Student marks"], show_hist=False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode="lines", name="mean"))
fig.add_trace(go.Scatter(x = [mean_of_sample_1, mean_of_sample_1], y=[0,0.17], mode="lines", name="mean of students who had math labs"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))


fig.show()

# #finding the mean of the STUDENTS WHO USED MATH PRACTISE APP and plotting it on the plot.
df = pd.read_csv('School_2_Sample.csv')
data = df["Math_score"].tolist()

mean_of_sample_2 = statistics.mean(data)
print('mean of sample 2:', mean_of_sample_2)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0, 0.17], mode="lines", name="mean"))

fig.add_trace(go.Scatter(x = [mean_of_sample_2, mean_of_sample_2], y=[0,0.17], mode="lines", name="mean of students who had math labs"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

fig.show()

# finding the mean of the STUDENTS WHO WERE ENFORCED WITH REGISTERS and plotting it on the plot.

df = pd.read_csv('School_3_Sample.csv')
data = df["Math_score"].tolist()

mean_of_sample_3 = statistics.mean(data)
print('mean of sample 3:', mean_of_sample_3)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0, 0.17], mode="lines", name="mean"))

fig.add_trace(go.Scatter(x = [mean_of_sample_3, mean_of_sample_3], y=[0,0.17], mode="lines", name="mean of students who had math labs"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))

fig.show()


#finding the z score using the formula
z_score = (mean-mean_of_sample_2)/std_deviation
print("The score is :", z_score)