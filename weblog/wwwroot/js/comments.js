"use strict";
var string_post_id = document.getElementById("name").getAttribute("data-post-id");

var connection = new signalR.HubConnectionBuilder().withUrl("/comments").build();

document.getElementById("sendButton").disabled = true;

connection.on("ReceiveMessage", function (comment) {
   if (comment.postId == string_post_id)
   {
       var body = comment.body.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
       var encodedMsg = comment.name + " says " + body;
       var li = document.createElement("li");
       li.textContent = encodedMsg;
       let firstElem = document.getElementById("messagesList").firstChild;
       document.getElementById("messagesList").insertBefore(li, firstElem);
   }
});

connection.start().then(function () {
    document.getElementById("sendButton").disabled = false;
}).catch(function (err) {
    return console.error(err.toString());
});

document.getElementById("sendButton").addEventListener("click", function (event) {
    var name = document.getElementById("userInput").value;
    var body = document.getElementById("commentInput").value;
    var post_id = parseInt(string_post_id, 10);

    var date = new Date(Date.now());
    var options = {
        year: '2-digit',
        month: 'short',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric',
        second: 'numeric'
    };
    date = date.toLocaleString("en-US", options);
    console.log(typeof date);
    connection.invoke("SendComment", {"Name": name, "Body": body, "PostId": post_id, "Date": date}).catch(function (err) {
        return console.error(err.toString());
    });
    event.preventDefault();
});