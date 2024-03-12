import React from 'react';
import './App.css'; // 确保引入了样式文件
import logo from './images/logo.png';
import smallImage1 from './images/funtion1.jpeg';
import smallImage2 from './images/funtion2.jpeg';
import smallImage3 from './images/function3.jpeg';
import team1 from './images/Ravi.jpeg';
import team2 from './images/Ankit2.png';
import team3 from './images/Xinyi.jpeg';
import uw from './images/University_of_Washington.png';
import droneindoor2 from './images/droneindoor5.png';
import abstract_graphic from './images/abstract_graphic.jpg';

// const applyFilters = () => {
//   // You can make an API request or navigate to the Streamlit app URL
//   // Here, I'm using window.open to open the Streamlit app in a new tab
//   window.open('http://localhost:8501/server.py', '_blank');
// };

function App() {
  return (
    <div className="app-container">

      <div className="main-image-container">
        <img src={droneindoor2} alt="Main" className="main-image" />
        <p className="main-image-description2">AeroNex</p>
        <p className="main-image-description3">Aerial Intelligence for Precision Operations</p>
        <p className="main-image-description">AeroNex drones, powered by real-time object detection, autonomously navigate high-risk zones, enhancing safety in inaccessible environments. Our integration of computer vision and machine learning sets a new standard for aerial technology, improving safety and decision-making in hazardous conditions. This innovative approach exemplifies our commitment to advancing unmanned aerial solutions for heightened efficiency and risk mitigation.</p>
      </div>

      <h2 className="subtitle">Process</h2>
      <div className="images-task">
        <div>
          <img src={smallImage1} alt="Row 1" className="task-image" />
          <div className="text-container2">
            <p>Capture: Autonomous drone aerial survey for comprehensive image and video acquisition.</p>
          </div>
          <a href="src/play.html"> <button className="button">Initiate Drone Capture</button> </a>
        </div>
        <div>
          <img src={smallImage2} alt="Row 2" className="task-image" />
          <div className="text-container2">
            <p>Enhance: Apply advanced filters using Convolutional Neural Networks (CNN) for improved analysis.</p>
          </div>
          <a href="http://localhost:8501"> <button className="button">Apply Filters</button></a>
        </div>
        <div>
          <img src={smallImage3} alt="Row 3" className="task-image" />
          <div className="text-container2">
            <p>Detect: Precise identification and categorization of objects.</p>
          </div>
          <a href="http://localhost:8502"> <button className="button">Detection & Classification</button></a>
        </div>
      </div>
      <h2 className="subtitle">Technical Diagram</h2>
      <div className="images-diagram">
        <div>
          <img src={abstract_graphic} alt="diagram 1" className="diagram-image" />
        </div>
      </div>
      <h2 className="subtitle">Research & Development Team</h2>
      <div className="image-team">
        <div className="team">
          <img src={team2} alt="Row 1" className="team-image" />
          <div className="name">
          <p>Ankit Shaw</p>
          </div>
          <div className="word">
          <p>Machine Learning Engineer</p>
          </div>
        </div>
        <div className="team">
          <img src={team3} alt="Row 1" className="team-image" />
          <div className="name">
          <p>Xinyi Zhou</p>
          </div>
          <div className="word">
          <p>Creative Engineer</p>
          </div>
        </div>
        <div className="team">
          <img src={team1} alt="Row 3" className="team-image" />
          <div className="name">
          <p>Ravinder Gulla</p>
          </div>
          <div className="word">
          <p>Technical Lead</p>
          </div>
          
        </div>
      </div>

      <img src={uw} className="uw" />


    </div>
  );
}

export default App;





//<header className="app-header">
//<div class="banner">AeroNex</div>
//</header>
//<div class="sub-banner">Aerial Intelligence for Precision Operations
//</div>
