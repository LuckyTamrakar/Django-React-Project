import React from 'react'
import { Link } from 'react-router-dom'
import { getToken } from '../Services/LocalServices'
import Navbar from './Navbar'
import doc1 from './images/1.png' 
import doc2 from './images/2.png' 
import doc3 from './images/3.png' 
import doc4 from './images/4.png' 
import doc5 from './images/5.png' 
import doc6 from './images/6.png' 

function DoctorApoointment() {
    const { access_token } = getToken()
  return (
    <div>
        <Navbar/>
        <br/>
        <div className='container'>
        {access_token ? <></> : <div className="alert alert-danger border border-light border-2" role="alert">
<h4 className="alert-heading text-red">Please Login!</h4>
<p>If you want to give quiz please login in your account</p>
<hr/>
<p className="mb-0">If you don't have account. Please Register to give Quiz</p>
<br/>
<Link to="/register" className='btn btn-danger'>Register</Link>
</div>}</div>
        <div className='container'>
        
        <div className="bg-dark row row-cols-1 row-cols-md-3 g-4">
        
  <div className="col">
    
    <div className="card h-100 text-white bg-dark border border-light border-2">
      <img src={doc4} className="card-img-top" alt="..."/>
      <div className="card-body">
        <h5 className="card-title">Dr. Sohil khan</h5>
        <p className="card-text">Our Medical expert doctor provide various types of medical treatment to our patient.</p>
        
      </div>
      
        {access_token ? <Link to="/patient-appointment" className="btn btn-primary">Book Appointment</Link> : <Link to="/login" className="btn btn-primary">Book Appointment</Link>}
  
    </div>
  </div>
  <div className="col">
    <div className="card h-100 text-white bg-dark border border-light border-2">
      <img src={doc5} alt="..."/>
      <div className="card-body">
        <h5 className="card-title">Dr. Himanshi</h5>
        <p className="card-text">Dr. Himanshi is expertise in Heart related treatment</p>
        
      </div>
      
      {access_token ? <Link to="/patient-appointment" className="btn btn-primary">Book Appointment</Link> : <Link to="/login" className="btn btn-primary">Book Appointment</Link>}
    
    </div>
  </div>
  <div className="col bg-dark">
    <div className="card h-100 text-white bg-dark border border-light border-2">
      <img src={doc3} className="card-img-top" alt="..."/>
      <div className="card-body">
        <h5 className="card-title">Dr. Ashutosh</h5>
        <p className="card-text">Dr. Ashutosh is expertise in anytype of surgery.</p>
        
      </div>
     
      {access_token ? <Link to="/patient-appointment" className="btn btn-primary">Book Appointment</Link> : <Link to="/login" className="btn btn-primary">Book Appointment</Link>}
  
    </div>
  </div>
  <div className="col">
    <div className="card h-100 text-white bg-dark border border-light border-2">
      <img src={doc2} className="card-img-top" alt="..."/>
      <div className="card-body">
        <h5 className="card-title">Dr. Ajeet</h5>
        <p className="card-text">Dr. Ajeet is expertise in our Dental department</p>
        
      </div>
      {access_token ? <Link to="/patient-appointment" className="btn btn-primary">Book Appointment</Link> : <Link to="/login" className="btn btn-primary">Book Appointment</Link>}
    </div>
  </div>
  <div className="col">
    <div className="card h-100 text-white bg-dark border border-light border-2">
      <img src={doc6} className="card-img-top" alt="..."/>
      <div className="card-body">
        <h5 className="card-title">Dr. Varsha</h5>
        <p className="card-text">Dr. Varsha is expertise in our Eye department.</p>
        
      </div>
      {access_token ? <Link to="/patient-appointment" className="btn btn-primary">Book Appointment</Link> : <Link to="/login" className="btn btn-primary">Book Appointment</Link>}
    </div>
  </div>
  <div className="col">
    <div className="card h-100 text-white bg-dark border border-light border-2">
      <img src={doc1} className="card-img-top" alt="..."/>
      <div className="card-body">
        <h5 className="card-title">Dr. Vandna</h5>
        <p className="card-text">Dr. Vandna is expertise for Unconscious.</p>
        
      </div>
      {access_token ? <Link to="/patient-appointment" className="btn btn-primary">Book Appointment</Link> : <Link to="/login" className="btn btn-primary">Book Appointment</Link>}
    </div>
  </div>
</div>
        </div>
    </div>
  )
}

export default DoctorApoointment