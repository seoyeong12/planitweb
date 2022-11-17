window.name = 'Kanban';

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function allowDrop(ev) {
    ev.preventDefault();
}

function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.currentTarget.appendChild(document.getElementById(data));//data를 ev의 자식으로 붙임
    //data의 status가 변경 -> database에 저장되어야 한다.
}

function createTask(pk){
    //창 크기 지정
    var width = 500;
    var height = 500;
    
    //pc화면기준 가운데 정렬
    var left = (window.screen.width / 2) - (width/2);
    var top = (window.screen.height / 4);
    
        //윈도우 속성 지정
    var windowStatus = 'width='+width+', height='+height+', left='+left+', top='+top+', scrollbars=yes, status=yes, resizable=yes, titlebar=yes';
    
    //연결하고싶은url
    const url = pk;

    //등록된 url 및 window 속성 기준으로 팝업창을 연다.
    window.open(url, "edit", windowStatus);
}

function editTask(pk){
    //창 크기 지정
    var width = 518;
    var height = 692;
    
    //pc화면기준 가운데 정렬
    var left = (window.screen.width / 2) - (width/2);
    var top = (window.screen.height / 4);
    
    //윈도우 속성 지정
    var windowStatus = 'width='+width+', height='+height+', left='+left+', top='+top+', scrollbars=yes, status=yes, resizable=yes, titlebar=yes';
    
    //연결하고싶은url
    const url = pk;

    //등록된 url 및 window 속성 기준으로 팝업창을 연다.
    window.open(url, "edit", windowStatus);
}

function deleteTask(){
    alert("삭제")
}

function insideKanban(pk){
    var width = 500;
    var height = 500;
    var left = (window.screen.width / 2) - (width/2);
    var top = (window.screen.height / 4);
    var windowStatus = 'width=' + width + ', height=' + height + ', left=' + left + ', top=' + top + ', scrollbars=yes, status=yes, resizable=yes, titlebar=yes';

    const url = pk;

    window.open(url, "edit", windowStatus);
}