from django.shortcuts import render
# Create your views here.

class Plant:
    def __init__(self, name, species, description, location):
        self.name = name
        self.species = species
        self.description = description
        self.location = location

# Sample data for Plant class

plants = [
    Plant(
        name="Aloe Vera",
        species="Aloe barbadensis miller",
        description="A succulent known for its medicinal gel and ability to thrive with minimal watering.",
        location="Living Room (sunny windowsill)"
    ),
    Plant(
        name="Spider Plant",
        species="Chlorophytum comosum",
        description="A hardy houseplant that produces long, arching leaves and tiny offshoots called 'spiderettes'.",
        location="Kitchen counter"
    ),
    Plant(
        name="Peace Lily",
        species="Spathiphyllum wallisii",
        description="A graceful indoor plant with glossy leaves and white, sail-like flowers. Prefers shade and humidity.",
        location="Bedroom corner"
    ),
    Plant(
        name="Japanese Maple",
        species="Acer palmatum",
        description="A small ornamental tree with colorful foliage that shifts hues through the seasons.",
        location="Front garden"
    ),
    Plant(
        name="Rosemary",
        species="Salvia rosmarinus",
        description="An aromatic herb used in cooking, with woody stems and needle-like leaves.",
        location="Kitchen windowsill"
    ),
    Plant(
        name="Bamboo Palm",
        species="Chamaedorea seifrizii",
        description="A tropical houseplant that helps purify indoor air and thrives in indirect light.",
        location="Office"
    ),
    Plant(
        name="Monstera",
        species="Monstera deliciosa",
        description="A popular tropical houseplant with large, split leaves and a striking appearance.",
        location="Dining room"
    ),
    Plant(
        name="Lavender",
        species="Lavandula angustifolia",
        description="A fragrant flowering plant commonly used for relaxation and essential oils.",
        location="Balcony planter"
    ),
    Plant(
        name="Cactus",
        species="Echinocactus grusonii",
        description="A desert plant with round shape and striking spines, often called 'Golden Barrel'.",
        location="Home office shelf"
    ),
    Plant(
        name="Fiddle Leaf Fig",
        species="Ficus lyrata",
        description="A trendy indoor tree known for its large, glossy leaves and sculptural shape.",
        location="Living room corner"
    ),
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plant_index(request):
    return render(request, 'plants/index.html', {'plants':plants})