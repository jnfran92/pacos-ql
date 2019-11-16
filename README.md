# :diamond_shape_with_a_dot_inside: :snake: PacosQL

Playing around with GraphQL and Django!



<img src="https://i.giphy.com/media/l2Je1Yvi3YbdhyWkw/source.gif" alt="">


## Steps
Project is ready to test. Run the server and open:

    http://127.0.0.1:8000/graphql


## Playing

There is one Model: `Paco` which is like a kind of Cop ^ ^.

Simple query:


    query{
      pacos{
        id
        firstName
        lastName
        likeDonuts
        hasAGun
      }
    }
 
 
 
Simple mutation:    
    
    
    mutation{
      createPaco(firstName:"Jhon", lastName:"Doe"){
        paco{
          id
          lastName
          firstName
        }
      }
    }


## Requirements

See `requirements.txt`
      
