var b=function(msg) {alert('message test ' + msg);};
    document.addEventListener('DOMContentLoaded', function() {
        var calendarEl = document.getElementById('calendar');
        var calendar = new FullCalendar.Calendar(calendarEl, {
            
        
        
        editable:true,
        selectable:true,
        contentWidth:300,
        navLinks: true,
        eventAdd:function(obj){
            console.log(obj);
            
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
            var title=prompt('Event Title');
            if(title){
                calendar.addEvent({
                    title:title,
                    start:arg.start,
                    end:arg.end,
                    allDay:arg.allDay
                })
            }
            calendar.unselect()
            //창 크기 지정
            var width = 500;
            var height = 500;
            
            //pc화면기준 가운데 정렬
            var left = (window.screen.width / 2) - (width/2);
            var top = (window.screen.height / 4);
            
                //윈도우 속성 지정
            var windowStatus = 'width='+width+', height='+height+', left='+left+', top='+top+', scrollbars=yes, status=yes, resizable=yes, titlebar=yes';
            
            //연결하고싶은url
            const url = "./edit.html";

            //등록된 url 및 window 속성 기준으로 팝업창을 연다.
            //window.open(url, "edit", windowStatus);
            // if(popup){
            //     calendar.addEvent({
            //         title:setTitle(),
            //         start:arg.start,
            //         end:arg.end,
            //         allDay:arg.allDay
            //     })
            //     calendar.unselect()
            // }
            // window.onbeforeunload=function(){
            //     //window.location.reload();
            //     calendar.unselect()
            // }
            
        },
        eventClick: function(arg) {
    	  // 있는 일정 클릭시,
            console.log("#등록된 일정 클릭#");
            console.log(arg.event);
            
            if (confirm('Are you sure you want to delete this event?')) {
            arg.event.remove()
            }
        }
        
        });
        
        calendar.render();
    }); 