#py para acceder a la terminal quit() para salir
# Tema : Numbers
# Primeros dos ejercicios Hello World & Lasagna
'''
# gr='Hello'
# print(gr)

#def add_three_numbers_misformatted(number_one, number_two, number_three):
#     result = number_one + number_two + number_three   # This was indented by 4 spaces.
#     print(result)

#add_three_numbers_misformatted(1,2,3)

#def add_two_numbers(number_one, number_two):
#  return number_one + number_two  
# def hello():
#    return 'Hello, World!'


E_B_T=40
a_b_t=input('¿Cuánto tiempo lleva la lasagna en el horno? ')
n_o_l=input('¿Cuántas capas tiene la lasagna? ')
a_b_t=int(a_b_t)
n_o_l=int(n_o_l)

def b_t_r(a_b_t):
    """Calculate the remaining bake time in minutes.

    :param a_b_t: int - actual minutes the lasagna has been in the oven.
    :return: int - the difference of time (minutes) that's remaining to cook the lasagna.

    This function takes one integer and a constant representing the minutes that the lasagna has
    been in the oven and the expected time it has to be in there to cook and calculates the total of
    time remaining for it to cook.
    """
    dif=E_B_T-a_b_t
    return dif

def p_t_i_m(n_o_l):
    """Calculate the preparation time in minutes.

    :param n_o_l: int - the number of layers in the lasagna.
    :return: int - total time it's needed per layer.

    This function takes one integer representing the number of lasagna layers
    and calculates the total minutes needed for cooking the lasagna.
    """
    t=n_o_l*2
    return t

def e_t_i_m(n_o_l,a_b_t):
    """Calculate the elapsed cooking time.

    :param n_o_l: int - the number of layers in the lasagna.
    :param a_b_t: int - actual cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    t=p_t_i_m(n_o_l)+a_b_t
    return t


print(f"El tiempo restante es: {b_t_r(a_b_t)} minutos")
print(f"El tiempo de preparación en minutos es: {p_t_i_m(n_o_l)} minutos")
print(f"Se lleva cocinando por: {e_t_i_m(n_o_l,a_b_t)} minutos")
'''
# Ejercicio 2 Currency Exchange
'''
budget=float(input('¿Con cuánto dinero cuenta? '))
exchange_rate=float(input('¿A cuánto equivale 1 moneda extranjera en la moneda local? '))
exchanging_value=float(input('¿Cuánto dinero quiere cambiar de su monto total? '))
denomination=float(input('¿Cuál es la denominación del billete que busca? '))
spread=float(input('¿Cuánto interés tiene el tipo de cambio? '))

def exchange_money(budget,exchange_rate):
    """Calculate the value of exchanged currency.

    :param budget: float - amount planning to exchange.
    :param exchange_rate: float - domestic equal to foreign currency.
    :return: float - value of exchange currency.
    """
    val=budget/exchange_rate
    return val

def get_change(budget,exchanging_value):
    """Calculate the currency left after an exchange.

    :param budget: float - amount planning to exchange.
    :param exchanging_value: float - amount of money 
    that is taken from budget to be exchanged.
    :return: float - value left from the budget.
    """
    val=budget-exchanging_value
    return val

def get_value_of_bills(denomination,number_of_bills):
    """Calculate the value of bills.

    :param denomination: int - Value of a single bill.
    :param number_of_bills: int - Number of bills.
    :return: int - value of the total bills.
    """
    val=denomination*number_of_bills
    return val

def get_number_of_bills(amount,denomination):
    """Calculate the number of bills.

    :param denomination: int - Value of a single bill.
    :param amount: int - initial amount to exchange.
    :return: int - number of bills.
    """
    val=amount//denomination
    return val

def get_leftover_of_bills(amount,denomination):
    """Calculate the leftover amount that cannot be returned from the starting amount.

    :param denomination: int - Value of a single bill.
    :param amount: int - initial amount to exchange.
    :return: int - leftover from the exchange amount.
    """
    val=amount%denomination
    return val

def exchangeable_value(budget,exchange_rate,spread,denomination):
    """Calculate the actual exchangeable amount.

    :param budget: float - the original budget.
    :param exchange_rate: float - domestic equal to foreign currency.
    :param spread: int - percentage taken as an exchange fee.
    :param denomination: int - Value of a single bill.
    :return: int - maximum value of the new currency after calculating the exchange rate plus the spread.
    """
    spread=spread/100
    spread=exchange_rate*spread
    exchange_rate=exchange_rate+spread
    mon=exchange_money(budget,exchange_rate)
    val=mon//denomination #Trunca el resultado redondeando hacia abajo
    val=val*denomination
    return val



print(f"La cantidad bruta del cambio de divisa es: {exchange_money(budget,exchange_rate)} en la moneda extranjera")
print(f"Su cambio sería: {get_change(budget,exchanging_value)} en moneda local")
print(f"Obtendría: {get_value_of_bills(denomination,get_number_of_bills(exchanging_value,denomination))} en billetes")
print(f"No se podrá devolver: {get_leftover_of_bills(exchanging_value,denomination)} extra")
print(f"Su dinero total, tomando en cuenta intereses es: {exchangeable_value(budget,exchange_rate,spread,denomination)} en moneda extranjera")
'''
# Ejercicio 3 Conjetura de Collatz
'''
number=int(input('Introduzca el número para probar la conjetura: '))
def steps(number):
    c=1
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    else:
        print(f"{c}.  {number}")
        while number!=1:
            c=c+1
            if number%2==0:
                number=number/2
            elif number%2!=0:
                number=3*number+1
            number=int(number)
            print(f"{c}.  {number}")
    return c-1

print(f"Número de pasos  {steps(number)}")
'''
# Ejercicio 4 Granos de maíz
'''
number=int(input('Introduzca un valor de cuadros: '))
def square(number):
    if number<1 or number>64:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2**(number-1)

def total():
    tg = sum(2 ** i for i in range(64))
    return tg

square(number)
print(f"Granos en el cuadro {number}: {square(number)}")
print(f"El total de granos es: {total()}")
'''
# Ejercicio 5 Armstrong Numbers
'''
number=input('Introduzca un número: ')
def is_armstrong_number(number):
    num=int(number)
    l=len(number)
    sum=0
    for i in number:
         sum += int(i) ** l
    
    if sum == num:
         
         return True
    else:
         return False

if is_armstrong_number(number):
    print(f"{number} número de armstrong")
else:
    print(f"{number} no es número de armstrong")
'''

