from flask import Blueprint, jsonify, request 
from app import db 
from app.models.cars import Car

# class Car:
#     def __init__(self, id, driver, team, mass_kg):
#         self.id = id 
#         self.driver = driver
#         self.team = team
#         self.mass_kg= mass_kg  

# cars = [
#     Car(7, "Sainz", "Ferrari", 795),
#     Car(88, "Sharles", "Ferrari", 800),
#     Car(4, "Danny Ric", "McLaren", 1138)
# ]

cars_bp = Blueprint("cars", __name__, url_prefix="/cars") # create a Blueprint obj - instantiating a class 
# first param - names Blueprint, second param - helping flask do it's magic, third param - what we want our route to start with 

@cars_bp.route("", methods=["POST"])
def create_car(): 
    request_body = request.get_json()

    new_car = Car(
        driver=request_body["driver"], 
        team=request_body["team"], 
        mass_kg=request["mass_kg"]
    ) 

    db.session.add(new_car)
    db.session.commit() # need this to save into db session 

    return { 
        "id":new_car.id
    }, 201              


@cars_bp.route("", methods=["GET"]) # can add more methods if need be 
# decorator changes what def get_all_cars() does 
def get_all_cars():
    params = request.args # can use anything as param - obj attr 
    if "driver" in params and "team" in params: 
        driver_query = params["driver"]
        team_query = params["team"]
        cars = Car.query.filter_by(driver=driver_query, team=team_query)

    if "driver" in params: 
        driver_query = params["driver"]
        cars = Car.query.filter_by(driver=driver_query)
        driver_query = request.args.get("driver")
    elif "team" in params:
        team_query = params["team"]
        cars = Car.query.filter_by(team=team_query)
        team_query = request.args.get("team")
    else: 
        cars = Car.query.all() 
    # if driver_query:
    #     cars = Car.query.filter_by(driver=driver_query)
    # else:
    #     cars = Car.query.all()
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
    
    chosen_car = Car.query.get(car_id)

    if chosen_car is None: 
        return jsonify({"msg":f"car {car_id} not found"}, 404)

    return jsonify({
                "id": chosen_car.id, 
                "driver": chosen_car.driver, 
                "team": chosen_car.team, 
                "mass_kg": chosen_car.mass_kg
            }), 200 # returns status code as well 


@cars_bp.route("/<car_id>", method=["PUT"])
def update_car(car_id): 
    try: 
        car_id = int(car_id) 
    except ValueError: 
        return jsonify({"msg":f"car {car_id} invalid. ID must be an integer"}, 400)
    
    request_body = request.get_json() # dict with k, v that were in JSON

    if "driver" not in request_body or \
        "team" not in request_body or \
        "mass_kg" not in request_body: 
        return jsonify({'msg': f"Request must include driver, team, and mass_kg"}), 400 

    chosen_car = Car.query.get(car_id)

    if chosen_car is None: 
        return jsonify({"msg":f"car {car_id} not found"}, 404)

    chosen_car.driver = request_body["driver"]
    chosen_car.team = request_body["team"]
    chosen_car.mass_kg = request_body["mass_kg"]

    db.session.commit() 

    return jsonify({'msg': f"Successfully replaced car with id {car_id}"}), 200 

@cars_bp.route("/<car_id>", method=["DELETE"])
def delete_car(car_id):
    try: 
        car_id = int(car_id) 
    except ValueError: 
        return jsonify({"msg":f"car {car_id} invalid. ID must be an integer"}, 400)
    
    chosen_car = Car.query.get(car_id)

    if chosen_car is None: 
        return jsonify({"msg":f"car {car_id} not found"}, 404)
    
    db.session.delete(chosen_car)
    db.session.commit() # any time making changes you want to save 

    return jsonify({'msg': f"Car #{car_id} successfully deleted"})
