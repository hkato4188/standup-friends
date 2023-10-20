import React, { useState } from "react";
import "../css/game.css";
function Game() {
  //   const [gamePattern, setGamePattern] = useState([]);
  //   const [userClickedPattern, setUserClickedPattern] = useState([]);
  const [started, updateStarted] = useState(false);
  const [level, setLevel] = useState(0);
  const [active, setActive] = useState("");

  let buttonColors = ["red", "blue", "green", "yellow"];

  // function handleStart() {
  //   if (!started) {
  //     nextSequence();
  //     updateStarted(true);
  //   }
  // }

  function handleClick(e) {
    let userChosenColor = e.target.id;
    console.log(userChosenColor);
    //       userClickedPattern.push(userChosenColor);
    //       playSound(userChosenColor);
    //       animatePress(userChosenColor);
    //       checkAnswer(userClickedPattern.length - 1);
  }

  //     function nextSequence() {
  //       setUserClickedPattern([]);
  //       setLevel(()=> level + 1)

  //       let randomNumber = Math.floor(Math.random() * 4);
  //       let randomChosenColor = buttonColors[randomNumber];
  //       setGamePattern(()=>[...gamePattern, randomChosenColor])

  //       setActive(randomChosenColor)

  //       playSound(randomChosenColor);
  //       setActive(randomChosenColor)
  //     }

  //     function playSound(name) {
  //       let audio = new Audio("sounds/" + name + ".mp3");
  //       audio.play();
  //     }

  //     function animatePress(currentColor) {
  //       document.getElementById("#" + currentColor).addClass("pressed");
  //       setTimeout(function () {
  //         document.getElementById("#" + currentColor).removeClass("pressed");
  //       }, 100);
  //     }

  //     function checkAnswer(currentLevel) {
  //       if (gamePattern[currentLevel] === userClickedPattern[currentLevel]) {
  //         console.log("success");
  //         if (userClickedPattern.length === gamePattern.length) {
  //           setTimeout(function () {
  //             nextSequence();
  //           }, 1000);
  //         }
  //       } else {
  //         console.log("wrong");
  //         playSound("wrong");
  //         document.getElementById("body").addClass("game-over");
  //         setTimeout(function () {
  //           document.getElementById("body").removeClass("game-over");
  //         }, 200);
  //         document.getElementById("#level-title").text("Game Over Press Any Key to Restart");
  //         startOver();
  //       }
  //     }

  //     function startOver() {
  //       setLevel(0)
  //       setGamePattern{[]};
  //       started = false;
  //     }

  return (
    <div className="top-div">
      {!started ? (
        <>
          <h1>Press play to start:</h1>
          <button className="game-button">Play</button>
        </>
      ) : (
        <h1>Level {level}</h1>
      )}

      <div className="game-container">
        <div className="game-row">
          <button
            onClick={handleClick}
            id="green"
            className={
              active === "green" ? "fadeIn btn green" : "fadeOut btn green"
            }
          ></button>
          <button
            onClick={handleClick}
            id="red"
            className={!active === "red" ? "fadeIn btn red" : "fadeOut btn red"}
          ></button>
        </div>

        <div className="row">
          <button
            onClick={handleClick}
            id="yellow"
            className={`btn yellow ${
              active === "yellow" ? "fadeIn" : "fadeOut"
            }`}
          ></button>
          <button
            onClick={handleClick}
            id="blue"
            className={
              active === "blue" ? "fadeIn btn blue" : "fadeOut btn blue"
            }
          ></button>
        </div>
      </div>
    </div>
  );
}
export default Game;
