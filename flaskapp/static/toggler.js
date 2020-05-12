const toggler=document.querySelector('#top-nav-toggler')
const splashImage = document.querySelector('.masthead')
var state = 1;

toggler.onclick = function(){
    state = state*-1;
    stateModifier();
}

function stateModifier()
{
    if(state==-1)
        splashImage.style.display='none';
    else
        splashImage.style.display='flex';
}