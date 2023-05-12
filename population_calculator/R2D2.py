# Calculate our new population depending on previous generation, rounding down via "//"
def advance_population(young, mature, old_fuck):
    new_young = (mature * 4) + (old_fuck * 2)
    new_mature = young // 2
    new_old_fuck = mature // 3

    # Return new population values
    return new_young, new_mature, new_old_fuck


# This simply prints our current population
def print_population(young, mature, old_fuck):
    print("Our current population is as follows:")
    print(f"Young R2D2: {young}")
    print(f"Mature R2D2: {mature}")
    print(f"Old R2D2: {old_fuck}\n")


# Set start values
year = 4000
END_YEAR = 4100
number_young = 10
number_mature = 10
number_old_fuck = 10

while year <= END_YEAR:
    print("Calculating population of year " + str(year) + ".")

    # Save the returned new population into a tuple
    advanced = advance_population(number_young, number_mature, number_old_fuck)

    # Save our new population values
    number_young = advanced[0]
    number_mature = advanced[1]
    number_old_fuck = advanced[2]

    print_population(number_young, number_mature, number_old_fuck)
    year += 1
