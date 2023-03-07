
// mediaRecorder setup for audio
if (navigator.mediaDevices) {
    console.log('getUserMedia supported.');
  
    const constraints = { audio: true };
    let chunks = [];
    var interval;
  
    navigator.mediaDevices.getUserMedia(constraints)
    .then((stream) => {
  
      const mediaRecorder = new MediaRecorder(stream);
  

      const record = document.querySelector("#btn_start_rec");
      const stop = document.querySelector("#btn_stop_rec");
  
      record.onclick = () => {
        mediaRecorder.start();
        console.log(mediaRecorder.state);
        console.log("recorder started");

            stop.style.display = "block"
            record.style.display = "none"
            document.querySelector("#controls_subtitle").style.display = "block";
            document.querySelector("#audioPlay").style.display = "none"

            var countDownDate = new Date();
            countDownDate.setMinutes(countDownDate.getMinutes() + 5)

            interval = setInterval(function() {

                    const distance = countDownDate - new Date();

                    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
                    
                    document.getElementById("controls_subtitle").innerHTML = "Recording..." + "<b>" + minutes + "</b>" +  "m " + "<b>" + seconds + "</b>" +  "s ";
                    
                    if (distance < 20) {
                        document.getElementById("controls_subtitle").style.color = "red"
                    }
                    if (distance < 0) {
                        mediaRecorder.stop();
                    } 
            }, 1000);
      }
  
      stop.onclick = () => {
        clearInterval(interval)
        mediaRecorder.stop();
        stop.style.display = "none"
        record.style.display = "block"
        document.querySelector("#controls_subtitle").style.display = "none";
        const audio = document.querySelector("#audioPlay")
        audio.style.display = "block"
      }
  
      mediaRecorder.onstop = (e) => {
        console.log("data available after MediaRecorder.stop() called.");
  
        const blob = new Blob(chunks, { 'type' : 'audio/mp3; codecs=opus' });
        chunks = [];
        const audioURL = URL.createObjectURL(blob);
        const audio = document.querySelector("#audioPlay");
        audio.src = audioURL;

        const file = new File([blob], "audio.mp3", { type : 'audio/mp3' });
        let list = new DataTransfer();
        list.items.add(file)
        document.getElementById("input_audio").files = list.files;

        console.log(document.getElementById("input_audio").files)
        console.log(audioURL)
        console.log("recorder stopped");

      }
  
      mediaRecorder.ondataavailable = (e) => {
        chunks.push(e.data);
      }
    })
    .catch((err) => {
      console.error(`The following error occurred: ${err}`);
    })
}

