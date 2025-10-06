def config_parking(status_parking, parking, force: bool = False):
    update = False
    if len(status_parking) == 0 and len(parking) > 0 or force:
        update = True
        all = []
        for parks in parking:
            for park_name, data in parks.items():
                for index in data:
                    all.append({
                        "id": index["id"],
                        "status": False,
                        "parking": park_name
                        })
        return all, update
    else:
        return status_parking, update