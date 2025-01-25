export default function SignupCard() {
  return (
    <section 
      
      style={{
        backgroundImage: "url('../../imagini/site mate.png')",
        backgroundSize: 'cover',
      }}
    >
      <div>
        <img
          src="../../imagini/loginMic.jpg"
          alt="Katherine Johnson"
          
        />
        <h1>Welcome To<br></br>Easymath?</h1>
        <p>Lorem adsafasfsafassafasf</p>
        <div 
          className="w-12 h-12 flex flex-col gap-4"
          style={{ backgroundColor: 'white' }}
        >
          <input 
            type="text" 
            placeholder="Name" 
            
          />
          <input 
            type="email" 
            placeholder="Email" 
            
          />
          <input 
            type="password" 
            placeholder="Password" 
            
          />
          <button 
            
          >
            Sign Up
          </button>
        </div>
      </div>
    </section>
  );
}
