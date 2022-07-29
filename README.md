# Wbjee-API

This is a rest api which takes two parameters named rank and quota
and returns json showing the colleges and available branches depending upon the input parameters.
The API is ------>
https://kilf4q0gf6.execute-api.us-east-1.amazonaws.com/wbjee/wbjee?rank=<integer>&quota=<integer>

#rank take the GMR rank

#The Quota takes integers values from 0 to 10.


["general","pgeneral","obca","pobca","obcb","pobcb","sc","psc","st","pst","tfw"]
 like (0 for general),(1 for pwd general)....(10 for tfw)

  example:
  rank=469
  quota=0 means grneral
  
  https://kilf4q0gf6.execute-api.us-east-1.amazonaws.com/wbjee/wbjee?rank=469&quota=0
  
  

output:########
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
  




