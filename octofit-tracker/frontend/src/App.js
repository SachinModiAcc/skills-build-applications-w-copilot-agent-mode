import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div>
      {/* Navigation Bar */}
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">OctoFit Tracker</a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item"><a className="nav-link active" href="#">Home</a></li>
              <li className="nav-item"><a className="nav-link" href="#">Teams</a></li>
              <li className="nav-item"><a className="nav-link" href="#">Activities</a></li>
              <li className="nav-item"><a className="nav-link" href="#">Leaderboard</a></li>
              <li className="nav-item"><a className="nav-link" href="#">Workouts</a></li>
            </ul>
          </div>
        </div>
      </nav>

      {/* Main Card */}
      <div className="container mt-5">
        <div className="row justify-content-center">
          <div className="col-md-8">
            <div className="card shadow">
              <div className="card-body text-center">
                <h1 className="card-title display-4 mb-3">Welcome to <span className="text-primary">OctoFit Tracker</span>!</h1>
                <p className="card-text lead">Your fitness, team, and leaderboard app is ready.</p>
                <a href="#" className="btn btn-primary btn-lg mt-3">Get Started</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
