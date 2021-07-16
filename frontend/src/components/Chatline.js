import React from 'react';

// import { Container } from './styles';

function Chatline({todo}) {
  return (
<>
<div className="lv-item media right"> 
<div className="media-body"> 
<div className="ms-item">
{todo.input}
</div>
</div>
</div>

<div className="lv-item media"> 
<div className="lv-avatar pull-left">
<img src={"https://hinhanhdep.net/wp-content/uploads/2015/12/anh-cho-va-meo-5.jpg"} alt=''/> 
</div> 
<div className="media-body">
    <div className="ms-item">
{todo.output}
</div>
</div>
</div>
</>
  );
}

export default Chatline;