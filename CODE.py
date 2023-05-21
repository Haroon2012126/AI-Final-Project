from rafay import *

# Loading csv file.
df=pd.read_csv('F:/hotel_bookings.csv')
df.head()



# =============================================================================
# df.info()
# =============================================================================
print(df)


# =============================================================================
# Dropping colum agent and company
# =============================================================================
df=df.drop(['company','agent'],axis=1)
df.head()



# =============================================================================
# printing tuple where there a re no guests
# =============================================================================
result = df[df.adults + df.babies + df.children == 0].shape
print(result)





# =============================================================================
# Deleting tuple where there are no guests
# =============================================================================

df = df.drop(df[(df.adults + df.babies + df.children == 0)].index).reset_index(drop=True)
df.head()
print(df)



# =============================================================================
# What number of booking were cancelled
# =============================================================================
booking_info=pd.DataFrame(df.groupby('hotel')['is_canceled'].value_counts())
booking_info
booking_info.columns=['no of bookings']
booking_info



# =============================================================================
# What percentage of booking were cancelled
# =============================================================================
booking_info['percentage']=df.groupby('hotel')['is_canceled'].value_counts(normalize=True)*100
booking_info



# =============================================================================
# Showing plot showing the number of canceled and non-canceled bookings for each hotel type
# =============================================================================
plt.rcParams['figure.figsize'] = (9, 4)
sns.countplot(x='hotel',data=df,hue='is_canceled',palette='husl',ec='black',lw=1).set(xlabel='Hotels')
plt.title('Booking Cancelled or not by Hotel Type')
plt.grid(True)
plt.show()



# =============================================================================
# Which type of hotel has more booking ?
# =============================================================================
preference = pd.DataFrame(df.hotel.value_counts())
preference['percentage']=df.hotel.value_counts(normalize=True)*100
preference.index.name='hotel'
preference.rename({'hotel':'no of bookings'},axis=1,inplace=True)
preference



# =============================================================================
# generates a list called labels that contains the unique hotel types from the 'hotel' column
# =============================================================================
labels=df['hotel'].value_counts().index.tolist()
labels
sizes=df['hotel'].value_counts().tolist()
sizes



# =============================================================================
# Making a pie chart of which type of hotel has more booking
# =============================================================================
colors=['yellowgreen','lightcoral']
explode=(0,0.1)
plt.pie(sizes,labels=labels,colors=colors,autopct="%1.1f%%",explode=explode,startangle=90,textprops={'fontsize': 14})
plt.show()



# =============================================================================
# Which month has the highest number of arrivals ? (people arrival count)
# =============================================================================
confirmed_booking=df.loc[df.is_canceled==0]
confirmed_booking.reset_index(drop=True,inplace=True)
confirmed_booking.head()
people_arrival_count_df=pd.DataFrame(confirmed_booking['arrival_date_month'].value_counts())
people_arrival_count_df.head()
people_arrival_count_df.columns=['No of bookings']
people_arrival_count_df.head()



# =============================================================================
# Peope arrival count in Percentage
# =============================================================================
people_arrival_count_df['booking_percentage'] =confirmed_booking['arrival_date_month'].value_counts(normalize=True)*100
people_arrival_count_df



# =============================================================================
# Plotting a graph representing the count of bookings for each month 
# =============================================================================
confirmed_booking['arrival_date_month'].value_counts().plot(kind='bar').set(xlabel=('Month'),ylabel=('Bookings count'))
plt.show()


# =============================================================================
# Which year has highest number of arrivals ?
# =============================================================================
yearly_bookings=pd.DataFrame(confirmed_booking.groupby('arrival_date_year')['hotel'].value_counts())
yearly_bookings
yearly_bookings.columns=['No of bookings']
yearly_bookings


# =============================================================================
# Plotting graph for yealy booking (highest number of arrivals)
# =============================================================================
sns.countplot(x='arrival_date_year',data=confirmed_booking,hue='hotel').set_title('Yearly Bookings')
plt.show()



# =============================================================================
# From which country people are comming the most ?
# =============================================================================
# Top 10 countries people are comming the most in number.
country=pd.DataFrame(confirmed_booking.country.value_counts())
country
country.columns=['no of bookings']
country


# =============================================================================
# Plotting graph to represent country
# =============================================================================
y=list(confirmed_booking.country.value_counts().head(10))
y
x=list(confirmed_booking.country.value_counts().head(10).keys())
x
sns.barplot(x=list(confirmed_booking.country.value_counts().head(10).keys()),y=list(confirmed_booking.country.value_counts().head(10)),ec='black',lw=1)
plt.xlabel('Countries')
plt.ylabel('Number of Bookings')
plt.show()



# =============================================================================
# Which is the most reserved room type ?
# =============================================================================
room_type=pd.DataFrame(df.reserved_room_type.value_counts(normalize=True)*100)
room_type
room_type.columns=['booking percentage']
room_type
room_type.index.name='room type'
room_type



# =============================================================================
# What is the most common customer type ?
# =============================================================================
customer_type=pd.DataFrame(df.customer_type.value_counts(normalize=True)*100)
customer_type
customer_type.columns=['booking percentage']
customer_type
customer_type.index.name='customer type'
customer_type


# =============================================================================
# Plotting a graph
# =============================================================================
list(customer_type['booking percentage'])
list(customer_type.index)
sns.barplot(y=list(customer_type['booking percentage']),x=list(customer_type.index),ec='black',lw=1).set(xlabel='Customer Type',ylabel='Booking Percentage (%)')
plt.show()






