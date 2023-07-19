function submitForm() {
  document.getElementById("orderForm").submit();
}

function updateInterest(ideaId, action){
    var csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;  // CSRF 토큰 가져오기

    $.ajax({
        type: "POST",
        url: "/",
        data: {
            csrfmiddlewaretoken: csrfToken,
            idea_id: ideaId,
            action: action,
            function: "interest",
        },
        success: function(data) {
          // 서버에서 새로운 관심도 값을 받아서 업데이트
          $("#interest_value").text(data.new_interest);
        },
        error: function(xhr, textStatus, errorThrown) {
          console.error("Error updating interest:", textStatus, errorThrown);
        }
      });
}

function updateStar(ideaId, url){
    var csrfToken = document.querySelector('input[name=csrfmiddlewaretoken]').value;  // CSRF 토큰 가져오기

    $.ajax({
        type: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken: csrfToken,
            idea_id: ideaId,
            function: "star",
        },
        success: function(data) {
          // 서버에서 새로운 관심도 값을 받아서 업데이트
          $("#star_value").text(data.star);
        },
        error: function(xhr, textStatus, errorThrown) {
          console.error("Error updating interest:", textStatus, errorThrown);
        }
      });
}