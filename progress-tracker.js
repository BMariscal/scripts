/*To run:

open two terminal tabs.
In the first one, enter:
        node progress-tracker.js
In the second one, enter:
        $curl --upload-file large_file.jpg http://localhost:8080
note: change "large_file.jpg" to the name of the file you want to upload*/


var fs = require('fs');
var http = require('http');

http.createServer(function(request, response){
    var newFile = fs.createWriteStream("readme_copy.pdf"); //readme_copy.pdf is the name of the file destination
    var fileBytes = request.headers['content-length']; //indicates the entire size of the readable/uploaded file(the content-length header from the request)
    var uploadedBytes = 0; //keeps track of how many bytes have been uploaded. Initializes it to zero

    request.on('readable', function(){ //listening to the readable event. Uses the readable event to keep track of progress
        var chunk = null; 
        //loops through and reads each of the chunks from the request
        while (null !== (chunk = request.read())){ 
            uploadedBytes += chunk.length;//inside of while loop, we increment the uploadedbytes variable with the length of each chunk
            var progress = (uploadedBytes / fileBytes) * 100; //then we calculate progress by dividing uploadedbytes by filebytes and multiply it by 100
            response.write("progress: " + parseInt(progress, 10)+ "%\n");//then we send the progress back to the client using the response.write function. 

        }

    });

    request.pipe(newFile); //pipe is taking care of the actual uploading 

    request.on('end', function(){ //listens to end event
      response.end('file uploaded!'); //closes the response with a "file uploaded!" string
    })


}).listen(8080); 
