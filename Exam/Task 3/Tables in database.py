* Readers:
    id : serial primary key,
    name : varchar(60),
    email : varchar(60),
    is_active : boolean, cannot be null, default value: true
* Books:
    id : serial primary key,
    title : varchar(60),
    price : decimal(5, 2),
    author : varchar(60),
    publishing_houses_id: int
* PublishingHouses:
    id : serial primary key,
    name : varchar(60),
    city : varchar(20),
    address : varchar(120)