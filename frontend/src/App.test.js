import { render, screen } from '@testing-library/react';
import App from './App';

// test('renders learn react link', () => {
//   render(<App />);
//   const linkElement = screen.getByText(/learn react/i);
//   expect(linkElement).toBeInTheDocument();
// });






/* 

<div className="container-fluid" >
    <div className="container ng-scope" >
        <div className="card m-b-0" id="messages-main" style={{boxwithShadow:"0 0 40px 1px #c9cccd" , maxWidth: "1500px",height:"85%" }}  >

            <div className="ms-menu"  >

                 <div className="ms-block" >

                    <div className="ms-user">
                        <img src={"https://i.pinimg.com/564x/dd/0e/86/dd0e86cc6c9ae4bc0473c762e275f9c4.jpg"} />
                        <h5 className="q-title"  align="center" >Sachin Yaday <br/><b>5</b> New Messages</h5>
                     </div>

                </div>

                <div className="ms-block">
                     <a  href="#"><span className="glyphicon glyphicon-envelope"></span>&nbsp; New Message</a>
                </div>
                <hr/>
                <div className="listview lv-user m-t-20" style={{overflow:"scroll", overflowX: "hidden"}} id="ms-scrollbar">
                    <div className="lv-item media active">
                        <div className="lv-avatar pull-left">
                           <img src={"https://hinhanhdep.net/wp-content/uploads/2015/12/anh-cho-va-meo-5.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title">Ashwani Singh Yadav</div>
                           <div className="lv-small"> Acadnote a world className website is processing surveys for </div>
                        </div>
                     </div>

                     <div className="lv-item media">
                        <div className="lv-avatar pull-left">
                           <img src={"https://tophinhanhdep.com/wp-content/uploads/2021/03/large.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title"><b>Ajit Gupta</b> <span className="pull-right">10 new </span></div>
                           <div className="lv-small"><b>Hello bro whatsup , how are you</b></div>
                        </div>
                     </div>

                     <div className="lv-item media">
                        <div className="lv-avatar pull-left">
                           <img src={"https://tophinhanhdep.com/wp-content/uploads/2021/03/large.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title"><b>Ajit Gupta</b> <span className="pull-right">10 new </span></div>
                           <div className="lv-small"><b>Hello bro whatsup , how are you</b></div>
                        </div>
                     </div>

                     <div className="lv-item media">
                        <div className="lv-avatar pull-left">
                           <img src={"https://tophinhanhdep.com/wp-content/uploads/2021/03/large.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title"><b>Ajit Gupta</b> <span className="pull-right">10 new </span></div>
                           <div className="lv-small"><b>Hello bro whatsup , how are you</b></div>
                        </div>
                     </div>

                     <div className="lv-item media">
                        <div className="lv-avatar pull-left">
                           <img src={"https://tophinhanhdep.com/wp-content/uploads/2021/03/large.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title"><b>Ajit Gupta</b> <span className="pull-right">10 new </span></div>
                           <div className="lv-small"><b>Hello bro whatsup , how are you</b></div>
                        </div>
                     </div>

                     <div className="lv-item media">
                        <div className="lv-avatar pull-left">
                           <img src={"https://tophinhanhdep.com/wp-content/uploads/2021/03/large.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title"><b>Ajit Gupta</b> <span className="pull-right">10 new </span></div>
                           <div className="lv-small"><b>Hello bro whatsup , how are you</b></div>
                        </div>
                     </div>

                     <div className="lv-item media">
                        <div className="lv-avatar pull-left">
                           <img src={"https://tophinhanhdep.com/wp-content/uploads/2021/03/large.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title"><b>Ajit Gupta</b> <span className="pull-right">10 new </span></div>
                           <div className="lv-small"><b>Hello bro whatsup , how are you</b></div>
                        </div>
                     </div>

                     <div className="lv-item media">
                        <div className="lv-avatar pull-left">
                           <img src={"https://tophinhanhdep.com/wp-content/uploads/2021/03/large.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title"><b>Ajit Gupta</b> <span className="pull-right">10 new </span></div>
                           <div className="lv-small"><b>Hello bro whatsup , how are you</b></div>
                        </div>
                     </div>

                     <div className="lv-item media">
                        <div className="lv-avatar pull-left">
                           <img src={"https://tophinhanhdep.com/wp-content/uploads/2021/03/large.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title"><b>Ajit Gupta</b> <span className="pull-right">10 new </span></div>
                           <div className="lv-small"><b>Hello bro whatsup , how are you</b></div>
                        </div>
                     </div>

                     <div className="lv-item media">
                        <div className="lv-avatar pull-left">
                           <img src={"https://tophinhanhdep.com/wp-content/uploads/2021/03/large.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title"><b>Ajit Gupta</b> <span className="pull-right">10 new </span></div>
                           <div className="lv-small"><b>Hello bro whatsup , how are you</b></div>
                        </div>
                     </div>

                     <div className="lv-item media">
                        <div className="lv-avatar pull-left">
                           <img src={"https://tophinhanhdep.com/wp-content/uploads/2021/03/large.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title"><b>Ajit Gupta</b> <span className="pull-right">10 new </span></div>
                           <div className="lv-small"><b>Hello bro whatsup , how are you</b></div>
                        </div>
                     </div>

                     <div className="lv-item media">
                        <div className="lv-avatar pull-left">
                           <img src={"https://tophinhanhdep.com/wp-content/uploads/2021/03/large.jpg"} alt=""/>
                        </div>
                        <div className="media-body">
                           <div className="lv-title"><b>Ajit Gupta</b> <span className="pull-right">10 new </span></div>
                           <div className="lv-small"><b>Hello bro whatsup , how are you</b></div>
                        </div>
                     </div>




                     




                </div>
            </div>



            <div className="ms-body" >
                <div className="listview lv-message" >
                    <div className="lv-header-alt clearfix">
                        <div id="ms-menu-trigger">
                            <div className="line-wrap">
                              <div className="line top"></div>
                              <div className="line center"></div>
                              <div className="line bottom"></div>
                           </div>
                        </div>
                        <div className="lvh-label hidden-xs">
                           <div className="lv-avatar pull-left">
                              <img src={"https://hinhanhdep.net/wp-content/uploads/2015/12/anh-cho-va-meo-5.jpg"} alt=""/>
                           </div>
                           <span className="c-black">Ashwani Singh Yadav<span style={{ marginLeft:"8px", position:"absolute", marginTop:"12px",width: "8px",height: "8px",lineHeight: "8px",    borderRadius: "50%", backgroundColor:"#80d3ab"}}></span></span>
                        </div>
                        
                        <ul className="lv-actions actions list-unstyled list-inline">
                           <li>
                              <a href="#" >
                              <i className="fa fa-check"></i>
                              </a>
                           </li>
                           <li>
                              <a href="#" >
                              <i className="fa fa-clock-o"></i>
                              </a>
                           </li>
                           <li>
                              <a data-toggle="dropdown" href="#" > <i className="fa fa-list"></i></a>
                              <ul role="menu">
                                 <li>
                                    <a >Top</a>
                                 </li>
                                
                              </ul>
                           </li>
                           <li>
                           
                              <ul role="menu">
                                 <li>
                                    <a >Bottom

                                    </a>
                                 </li>
                              </ul>
                           </li>
                           <li>
                           
                              <ul className="dropdown-menu user-detail" role="menu">
                                 <li>
                                    <a href="">Delete Messages
                                    </a>
                                 </li>
                              </ul>
                           </li>
                        </ul>

                    </div>
                    <div className="lv-body" id="ms-scrollbar" name="thang" style={{overflow:"scroll", overflowX: "hidden", height:"80vh"  }}>
                    
                    </div>

                    <div className="clearfix"></div>
                    <div className="lv-footer ms-reply">

                    </div>


                </div>


            </div>





        </div>
    </div>

</div>
          
                        */