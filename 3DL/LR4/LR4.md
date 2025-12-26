Задание 1
 ```mermaid
classDiagram
    class SmartLight {
    +int brightness
    +String color
    -bool is_on
    +turn_on()
    +turn_off()
    +set_color(new_color String)
    }
```
Задание 2
 ```mermaid
classDiagram
    class CreditCard { 
    +String owner_name
    #float balance
    -String number
    -String cvc
    -int pin()
    +pay(float amount) bool
    -chech_pin(int input_pin) bool
    }
   ```

Задание 3
 ```mermaid
classDiagram
    class Character {
        +name : string
        +move()
    }
    
    class Archer {
        +shoot()
    }
    
    class Knight {
        +attack_sword()
    }
    
    Character <|-- Archer : наследование
    Character <|-- Knight : наследование
```
Задание 4
```mermaid
classDiagram
    class Playlist {
        +name : string
        -songs : List~Song~
        +add_song(song : Song)
        +remove_song(song : Song)
        +get_songs() List~Song~
    }
    
    class Song {
        +title : string
        +duration : float
    }
    
    Playlist "1" *-- "*" Song : содержит
```
Задание 5
```mermaid
classDiagram
    class Order {
        +status : string
        -items : List~Item~
        +delivery_method : DeliveryAgent
        +add_item(item : Item)
        +remove_item(item : Item)
        +get_items() List~Item~
    }
    
    class Item {
        +name : string
        +price : float
    }
    
    class DeliveryAgent {
        +speed : float
        +deliver(order : Order)
    }
    
    class Courier {
        +call_client()
    }
    
    class Drone {
        +fly()
    }
    
    Order "1" *-- "*" Item : содержит
    Order "1" o-- "1" DeliveryAgent : использует
    DeliveryAgent <|-- Courier : наследование
    DeliveryAgent <|-- Drone : наследование
```
Задание 6
```mermaid
classDiagram
    class User {
        +username : string
        +email : string
        +posts : List~Post~
        +create_post(content : string) Post
        +delete_post(post : Post)
    }
    
    class Post {
        +content : string
        +created_at : datetime
        -comments : List~Comment~
        +author : User
        +add_comment(user : User, text : string) Comment
        +delete_comment(comment : Comment)
        +get_comments() List~Comment~
    }
    
    class Comment {
        +text : string
        +created_at : datetime
        +author : User
    }
    
    User "1" o-- "*" Post : создает
    Post "1" *-- "*" Comment : содержит
```