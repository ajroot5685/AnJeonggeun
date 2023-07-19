구현한 기능: 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

구현하지 못한 기능: X

- 주요 구현 기능 : 이미지 업로드, 관심도 버튼, 찜하기 기능, 페이지네이션  

<br>
1️⃣ 이미지 업로드

- 저번 과제 때 언젠가 구현하겠다고 했던 이미지 업로드 기능이 과제로 나와버렸군요..😓
- modelForm을 배웠지만 커스텀하기 쉽지 않고 css 적용도 쉽지 않아 보여서 수작업을 했습니다. 그 덕분에 조금 더 고생한 것 같네요.
- media 세팅, form enctype="multipart/form-data" 설정, request.FILES['image']을 잘 숙지하고 update 페이지까지 고려하여 조건분기를 잘 설정해주었습니다.
```html
    <span>Image : </span>
    <br />
    <span>Currently : </span>
    {% if idea.image %} {{ idea.image }} 
    {% else %} image doesn't exist.
    {% endif %}
    <input type="checkbox" name="clear"><span> Clear</span>
    <br />
    <span>Change : </span>
    <input type="file" name="image" id="image" />
```
```python
    if request.method == "POST":
        idea.title=request.POST["title"]
        idea.content=request.POST["content"]
        idea.interest=request.POST["interest"]
        idea.devtool=Devtool.objects.get(name=request.POST["devtool"])

        if request.FILES.get('image'):
            tmpimage=request.FILES['image']
            idea.image=tmpimage
            
        elif request.POST.get('clear') != None:
            idea.image=None
        idea.save()
            
        return redirect(f"/ideas/{idea.pk}")
```

<br>
2️⃣ 관심도 버튼

- Ajax 를 처음 익히는데에 적당한 기능이었습니다.
```html
    <p>아이디어 관심도 : <button class="interest_ajax_btn" onclick="updateInterest('{{idea.pk}}', 'increase')">+</button><span id="interest_value{{idea.pk}}">{{ idea.interest }}</span>
        <button class="interest_ajax_btn" onclick="updateInterest('{{idea.pk}}', 'decrease')">-</button></p>
```
- button에 onclick 이벤트를 설정하고 updateInterest에 해당 idea의 pk, 증가인지 감소인지 여부까지 같이 넘겨줍니다.

<br>

```js
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
          $("#interest_value"+ideaId).text(data.new_interest);
        },
        error: function(xhr, textStatus, errorThrown) {
          console.error("Error updating interest:", textStatus, errorThrown);
        }
      });
}
```
- 안하면 오류가 나는 csrf 토큰을 만들어줍니다. ⛔
- POST 방식으로 views.py를 거쳐 바꿀 값을 받아옵니다.
- function 값은 뒤에 설명할 찜하기 기능이 views.py의 같은 함수에서 작동하기 때문에 이를 구분하기 위한 값입니다.

<br>

```python
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH')=='XMLHttpRequest'

def idea_list(request):
    if is_ajax(request=request):
        if request.POST.get("function")=="interest":
            idea_id=request.POST.get("idea_id")
            action = request.POST.get("action")

            idea_ajax=Idea.objects.get(pk=idea_id)
            if action=="increase" and idea_ajax.interest<10:
                idea_ajax.interest+=1
            elif action=="decrease" and idea_ajax.interest>0:
                idea_ajax.interest-=1
            idea_ajax.save()
            response_data = {"new_interest":idea_ajax.interest}
            return JsonResponse(response_data)
    .
    .
    .
```
- ajax에서 넘겨준 idea의 pk와 action을 통해서 어떤 idea의 값을 바꿀 것인지, 어떤 작업을 할 것인지를 정하고 해당 작업을 완료한 뒤 바꾸어야 할 값을 JSON 형태로 ajax에게 보내줍니다.
- 이 과정을 통해 비효율적인 전체 페이지 랜더링 대신 부분 랜더링을 구현할 수 있었습니다.

<br>
3️⃣ 찜하기 기능

- django도 익숙치 않고, ajax도 익숙하지 않았기에 가장 힘들었던 구현이었습니다.
- 먼저 새로운 모델 IdeaStar를 추가해줍니다. IdeaStar는 Idea를 외래키로 갖습니다.
```python
class IdeaStar(models.Model):
    idea=models.ForeignKey(Idea, verbose_name="찜", on_delete=models.CASCADE)
```

<br>

- 찜하기 등록, 삭제는 idea list와 idea detail 페이지에서 할 수 있습니다.
- 별표를 눌러서 등록, 삭제가 가능합니다.

<br>

```html
    <div class="star"><button id="star_value{{idea.pk}}" class="star" onclick="updateStar('{{idea.pk}}','/')">
        {% if idea.ideastar_set.exists %}★
        {% else %}☆
        {% endif %}</button></div>
```
- 노란별을 누르면 updateStar 함수를 호출하고 idea.pk, 경로를 전달합니다. ⭐
- 경로는 idea list에서 호출되었는지 idea detail에서 호출되었는지 구분하기 위함입니다.

<br>

```js
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
          $("#star_value"+ideaId).text(data.star);
        },
        error: function(xhr, textStatus, errorThrown) {
          console.error("Error updating interest:", textStatus, errorThrown);
        }
      });
}
```
- 관심도 버튼과 마찬가지로 ideaId과 function을 넘겨줍니다.

<br>

```python
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH')=='XMLHttpRequest'

def idea_list(request):
    if is_ajax(request=request):
        if request.POST.get("function")=="interest":
        .
        .
        .
        elif request.POST.get("function")=="star":
            idea_id=request.POST.get("idea_id")
            idea_ajax=Idea.objects.get(pk=idea_id)

            ideastar=IdeaStar.objects.filter(idea=idea_ajax)
            isStar=ideastar.exists()

            if isStar:
                ideastar.delete()
                response_data = {"star":"☆"}
            else:
                IdeaStar.objects.create(
                    idea=idea_ajax
                )
                response_data = {"star":"★"}
            return JsonResponse(response_data)
```
- ideastar(찜목록)에 내가 등록하고자 하는 idea가 있는지 확인하고 없다면 등록, 있다면 삭제합니다.
- 그리고 html에 표시할 값도 ajax에 전달합니다.

<br>
4️⃣ 페이지네이션

- 이 기능은 완전 처음보는 것이기 때문에 그저 따라치기만 했습니다...  
| https://yeko90.tistory.com/entry/django-%EA%B8%B0%EC%B4%88-%ED%8E%98%EC%9D%B4%EC%A7%95-%EC%B2%98%EB%A6%ACpagination-%EB%A7%88%EC%8A%A4%ED%84%B0-%ED%95%98%EA%B8%B0