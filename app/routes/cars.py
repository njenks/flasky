from flask import Blueprint, jsonify 

class Car:
    def __init__(self, id, driver, team, mass_kg):
        self.id = id 
        self.driver = driver
        self.team = team
        self.mass_kg= mass_kg  

cars = [
    Car(7, "Sainz", "Ferrari", 795),
    Car(88, "Sharles", "Ferrari", 800),
    Car(4, "Danny Ric", "McLaren", 1138)
]

cars_bp = Blueprint("cars", __name__, url_prefix="/cars") # create a Blueprint obj - instantiating a class 
# first param - names Blueprint, second param - helping flask do it's magic, third param - what we want our route to start with 

@cars_bp.route("", methods=["GET"]) # can add more methods if need be 
# decorator changes what def get_all_cars() does 
def get_all_cars():
    response = [] 
    for car in cars: 
        response.append(
            {
                "id": car.id, 
                "driver": car.driver,
                "team": car.team, 
                "mass_kg": car.mass_kg 
            }
        )
    return jsonify(response) # converts list of dicts into JSON list of JSON obj - response that goes back to client 
    # with lists, explicity have to use jsonify to return JSON obj  - good idea to always use it, just in case 


@cars_bp.route("/<car_id>", methods=["GET"])
def get_one_car(car_id): # making var that needs same exact name as route 
    try: 
        car_id = int(car_id) 
    except ValueError: 
        return jsonify({"msg":f"car {car_id} invalid. ID must be an integer"}, 400)

    chosen_car = None
    for car in cars:
        if car.id == car_id:
            chosen_car = {
                "id": car.id, 
                "driver": car.driver, 
                "team": car.team, 
                "mass_kg": car.mass_kg
            }
    if chosen_car is None: 
        return jsonify({"msg":f"car {car_id} not found"}, 404)
    return jsonify(chosen_car), 200 # returns status code as well 