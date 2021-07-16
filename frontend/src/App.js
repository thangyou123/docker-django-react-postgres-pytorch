import './App.css';
import React, { useEffect } from 'react';
import { useState } from 'react';
import Chatlist from './components/Chatlist';
import axios from 'axios';
import FormData from 'form-data';
import { v4 as uuidv4 } from 'uuid';
import Image  from './components/Image';
function App(){

const [todolist,setTodoList]=useState([]);
const [textInput,setTextInput]=useState('');

useEffect(() => {
    var newState = [];
axios({
    method: "get",
    url: "http://127.0.0.1:8000/api/MyAPI/",
    headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
}).then(function(response){
const l=response.data.length;

for (var i=0;i<l;i++){
  
   newState[i]={id:uuidv4() , input: response.data[i]['text'],output: response.data[i]['text2'] };
} 


setTodoList(newState);  

})

}, []);
const TextInputChange=(e)=>{
    setTextInput(e.target.value);
};
const onAddbtnClick=(e)=>{
    
    var bodyFormData = new FormData();
    bodyFormData.append('text', textInput);
    bodyFormData.append('text2', 'Null');
    axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/MyAPI/",
        data: bodyFormData,
        headers: { "Content-Type": "multipart/form-data" },
      })
        .then(function (response) {
          //handle success
          console.log(response.data['text']);
          setTodoList([...todolist,{id:uuidv4() , input: textInput,output: response.data['text2'] } ] ) ;
          
        })
       
        .catch(function (response) {
          //handle error
          console.log(response);
        });
       
    setTextInput('');
}



return (
    <div>
<div className="lv-body" id="ms-scrollbar" name="thang" style={{overflow:"scroll", overflowX: "hidden", height:"80vh"  }}>

<Chatlist todolist={todolist} />


                    </div>
                    <div className="clearfix"></div>
                    <div className="lv-footer ms-reply">
                        <form>
                <textarea value={textInput}  onChange={TextInputChange} >
                </textarea>
             <Image/>
                <button  type='button' onClick={onAddbtnClick}  className=""><span className="glyphicon glyphicon-send"></span> </button>
                </form>
</div>
    </div>   
);
}


export default App;