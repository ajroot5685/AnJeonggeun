구현한 기능: 로그인, 좋아요, 댓글 작성, 댓글 삭제

구현하지 못한 기능: X

<br>
1️⃣ 로그인

- 과제를 끝내고 보니 로그인 기능을 괜히 넣었나 싶습니다
- 로그인만 안했더라도 과제가 굉장히 빨리 끝났을 것 같은 느낌적인 느낌..

<br>
2️⃣ 좋아요

- 마지막 교육 세션 때 했던 기능입니다.(다들 아시죠?😏)

```python
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    image = models.ImageField('이미지', blank=True, upload_to='idea/%Y%m%d')
    content = models.TextField()
    like = models.IntegerField(null=True, default=0)
    like_users = models.ManyToManyField(User, through='Like', related_name='liked_post')

    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post')
    created_at = models.DateTimeField(auto_now_add=True)
```

- 먼저 모델입니다.
- Post에서 Like모델을 다대다 관계로 like_users필드로 사용합니다.
- Like모델은 user와 post 하나씩을 외래키로 가집니다.
- 이러한 설계는 중복되는 것을 막고 회원별로 구분이 되도록 해줍니다.

<br>

```html
{% if user != none %}
    {% if user in post.like_users.all %}
        <img src="{% static 'pgram/image/like.png' %}" alt="" onclick="onClickLike({{post.id}}, {{user.id}}, 'unlike')">
    {% else %}
        <img src="{% static 'pgram/image/unlike.png' %}" alt="" onclick="onClickLike({{post.id}}, {{user.id}}, 'like')">
    {% endif %}
{% else %}
    <img src="{% static 'pgram/image/unlike.png' %}" alt="">
{% endif %}
```

- 처음 랜더링 시 유저가 해당 포스트에 좋아요를 눌렀는지 여부에 따라 다른 이미지가 보여집니다.
- 로그인된 상태에서 좋아요 버튼을 누르면 onclick이벤트가 발생하여 ajax로 비동기 처리합니다.

<br>

```js
const requestLike = new XMLHttpRequest();

const onClickLike = (id, userid, type) => {
  const url = "/like_ajax/";
  requestLike.open("POST", url, true);
  requestLike.setRequestHeader(
    "Content-Type",
    "application/x-www-form-urlencoded"
  );
  requestLike.send(JSON.stringify({ id: id, userid: userid, type: type }));
};

requestLike.onreadystatechange = () => {
  if (requestLike.readyState === XMLHttpRequest.DONE) {
    if (requestLike.status < 400) {
      const { id, userid, type } = JSON.parse(requestLike.response);
      const element = document.querySelector(`.post-id-${id} .btn_box`);
      let imgHTML;
      let btntype;
      if (type == "like") {
        imgHTML = "../../static/pgram/image/like.png";
        btntype = "unlike";
      } else {
        imgHTML = "../../static/pgram/image/unlike.png";
        btntype = "like";
      }
      const newHTML = `<img src=${imgHTML} alt="" onclick="onClickLike(${id}, ${userid}, '${btntype}')">`;
      element.innerHTML = newHTML;
      const commentHTML =
        '<img src="../../static/pgram/image/comment.png" alt="">';
      element.insertAdjacentHTML("beforeend", commentHTML);

      const countelement = document.querySelector(
        `.post-id-${id} .post_like .bold`
      );
      const originHTML = countelement.innerHTML;
      const [buttonType, num, trash] = originHTML.split(" ");
      let count;
      if (type == "like") {
        count = Number(num) + 1;
      } else {
        count = Number(num) - 1;
      }
      countelement.innerHTML = `좋아요 ${count} 개`;
    }
  }
};
```

- 회원별로 좋아요 유무를 구분해야 하므로 views.py 에 user id 까지 넘겨줍니다.
- 데이터를 다시 받으면 해당 데이터에 따라 이미지를 바꾸고 좋아요 수를 업데이트합니다.

<br>

```python
@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    user_id = req['userid']
    button_type = req['type']

    post = Post.objects.get(id=post_id)
    user = User.objects.get(id=user_id)

    if button_type=='like':
        post.like+=1
        Like.objects.create(
            post = post,
            user = user,
        )
    else:
        post.like-=1
        Like.objects.filter(user=user,post=post).delete()

    post.save()

    return JsonResponse({'id':post_id, 'userid':user_id, 'type':button_type})
```

- 세션 때 했던 내용에서 로그인 부분만 추가되었습니다.
- 좋아요를 누른 포스트의 좋아요 수를 업데이트하고 Like 모델을 생성 또는 삭제합니다.

<br>

<br>
3️⃣ 댓글 작성

- 로그인을 왜 구현했을까? 라고 후회하게 했던 녀석입니다.🙉
- 로그인에 더해 비동기 처리까지 하려니 해야할일이 곱절이 되었습니다.

```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    text = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```
- 댓글 모델입니다.
- 어느 포스트의 댓글인지, 어느 유저가 작성했는지 알기 위해 user와 post 모델을 외래키로 사용합니다.

<br>

```html
<div class="post_comment_add">
    <form onsubmit="submitForm(event, {{post.id}}, {{user.id}})">
        {% csrf_token %}
        <input type="text" name="content" placeholder="댓글 달기..." required>
        <input type="submit" value="작성 완료!" class="submit" />
    </form>
</div>
```
- 댓글을 작성하면 action이 아닌 onsubmit로 js로 데이터가 전달됩니다.

<br>

