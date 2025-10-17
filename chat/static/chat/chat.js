document.addEventListener("DOMContentLoaded", () => {
    
    document.querySelector('#crt').style.display = 'none';
    document.querySelector('#newGroupBtn').addEventListener('click', () => {
        document.querySelector('.welcome').style.display = 'none';
        document.querySelector('#crt').style.display = 'block';
    })

    const roomName = document.getElementById('room-name').dataset.room;
    const userName = document.getElementById('user-name').dataset.user; 
    const chatSocket = new WebSocket(
        "ws://" + window.location.host + "/ws/chat/" + roomName + "/"
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const div = document.createElement("div");
        div.className = (data.sender === userName) 
            ? "d-flex justify-content-end mb-2"
            : "d-flex justify-content-start mb-2";

        const inner = document.createElement("div");
        inner.className = (data.sender === userName)
            ? "d-flex flex-column align-items-end"
            : "d-flex flex-column align-items-start";

        const text = document.createElement('span');
        text.className = (data.sender === userName)
            ? "badge bg-primary text-wrap p-2"
            : "badge bg-secondary text-wrap p-2";
        text.innerText = data.message;

        const small = document.createElement('small');
        small.className = 'text-muted';
        small.innerText = (data.sender === userName)? "Me": data.sender;

        inner.appendChild(text);
        inner.appendChild(small);
        div.appendChild(inner);

        document.querySelector("#chat-messages").appendChild(div);

    };

    window.addEventListener("load", () => {
        const box = document.getElementById("chat-messages");
        box.scrollTop = box.scrollHeight;
    }, 50);

    const form = document.getElementById("chatForm");
    form.addEventListener("submit", function(e) {
        e.preventDefault();       // stop page reload
        const input = document.getElementById("chatMessageInput");
        const box = document.getElementById("chat-messages");
        box.scrollTop = box.scrollHeight;
        if (input.value.trim() === "") return;  // ignore empty messages 

        chatSocket.send(JSON.stringify({
            "message": input.value,
            "sender": userName
        }));
        input.value = "";

        const msgBox = document.getElementById("chat-messages");
        requestAnimationFrame(() => {
            msgBox.scrollTop = msgBox.scrollHeight;
        });
        
    });
});
    