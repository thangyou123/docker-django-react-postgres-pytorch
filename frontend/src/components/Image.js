import React from 'react';

// import { Container } from './styles';

function Image() {



  return (

    
    <label for="file-input" >

    <img src={"https://www.clipartmax.com/png/middle/145-1454284_software-for-laser-cutting-engraving-icon-no-image-available.png"} style={{height:"80%" ,width:"50px"}} alt=''  />
      <input id="file-input" type="file" style={{display:"none"}} />
  </label>
   
  );
}

export default Image;