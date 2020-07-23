console.log('File loaded');

const form = document.querySelector('#chatbot-usertext');
const button = document.querySelector('#exampleInputEmail1');
const userQuery = document.querySelector('#user-input');
const botResponse = document.querySelector('#bot-response');

form.addEventListener('submit',(e) => {
    e.preventDefault();
    console.log(button.value);
    const input = button.value;
    fetch('http://localhost:5000/endpoint?input='+input).then((response) =>{
    response.json().then((data) =>{
        if(data.error){
           console.log(data.error); 
        }else{
            console.log(data.response);
            userQuery.innerHTML="User : " + button.value;
            botResponse.innerHTML="CardioBot :" + data.response;
        }
    });
});
});

// fetch('http://localhost:5000/endpoint?input='+input).then((response) =>{
//         response.json().then((data) =>{
//             if(data.error){
//                console.log(data.error); 
//             }else{
//                 console.log(data.response);
//                 // console.log(data.forecast);
//             }
//         }
// })

