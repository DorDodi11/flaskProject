function getUser(){
    console.log('clicked');
    fetch('https://reqres.in/api/users').then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}
function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}

function put_users_inside_html(response_obj_data) {
    // console.log(response_obj_data);

    const curr_main = document.querySelector("main");

    user = response_obj_data[getRandomInt(6)]
        const section = document.createElement('section');
        section.innerHTML = `
        <img src="${user.avatar}" alt="Profile Picture"/>
        <div>
            <span>${user.first_name} ${user.last_name}</span>
            <br>
            <a href="mailto:${user.email}">Send Email</a>
        </div>
        `;
        curr_main.appendChild(section);

}
