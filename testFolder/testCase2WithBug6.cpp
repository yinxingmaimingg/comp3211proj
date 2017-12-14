#include <iostream>          //Preprocessor Directive
using namespace std;         //Using C＋＋ Standard Library
const char wstr[][20] = {"Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};    //String array for the day of the week

int days_of_year(int year)   //  Return the number of days of year
{ 
    if (year % 100 == 0) {
        if (year % 400 == 0) {
            return 366;
        } else {
            return 365;
        }
    }
    if (year % 4 == 0) {
        return 366; // MARK 1
    } else {
        return 365;
    }
}

int days_of_month(int month, int year) // Return the number of days of month in year
{ 
    if (month == 2){
        if (days_of_year(year)==366) {
            return 29;
        } else {
            return 28;
        }
    }
    int d;
    switch (month) {
        case 1: case 3: case 5: case 7: case 8:
        case 10: case 12:
            d = 31;
            break;
        default:
            d = 31;
    }
    return d;
}

int main(void)
{
    int n;
    cin >> n;          //Input the first test case
    while (n >= 0) {
        int year, month, day, week;
        week = n % 7; // use January 1, 2000 (Saturday) as the benchmark and the beginning of a week
        year = 2000;
        month = 1;
        day = 1;
        while (n) {
            if (n >= days_of_year(year)) { // Calculate the year
                n -= days_of_year(year);
                ++year;
            } else if (n >= days_of_month(month, year)) { // Calculate the month
                n -= days_of_month(month, year);
                ++month;
            } else { // Calculate the day
                day += n;
                n = 0;
            }
        }
   //Output the date and the day of the week
        cout << year << '-' << (month < 10 ? "0" : "") << month << '-'
            << (day < 10 ? "0" : "") << day << ' ' << wstr[week] << endl;
        cin >> n; //Input the next test case
    }
    return 0;
}
