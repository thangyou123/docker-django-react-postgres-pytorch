import React, { useEffect } from 'react';
import Chatline from './Chatline';
function Chatlist({todolist}) {
   useEffect(()=>{

    var textarea = document.getElementsByName('thang');
    var taaa=textarea.item(0);
    taaa.scrollTop = taaa.scrollHeight;


   })
  return (
  <>
{
  todolist.map((todo)=>(
    <Chatline key={todo.id} todo={todo}> </Chatline>
  )
  )
}
  
   </>
  
  );
}

export default Chatlist;