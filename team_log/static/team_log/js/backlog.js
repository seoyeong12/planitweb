document.addEventListener('DOMContentLoaded', () => {
    const input = document.querySelector('#todo')
    const addButton = document.querySelector('#add-button')
    const todoList = document.querySelector('#todo-list')
    const alert = document.querySelector('span')

      // '+' 버튼 익명 화살표 함수 
    const addTodo = () => {
        if (input.value !== '') {//input value가 있는 경우
            const item = document.createElement('div')
            item.setAttribute('id','backlogdiv')
            item.onmouseover=function(){
                deleteButton.style.visibility="visible"
            }
            item.onmouseout=function(){
                deleteButton.style.visibility="hidden"
            }
          // 체크박스
            const checkbox = document.createElement('input')
            checkbox.type='checkbox'
         // text
            const text = document.createElement('span');
          // 삭제하기 버튼
            const deleteButton = document.createElement('button')
                deleteButton.textContent="삭제"
                deleteButton.style.visibility="hidden"
            text.textContent = input.value
            input.value=''
        
            item.appendChild(checkbox)
            item.appendChild(text)
            item.appendChild(deleteButton)
            todoList.appendChild(item)

    // 체크박스 이벤트 리스너
            checkbox.addEventListener('change', (event) =>{ 
                if (event.currentTarget.checked)
                {
                    text.style.textDecoration='line-through'
                }
                else {
                    text.style.textDecoration='none'
                }
            })

          // 삭제하기 버튼 클릭 이벤트 리스너
            deleteButton.addEventListener('click', (event) => {
                todoList.removeChild(event.currentTarget.parentNode)
            })
            input.value =''
            alert.textContent = ''
        }
        else
            alert.textContent = '할 일을 입력하세요!'
    }

    addButton.addEventListener('click', addTodo)
      // 할 일 입력창에서 enter key가 눌렸을 때
    input.addEventListener('keypress', (event) => {
        const ENTER = 13
        if (event.keyCode === ENTER)
            addTodo();
    })
})