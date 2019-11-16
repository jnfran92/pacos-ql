# :diamond_shape_with_a_dot_inside: :snake: PacosQL

Playing around with GraphQL and Django!
Project is ready to test!

<img src="https://i.giphy.com/media/l2Je1Yvi3YbdhyWkw/source.gif" alt="">


## Steps

Run the server and open:

    http://127.0.0.1:8000/graphql



## Query

Simple query sample:

    query{
       allPacos{
        edges{
          node{
            firstName
            lastName
            hasAGun
            likeDonuts
            wasteTime
          }
        }
      }
    }


## Requirements:

See `requirements.txt`
      