# Tema : Bools - Ghost Gobble Arcade Game
'''

def eat_ghost(active_pellet,touching_ghost):
    """Verify that Pac-Man can eat a ghost if he is empowered by a power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - can a ghost be eaten?
    """
    if active_pellet==True and touching_ghost==True:
        return True
    else:
        return False 
    
def score(touching_pellet,touching_dot ):
    """Verify that Pac-Man has scored when a power pellet or dot has been eaten.

    :param touching_power_pellet: bool - is the player touching a power pellet?
    :param touching_dot: bool - is the player touching a dot?
    :return: bool - has the player scored or not?
    """
    if touching_pellet==True or touching_dot==True:
        return True
    else:
        return False 
    
def lose(active_pellet,touching_ghost):
    """Trigger the game loop to end (GAME OVER) when Pac-Man touches a ghost without his power pellet.

    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player lost the game?
    """
    if active_pellet==False and touching_ghost==True:
        return True
    else:
        return False 
    
def win(all_dots,active_pellet,touching_ghost):
    """Trigger the victory event when all dots have been eaten.

    :param has_eaten_all_dots: bool - has the player "eaten" all the dots?
    :param power_pellet_active: bool - does the player have an active power pellet?
    :param touching_ghost: bool - is the player touching a ghost?
    :return: bool - has the player won the game?
    """
    if all_dots==True and lose(active_pellet,touching_ghost)==False:
        return True
    else:
        return False 

'''
# Ejercicio 2 Determinar tipo de triángulo
'''

def equilateral(sides):
    if triangle(sides)==True:
        a, b, c = sides
        if a==b and b==c:
            return True
        else: return False
    else: return False

def isosceles(sides):
   if triangle(sides)==True:
        a, b, c = sides
        if (a==b and b!=c) or (b==c and b!=a) or (a==c and b!=a) or (a==b and b==c):
            return True
        else: return False
   else: return False


def scalene(sides):
    if triangle(sides)==True:
        a, b, c = sides
        if a!=b and b!=c and b!=a and a!=c:
            return True
        else: return False
    else: return False

def triangle(sides):
    a, b, c = sides
    if a!=0 and b!=0 and c!=0:
        if a+b>=c and a+c>=b and c+b>=a:
            return True
        else: return False
    else: return False

'''
# Ejercicio 3 Año Bisiesto
'''

def leap_year(year):
    if year%100==0:
        if year%400!=0:
            return False
        else: return True
    elif year%4==0:
        return True
    else: return False

print(f"{leap_year(1900)}") 
'''

