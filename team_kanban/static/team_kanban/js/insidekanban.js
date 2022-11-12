window.onload=function(){
    var sub_btn = document.getElementById('sub_btn');
    sub_btn.onclick=function(){
        document.myForm.target= opener.name; //호출하고자하는 부모창의 이름
        document.myForm.submit(); // 폼 전송
        self.close(); //창 닫기 
    }
};

function check(document){
    if(document.check=false){
        document.style.backgroundColor='#F4E3D2'
        document.style.color='black';
        //선택 해제
    }
    document.style.backgroundColor='black';
    document.style.color='white';
}
