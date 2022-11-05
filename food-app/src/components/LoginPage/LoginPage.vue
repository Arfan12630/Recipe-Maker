<template>
<form class="form-box"> 
    <div class="form-inner"> 
      <h2> Recipe ShareSpot </h2> 

        <div class="form-group"> 
            <label> <b> Username </b> </label>
            <input placeholder="Enter username"/>
        </div>


        <div class="form-group"> 
            <label> <b> Password </b> </label>
            <input placeholder="Enter password"/>

        </div>
    </div> 

    </form>
</template>

<script>


export default ({
    setup() {
        
    },
})
</script>


<style>
.form-box{
    height:100vh;
    display:flex;
    align-items:center;
    justify-content: center;
   
}

form{
    display:block;
    position:relative;
}

form:after{
    content:"";
    display:block;
    position:absolute;
    top:-5px;
    left:-5px;
    right:-5px;
    bottom:-5px;
    z-index:1;
}


form .form-inner{
    position:relative;
    display:block;
    background-color:#FFF;
    padding:30px;
    z-index:2;
}
.form-inner{
    border: 3px solid black;
    background-image: linear-gradient(to bottom right, #018749  , #018749 ); 
    border-radius: 25px;
    

}
/* form .LoginForm_form-inner h2{
    color: black;
    font-size: 28px;
    font-weight: 500;
    margin-bottom: 30px;
    
} */

input{
    border:2px solid #DDA0DD;
    border-radius:7px;
}
form .form-inner h2{
    color:#FFD700;
    font-size:28px;
    font-weight:500;
    margin-bottom:50px;
    justify-content: center;
    align-items: center;
    display: flex;
    text-align:center ;
    text-align:justify ;
    vertical-align:baseline;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    font-weight:bold;
    text-transform:uppercase;
    letter-spacing:1px;
}
form .form-inner .form-group{
    display:block;
    width:300px;
    margin-bottom:46px;

}

.form-inner .form-group label{
    
    color:white;
    font-size:12px;
    margin-bottom:7px;
    transition:0.4s;

}

.form-inner .form-group:focus-within label{
    color:#FFD700;
    
}
.form-inner .form-group:focus-within input{
    border-color: #FFD700;
}

.form-inner .form-group input{
    display:block;
    width:93%;
    padding:10px 15px;
    background-color: #F8F8F8;
    border-radius:8px;
    transition:0.4s;
}


form .form-inner .form-group input:focus{
    box-shadow: 0px 0px 3px rgba(0,0,0,0.2);
    
}



form .form-inner input[type="submit"]{
    display:inline-block;
    padding:10px 15px;
}

button{
    color:black;
    font-weight:500;
    justify-content: center;
    align-items: center;
   
    vertical-align:baseline;
    font-family:Verdana, Geneva, Tahoma, sans-serif;
    font-weight:bold;
    text-transform:uppercase;
    letter-spacing:1px;
    margin-top:12px;
    position: absolute;
  
    /* -ms-transform: translate(-50%, -50%); */
    /* transform: translate(-50%, -50%); */
   
    border-radius: 140px;
}
</style>