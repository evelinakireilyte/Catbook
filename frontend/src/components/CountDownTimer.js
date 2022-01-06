import React from 'react'
import Countdown from 'react-countdown'
import { useState, useEffect } from 'react'

const CountDownTimer = () => {
  const [data, setData] = useState({ date: Date.now(), delay: 10000 })

  const TimeUp = () => <span className="timer">Reloading...</span>

  const renderer = ({ minutes, seconds, completed }) => {
    if (completed) {
      setData({ date: Date.now(), delay: 30000 })

      return <TimeUp />
    } else {
      return (
        <div className="timer">
          {minutes}:{seconds}
        </div>
      )
    }
  }

  return (
    <div className="timerWrap">
      <div>
        <p> The content will reload in: </p>
      </div>
      <div>
        <Countdown
          date={data.date + data.delay}
          renderer={renderer}
          onComplete={renderer}
        />
      </div>
    </div>
  )
}
export default CountDownTimer
