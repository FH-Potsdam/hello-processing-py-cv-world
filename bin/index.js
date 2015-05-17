var ghr = require("github-url-raw");
var fs = require("fs");
var path = "https://github.com/FH-Potsdam/hello-processing-py-cv-world/blob/master/";

// ghr();

var obj = {
  files: ["background_subtraction.pyde", "brightness_tracking.pyde", "color_tracking.pyde", "contour_tracking.pyde", "empty_example.pyde", "filtering_and_display.pyde", "find_lines.pyde", "using_saturation_channel.pyde"]
};

var toc = [];
for(var i = 0; i < obj.files.length;i++){
  str = "";
  var f = obj.files[i];
  var name = f.split(".")[0];
  var res = ghr(path + f);
  console.log(res.raw);
  str = "##" + name + "\n";
  str+= "![](images/"+name+".png)  \n";

  var data = fs.readFileSync("../" + name + "/" + f,"utf8");
  var regex = /"""\n(.*?)\n"""/;
  var result = regex.exec(data);
  if( result !== null){
    console.log(result[1]);
    str += result[1] + "  \n";
  }
  toc.push(str);
}

fs.writeFile("../toc.md", toc.join("\n------------\n"), function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
});