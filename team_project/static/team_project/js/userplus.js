document.addEventListener('DOMContentLoaded', () => {
    const input = document.querySelector('#input')
    const addButton = document.querySelector('#add-button')
    const user = document.querySelector('#user')

      // '+' 버튼 익명 화살표 함수 
    const addTodo = () => {
        if (input.value !== '') {//input value가 있는 경우
            const item = document.createElement('div')//div 를 만든다
            item.setAttribute('id','user')

         // text
            const text = document.createElement('span');
            text.textContent = input.value//input에 작성한 값을 text에 넣는다
            input.value=''//input을 초기화한다

            item.appendChild(text)//item에 text
            user.appendChild(item)//item을 붙인다.
            })
        }
        else //
            alert.textContent = '이메일을 입력하세요!'
    }

    addButton.addEventListener('click', addTodo)
      // 할 일 입력창에서 enter key가 눌렸을 때
    input.addEventListener('keypress', (event) => {
        const ENTER = 13
        if (event.keyCode === ENTER)
            addTodo();
    })
})