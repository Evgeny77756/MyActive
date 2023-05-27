window.onload = function(){

    const error = document.createElement('div');
    error.textContent = 'Слишком большая сумма для вывода!';
    error.style.backgroundColor = 'red';
    error.style.color = 'white';
    error.style.padding = '20px 50px';
    error.style.position = 'absolute';
    error.style.top = '50%';
    error.style.left = '50%';
    error.style.transform = 'translate(-50%, -50%)';

    const parentElem = document.getElementById('parent_elem');
//    parentElem.style.position = 'relative';


    parentElem.appendChild(error);

    parentElem.onclick=(event)=>{
        window.location.href = '../action_list_user';
    }

}
