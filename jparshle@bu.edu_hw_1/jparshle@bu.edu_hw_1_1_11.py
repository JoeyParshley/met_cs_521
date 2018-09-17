'''
	Chapter 1 problem: 1.11
	
	US Population projection is based on the following assumptions:
	1) 1 birth every 7 seconds
	2) 1 death every 13 seconds
	3) 1 new immigrant every 45 seconds
	4) current population is 312032486
	5) 1 year has 365 days
	6) poulations events are birth, death immigration
	7) each yearly population is calculated by adding the amount of births and immigrants
	   and subtracting the amount of deaths to / from the previous population

	Display to the console for each of the next five years

'''
# constants (CURRENT_POPULATION, DAYS_PER_YEAR, SECONDS_PER_YEAR, SECONDS_PER_BIRTH, SECONDS_PER_IMMIGRANT)
CURRENT_POPULATION = 312032486
SECONDS_PER_YEAR = 365 * 24 * 3600
SECONDS_PER_BIRTH = 7
SECOND_PER_DEATH = 13
SECONDS_PER_IMMIGRANT = 45

# Each rate of population event is calculated by dividing the SECONDS_PER_YEAR by the rate of the poulation event
births_per_year = SECONDS_PER_YEAR // SECONDS_PER_BIRTH
deaths_per_year = SECONDS_PER_YEAR // SECOND_PER_DEATH
immigrants_per_year = SECONDS_PER_YEAR // SECONDS_PER_IMMIGRANT

'''
	Each year's population is calculated by:
	yearly_population = previous_population + births_per_year - deaths_per_year + immigrants_per_year
'''
year_1_population = CURRENT_POPULATION + births_per_year - deaths_per_year + immigrants_per_year
year_2_population = year_1_population + births_per_year - deaths_per_year + immigrants_per_year
year_3_population = year_2_population + births_per_year - deaths_per_year + immigrants_per_year
year_4_population = year_3_population + births_per_year - deaths_per_year + immigrants_per_year
year_5_population = year_4_population + births_per_year - deaths_per_year + immigrants_per_year

print("\n")
print("year_1_population: ", year_1_population)
print("year_2_population: ", year_2_population)
print("year_3_population: ", year_3_population)
print("year_4_population: ", year_4_population)
print("year_5_population: ", year_5_population)
print("\n")
