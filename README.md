1.Creating a JSON file with dummy data is relatively straightforward. You can structure your data to mimic real-world scenarios.
[
    {
        "restaurant_name": "Sample Restaurant",
        "cuisine": "Italian",
        "menu_items": [
            {
                "dish_name": "Spaghetti Carbonara",
                "price": 12.99
            },
            {
                "dish_name": "Margherita Pizza",
                "price": 10.99
            }
        ]
    }
]

2.To create a NoSQL database using MongoDB, by using terminal I am able to creating collection of restaurants data.
  {
    _id: ObjectId("64fad0ce2d19922efade0949"),
    restaurant_name: 'Sample Restauraunt1',
    cuisine: 'Indian',
    menu_items: [
      { dish_name: 'Dosa', price: 40 },
      { dish_name: 'Idli', price: 10 }
    ]
  }
3.Retrieving all search data with a single dish name.
db.restaurants.find({
     "menu_items.dish_name": "Spaghetti Carbonara"
 });
 4.Display how many people searched for each dish/cuisine.
  db.search_logs.insertOne({
     "search_term": "Spaghetti Carbonara",
     "timestamp": ISODate("2023-09-08T00:00:00Z")
 });

 db.search_logs.aggregate([
...     {
...         $group: {
...             _id: "$search_term",
...             count: { $sum: 1 }
...         }
...     }
... ]);
