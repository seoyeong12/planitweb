    var b=function(msg) {alert('message test ' + msg);};

    document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById('calendar');
        var start;
        var end;
        var month;
        var year;
        var date;
        var result;
        var dateS;

        var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridWeek',
        views: {
            month: {
                editable: false
            },
            week: {
                columnFormat: 'dddd' // set format for week here
            },
        },
        editable:true,
        selectable:true,
        contentWidth:300,


        events : [
            {
                title:"All day",
                start : "2022-11-15T09:00:00",
                end: "2022-11-15T10:00:00",
            }
        ],


        select:function(arg){
            console.log(arg);

            function start(){
                start = arg.start.getHours();
                String(start);
                return start;
            }

             function end(){
                end = arg.end.getHours();
                String(end);
                return end;
            }

            start();
            end();

            document.getElementById("time1").innerHTML = start;
            document.getElementById("time2").innerHTML = end;

            function resDate(){
                dateS = arg.start;
                year = dateS.getFullYear();
                String(year);
                month = dateS.getMonth()+1;
                String(month);
                date = dateS.getDate();
                String(date);
                result = year+"-"+month+"-"+date;
                String(result);
                return result;
            }
            resDate();

            document.getElementById("date").innerHTML = result;

            function openChild(){
                window.name="parentForm";
                window.open("/single/create_post","editForm","width=500,height=500,resizable = no, scrollbars =no");
            }

           openChild();

           calendar.unselect();
        }
    });
        calendar.render();
    });

<!--    function addlist(title,date){-->
<!--        // var yy=date.format("YYYY");-->
<!--        //     var mm=date.format("MM");-->
<!--        //     var dd=date.format("DD");-->
<!--        //     var ss=date.format("dd");-->

<!--        document.getElementById("titletext").textContent=title;-->
<!--        document.getElementById("start").textContent=date;-->


<!--    }-->

</script>