# Tema : Condicionales - Meltdown Mitigation
'''
def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    if temperature<800 and neutrons_emitted>500 and (temperature*neutrons_emitted)<500000:
        return True
    return False 
    
def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """
    generated_power=voltage*current
    percentage=(generated_power/theoretical_max_power)*100
    if percentage>=80:
        return 'green'
    elif  percentage<80 and percentage>=60: #60 <= percentage < 80
        return 'orange'
    elif percentage<60 and percentage>=30: #30 <= percentage < 60
        return 'red'
    elif percentage<30:
        return 'black'
    
def fail_safe(temperature, neutrons_produced_per_second,threshold):
     """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
     if temperature*neutrons_produced_per_second<(threshold*.9):
         return 'LOW'
     elif temperature*neutrons_produced_per_second==threshold or temperature*neutrons_produced_per_second<=(threshold+(threshold*.1)) or temperature*neutrons_produced_per_second<=(threshold-(threshold*.1)):
         return 'NORMAL'
     else: return 'DANGER'

print(f"{fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000)}")
'''

# Tema: Comparisons - Black Jack
'''
def value_of_card(card):
    card=str(card)
    card=card.lower()
    if card=='j' or card=='q' or card=='k':
        return 10
    elif card=='1' or card=='2' or card=='3' or card=='4' or card=='5' or \
         card=='6' or card=='7' or card=='8' or card=='9' or card=='10':
        return int(card)
    elif card=='a':
        return 1
    else: return 'No es un valor válido'

def higher_card(card_one,card_two):
    a=value_of_card(card_one)
    b=value_of_card(card_two)
    if a>b:
        return card_one
    elif b>a:
        return card_two
    else: return card_one,card_two

def value_of_ace(card_one,card_two):
    a=value_of_card(card_one)
    b=value_of_card(card_two)
    if card_one=='A' or card_two=='A':
        return 1
    elif a+b+11>21:
        return 1
    else: return 11

def is_blackjack(card_one,card_two):
    a=card_one.lower()
    b=card_two.lower()
    hand ={a,b}
    if 'a' in hand and ('10'in hand or 'k'in hand or 'q'in hand or 'j'in hand ):
        return True
    else: return False        

def can_split_pairs(card_one,card_two):
    a=value_of_card(card_one)
    b=value_of_card(card_two)
    if a==b:
        return True
    else: return False

def can_double_down(card_one,card_two):
    a=value_of_card(card_one)
    b=value_of_card(card_two)
    if 9<=a+b<=11:
        return True
    else: return False

print(f"{can_split_pairs('K','Q')}")
'''

# Tema : Strings - Little Sister's Vocabulary
'''
def add_prefix_un(word):
    return 'un'+ word

def make_word_groups(vocab_words):
    pre=vocab_words[0]
    x=len(vocab_words)
    for i in range(1,x):
        vocab_words[i]=pre+vocab_words[i]
    vocab_words=' :: '.join(vocab_words)
    return vocab_words

def remove_suffix_ness(word):
    word=word[:-4]
    if word[-1]=='i':
        word=word[:-1]+'y'
        return word
    else: return word

def adjective_to_verb(sentence,index):
    sentence=sentence.split()
    sentence=sentence[index]
    if sentence[-1]=='.' or sentence[-1]==',':
        sentence=sentence[:-1]
        return sentence+'en'
    else: return sentence +'en'
    
print(adjective_to_verb('I need to make that bright.', -1 ))
'''

