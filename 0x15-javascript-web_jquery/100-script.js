// updates the text color of the <header> element to red
/*
// this function sets the defer property of the script that contains the string <check> to true
const setDefer = function (check){
    const scripts = $('script')
    $.each(scripts, function (index, value) {
     if (value.src.includes(check)){
        value.defer = true;
     }
    }
 );
}
*/
document.addEventListener('DOMContentLoaded', (event) => {
  document.querySelector('header').style.color = 'red';
});
