from faker import Faker
import pandas as pd
import random
from pathlib import Path

# Directorio donde está el script
BASE_DIR = Path(__file__).resolve().parent

# Carpeta para datasets
DATASET_DIR = BASE_DIR / "datasets"

# Crear carpeta si no existe
DATASET_DIR.mkdir(exist_ok=True)

print("\n" + "=" * 60)
print("DATASET OUTPUT DIRECTORY")
print("=" * 60)
print(f"Datasets will be saved in:\n{DATASET_DIR}")
print("=" * 60 + "\n")

# ==========================================
# FAKER-CONFIG
# ==========================================

fake = Faker()

NUM_CLIENTS = 1000
NUM_VEHICLES = 2000
NUM_MECHANICS = 50
NUM_SPARES = 300
NUM_REPAIRS = 15000
NUM_REPAIR_DETAILS = 30000

# ==========================================
# VEHICLE BRANDS AND MODELS
# ==========================================

brands_models = {
    "Honda": ["Prelude", "Civic", "Accord", "CR-V"],
    "Toyota": ["Corolla", "Camry", "Supra", "Yaris"],
    "Nissan": ["Sentra", "Altima", "370Z", "Versa"],
    "Mazda": ["Mazda3", "Mazda6", "RX-8", "CX-5"],
    "Hyundai": ["Elantra", "Accent", "Sonata"],
    "Kia": ["Rio", "Cerato", "Sportage"],
    "Ford": ["Mustang", "Focus", "Fusion"],
    "Chevrolet": ["Cruze", "Spark", "Camaro"],
    "Volkswagen": ["Golf", "Jetta", "Passat"],
    "BMW": ["320i", "330i", "M3"]
}

# ==========================================
# MECHANIC SPECIALTIES
# ==========================================

specialties = [
    "Engine",
    "Transmission",
    "Suspension",
    "Electrical",
    "Brakes",
    "Diagnostics"
]

# ==========================================
# REPAIR TYPES
# ==========================================

repair_types = [
    "Oil Change",
    "Brake Replacement",
    "Battery Replacement",
    "Engine Repair",
    "Suspension Repair",
    "Transmission Repair",
    "Electrical System Repair",
    "Wheel Alignment",
    "Wheel Balancing"
]

# ==========================================
# SPARE PART CATALOG
# ==========================================

engine_spares = [
    "Piston",
    "Connecting Rod",
    "Piston Ring",
    "Head Gasket",
    "Valve",
    "Oil Pump",
    "Timing Belt",
    "Water Pump"
]

brake_spares = [
    "Brake Pad",
    "Brake Disc",
    "Brake Caliper",
    "Brake Fluid",
    "Master Cylinder"
]

suspension_spares = [
    "Shock Absorber",
    "Control Arm",
    "Tie Rod",
    "Ball Joint",
    "Coil Spring"
]

transmission_spares = [
    "Clutch Kit",
    "Flywheel",
    "Transmission Filter",
    "Gear Synchronizer",
    "Torque Converter"
]

electrical_spares = [
    "Alternator",
    "Starter Motor",
    "Battery",
    "Spark Plug",
    "Ignition Coil",
    "Fuse"
]

lubrication_spares = [
    "Engine Oil",
    "Oil Filter",
    "Air Filter",
    "Fuel Filter",
    "Cabin Filter"
]

spare_catalog = {
    "Engine": engine_spares,
    "Brakes": brake_spares,
    "Suspension": suspension_spares,
    "Transmission": transmission_spares,
    "Electrical": electrical_spares,
    "Lubrication": lubrication_spares
}

# ==========================================
# CLIENTS
# ==========================================

print("Generating clients...")

clients = []

for client_id in range(1, NUM_CLIENTS + 1):
    clients.append([
        client_id,
        fake.name(),
        fake.phone_number(),
        fake.city()
    ])

clients_df = pd.DataFrame(
    clients,
    columns=[
        "client_id",
        "name",
        "phone",
        "city"
    ]
)

# ==========================================
# VEHICLES
# ==========================================

print("Generating vehicles...")

vehicles = []

