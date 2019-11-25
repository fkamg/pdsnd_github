import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

        
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    my_list=['chicago','new york','washington']
    while 1:
        city=input('Type the city you want to explore( chicago,new york or washington):').lower()
        #city=city.lower()
        if city in my_list:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Would you like to filter by month? Type 'yes' or 'no':  ")
    month=month.lower()
    if month == 'yes':
        month=input("which month? January, Febrauary,March,April,May or June: ")
        month=month.lower()
    elif month == 'no':
        month='all'
    else:
        print("You didnt type yes or no. our default is no")
        month='all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Would you like to filter by day? Type 'yes' or 'no': ")
    day=day.lower()
    if day == 'yes':
        day=input("which day? Sunday, Monday,Tuesday,Wednesday,Thursday, Friday or Saturday: ")
        day= day.lower()
    elif day == 'no':
        day='all'
    else:
        print("You didnt type yes or no. our default is no")
        day='all'

    print('-'*40)
    my=[city,month,day]
    return my


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month,day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['Hour'] =df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    m = ['January', 'February', 'March', 'April', 'May', 'June']
    popular_month = m[popular_month - 1]
    print('Most Frequent Travel Month:', popular_month)

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Frequent Travel day_of_week:', popular_day_of_week)

    # TO DO: display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('Most Frequent Travel Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_station = df['Start Station'].mode()[0]
    print("The most common start station is:", Start_station )

    # TO DO: display most commonly used end station
    End_station = df['End Station'].mode()[0]
    print("The most common End station is:", End_station  )

    # TO DO: display most frequent combination of start station and end station trip
    start_end = df[['Start Station','End Station']].mode().loc[0]
    print("The most frequent combination of stations is {} and {}".format(start_end[0], start_end[1]) )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print("Total travel time :", total)

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print("Mean travel time :", mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type']
    print("User types and their counts")
    print(user_types.value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender = df['Gender']
        print("Gender and their counts")
        print(counts_of_gender.value_counts())
    else:
        print("This dataset has no column for gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year'].mode()[0]
        print("The most common birth year:", birth_year)
        most_recent = df['Birth Year'].max()
        print("The most recent birth year:", most_recent)
        # the most earliest birth year
        earliest_year = df['Birth Year'].min()
        print("The most earliest birth year:", earliest_year)
    else:
        print("This dataset has no column for Birth Year")
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
       
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            id1=input("Would you like to see some individuals trip raw data(yes or no)?").lower()
            if id1== 'yes':
                print(df.sample(5))
            else:
                break;
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
