- user {point, name, username, password}
    - Create / Update(email--Unique)
        - Method: POST
        - Url: api/user/
        - Payload: {
            "username": "abc@gmail.com",
            "password": "harry0210",
            "name": "Harry Wu",
            "email": "abc@gmail.com"
        }

    - Delete / Retrieve
        - Method: DELETE / GET
        - Url: api/user/<id>

    - Login
        - Method: POST
        - Url: api/user/login/
        - Payload: {
            "username": "",
            "password": ""
        }

    - Deposit
        - Method: POST
        - Url: api/user/deposite/
        - Payload: {
            "point": 0
        }
        
- gift {point, amount, name}
    - Create, Update, Retrieve, List
    - exchange
- order {user, gift, time, amount}
    - Retrieve, List