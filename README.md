# saleor-paydotir

for a query type :
```graphql
query{  
paydotirs{
id,
transid,
token,
username
}
}

for a mutation : 
mutation {
  createPaydotir(
    username:"username",
    amount:'amount as int'
    
  ){
    id
    nextUrl
    username
    token
  }
}
```
