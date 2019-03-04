#python cornerstone project - datenight app searches for random activity and meal 
import config
import time
import random
from yelpapi import YelpAPI
yelp_api = YelpAPI(config.api_key)
#gets list of 
def get_restaurants(meal,location, price):
    price = price
    meal = meal
    location = location
    sort_by = "rating"
    restaurants = yelp_api.search_query(term= meal,location= location, price= price, sort_by= sort_by, limit= 10)
    r_list = []
    for business in restaurants["businesses"]:
        if business["rating"] >= 4:
            r_list.append(business["id"])
    return r_list

def find_restaurant(r_list,day):
    restaurants = []
    for business in r_list:
        r_check = yelp_api.business_query(business)
        try:
            restaurants = [(r_check['name'], r_check["location"]["display_address"],r_check["coordinates"]) for item in r_check["hours"][0]["open"] if item['day']== day and int(item["start"])<= 1700 < int(item['end'])<=2359]
        except:
            pass
    return random.choice(restaurants)

def find_movie(coordinates):
    term = "movie+theater"
    longitude = coordinates["longitude"]
    latitude = coordinates["latitude"]
    radius = 8000
    sort_by = "rating"
    movies = yelp_api.search_query(term= term,longitude= longitude,latitude= latitude,radius= radius, sort_by= sort_by, limit =5) #searches movie theaters near restaurant
    m_list = []
    for theater in movies["businesses"]:
        if theater["rating"] > 3:
            m_list.append([theater["name"], theater["location"]["display_address"]])
    theater = random.choice(m_list)
    return f'Go see a movie at {theater[0]} located on {" ".join(theater[1])}'

def find_music(coordinates, day):
    term = "live+music"
    longitude = coordinates["longitude"]
    latitude = coordinates["latitude"]
    radius = 8000
    sort_by = "rating"
    music = yelp_api.search_query(term= term,longitude= longitude,latitude= latitude,radius= radius, sort_by= sort_by, limit= 10) #searches music venues near retaurant
    music_list = []
    venues = []
    for venue in music["businesses"]:
        if venue["rating"] > 3:
            music_list.append(venue["id"])
            for number in music_list:
                v_check = yelp_api.business_query(number)
                try:
                    venues =[(v_check['name'], v_check["location"]["display_address"]) for item in v_check["hours"][0]["open"] if item['day']== day and int(item["start"])<= 1700 < int(item['end'])<=2359]
                except:
                    pass
    try:
        venue =random.choice(venues)
        return f'Go listen to music at {venue[0]} located at {" ".join(venue[1])}'
    except:
        return f" "

def find_other(coordinates,day):
    term = "fun things to do at night"
    longitude = coordinates["longitude"]
    latitude = coordinates["latitude"]
    radius = 8000
    sort_by = "rating"
    other = yelp_api.search_query(term= term,longitude= longitude,latitude= latitude,radius= radius, sort_by= sort_by, limit= 10)
    other_list = []
    others = []
    for thing in other["businesses"]:
        if thing["rating"] > 3:
            other_list.append(thing["id"])
            for number in other_list:
                o_check = yelp_api.business_query(number)
                #if o_check["is_claimed"] == True:
                try:
                    others =[(o_check['name'], o_check["location"]["display_address"]) for item in o_check["hours"][0]["open"] if item['day']== day and int(item["start"])<= 1700 < int(item['end'])<=2359]
                except:
                    pass
    try:
        other = random.choice(others)
        return f'Go visit {other[0]} at {" ".join(other[1])}'
    except:
        return f" "

day_dict = {"sunday": 0, "monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6}

print("Welcome to date night!") #inputs 
while True:
    day = input("What day of the week do you want to go out? ").lower()
    while day not in day_dict.keys():
        print("lets try that again")
        day = input("What day of the week do you want to go out? ").lower()
    location = input(f'What area would you like to visit on your date?<enter city or zip code>: ')
    meal = input(f'Would you like to have "dinner" or just have "drinks"? ')
    while meal != "dinner" and meal != "drinks":
        print("sorry I didn't get that.")
        meal = input(f'Would you like to have "dinner" or just have "drinks"? ')
    price = input(f"What price range are you looking for? type in a number betweeen 1-4: ")
    while int(price) not in range(1,5):
        print("thats out of my range!")
        price = input(f"What price range are you looking for? type in a number betweeen 1-4: ")
    break
time.sleep(1)
print("One moment while we scower the area for the perfect datenight..........")
r_list = get_restaurants(meal,location, price) #starts the restaurant search 
restaurant = find_restaurant(r_list,day_dict[day]) #verifies the restaurants in the list are open on the day 

r_name = restaurant[0] #formating the restaurant data
r_address = restaurant[1]
coordinates = restaurant[2] #uses long,lat from restaurant for activity searches
movie = find_movie(coordinates) 
#     # print(f'the movie is {movie[0]}')
music = find_music(coordinates,day_dict[day])

other = find_other(coordinates,day_dict[day])
print("")
print(f'Next {day} you will enjoy {meal} at {r_name} located at {" ".join(r_address)} \n\nThen you can:\n{movie}\n{music}\n{other}\nHave a great night!')