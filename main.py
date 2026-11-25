
from pyscript import document, when

non_metals = {
    "hydrogen": ("H", 1, 1.008),
    "helium": ("He", 2, 4.0026),
    "carbon": ("C", 6, 12.011),
    "nitrogen": ("N", 7, 14.007),
    "oxygen": ("O", 8, 15.999),
    "fluorine": ("F", 9, 18.998),
    "neon": ("Ne", 10, 20.180),
    "phosphorus": ("P", 15, 30.974),
    "sulfur": ("S", 16, 32.06),
    "chlorine": ("Cl", 17, 35.45),
    "argon": ("Ar", 18, 39.948),
    "selenium": ("Se", 34, 78.971),
    "bromine": ("Br", 35, 79.904),
    "krypton": ("Kr", 36, 83.798),
    "iodine": ("I", 53, 126.904),
    "xenon": ("Xe", 54, 131.293),
    "radon": ("Rn", 86, 222),
}

@when("submit", "#elementForm")
def check_element(event):

    event.preventDefault()

    query = document.querySelector("#elementInput").value.strip().lower()

    result = document.querySelector("#result")

    if query == "":
        result.innerHTML = "Please enter an element name or symbol!"

    else:
        element_name = query
        element_data = non_metals.get(query)

        if element_data is None:
            for name, data in non_metals.items():
                if data[0].lower() == query:
                    element_name = name
                    element_data = data
                    break

        if element_data is None:
            result.innerHTML = "<strong>Element not found.</strong>"

        else:
            symbol, atomic_number, atomic_mass = element_data

            result.innerHTML = (
                "<strong>Element:</strong> " + element_name.title() + "<br>"
                + "<strong>Symbol:</strong> " + symbol + "<br>"
                + "<strong>Atomic Number:</strong> " + str(atomic_number) + "<br>"
                + "<strong>Atomic Mass:</strong> " + str(atomic_mass)
            )