# Tema : String methods - Little Sister's Essay
'''
def capitalize_title(title):
    title=title.title()
    #title=x[0]+title[1:]
    return title
def check_sentence_ending(sentence):
    if sentence[-1]=='.':
        return True
    else: return False
def clean_up_spacing(sentence):
    sentence=sentence.strip()
    return sentence
def replace_word_choice(sentence,old_word,new_word):
    sentence=sentence.replace(old_word,new_word)
    return sentence

print(clean_up_spacing(" I like to go on hikes with my dog.  "))
'''

# Tema : Lists - Card Games
'''
def get_rounds(round_number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    rounds=[round_number,round_number+1,round_number+2]
    return rounds
def concatenate_rounds(rounds_1,rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    rounds=rounds_1+rounds_2
    return rounds
def list_contains_round(rounds,round_number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if round_number in rounds:
        return True
    else: return False
def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    s=sum(hand)
    x=len(hand)
    prom=s/x
    return prom
def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    ca=card_average(hand)
    m=hand[round(len(hand)/2)]
    fl_a=(hand[0]+hand[-1])/2
    if ca==m or ca==fl_a:
        return True
    else: return False
def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even=[]
    odd=[]
    for i in range(len(hand)):
        if i%2==0:
            even.append(hand[i]) #even+=[i]
        else: odd.append(hand[i]) #odd+=[i]
    if card_average(even)==card_average(odd):
        return True
    else: return False
def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    j=[22]
    if hand[-1]==11:
        hand=hand[:-1]+j[:]
        return hand
    else: return hand

print(average_even_is_average_odd([1, 3, 5, 7, 9]))
'''

# Tema : List Methods - Chaitana's Colossal Coaster
''' 
def add_me_to_the_queue(express_queue, normal_queue,ticket_type,person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """
    if ticket_type==1:
        express_queue.append(person_name)
        return express_queue
    elif ticket_type==0:
        normal_queue.append(person_name)
        return normal_queue    
def find_my_friend(queue,friend_name):
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """
    return queue.index(friend_name)
def add_me_with_my_friends(queue,index,person_name):
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """
    queue.insert(index,person_name)
    return queue
def remove_the_mean_person(queue,person_name):
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """
    queue.remove(person_name)
    return queue
def how_many_namefellows(queue,person_name):
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """
    return queue.count(person_name)
def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """
    return queue.pop()
def sorted_names(queue):
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """
    queue.sort()
    return queue

print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=1, person_name="RichieRich"))
print(add_me_to_the_queue(express_queue=["Tony", "Bruce"], normal_queue=["RobotGuy", "WW"], ticket_type=0, person_name="HawkEye"))
print(find_my_friend(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], friend_name="Steve")
)
print(add_me_with_my_friends(queue=["Natasha", "Steve", "T'challa", "Wanda", "Rocket"], index=1, person_name="Bucky")
)
print(remove_the_mean_person(queue=["Natasha", "Steve", "Eltran", "Wanda", "Rocket"], person_name="Eltran")
)
print(how_many_namefellows(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"], person_name="Natasha")
)
print(remove_the_last_person(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
)
print(sorted_names(queue=["Natasha", "Steve", "Eltran", "Natasha", "Rocket"])
)
'''

