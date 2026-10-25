from pricing_stratergy import PricingStratergy
from enums import VehicleType

class BasicPricing(PricingStratergy):
    def calculate_fees(self, session):
        duration = (session.end_time - session.start_time)/3600

        if(session.vehicle.vehicle_type == VehicleType.BIKE):
            session.fee = duration*10

        elif(session.vehicle.vehicle_type == VehicleType.EV):
            session.fee = duration*15

        else:
            session.fee = duration*20
        
            
        
