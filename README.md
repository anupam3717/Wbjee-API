# Wbjee-API

This is a rest api which takes two parameters named rank and quota
and returns json showing the colleges and available branches depending upon the input parameters.
The API is ------>
https://kilf4q0gf6.execute-api.us-east-1.amazonaws.com/wbjee/wbjee?rank=<integer>&quota=<integer>

#rank take the GMR rank
#The Quota takes 11 integers taking values from 0 to 10.
  head=["general","pgeneral","obca","pobca","obcb","pobcb","sc","psc","st","pst","tfw"]
  0 implies general quota
  1 implies pwd general quota
  2 implies pwd general quota
  ...
  ...
  ...
  9 implies pwd st quota
  10 implies tfw quota
  
  
  example:
  rank=469
  quota=0 means grneral
  
  https://kilf4q0gf6.execute-api.us-east-1.amazonaws.com/wbjee/wbjee?rank=469&quota=0
  
  

output:
  {
    "Cooch Behar Government Engineering College_Cooch Behar": [
        "Civil Engineering",
        "COMPUTER SCIENCE & ENGINEERING",
        "Electrical Engineering",
        "Electronics & Communication Engineering/Electronics & Telecommunication Engineering",
        "Mechanical Engineering"
    ],
    "Goverment College of Engineering and Leather Technology_Kolkata": [
        "COMPUTER SCIENCE & ENGINEERING",
        "Information Technology",
        "Leather Technology"
    ],
 .....
  .....
  .....
}
  