# Tema : Loops - Making the grade
''' 
""" 
# Python will keep track of the loop count internally.
for item in sequence:
    set_of_statements
    
# `range()` is used as an explicit loop counter.  
# This will loop 12 times, from index 0 to index 11.
for item in range(12):
    set_of_statements """

def round_scores(student_scores):
    """
    Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    score=[]
    for i in range(len(student_scores)):
        score.append(round(student_scores[i]))
    return score
def count_failed_students(student_scores):
    """
    Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    aux=0
    for i in student_scores:
        if i<=40:
            aux+=1
        else: continue
    return aux
def above_threshold(student_scores,threshold):
    """
    Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    aux=[]
    for i in student_scores:
        if i>=threshold:
            aux.append(i)
        else: continue
    return aux
def letter_grades(highest):
    """
    Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    high=100-highest
    res=14-(high/4)
    aux=[]
    for i in range(1,5):
        highest=highest-res
        aux.append(int(highest))
        highest-=1
    aux.reverse()
    return aux
def student_ranking(student_scores,student_names):
    """
    Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    aux=[]
    for i,j in enumerate(student_scores):
        aux.append(f"{i+1}. {student_names[i]}: {j}")
    return aux
def perfect_score(student_info):
    """
    Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    aux=[]
    for i in student_info:
        while len(aux)<1:
            if i[1]==100:
                aux.append(i[0])
                aux.append(i[1])
            break
        if len(aux)==1: break
    return aux


student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
print(round_scores(student_scores))
print(count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40]))
print(above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75)
)
print(letter_grades(highest=100))
print(letter_grades(highest=88))
student_scores = [100, 99, 90, 84, 66, 53, 47]
student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
print(student_ranking(student_scores, student_names))
print(perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]]))
print(perfect_score(student_info=[["Charles", 90], ["Tony", 80]]))
'''

# Tema : Tuples - Tisbury Treasure Hunt 
''' 
def get_coordinate(treasure_coordinate):
    """
    Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """
    return treasure_coordinate[1]
def convert_coordinate(coordinate):
    """
    Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    return tuple(coordinate)
def compare_records(treasure_coordinate,location_coordinate_quadrant):
    """
    Compare two record types and determine if their coordinates match.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, tuple(coordinate_1, coordinate_2), quadrant) trio.
    :return: bool - do the coordinates match?
    """
    coord=tuple(treasure_coordinate[1])
    if coord==location_coordinate_quadrant[1]:
        return True
    else: return False
def create_record(treasure_coordinate,location_coordinate_quadrant):
    """
    Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    if compare_records(treasure_coordinate,location_coordinate_quadrant):
        return treasure_coordinate+location_coordinate_quadrant
    else: return "not a match"

def clean_up(treasure_coordinate_location_coordinate_quadrant):
    """
    Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    """
    r=""
    for i in treasure_coordinate_location_coordinate_quadrant:
        j=(i[0],i[2],i[3],i[4])
        r+=f"{j}\n"
    return r

print(get_coordinate(('Scrimshawed Whale Tooth', '2A')))
print(convert_coordinate("2A"))
print(compare_records(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))
print(compare_records(('Model Ship in Large Bottle', '8A'), ('Harbor Managers Office', ('8', 'A'), 'purple')))
print(create_record(('Brass Spyglass', '4B'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue')))
print(create_record(('Brass Spyglass', '4B'), ('Seaside Cottages', ('1', 'C'), 'blue')))
print(clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple'))))

'''

# Tema : Dicts - Inventory Managment
''' 
def create_inventory(input_list):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    inventory={}
    for i in input_list:
        if i in inventory:
            inventory[i]+=1
        else:
            inventory[i]=1
    return inventory

def add_items(inventory_dict,item_list):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    for i in item_list:
        if i in inventory_dict:
            inventory_dict[i]+=1
        else: inventory_dict[i]=1
    return inventory_dict

def decrement_items(inventory_dict,item_list):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for i in item_list:
         if i in inventory_dict:
             inventory_dict[i]-=1
             if inventory_dict[i]<0:
                 inventory_dict[i]=0
    return inventory_dict

def remove_item(inventory_dict,item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory_dict:
        inventory_dict.pop(item)
    return inventory_dict

def list_inventory(inventory_dict):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    list=[]
    for i in inventory_dict:
        if inventory_dict[i]==0:
            continue
        else:
            list.append((i,inventory_dict[i]))
    return list

print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))
print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))
print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))
print(decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))
print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))
print(remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))
print(list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))
'''

#Tema : Dict Methods - Mecha Munch Managment
''' 

'''

