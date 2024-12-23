class Delivery:
    def further_area(self, city_code):
        city_areas = {
            1: ["Blue Area", "F-6", "F-7", "G-10", "H-8"],
            2: ["DHA Phase 5", "Gulberg", "Johar Town", "Model Town"],
            3: ["Clifton", "Defense", "Gulshan-e-Iqbal", "North Nazimabad"],
            7: ["Jinnah Road", "Cantt Area", "Supply Bazar", "Mandian"]
        }

        city_map = {
            1: "Islamabad",
            2: "Lahore",
            3: "Karachi",
            7: "Abottabad"
        }

        if city_code in city_areas:
            city_name = city_map[city_code]  
            print(f"\nAvailable Areas in {city_name}:")
            for area in city_areas[city_code]:
                print(f"- {area}")
            return city_areas[city_code]
        else:
            print("Invalid city code! No areas found.")
            return []
