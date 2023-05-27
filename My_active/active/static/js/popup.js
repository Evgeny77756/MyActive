window.onload = function(){


    cli = document.getElementById('btn')
    cli.onclick = (event) => {
        document.getElementById('modal').style.display = 'block';
        alert('hello!');

    }

    btn = document.getElementById('btn__click');
    btn.style.cursor = 'pointer';
    btn.onclick = (event) => {
        document.getElementById('modal').style.display = 'none';
        alert('hello!1234');

    }



//$(document).ready(function(){
//    $('#btn').click(function(){
//        $('#buyStock').show();
//    });
//});


//
//    $(document).ready(function(){
//        $('#buyStock').on('submit', function(e){
//            e.preventDefault();
//            $.ajax({
//                url:"{% url 'buy_stock_user' %}",
//                type: 'POST',
//                data: $(this).serialize(),
//                success: function(data){
//                    if(data.success){
//                        alert('success!');
//                    }
//                    else{
//                        alert('error!');
//                    }
//                }
//            });
//        });
//    });

}
