const toggler=document.querySelector('#top-nav-toggler')
const splashImage = document.querySelector('.masthead')
const loginToggler = document.querySelector('#navbarSignIn');
const page = document.querySelector('html');
const signUpForm = document.querySelector('#signup');
const homeForm = document.querySelector('#home-form');
var maststate = 1;
var logState = -1;

toggler.onclick = function(){
    maststate = maststate*-1;
    maststateModifier();
}
function maststateModifier()
{
    if(maststate==-1){
        splashImage.style.display='none';
        document.getElementById('top-right-user').style.visibility='hidden';
    }
    else{
        splashImage.style.display='flex';
        document.getElementById('top-right-user').style.visibility='visible';

    }

}

