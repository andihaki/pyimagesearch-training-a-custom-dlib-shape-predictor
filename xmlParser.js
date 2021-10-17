// const xmlFile = require('ibug_300W_large_face_landmark_dataset/labels_ibug_300W_train.xml');
var xmlFile = 'https://raw.githubusercontent.com/olayenca/externals/master/XMLParse.xml';


function loadDoc() {
  var xhttp = new XMLHttpRequest();

  xhttp.open("GET", xmlFile, true);
  xhttp.send();
  xhttp.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      // xmlFunction(this.response);
      console.log(this.response)
    }
  };

}
loadDoc();