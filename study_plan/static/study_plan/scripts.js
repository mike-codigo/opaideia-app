/* LOGIN and REGISTER - INSTRUCTIONS */
function input_instruct(instructions, input){
    if (input.style.borderColor != "rgb(0, 172, 172)"){
        const div_input = input.parentElement;
        const div_instructions = document.createElement("div");

        div_instructions.innerHTML = `${instructions}`;
        div_instructions.setAttribute("id","div_instructions");
        div_instructions.style = "display: block !important; visibility: visible !important;"
        div_input.insertBefore(div_instructions, input)
    }
}

function clear_instruct(input){
    const div_instructions = input.parentElement;
    div_instructions.innerHTML = ""
    div_instructions.appendChild(input)
}

/* LOGIN and REGISTER - VERIFICATIONS */
function verifi_username(input){
    const username = input.value;
    const username_register = document.getElementById('username_register');
    username_register.style = ""
    fetch(`/uadoajsersalladaqeqe/${username}`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(exist_user => {
        if (exist_user.exist == 1 || username.length < 4){
            username_register.style = "border-color: red; box-shadow: 0px 5px 25px -11px rgba(191,36,31,1);"
        } else if (exist_user.exist == 0){
            username_register.style = "border-color: #00acac; box-shadow: 0px 5px 25px -11px rgba(32,189,126,1);"
        }
    })
}

function verifi_email(input){
    const email = input.value;
    const email_register = document.getElementById('email_register');
    email_register.style = ""
    fetch(`/asdajdawqeqweomemail/${email}`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(exist_user => {
        if (exist_user.exist == 1 || !(email.includes('@'))){
            email_register.style = "border-color: red; box-shadow: 0px 5px 25px -11px rgba(191,36,31,1);"
        } else if (exist_user.exist == 0 && email.includes('@')){
            email_register.style = "border-color: #00acac; box-shadow: 0px 5px 25px -11px rgba(32,189,126,1);"
        }
    })
}

function verifi_pass(){
    const pass1 = document.getElementById("pass1_register").value
    const pass2 = document.getElementById("pass2_register").value
    document.getElementById("pass1_register").style = ""
    document.getElementById("pass2_register").style = ""

    if (pass1 == pass2){
        document.getElementById("pass1_register").style = "border-color: #00acac; box-shadow: 0px 5px 25px -11px rgba(32,189,126,1);"
        document.getElementById("pass2_register").style = "border-color: #00acac; box-shadow: 0px 5px 25px -11px rgba(32,189,126,1);"
    } else if (pass1 != pass2){
        document.getElementById("pass1_register").style = "border-color: red; box-shadow: 0px 5px 25px -11px rgba(191,36,31,1);"
        document.getElementById("pass2_register").style = "border-color: red; box-shadow: 0px 5px 25px -11px rgba(191,36,31,1);"
    }
}

function verifi_image(input){
    input.style = "background-color: #00acac;"
}

/*_______ANIMATIONS______ */
function open_cont_nav_left(){
    const btns = document.querySelectorAll("#content_studys, #content_courses, #content_discussions, #content_problems_solutions, #content_news_discoveries, #content_events, #content_awards")
    btns.forEach(function(btn){
        btn.style = "opacity: 1; transform: scale(1,1) translate(0,0); width: 20vh;"
    })
}

function close_cont_nav_left(){
    const btns = document.querySelectorAll("#content_studys, #content_courses, #content_discussions, #content_problems_solutions, #content_news_discoveries, #content_events, #content_awards")
    btns.forEach(function(btn){
        btn.style = "opacity: 0; transform: scale(0,1) translate(-20vh,0); width: 0; visibility: hidden;"
    })
}


function open_opt_sa(subarea){
    const opt_sa = subarea.querySelector("#opt_sa")
    opt_sa.style = "display: flex; animation-name: fadein !important; animation-play-state: running;"
}

function close_opt_sa(subarea){
    const opt_sa = subarea.querySelector("#opt_sa")
    opt_sa.style = "display: flex; animation-name: fadeout !important; animation-play-state: running;"
    setTimeout(() => {
        opt_sa.style.display = "none";
    }, 160)
}

function open_sciences_nav(){
    document.querySelector("#btns_sciences").style = "visibility: visible;"
    document.querySelector(".sciences_nav").style = "opacity: 1; transform: translateY(0px);"
    document.querySelector("#btn_create_study_close").style.display = "block";
    if (document.querySelector(".navbar_app_content").style.display = "flex"){
        close_nav_app();
    }
    if (document.querySelector(".navbar_user_left").style.visibility = "visible"){
        close_nav_user();
    }
    window.location.hash = '#btn_search';
}

function close_sciences_nav(){
    window.location.hash = '';
    document.querySelector(".sciences_nav").style = "visibility: hidden; opacity: 0; transform: translateY(-100%);";
    document.querySelector(".subtopics").style = "transform: translateY(-100%);";
    document.querySelector(".subareas").style = "transform: translateY(-100%);";
    document.querySelector("#btns_sciences").style = "visibility: hidden;"
    document.querySelector("#btn_create_study").style.display = "block";
    document.querySelector("#btn_create_study_close").style.display = "none";
}

function open_nav_user(){
    document.querySelector(".navbar_user_left").style = "visibility: visible; transform: translateX(0px); opacity: 1;"
    if (document.querySelector(".sciences_nav").style.display = "flex"){
        close_sciences_nav();
    }
    if (document.querySelector(".navbar_app_content").style.visibility = "visible" && window.innerWidth < 726){
        close_nav_app();
    }
}
function close_nav_user(){
    document.querySelector(".navbar_user_left").style = "visibility: hidden; transform: translateX(-100%); opacity: 0;"
}
function open_app_calendar(){
    document.querySelector(".navbar_app_content").style = "transform: translateX(0px);"
    if (document.querySelector(".sciences_nav").style.display = "flex"){
        close_sciences_nav();
    }
    if (document.querySelector(".navbar_user_left").style.visibility = "visible"  && window.innerWidth < 726){
        close_nav_user();
    }
    window.location.hash = '#btn_calendar';
}
function close_nav_app(){
    document.querySelector(".navbar_app_content").style = "visibility: hidden; opacity: 0; transform: translateX(100%);"
    window.location.hash = '';
}
function open_att(){
    document.querySelector("#study_att_content").style = "visibility: visible; opacity: 1;"
}
function close_att(){
    let width = document.querySelector("#study_att_content").offsetWidth;
    document.querySelector("#study_att_content").style = `position: absolute; visibility: hidden; margin-left: calc(-${width}px * 2); opacity: 0;`
    document.querySelector("#nav_files_att").style = "display: none !important;"
    document.querySelector("#study_info").style = "width: calc(100% - 10em) !important;"
}
function open_study_info(){
    document.querySelector("#study_info").style = "visibility: visible; transform: translateY(0px); opacity: 1;"
    document.querySelector("#btn_open_info").style.display = "none";
    document.querySelector("#btn_close_info").style.display = "block";
    document.querySelector('#div_textarea').style.position = "unset";
}
function close_study_info(){
    document.querySelector("#study_info").style = "visibility: hidden; transform: translateY(100%); opacity: 0;"
    document.querySelector("#btn_open_info").style.display = "block";
    document.querySelector("#btn_close_info").style.display = "none";
    document.querySelector('#div_textarea').style.position = "absolute";
}
/*_______SCIENCE NAV_____ */
function get_subareas(science) {
    const subareas_div = document.querySelector(".subareas");
    const subtopics_div = document.querySelector(".subtopics");
    subtopics_div.innerHTML = ""
    subtopics_div.style = "display: none;"
    subareas_div.innerHTML = ""
    subareas_div.style = "display: flex;"
    document.documentElement.style.setProperty('--inverse-height-sciences-nav', '-18vh')

    const url = window.location.pathname;
    const is_create_study = url.includes('/create_study/');

    fetch(`/get_subareas/${science}`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(subareas => {
         subareas.forEach(subarea =>{
            const subarea_div = document.createElement('div')
            subarea_div.setAttribute("class","subarea")
            subarea_div.setAttribute("onmouseenter","open_opt_sa(this)")
            subarea_div.setAttribute("onmouseleave","close_opt_sa(this)")
            if (is_create_study == true){
                subarea_div.innerHTML = `
            <div onclick="get_subtopics('${subarea.name}')" id="subarea_title">
                <h2>${subarea.name}</h2>
            </div>
            <div id="opt_sa">
                <div onclick="add_topic('subarea', '${subarea.name}')" id="osa_btn_add_topic"></div>
                <div onclick="get_content_items('a', '${subarea.name}', 'courses', 0)" id="osa_btn_view"></div>
            </div>`
            }else{
                subarea_div.innerHTML = `
            <div onclick="get_subtopics('${subarea.name}')" id="subarea_title">
                <h2>${subarea.name}</h2>
            </div>
            <div id="opt_sa">
                <a id="link_opt_sa" href="/create_study/1/${subarea.name}"><div id="osa_btn_create"></div></a>
                <div onclick="get_content_items('a', '${subarea.name}', 'courses', 0)" id="osa_btn_view"></div>
            </div>`
            }
            
            subareas_div.appendChild(subarea_div)
        })

    })
}


function get_subtopics(subarea) {
    const subtopics_div = document.querySelector(".subtopics");
    subtopics_div.innerHTML = ""
    document.documentElement.style.setProperty('--inverse-height-sciences-nav', '-24vh')

    const url = window.location.pathname;
    const is_create_study = url.includes('/create_study/');

    fetch(`/get_subtopics/${subarea.split(' ').join('_')}`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(subtopics => {
         subtopics.forEach(subtopic =>{
            const subtopic_div = document.createElement('div');
            subtopic_div.setAttribute("class","subtopic")
            subtopic_div.setAttribute("onmouseenter","open_opt_sa(this)")
            subtopic_div.setAttribute("onmouseleave","close_opt_sa(this)")
            if (is_create_study == true){
                subtopic_div.innerHTML = `
            <div id="subtopic_title">
                <h2>${subtopic.name}</h2>
            </div>
            <div id="opt_sa">
                <div onclick="add_topic('subtopic', '${subtopic.name}')" id="osa_btn_add_topic"></div>
                <div onclick="get_content_items('t', '${subtopic.name}', 'courses', 0)" id="osa_btn_view"></div>
            </div>`
            }else{
                subtopic_div.innerHTML = `
            <div id="subtopic_title">
                <h2>${subtopic.name}</h2>
            </div>
            <div id="opt_sa">
            <a id="link_opt_sa" href="/create_study/2/${subtopic.name}"><div id="osa_btn_create"></div></a>
                <div onclick="get_content_items('t', '${subtopic.name}', 'courses', 0)" id="osa_btn_view"></div>
            </div>`  
            }
            
            subtopics_div.appendChild(subtopic_div)
        })
        if (subtopics_div.innerHTML == ''){
            subtopics_div.style = "display: none;"
        }
        else{
            subtopics_div.style = "display: flex;"
        }
    })
}
/*____________________VARIABLES TO GET CONTENT_______________*/


/*____________________CONTENT PAGE___________________ */

function get_content_items(type, name, content_name, is_review){
    const div_content = document.querySelector("#content_nav_right_items");
    div_content.innerHTML = ""
    atual_content = {type: type, name: name};
    fetch(`/get_content_items/${type}/${name}/${content_name}/${is_review}`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(content => content.forEach(item =>{
        if(content_name.toLowerCase() == 'studys'){
            const item_div = document.createElement("div");
            item_div.setAttribute("class", "div_item_study");
            item_div.innerHTML = `
            <div class="div_study_title">${item.title}</div>
            <div class="div_study_areas">
                <div class="div_study_area">${item.area}</div>
                <div class="div_study_area">${item.topic}</div>
            </div>
            <div class="div_study_summary">${item.summary}</div>
            <figure id="audio_summary_study">
                <audio controls src="${item.teaching_audio[0].file}">
                    <a href="${item.teaching_audio[0].file}">
                        Download audio
                    </a>
                </audio>
            </figure>
            <div class="div_study_files">
                <div class="div_study_pdfs">
                    <div class="div_sp_icon"></div>
                    ${item.pdf.length}
                </div>
                <div class="div_study_audios">
                    <div class="div_sa_icon"></div>
                    ${item.teaching_audio.length}
                </div>
            </div>`
            div_content.appendChild(item_div)
        }
        else if(content_name.toLowerCase() == 'courses'){
            const hard_skills_div = document.createElement("div");
            hard_skills_div.setAttribute("class", "div_item_course_hardskills")
            item.hard_skills.forEach(hard_skill =>{
                const h_skill = document.createElement("div")
                h_skill.setAttribute("class","div_h_skill")
                h_skill.style = `background-image: url('${hard_skill.icon}');`
                hard_skills_div.append(h_skill)
            })
            const item_div = document.createElement("div");
            item_div.setAttribute("class", "div_item_course")
            item_div.innerHTML = `<div class="div_cover_image_course" style="background-image: url('${item.cover_image}');"></div>
            <div class="div_info_course">
                <h6 class="div_item_title_course">${item.title}</h6>
                <div class="div_info_course_desc">
                    <div class="div_item_course_model">
                        <div class="div_icon_course_model"></div>
                        <p>${item.course_model}</p>
                    </div>
                    <div class="div_item_course_duration">
                        <div class="div_icon_course_duration"></div>
                        <p>${item.duration}</p>
                    </div>
                    <div class="div_item_rooms_course">
                        <div class="div_icon_course_rooms"></div>
                        <p>${item.rooms.length}</p>
                        <div class="div_icon_course_schedule"></div>
                        <p>${item.rooms[0].course_schedule}</p>
                    </div>
                </div>
                <div class="div_image_institution" style="background-image: url('${item.credits[0].logo}');"></div>
            </div>
            <div class="div_item_course_hardskills">
                    ${hard_skills_div.innerHTML}
            </div>
            <div class="btn_enter_course">
            Enter in course
            </div>`
            div_content.appendChild(item_div)
        }
    }))
}

function open_course_page(){
    const div_content = document.getElementById("content_nav_right_items");

    fetch(`/get_content_items/t/Software/${content}`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(course => course)
}

/*___________________________________REVIEWS NAV____________________________*/

function get_studys_reviews(type, name, content_name, is_review){
    const div_reviews_studys = document.querySelector(".reviews_studys");
    div_reviews_studys.innerHTML = ""
    atual_content = {type: type, name: name};
    fetch(`/get_content_items/${type}/${name}/${content_name}/${is_review}`, {
        method: 'GET'
    })
    .then(response => response.json())
    .then(content => content.forEach(item =>{
        var revs = [item.rev1_date, item.rev2_date, item.rev3_date, item.rev4_date]
        var revs_colors = []
        revs.forEach((rev)=>{
            var ToDate = new Date();
            var rev_date = new Date(rev)
            rev_date.setDate(rev_date.getDate() + 1)
            if (rev_date.getDate() == ToDate.getDate() && rev_date.getMonth() == ToDate.getMonth() && rev_date.getFullYear() == ToDate.getFullYear()){
                revs_colors[rev] = "#c7ffbd"
            }
            else if(rev_date < ToDate) {
                revs_colors[rev] = "#ffbdbd"
            }else{
                revs_colors[rev] = "#fff"
            }
        })

        const item_div = document.createElement("div");
        item_div.setAttribute("class", "div_item_study");
        item_div.innerHTML = `
        <div class="div_study_title">${item.title}</div>
        <div class="div_study_areas">
            <div class="div_study_area">${item.area}</div>
            <div class="div_study_area">${item.topic}</div>
        </div>
        <div class="div_study_summary">${item.summary}</div>
        <figure id="audio_summary_study">
            <audio controls src="${item.teaching_audio[0].file}">
                <a href="${item.teaching_audio[0].file}">
                    Download audio
                </a>
            </audio>
        </figure>
        <div class="div_study_revs">
            <div class="div_study_rev" style="background-color: ${revs_colors[item.rev1_date]} !important;"><p>First review</p>${item.rev1_date}</div>
            <div class="div_study_rev" style="background-color: ${revs_colors[item.rev2_date]} !important;"><p>Second review</p>${item.rev2_date}</div>
            <div class="div_study_rev" style="background-color: ${revs_colors[item.rev3_date]} !important;"><p>Third review</p>${item.rev3_date}</div>
            <div class="div_study_rev" style="background-color: ${revs_colors[item.rev4_date]} !important;"><p>Fourth review</p>${item.rev4_date}</div>
        </div>
        <div class="div_study_files">
            <div class="div_study_pdfs">
                <div class="div_sp_icon"></div>
                ${item.pdf.length}
            </div>
            <div class="div_study_audios">
                <div class="div_sa_icon"></div>
                ${item.teaching_audio.length}
            </div>
        </div>`
        div_reviews_studys.appendChild(item_div)
    }))
}