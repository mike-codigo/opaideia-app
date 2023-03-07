function change_credit(credit){
    if (credit.value == "by_me"){
        document.getElementById("credit_name").style = "display: none !important;"
    } else {
        document.getElementById("credit_name").style = "display: block !important;"
    }
   
}

function open_post_info(){
    document.getElementById("div_post_info").style = "visibility: visible; transform: scale(1,1); opacity: 1;"
}

function close_post_info(){
    document.getElementById("div_post_info").style = "visibility: hidden; transform: scale(1.05, 1.05); opacity: 0;"
}

function add_topic_del_text(div_topic){
    const width = div_topic.offsetWidth
    div_topic.innerHTML = "remove";
    div_topic.style = `min-width: ${width}px !important; text-align: center;`
}

function remove_topic_del_text(div_topic, name_topic){
    div_topic.innerHTML = `${name_topic}`;
}

function remove_topic(div_topic, name_topic){
    const option_selected = document.querySelector("#select_topic").querySelector(`#${name_topic.replace(" ", "_")}_opt`)
    document.querySelector("#select_topic").removeChild(option_selected)
    document.querySelector("#div_selected_opt").removeChild(div_topic)
}

function add_topic(type, name_topic){
    if (type == 'subarea'){
        const verify_exist = document.querySelector("#div_selected_opt").querySelector(`#${name_topic.replace(" ", "_")}`)
        if (verify_exist == null) {
            const subarea_selected = document.createElement("div");
            subarea_selected.innerHTML = `${name_topic}`;
            subarea_selected.setAttribute("class", "div_subarea_selected");
            subarea_selected.setAttribute("id", `${name_topic.replace(" ", "_")}`);
            subarea_selected.setAttribute("onmouseenter", "add_topic_del_text(this)");
            subarea_selected.setAttribute("onmouseleave", `remove_topic_del_text(this, '${name_topic}')`);
            subarea_selected.setAttribute("onclick", `remove_topic(this, '${name_topic.replace(" ", "_")}')`);
            document.querySelector("#div_selected_opt").appendChild(subarea_selected);

            const subarea_opt = document.createElement("option");
            subarea_opt.innerHTML = `${name_topic}`
            subarea_opt.setAttribute("value", `${name_topic.replace(" ", "_")}`);
            subarea_opt.setAttribute("id", `${name_topic.replace(" ", "_")}_opt`);
            subarea_opt.setAttribute("selected", "true");
            document.querySelector("#select_topic").appendChild(subarea_opt);
        }
    } else if(type == 'subtopic'){
        const verify_exist = document.querySelector("#div_selected_opt").querySelector(`#${name_topic.replace(" ", "_")}`)
        if (verify_exist == null) {
            const subtopic_selected = document.createElement("div");
            subtopic_selected.innerHTML = `${name_topic}`;
            subtopic_selected.setAttribute("class", "div_subtopic_selected");
            subtopic_selected.setAttribute("id", `${name_topic.replace(" ", "_")}`);
            subtopic_selected.setAttribute("onmouseenter", "add_topic_del_text(this)");
            subtopic_selected.setAttribute("onmouseleave", `remove_topic_del_text(this, '${name_topic}')`);
            subtopic_selected.setAttribute("onclick", `remove_topic(this, '${name_topic.replace(" ", "_")}')`);
            document.querySelector("#div_selected_opt").appendChild(subtopic_selected);

            const subtopic_opt = document.createElement("option");
            subtopic_opt.innerHTML = `${name_topic}`
            subtopic_opt.setAttribute("value", `${name_topic.replace(" ", "_")}`);
            subtopic_opt.setAttribute("id", `${name_topic.replace(" ", "_")}_opt`);
            subtopic_opt.setAttribute("selected", "true");
            document.querySelector("#select_topic").appendChild(subtopic_opt);
        }
    }
}

/*________STUDY-ATTATCHMENTS__________ */

function open_images_std() {
    open_att()
}

function open_pdfs_std() {
    open_att()
    document.querySelector("#nav_files_att").style = "display: flex !important;"
    document.querySelector("#study_info").style =  "width: calc(100% - (6em + 5vh + 25vw)) !important;"
}

function open_input_pdf(){
    const input_pdf = document.getElementById("pdf_input")
    input_pdf.click()
}

