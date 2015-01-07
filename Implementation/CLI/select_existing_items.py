import sqlite3

def select_all_items(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""select
                          Item.ItemID,
                          Item.ItemName,
                          Item.ItemValue,
                          Item.LoanRate,
                          Item.ItemClass,
                          Item.FuseRating,
                          ItemType.ItemType,
                          Location.Location,
                          ItemType.ItemTypeID,
                          Location.LocationID
                          from Item, ItemType, Location
                          where Item.LocationID = Location.LocationID and Item.ItemTypeId = ItemType.ItemTypeID
                          """)
        items = cursor.fetchall()
    return items

def select_item(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """select
                 Item.ItemID,
                 Item.ItemName,
                 Item.ItemValue,
                 Item.LoanRate,
                 Item.ItemClass,
                 Item.FuseRating
                 ItemType.ItemType,
                 Location.Location,
                 ItemType.ItemTypeID,
                 Location.LocationID
                 from Item, ItemType, Location
                 where ItemID = ?
                 and Item.LocationID = Location.LocationID and Item.ItemTypeId = ItemType.ItemTypeID
                 """
        id = (id,)
        cursor.execute(sql,id)
        item = cursor.fetchone()
    return item

def select_all_locations(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""select
                          Location.LocationID,
                          Location.Location
                          from Location
                          order by Location ASC
                          """)
        locations = cursor.fetchall()
    return locations

def select_all_locations_for_id_selection(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""select
                          Location.LocationID,
                          Location.Location
                          from Location
                          """)
        locations = cursor.fetchall()
    return locations

def select_location(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        data = (id,)
        cursor.execute("""select
                          Location.LocationID,
                          Location.Location,
                          Item.ItemName
                          from Location, Item
                          where LocationID = ?
                          and Location.LocationID = Item.ItemID
                          """, data)
        location = cursor.fetchone()
    return location

def select_all_item_types(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""select
                          ItemType.ItemTypeID,
                          ItemType.ItemType
                          from ItemType
                          order by ItemType ASC
                          """)
        item_types = cursor.fetchall()
    return item_types

def select_all_item_types_for_id_selection(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""select
                          ItemType.ItemTypeID,
                          ItemType.ItemType
                          from ItemType
                          """)
        item_types = cursor.fetchall()
    return item_types

def select_item_type(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        data = (id,)
        cursor.execute("""sselect
                          ItemType.ItemTypeID,
                          ItemType.ItemType,
                          Item.ItemName
                          from ItemType, Item
                          where ItemTypeID = ?
                          and ItemType.ItemTypeID = Item.ItemTypeID
                          """, data)
        item_type = cursor.fetchone()
    return item_type
