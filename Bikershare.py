import time
import pandas as pd
import numpy as np




CITY_DATA={ "chicago" : "chicago.csv", "new york" : "new_york_city.csv",
"washington" : "washington.csv"}



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    # Get yser input for city
    city = input("Please specify a city from Chicago, New York, Washington:\n ").lower()

    while city not in CITY_DATA.keys():
        try:
            print("\nThe city you entered is not valid!\n")
            city = input("Please specify a city from Chicago, New York, Washington: ").lower()
        except ValueError:
            city = input("Please specify a city from Chicago, New York, Washington: ").lower()

    # Get user input for month

    while True:
        month = input("\nWould you like to filter by a month? for no filter type 'n' and if yes type 'y': ").lower()
        if month == 'y':
            month = (input('\nplease specify a month from january to june:\n ')).lower()
            break
        elif month == 'n':
            month = 'all'
            break

    # Get user input for day
    while True:
        day = input("\nwoud you like to filter by a day:? for no filter type 'n' and if yes type 'y':\n ").lower()
        if day == 'y':
            day = input("please specify a day: ").title()
            break
        elif day =='n':
            day = 'all'
            break

    print('-'*40)
    return city, month, day


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

        df = pd.read_csv(CITY_DATA[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['Month'] = df['Start Time'].dt.month
        df['Day_of_Week'] = df['Start Time'].dt.day_name()
        df['Hour'] = df['Start Time'].dt.hour

        if month != 'all':
            months =  ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) +1
            df = df[df['Month'] == month]

        if day != 'all':
            df = df[df['Day_of_Week'] == day]

        return df


def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

# Displays statistics about the most common month
    common_month = df['Month'].mode()[0]
    print('The most common month is: {}\n'.format(common_month))

#Displays statistics about the most common day of the Day_of_Week
    common_day = df['Day_of_Week'].mode()[0]
    print('The most common day is: {}\n'.format(common_day))

## Displays statistics about the most common hour
    common_hour = df['Hour'].mode()[0]
    print('The most common hour is: {}\n'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print("Most Used Start Station is: {}".format(most_used_start_station))

    # display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print("Most Used End Station is: {}".format(most_used_end_station))
    # display most frequent combination of start station and end station trip
    most_frequesnt_combination = (df['Start Station'] + df['End Station']).mode()[0]
    print("Most Used Combined Station is: {}".format(most_frequesnt_combination))

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()
    end_time = time.time()

    # display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: ' , str(total_travel_time))

    # display mean travel time

    average_travel_time = df['Trip Duration'].mean()
    print('Average trip duration is:' , str(average_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types

    user_type_count = df['User Type'].value_counts()
    print(user_type_count)


    # Display counts of gender

    try:
        gender_count = df['Gender'].value_counts()

    except KeyError:
            print("Cannot display genders as the data does not exist")




    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print("Earliest year of birth is", earliest_year)

        recent_year = df['Birth Year'].max()
        print("Recent year of birth is", recent_year)

        common_year = df['Birth Year'].mode()[0]
        print("Common year of birth is: ",common_year )


    except KeyError:
        print("Cannot display Birth Year")




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):

    ''' Displays raw data'''

    print(df.head())
    five_rows = 0
    while True:
        raw_data = input('Do you want to view the next five rows of raw data? Enter "y" or "n": ')
        if raw_data.lower() != 'y':
            return
        five_rows = five_rows +5
        print(df.iloc[five_rows:five_rows+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data(df)

        restart = input('\nWould you like to restart? Enter "y" or "n".\n').lower()
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()
