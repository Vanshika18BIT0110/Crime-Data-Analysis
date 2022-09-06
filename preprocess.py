import numpy as np
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
#to set a white grid
sns.set(style="whitegrid")  

def process(path):
	#prints preprocess on the command prompt
	print("preprocess")
	#reading the csv file
	df_main = pd.read_csv(path)
	#getting all the columns 
	names=list(df_main.columns)
	#used to find pairwise correlations between the columns
	correlations = df_main.corr()
	# plot correlation matrix
	fig = plt.figure()
	fig.canvas.set_window_title('Correlation Matrix')
	ax = fig.add_subplot(111)
	cax = ax.matshow(correlations, vmin=-1, vmax=1)
	fig.colorbar(cax)
	ticks = np.arange(0,22,1)
	#setting the values and names in the x and y axis
	ax.set_xticks(ticks)
	ax.set_xticklabels(names)
	#get the labels in x-axis inverted to 90 degrees
	for label in ax.get_xticklabels():
		label.set_rotation(90)
		label.set_ha('right')   
	ax.set_yticks(ticks)
	ax.set_yticklabels(names)
	#saving the figure in results folder
	fig.savefig('results/Correlation Matrix.png')
	#displaying the figure for 5 secs and then closing it   
	plt.pause(2)
	plt.show(block=False)
	plt.close() 
	#top 10 crimes
	crimes = read_csv(path, index_col='Date')
	s = crimes[['PrimaryType']]
	crimes.index = pd.to_datetime(crimes.index)
	crime_count = pd.DataFrame(s.groupby('PrimaryType').size().sort_values(ascending=False).rename('counts').reset_index())
	
	# Initialize the matplotlib figure
	f, ax = plt.subplots(figsize=(16, 15))
	# Plot the total crashes
	sns.set_color_codes("pastel")
	sns.barplot(x="counts", y="PrimaryType", data=crime_count.iloc[:10, :],label="Total", color="b")
	
	ax.legend(ncol=2, loc="lower right", frameon=True)
	ax.set(ylabel="Type",xlabel="Crimes")
	sns.despine(left=True, bottom=True)
	plt.savefig('results/Top 10 Crimes.png')
	# Add a legend and informative axis label
	plt.pause(2)
	plt.show(block=False)
	plt.close() 
	crimes_2015 = crimes.loc['2015']
	## Yearly crimes
	arrest_yearly = crimes[crimes['Arrest'] == True]['Arrest']
	plt.subplot()
	# Monthly arrest
	#resampling the yearly data in terms of months and adding them to show monthly total
	arrest_yearly.resample('M').sum().plot()
	plt.title('Monthly arrests')
	plt.savefig('results/Monthly arrests.png')
	plt.pause(2)
	plt.show(block=False)
	plt.close() 
	# Weekly arrest
	#resampling the yearly data in terms of weeks and adding them to show weekly total
	arrest_yearly.resample('W').sum().plot()
	plt.title('Weekly arrests')
	plt.savefig('results/Weekly arrests.png')
	
	plt.pause(2)
	plt.show(block=False)
	plt.close() 
	# daily arrest
	#resampling the yearly data in terms of days and adding them to show daily total
	arrest_yearly.resample('D').sum().plot()
	plt.title('Daily arrests')
	plt.savefig('results/Daily arrests.png')
	plt.pause(2)
	plt.show(block=False)
	plt.close() 
	#taking all the domestic crimes that happenend in that year
	domestic_yearly = crimes[crimes['Domestic'] == True]['Domestic']
	plt.subplot()
	# Monthly domestic violence
	domestic_yearly.resample('M').sum().plot()
	plt.title('Monthly domestic violence')
	plt.savefig('results/Monthly domestic violence.png')
	plt.pause(2)
	plt.show(block=False)
	plt.close()
	# Weekly domestic violence
	domestic_yearly.resample('W').sum().plot()
	plt.title('Weekly domestic violence')
	plt.savefig('results/Weekly domestic violence.png')
	plt.pause(2)
	plt.show(block=False)
	plt.close()	
	# daily domestic violence
	domestic_yearly.resample('D').sum().plot()
	plt.title('Daily domestic violence')
	plt.savefig('results/Daily domestic violence.png')
	plt.pause(2)
	plt.show(block=False)
	plt.close()
	#top 5 monthly crimes
	theft_2015 = pd.DataFrame(crimes_2015[crimes_2015['PrimaryType'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['PrimaryType'])
	grouper_2015 = theft_2015.groupby([pd.Grouper(freq = 'M'), 'PrimaryType'])
	data_2015 = grouper_2015['PrimaryType'].count().unstack()
	data_2015.plot()
	plt.title("Top 5 monthly crimes 2015")
	plt.savefig('results/Top 5 monthly crimes 2015.png')
	plt.pause(2)
	plt.show(block=False)
	plt.close()
	#top 5 weekly crimes
	grouper_2015 = theft_2015.groupby([pd.Grouper(freq = 'W'), 'PrimaryType'])
	data_2015 = grouper_2015['PrimaryType'].count().unstack()
	data_2015.plot()
	plt.title("Top 5 Weekly crimes 2015")
	plt.savefig('results/Top 5 Weekly crimes 2015.png')
	plt.pause(2)
	plt.show(block=False)
	plt.close()
	#top 5 daily crimes
	grouper_2015 = theft_2015.groupby([pd.Grouper(freq = 'D'), 'PrimaryType'])
	data_2015 = grouper_2015['PrimaryType'].count().unstack()
	data_2015.plot()
	plt.title("Top 5 daily crimes 2015")
	plt.savefig('results/Top 5 daily crimes 2015.png')
	plt.pause(2)
	plt.show(block=False)
	plt.close()
	#creating cleaned.csv
	data = pd.read_csv(path,usecols=['Date', 'PrimaryType','Latitude','Longitude']) 
	# Preview the first 5 lines of the loaded data 
	data.dropna(inplace=True)
	print(data)
	
	print(data.head())
	print(data.PrimaryType.unique())
	#replacing the name of the crime to numbers
	data[["PrimaryType"]] = data[["PrimaryType"]].replace(['BATTERY','OTHER OFFENSE','ROBBERY','NARCOTICS','CRIMINAL DAMAGE','WEAPONS VIOLATION','THEFT','BURGLARY','MOTOR VEHICLE THEFT','PUBLIC PEACE VIOLATION','ASSAULT','CRIMINAL TRESPASS','CRIM SEXUAL ASSAULT','INTERFERENCE WITH PUBLIC OFFICER','ARSON','DECEPTIVE PRACTICE','LIQUOR LAW VIOLATION','KIDNAPPING','SEX OFFENSE','OFFENSE INVOLVING CHILDREN','PROSTITUTION','GAMBLING','INTIMIDATION','STALKING','OBSCENITY','PUBLIC INDECENCY','HUMAN TRAFFICKING','CONCEALED CARRY LICENSE VIOLATION','OTHER NARCOTIC VIOLATION','HOMICIDE','NON-CRIMINAL'], [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
	print(data.PrimaryType.unique())
	print(data)

	
	