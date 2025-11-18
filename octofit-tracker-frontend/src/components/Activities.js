import React, { useEffect, useState } from 'react';

const Activities = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : 'http://localhost:8000/api/activities/';
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        console.log('Activities endpoint:', endpoint);
        console.log('Fetched activities:', data);
        setActivities(data.results || data);
      });
  }, [endpoint]);

  return (
    <div className="card mt-4">
      <div className="card-body">
        <h2 className="card-title text-primary">Activities</h2>
        <table className="table table-striped table-bordered mt-3">
          <thead className="table-dark">
            <tr>
              <th>#</th>
              <th>Type</th>
              <th>Duration (min)</th>
              <th>User</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity, idx) => (
              <tr key={idx}>
                <td>{idx + 1}</td>
                <td>{activity.type}</td>
                <td>{activity.duration}</td>
                <td>{activity.user?.name || activity.user}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default Activities;
