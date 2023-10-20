import React from "react";
import "./css/styles.css";
function About() {
  return (
    <>
      <div className="flex-container">
        <div className="list-card">
          <h1 className="about-header">Welcome to Standup, Friends!</h1>
          <div className="about-text">
            <p>
              Daily standups play a crucial role in fostering communication,
              transparency, adaptability, and collaboration.
            </p>
            <p>
              The core purpose of this app is to help foster a strong learning
              team dynamic. It provides visibility into each team member’s work
              and focus for the day, coordinates efforts within the team, helps
              teams identify and address obstacles promptly, and results in a
              fostered sense of shared responsibility and accountability while
              you track your tasks to resolution.{" "}
            </p>
            <p>
              Brief and focused status updates keep everyone informed--which in
              turn helps minimize the need for further meetings. Daily standup
              discussions improve transparency by bringing visibility to the
              team’s work. They also encourage behaviors, like promptly
              identifying obstacles, that allow more time to adapt to a
              situation and respond with an effective solution resolution. Most
              importantly, this app helps users stay on track with their goals
              and maintain a strong focus on delivering value to the customer.
            </p>

            <p>
              However, daily meeting schedules can be overwhelming obstacles at
              times. For this situation, Standup, Friends! allows you to benefit
              from standup meetings with your team asynchronously!
            </p>
          </div>
        </div>
      </div>
      <div className="white-space about-text">Flatiron Phase 5 Project</div>
    </>
  );
}

export default About;
