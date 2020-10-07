from pypika import Query, Table


def select_event(vins, location, event_type):
    vin_event = Table('POT_PO_VIN_EVENT')
    result = Query.from_(vin_event).select('*').where(
        vin_event.VIN_NO.isin(vins)
        & vin_event.EVT_TYPE_CD.isin(event_type)
        & vin_event.EVT_LOC == location
    )
    return result


def delete_event(vins, location, event_type):
    vin_event = Table('POT_PO_VIN_EVENT')
    result = Query.from_(vin_event).where(
        vin_event.VIN_NO.isin(vins)
        & vin_event.EVT_TYPE_CD.isin(event_type)
        & vin_event.EVT_LOC == location
    ).delete()
    return result