for vehicle_id in range(1, NUM_VEHICLES + 1):

    brand = random.choice(list(brands_models.keys()))
    model = random.choice(brands_models[brand])

    vehicles.append([
        vehicle_id,
        random.randint(1, NUM_CLIENTS),
        brand,
        model,
        random.randint(2000, 2025),
        random.randint(10000, 350000),
        f"PLT-{random.randint(1000,9999)}"
    ])

vehicles_df = pd.DataFrame(
    vehicles,
    columns=[
        "vehicle_id",
        "client_id",
        "brand",
        "model",
        "year",
        "mileage",
        "license_plate"
    ]
)

# ==========================================
# MECHANICS
# ==========================================

print("Generating mechanics...")

mechanics = []

for mechanic_id in range(1, NUM_MECHANICS + 1):
    mechanics.append([
        mechanic_id,
        fake.name(),
        random.choice(specialties),
        random.randint(1, 30)
    ])

mechanics_df = pd.DataFrame(
    mechanics,
    columns=[
        "mechanic_id",
        "name",
        "specialty",
        "experience_years"
    ]
)

# ==========================================
# SPARES
# ==========================================

print("Generating spares...")

spares = []
spare_id = 1

while spare_id <= NUM_SPARES:

    category = random.choice(list(spare_catalog.keys()))
    spare_name = random.choice(spare_catalog[category])

    spares.append([
        spare_id,
        spare_name,
        category,
        round(random.uniform(5, 1200), 2)
    ])

    spare_id += 1

spares_df = pd.DataFrame(
    spares,
    columns=[
        "spare_id",
        "spare_name",
        "category",
        "unit_price"
    ]
)

# ==========================================
# REPAIRS
# ==========================================

print("Generating repairs...")

repairs = []

for repair_id in range(1, NUM_REPAIRS + 1):

    repairs.append([
        repair_id,
        random.randint(1, NUM_VEHICLES),
        random.randint(1, NUM_MECHANICS),
        fake.date_between(
            start_date="-5y",
            end_date="today"
        ),
        random.choice(repair_types),
        round(random.uniform(20, 2500), 2)
    ])

repairs_df = pd.DataFrame(
    repairs,
    columns=[
        "repair_id",
        "vehicle_id",
        "mechanic_id",
        "repair_date",
        "repair_type",
        "labor_cost"
    ]
)

# ==========================================
# REPAIR DETAILS
# ==========================================

print("Generating repair details...")

repair_details = []

for detail_id in range(1, NUM_REPAIR_DETAILS + 1):

    repair_details.append([
        detail_id,
        random.randint(1, NUM_REPAIRS),
        random.randint(1, NUM_SPARES),
        random.randint(1, 5)
    ])

repair_details_df = pd.DataFrame(
    repair_details,
    columns=[
        "detail_id",
        "repair_id",
        "spare_id",
        "quantity"
    ]
)

# ==========================================
# EXPORT CSV FILES
# ==========================================
print("Exporting CSV files...\n")

clients_file = DATASET_DIR / "clients.csv"
vehicles_file = DATASET_DIR / "vehicles.csv"
mechanics_file = DATASET_DIR / "mechanics.csv"
spares_file = DATASET_DIR / "spares.csv"
repairs_file = DATASET_DIR / "repairs.csv"
repair_details_file = DATASET_DIR / "repair_details.csv"

clients_df.to_csv(clients_file, index=False)
vehicles_df.to_csv(vehicles_file, index=False)
mechanics_df.to_csv(mechanics_file, index=False)
spares_df.to_csv(spares_file, index=False)
repairs_df.to_csv(repairs_file, index=False)
repair_details_df.to_csv(repair_details_file, index=False)
# ==========================================
# SUMMARY
# ==========================================
print("\nData generation completed successfully.\n")

print(f"Clients: {len(clients_df):,}")
print(f"Vehicles: {len(vehicles_df):,}")
print(f"Mechanics: {len(mechanics_df):,}")
print(f"Spares: {len(spares_df):,}")
print(f"Repairs: {len(repairs_df):,}")
print(f"Repair Details: {len(repair_details_df):,}")

print("\n" + "=" * 60)
print("GENERATED FILES")
print("=" * 60)

print(clients_file)
print(vehicles_file)
print(mechanics_file)
print(spares_file)
print(repairs_file)
print(repair_details_file)

print("=" * 60)
print(f"All datasets were saved to:\n{DATASET_DIR}")
print("=" * 60)