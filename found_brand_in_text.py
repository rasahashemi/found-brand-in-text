car_brands = {
    "Acura": ["ILX", "MDX", "NSX", "RDX", "TLX"],
    "Alfa Romeo": ["Giulia", "Stelvio", "Tonale"],
    "Aston Martin": ["DB11", "DBX", "Vantage", "Vanquish"],
    "Audi": ["A3", "A4", "A5", "A6", "A7", "A8", "Q3", "Q5", "Q7", "Q8", "R8", "RS5", "RS7", "TT"],
    "Bentley": ["Bentayga", "Continental GT", "Flying Spur", "Mulsanne"],
    "BMW": ["1 Series", "2 Series", "3 Series", "4 Series", "5 Series", "7 Series", "8 Series", "X1", "X3", "X5", "X7", "i4", "iX"],
    "Bugatti": ["Chiron", "Divo", "Veyron"],
    "Buick": ["Enclave", "Encore", "Envision", "Regal"],
    "Cadillac": ["CT4", "CT5", "Escalade", "XT4", "XT5", "XT6"],
    "Chevrolet": ["Blazer", "Camaro", "Colorado", "Corvette", "Equinox", "Malibu", "Silverado", "Tahoe", "Traverse"],
    "Chrysler": ["300", "Pacifica", "Voyager"],
    "Citroën": ["C3", "C4", "C5 Aircross", "Berlingo"],
    "Dodge": ["Challenger", "Charger", "Durango", "Journey"],
    "Ferrari": ["488", "812 Superfast", "F8 Tributo", "LaFerrari", "Portofino", "SF90 Stradale"],
    "Fiat": ["500", "500X", "Panda", "Tipo"],
    "Ford": ["Bronco", "EcoSport", "Edge", "Escape", "Expedition", "Explorer", "F-150", "Fiesta", "Focus", "Mustang", "Ranger"],
    "Genesis": ["G70", "G80", "G90", "GV70", "GV80"],
    "GMC": ["Acadia", "Canyon", "Sierra", "Terrain", "Yukon"],
    "Honda": ["Accord", "Civic", "CR-V", "Fit", "HR-V", "Odyssey", "Pilot", "Ridgeline"],
    "Hyundai": ["Elantra", "Kona", "Palisade", "Santa Fe", "Sonata", "Tucson", "Venue"],
    "Infiniti": ["Q50", "Q60", "QX50", "QX60", "QX80"],
    "Jaguar": ["E-PACE", "F-PACE", "F-TYPE", "I-PACE", "XE", "XF", "XJ"],
    "Jeep": ["Cherokee", "Compass", "Gladiator", "Grand Cherokee", "Renegade", "Wrangler"],
    "Kia": ["Carnival", "EV6", "Forte", "K5", "Niro", "Seltos", "Sorento", "Sportage", "Telluride"],
    "Koenigsegg": ["Agera", "Jesko", "Regera"],
    "Lamborghini": ["Aventador", "Huracán", "Urus"],
    "Land Rover": ["Defender", "Discovery", "Range Rover", "Range Rover Evoque", "Range Rover Sport"],
    "Lexus": ["ES", "GS", "GX", "IS", "LC", "LS", "LX", "NX", "RC", "RX", "UX"],
    "Lincoln": ["Aviator", "Corsair", "Nautilus", "Navigator"],
    "Lotus": ["Evija", "Evora", "Exige"],
    "Maserati": ["Ghibli", "Levante", "MC20", "Quattroporte"],
    "Mazda": ["CX-3", "CX-30", "CX-5", "CX-9", "Mazda3", "Mazda6", "MX-5 Miata"],
    "McLaren": ["540C", "570S", "600LT", "720S", "Artura", "GT", "P1"],
    "Mercedes-Benz": ["A-Class", "C-Class", "E-Class", "G-Class", "GLA", "GLC", "GLE", "GLS", "S-Class", "SL", "AMG GT"],
    "Mini": ["Clubman", "Convertible", "Countryman", "Hardtop 2 Door", "Hardtop 4 Door"],
    "Mitsubishi": ["Eclipse Cross", "Mirage", "Outlander", "Pajero"],
    "Nissan": ["370Z", "Altima", "Ariya", "Frontier", "GT-R", "Kicks", "Maxima", "Murano", "Pathfinder", "Rogue", "Sentra", "Titan", "Versa"],
    "Pagani": ["Huayra", "Zonda"],
    "Peugeot": ["2008", "3008", "5008", "508"],
    "Porsche": ["718 Cayman", "911", "Cayenne", "Macan", "Panamera", "Taycan"],
    "Ram": ["1500", "2500", "3500"],
    "Renault": ["Clio", "Koleos", "Megane", "Talisman"],
    "Rolls-Royce": ["Cullinan", "Dawn", "Ghost", "Phantom", "Wraith"],
    "Saab": ["9-3", "9-5"],
    "Subaru": ["Ascent", "BRZ", "Crosstrek", "Forester", "Impreza", "Legacy", "Outback", "WRX"],
    "Suzuki": ["Alto", "Celerio", "Jimny", "Swift", "Vitara"],
    "Tesla": ["Model 3", "Model S", "Model X", "Model Y", "Cybertruck", "Roadster"],
    "Toyota": ["4Runner", "Avalon", "Camry", "Corolla", "Highlander", "Land Cruiser", "Prius", "RAV4", "Sequoia", "Sienna", "Tacoma", "Tundra", "Yaris"],
    "Volkswagen": ["Arteon", "Atlas", "Golf", "ID.4", "Jetta", "Passat", "Tiguan", "Touareg"],
    "Volvo": ["S60", "S90", "V60", "V90", "XC40", "XC60", "XC90"]
}


import re



def find_car_models(text):
    found_models = []
    for brand, models in car_brands.items():
        for model in models:
            if re.search(rf'\b{model}\b', text, re.IGNORECASE):
                found_models.append((brand, model))
    return found_models

# Example usage
text = "2021 model araba modeli #toyota rav4"
print(find_car_models(text))



result = find_car_models(text)



# Ensure it's a list of tuples before processing
if isinstance(result, list):  
    formatted_output = ", ".join([f"{brand} {model}" for brand, model in result])
    print(formatted_output)
else:
    print("Unexpected data format:", result)