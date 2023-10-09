from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
stations_under_construction = []# add all stations that are closed here
# just put the landmark_chocies into a string
for letter, landmark in landmark_choices.items():
  landmark_string += "{0} - {1}\n".format(letter, landmark)

# now landmark has the entire landmark_choices in the string

def greet():
  print("Hi there and welcome to SkyRoute!")
  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
  greet()
  new_route()
  goodbye()

def get_start():
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices:
    start_point = landmark_choices[start_point_letter]
    return start_point 
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_start()


def get_end():
  end_point_letter = input("Where are you going to? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices:
    end_point = landmark_choices[end_point_letter] 
    return end_point 
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_end()
  

def set_start_and_end(start_point, end_point):
  if start_point is not None:
    # get user input and ask
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    if change_point == 'b':
      start_point = get_start()
      end_point = get_end()
    elif change_point == 'o':
      start_point = get_start()
    elif change_point == 'd':
      end_point = get_end()
    else:
      print("Oops, that isn't 'o', 'd', or 'b'...")
      set_start_and_end(start_point, end_point)
  else:
    start_point = get_start()
    end_point = get_end()
  return start_point, end_point

# function to solve the program
'''
-get and set the origin and destination
-call search to get the recommended route
-allow users to search for another route
'''
def new_route(start_point = None, end_point= None):
  start_point, end_point = set_start_and_end(start_point, end_point)
  shortest_route = get_route(start_point, end_point)
  if shortest_route is not None:
    shortest_route_string = '\n'.join(shortest_route)
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point,end_point, shortest_route_string))
  else:
    print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))

  again = input("Would you like to see another route? Enter y/n: ")
  if again == 'y':
    new_route(start_point, end_point)

def get_route(start_point, end_point):
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes=[]
  for i in start_stations:
    for j in end_stations:
      metro_system = get_active_stations() if stations_under_construction else vc_metro
      if len(stations_under_construction)>0:
        possible_route = dfs(metro_system, i,j)
        if not possible_route :
          return None
      route = bfs(metro_system, i, j)
      if route is not None:
        routes.append(route)
  shortest_path = min(routes, key=len)
  return shortest_path
      
# list of all the stops we need to take between MB and CP
#print(get_route('Marine Building', 'Canada Place'))
def get_active_stations():
  updated_metro = vc_metro
  for station_under_construction in stations_under_construction:
    for current_station, neighboring_stations in vc_metro:
      if current_station != station_under_construction:
        # if staion not under construction
        # remove any connecting stations that are under construction
        # give the set of current station - stations_under_construction
        updated_metro[current_station] -= set(stations_under_construction)
      else:
        # station is under construction, remove it from updayed
        updated_metro[current_station] =set([])
  return updated_metro


def goodbye():
  print('Thanks for using our system')

skyroute()