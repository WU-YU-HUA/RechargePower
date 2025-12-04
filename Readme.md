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
    - Create
        - Method: POST
        - Url: api/gift/
        - Payload: {
            "name": "禮物1",
            "point": 20,
            "amount": 100
        }

    - Update
        - Method: PATCH
        - Url: api/gift/<id>
        - Payload: {
            "point": 0,
            "amount": 0, 
            # One or Both are access.
        }

    - Retrieve, Delete
        - Method: GET / DELETE
        - Url: api/gift/<id>

    - List
        - Method: GET
        - Url: api/gift/

    - exchange
        - Method: POST
        - Url: api/gift/exchange/
        - Payload: {
            "quantity": 50,
            "id": 2
        }

- order {user, gift, time, amount, point}
    - List
        - Method: GET
        - Url: api/order/