function add_pdf_itens(){
    const input_pdf = document.getElementById("pdf_input")
    const files = input_pdf.files;
    const files_att = document.getElementById("files_att");
    files_att.innerHTML = ""
    myState = {pdf: null, currentPage: 1, totalPagesCount: null, zoom: 0.75}
    const canvas = document.getElementById("pdf_renderer");
    document.getElementById("pdf_renderer").getContext("2d").clearRect(0, 0, canvas.width, canvas.height);

    if (files.length > 5){
        alert("You can select only 5 files! Try again")
        input_pdf.value = null;
    } else {
        for (let i = 0; i < files.length; i++){
            const div_file_pdf = document.createElement("div")
            const file_icon = document.createElement("div")
            const file_name_div = document.createElement("div")
    
            div_file_pdf.setAttribute("class", "div_file_att")
            div_file_pdf.setAttribute("onclick", `open_pdf_viewer(${i})`)
            file_icon.setAttribute("class","file_att")
            file_name_div.setAttribute("class", "file_name")
            file_name_div.innerHTML = `${files[i].name}`
            div_file_pdf.appendChild(file_icon)
            div_file_pdf.appendChild(file_name_div)
            files_att.appendChild(div_file_pdf)
        }
    }
}

var myState = {
    pdf: null,
    currentPage: 1,
    totalPagesCount: null,
    zoom: 0.75
}

function render() {
    myState.pdf.getPage(myState.currentPage).then((page) => {
  
        var canvas = document.getElementById("pdf_renderer");
        var ctx = canvas.getContext('2d');

        var viewport = page.getViewport(myState.zoom);

        canvas.width = viewport.width;
        canvas.height = viewport.height;
  
        page.render({
            canvasContext: ctx,
            viewport: viewport
        });
    });
}

function open_pdf_viewer(pdf_file_number){

    const files = document.getElementById("pdf_input").files
    const current_page_input = document.getElementById("current_page")
    const total_pages = document.getElementById("total_pages")
    const pdf_file = files[`${pdf_file_number}`]
    const pdf = []
    pdf.push(pdf_file)
    var pdf_url = window.URL.createObjectURL(new Blob(pdf, {type: "application/pdf"}))
  
    pdfjsLib.getDocument(pdf_url).then((pdf) => {
        total_pages.innerHTML = `${pdf.numPages} pgs`
        current_page_input.setAttribute("min","1")
        current_page_input.setAttribute("max",`${pdf.numPages}`)
        myState.totalPagesCount = pdf.numPages;
        myState.pdf = pdf;
        render();

    });
}
window.onload = function() {
    var useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;

    tinymce.init({
    selector: '#textarea_study',
    menubar: true,
    plugins: [
        'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview', 'anchor',
        'searchreplace', 'visualblocks', 'code', 'fullscreen',
        'insertdatetime', 'media', 'table', 'code', 'help', 'wordcount',
    ],
    toolbar: 'undo redo | formatselect | ' +
    'bold italic backcolor | alignleft aligncenter ' +
    'alignright alignjustify | bullist numlist outdent indent | ' +
    'removeformat | help',
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
    });

    document.getElementById('go_previous').addEventListener('click', (e) => {
        if(myState.pdf == null|| myState.currentPage == 1) {
            return;
        }
            
        myState.currentPage -= 1;
        if (myState.currentPage >= 1){
            document.getElementById("current_page").value = myState.currentPage;
        } else {
            myState.currentPage += 1;
            return;
        }
        render();
    });
    
    document.getElementById('go_next').addEventListener('click', (e) => {
        if(myState.pdf == null || myState.currentPage > myState.pdf._pdfInfo.numPages){
            return;
        }
        myState.currentPage += 1;
        if (myState.currentPage <= myState.totalPagesCount){
            document.getElementById("current_page").value = myState.currentPage;
        } else {
            myState.currentPage -= 1;
            return;
        }
        render();
    });
    
    document.getElementById('current_page').addEventListener('keypress', (e) => {
        if(myState.pdf == null) {
            return;
        }
      
        // Get key code
        var code = (e.keyCode ? e.keyCode : e.which);
      
        // If key code matches that of the Enter key
        if(code == 13) {
            var desiredPage = document.getElementById('current_page').valueAsNumber;
                              
            if(desiredPage >= 1 && desiredPage <= myState.pdf._pdfInfo.numPages) {
                myState.currentPage = desiredPage;
                document.getElementById("current_page").value = desiredPage;
                render();
            }
        }
    });

    document.getElementById('zoom_in')
    .addEventListener('click', (e) => {
    if(myState.pdf == null) return;
    myState.zoom += 0.05;
 
    render();
    });

    document.getElementById('zoom_out')
    .addEventListener('click', (e) => {
    if(myState.pdf == null) return;
    myState.zoom -= 0.05;
     
    render();
    });
}