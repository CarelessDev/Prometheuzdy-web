import { useRef } from "react";

import styles from "./Promote.module.css";

import creeper from "./prometheuzdy_creeper.wav";
import pig from "./prometheuzdy_pig.wav";
import niwat from "./prometheuzdy_niwat.wav";
import steve from "./prometheuzdy_steve.wav";
import villager from "./prometheuzdy_villager.wav";

const audios = [creeper, pig, niwat, steve, villager];

export const Promote = () => {
  const audioRef = useRef<HTMLAudioElement>(null);
  const popupDiv = useRef<HTMLDivElement>(null);

  function buttonHandler(playAudio: boolean) {
    popupDiv.current.style.display = "none";

    if (playAudio) {
      const random = Math.floor(Math.random() * audios.length);
      audioRef.current.src = audios[random];

      audioRef.current.play();
    }
  }

  return (
    <>
      <div ref={popupDiv} className={styles.popup}>
        <div className={styles.popupContent}>
          <div>
            <h1>Consent Form</h1>
            <p>
              We would like to play audio on your device to enhance your
              experience on our website. Our website don't use cookie because we
              prefer biscuits.
            </p>
          </div>
          <button
            onClick={() => buttonHandler(true)}
            style={{ margin: "1rem", padding: "1rem", fontSize: "4rem" }}
          >
            I accept
          </button>

          <button
            onClick={() => buttonHandler(false)}
            style={{ margin: "1rem", fontSize: "0.5rem" }}
          >
            I decline
          </button>
        </div>
      </div>

      <audio ref={audioRef} src="" loop />
    </>
  );
};
