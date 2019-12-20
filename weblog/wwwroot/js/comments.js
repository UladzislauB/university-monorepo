"use strict";
var string_post_id = document.getElementById("data").getAttribute("data-post-id");

var connection = new signalR.HubConnectionBuilder().withUrl("/comments").build();

document.getElementById("sendButton").disabled = true;

connection.on("ReceiveMessage", function (comment, username) {
   if (comment.postId == string_post_id)
   {
       var body = comment.body.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
       var hr = document.createElement("hr");
       var h3 = document.createElement("h3");
       h3.innerText = username;
       h3.classList.add("h4","text-dark");
       var h4 = document.createElement("h4");
       h4.innerText = body;
       h4.classList.add("h5","text-muted");
       var h6 = document.createElement("h6");
       h6.innerText = comment.date;
       h6.classList.add("text-dark");
       var div = document.createElement("div");
       div.appendChild(hr);
       div.appendChild(h3);
       div.appendChild(h4);
       div.appendChild(h6);
       let firstElem = document.getElementById("messagesList").firstChild;
       document.getElementById("messagesList").insertBefore(div, firstElem);
   }
});

connection.on("Notify", function (log) {
    console.log("NOTIFY....");
    console.log(log);
});

connection.start().then(function () {
    document.getElementById("sendButton").disabled = false;
}).catch(function (err) {
    return console.error(err.toString());
});

document.getElementById("sendButton").addEventListener("click", function (event) {
    var name = document.getElementById("data").getAttribute("data-name-user");
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