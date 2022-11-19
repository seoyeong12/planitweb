
var b=function(msg) {alert('message test ' + msg);};
    document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById('calendar');
        var calendar = new FullCalendar.Calendar(calendarEl, {        
        initialView: 'timeGridWeek',
        views: {
            
            week: {
                columnFormat: 'dddd' // set format for week here
            },
        },
        
        editable:true,
        selectable:true,
        contentWidth:300,
        
        eventAdd:function(obj){
            console.log(obj);
            alert(obj.month);
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
            var title = prompt('Event');         
        //openWin=window.open("./edit.html","editForm","width=500,height=500,resizable = no, scrollbars =no");

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
        calendar.on('dateClick', function(info) {
            console.log('clicked on ' + info.dateStr);
        });
    }); 
