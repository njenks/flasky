from flask import Blueprint, jsonify, request, make_response

from app import db
from app.models.drivers import Driver
from app.models.cars import Car

drivers_bp = Blueprint("drivers", __name__, url_prefix="/drivers")

@drivers_bp.route("", methods=["POST"])
def create_car():
    request_body = request.get_json()

    new_driver = Driver(
        name=request_body["name"],
        team=request_body["team"],
        country=request_body["country"], 
        handsome=request_body["handsome"]
    )

    db.session.add(new_driver)
    db.session.commit()

    return {
        "id": new_driver.id
    }, 201

@drivers_bp.route("", methods=["GET"])
def get_all_drivers():
    response = []
    drivers = Driver.query.order_by(Driver.id).all() # get each driver and order them by id
    for driver in drivers:
        response.append(
            driver.to_dict()
        )
    return jsonify(response)

def validate_driver(driver_id):
    try:
        driver_id = int(driver_id)
    except ValueError:
        return jsonify({'msg': f"Invalid driver id: '{driver_id}'. ID must be an integer"}), 400

    chosen_driver = Driver.query.get(driver_id)

    if chosen_driver is None:
        return jsonify({'msg': f'Could not find driver with id {driver_id}'}), 404 
    
    return chosen_driver 

@drivers_bp.route("/<driver_id>", methods=["GET"])
def get_one_driver(driver_id):
    driver = validate_driver(driver_id)

    return jsonify(driver.to_dict()), 200

def validate_car(car_id): 
    try:
        car_id = int(car_id)
    except ValueError:
        return jsonify({'msg': f"Invalid car id: '{car_id}'. ID must be an integer"}), 400

    chosen_car = Car.query.get(car_id)

    if chosen_car is None:
        return jsonify({'msg': f'Could not find car with id {car_id}'}), 404 
    
    return chosen_car 

@drivers_bp.route("/<driver_id>/cars", methods=["POST"])
def add_cars_to_driver(driver_id):
    driver = validate_driver(driver_id)

    request_body = request.get_json()
    try:
        car_ids = request_body
    except KeyError: 
        return jsonify({'msg': f"Missing car_ids in request body"}), 400 # missing key in k: v pair 

    if not isinstance(car_ids, list): 
        jsonify({'msg': f"Expected list of car ids"}), 400
    
    cars = []
    for id in car_ids:  # checking to see if car_ids are incorrect 
        cars.append(validate_car(id))

    for car in cars: 
        car.driver = driver 
    
    db.session.commit()

    return jsonify({f'msg': "Added cars to driver {driver_id}"}), 200 

@drivers_bp.route("/<driver_id>", methods=["DELETE"])
def delete_one_driver(driver_id):
    chosen_driver = validate_driver(driver_id)

    db.session.delete(chosen_driver)
    db.session.commit()

    return jsonify({'msg': f'Deleted driver with id {driver_id}'})
    

@drivers_bp.route("/<driver_id>/fliphandsome", methods=["PATCH"])
def flip_driver_handsomeness_with_id(driver_id):
    driver = validate_driver(driver_id)
    driver.handsome = not driver.handsome

    db.session.commit()
    return jsonify({'msg': f'Flipped driver handsomeness with id {driver_id} to {driver.handsome}'})