```js
const requestComment = new XMLHttpRequest();

    const submitForm = (event, post_id, user_id) =>{
        event.preventDefault();

        if(user_id==null)
            return;

        const formData = new FormData(event.target);

        formData.append('post_id', post_id);
        formData.append('user_id', user_id);

        const url = "/pgram/comment";
        requestComment.open("POST",url,true);
        requestComment.send(formData);

        const inputElement = event.target.querySelector('input[name="content"]');
        if (inputElement) {
            inputElement.value = "";
        }
    };
```
- 우선 event.preventDefault(); 로 폼이 2번 작성되지 않도록 합니다.
- 또한 현재 로그인된 유저 id를 검사하여 로그인이 되어있지 않은 경우 그대로 반환합니다.
- 로그인한 유저인 경우 post_id와 user_id 까지 추가한 formData를 전달합니다.

<br>

```python
@csrf_exempt
def pgram_comment(request):
    user_id = request.POST.get("user_id")
    post_id = request.POST.get("post_id")

    comment_user=User.objects.get(id=user_id)
    post=Post.objects.get(id=post_id)
    text=request.POST.get("content")

    Comment.objects.create(
        post=post,
        user=comment_user,
        text=text,
    )

    comments=Comment.objects.filter(post=post)

    comments_data = []
    for item in comments:
        user = item.user
        comment_data={
            'id':item.id,
            'user_id':user.id,
            'username':user.username,
            'text':item.text,
        }
        comments_data.append(comment_data)

    return JsonResponse({'post_id':post_id, 'comments':comments_data})
```
- 전달받은 데이터로 Comment 모델을 생성하고 html을 업데이트하기 위해 해당 post의 comment들을 json형식으로 다시 전달합니다.

<br>

```js
requestComment.onreadystatechange=()=>{
    if(requestComment.readyState === XMLHttpRequest.DONE){
        if(requestComment.status<400){
            const{post_id, comments}=JSON.parse(requestComment.response);

            const element = document.querySelector(`.post-id-${post_id} .post_comment`);
            element.innerHTML ='';

            for (const comment of comments) {
                const commentElement = document.createElement('p');
                commentElement.innerHTML = `<a onclick="delete_comment(${comment.id}, ${post_id}, ${comment.user_id})" class="comment_delete">X</a><span class="bold">${comment.username}</span> ${comment.text}`;
                element.appendChild(commentElement);
            }
        }
    }
};
```
- 전달받은 데이터들로 해당 포스트의 댓글 목록들을 업데이트합니다.


<br>
4️⃣ 댓글 삭제

- 드디어 마지막! 댓글 삭제 입니다!

```html
{% for comment in comments %}
    {% if comment.post.id == post.id %}
        <p><a onclick="delete_comment({{comment.id}}, {{post.id}}, {{comment.user.id}})" class="comment_delete">X</a><span class="bold">{{ comment.user.username }}</span> {{ comment.text }}</p>
    {% endif %}
{% endfor %}
```
- 시작부터 어지럽습니다.😵
- 비동기 처리를 위해서는 어쩔 수 없습니다.
- 댓글 왼쪽의 x 표시를 누르면 delete_comment()가 호출됩니다.

```js
const requestDeleteComment = new XMLHttpRequest();

    const delete_comment = (comment_id, post_id, user_id) =>{
        if(user_id==null)
            return;

        const url = "/comment/delete";
        requestDeleteComment.open("POST",url,true);
        requestDeleteComment.setRequestHeader(
            "Content-Type",
            "application/x-www-form-urlencoded"
        );
        requestDeleteComment.send(JSON.stringify({comment_id: comment_id, post_id: post_id, user_id: user_id}))
    };
```
- 특정 Comment 객체를 삭제해야 하므로 그와 관련된 id들과 현재 삭제 요청을 한 유저의 id도 넘겨줍니다.

<br>

```python
@csrf_exempt
def pgram_comment_delete(request):
    req = json.loads(request.body)
    comment_id = req['comment_id']
    post_id = req['post_id']
    user_id = req['user_id']

    current_user = request.user
    
    comment=Comment.objects.get(id=comment_id)
    post=Post.objects.get(id=post_id)

    deleted=False

    if user_id==current_user.id:
        comment.delete()
        deleted=True

    comments=Comment.objects.filter(post=post)

    comments_data = []
    for item in comments:
        user = item.user
        comment_data={
            'id':item.id,
            'user_id':user.id,
            'username':user.username,
            'text':item.text,
        }
        comments_data.append(comment_data)

    return JsonResponse({'comment_id':comment_id, 'post_id':post_id, 'user_id':user_id, 'comments':comments_data, 'deleted':deleted})
```
- 본인이 아닌 다른사람이 자신의 댓글을 지우는 경우가 생겨선 안됩니다.
- 따라서 삭제 요청한 유저와 댓글의 유저 아이디가 일치하는지 검증합니다.
- 본인이 맞다면 해당 댓글을 삭제하고 댓글 목록을 업데이트하기 위한 데이터들을 넘겨줍니다.

```js
requestDeleteComment.onreadystatechange=()=>{
    if(requestDeleteComment.readyState === XMLHttpRequest.DONE){
        if(requestDeleteComment.status<400){
            const{comment_id,post_id,user_id, comments, deleted}=JSON.parse(requestDeleteComment.response);

            if (deleted==false){
                return;
            }

            const element = document.querySelector(`.post-id-${post_id} .post_comment`);
            element.innerHTML ='';

            for (const comment of comments) {
                const commentElement = document.createElement('p');
                commentElement.innerHTML = `<a onclick="delete_comment(${comment.id}, ${post_id}, ${comment.user_id})" class="comment_delete">X</a><span class="bold">${comment.username}</span> ${comment.text}`;
                element.appendChild(commentElement);
            }
        }
    }
};
```
- 삭제되지 않은 경우 업데이트할 필요가 없으므로 바로 반환합니다.
- 삭제되었을 경우 해당 포스트의 댓글 목록들을 업데이트합니다.

| 와 드디어 끝났다! \\(^0^)/