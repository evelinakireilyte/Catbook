import React from 'react'
import Countdown from 'react-countdown'
import { useState } from 'react'

const CountDownTimer = ({ timeImterval }) => {
  const [data, setData] = useState(Date.now() + timeImterval)
  const [key, setKey] = useState(0)
  const TimeUp = () => <span className="timer">Reloading...</span>

  const renderer = ({ minutes, seconds }) => {
    if (String(minutes).length === 1) {
      minutes = `0${minutes}`
    }
    if (String(seconds).length === 1) {
      seconds = `0${seconds}`
    }
    return (
      <div className="timer">
        {minutes}:{seconds}
      </div>
    )
  }

  const handleComplete = (props) => {
    console.log(props)
    setData(Date.now() + timeImterval)
    props.completed = false
    setKey(key + 1)
    return <TimeUp />
  }

  return (
    <div className="timerWrap">
      <div>
        <p> The content will reload in: </p>
      </div>
      <div>
        <Countdown
          date={data}
          key={key}
          renderer={renderer}
          onComplete={handleComplete}
        />
      </div>
    </div>
  )
}
export default CountDownTimer
