    var b=function(msg) {alert('message test ' + msg);};

    document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById('calendar');
        var start;
        var end;

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
        eventAdd:function(obj){
            console.log(obj);
<!--            addlist(obj.title,obj.date);-->
<!--            alert(obj.start);-->
            //이벤트 추가되면
        },
        eventChange:function(obj){
            console.log(obj);
            //이벤트 수정
        },
        eventRemove:function(obj){
            console.log(obj);
        },
        select:function(arg){



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

              window.open("/single/create_post","editForm","width=500,height=500,resizable = no, scrollbars =no");

                if(title){
                calendar.addEvent({
                    title:title,
                    start:arg.start,
                    end:arg.end,
                    allDay:arg.allDay
                })
                document.getElementById("titletext").textContent=title;

            }

            calendar.unselect();

        },

        eventClick: function(arg) {
    	  // 있는 일정 클릭시,
            console.log("#등록된 일정 클릭#");
            console.log(arg.event);
             if (confirm('정말 삭제하시겠습니까?')) {
            arg.event.remove()
            }
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
