// 회원가입
function checkValidation(){
    let email = $("#email").val();
    let password = $("#check-password").val();
    let password2 = $("#current-password").val();    
    let nickName = $("#nickname").val();    
    let profileImg = $("#profile-img")[0].files[0];
    
    if(email == '' || password == '' || password2 == '' || nickName == '' ){
        alert("가입에 필요한 정보를 입력해주세요.");
        return;
    }

    if(password !== password2){
        alert("비밀번호를 확인해주세요.");
        return;
    }

    signUp();    
    
}





function signUp(){
    let email = $("#email").val();
    let password = $("#check-password").val();    
    let nickName = $("#nickname").val();
    let bio = $("#bio").val();
    let profileImg = $("#profile-img")[0].files[0];

    let formData = new FormData();
    formData.append("nickname", nickName);
    formData.append("password2", password);
    formData.append("email", email);
    formData.append("img", profileImg);
    formData.append("bio", bio);

    $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });

    $.ajax({
        type: 'POST',
        url: '/accounts/signup/',  
        cache: false,
        contentType: false,
        processData: false,
        mimeType: "multipart/form-data",
        data: formData, 
        success: function (response) {
            console.log(response)
            alert("회원가입이 완료되었습니다.")
            window.location.replace('/')            
        }
    })
}



// 이메일 중복 체크

function checkDuplicated() {
    let email = $("#email").val();  

    $.ajax({
        type: "GET",
        url: `/accounts/signup/check/`,
        data: {email : email},
        success: function (response) {
            // 서버에서 받은 response에서 duplicated 값이 true이면 중복확인 텍스트를 노출합니다.
            if (response["duplicated"]) {                
                alert("이미 존재하는 이메일 주소입니다.")
                return;
            } else {
                checkValidation();
            } 

        }
    });
}