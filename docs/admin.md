# POST /api/login 后台用户登录
---
## request

- username string
- password string

## response

- status
- data
- message

# GET /api/logout 后台用户登出
---
## request
## response

- status
- data
- message

# POST /api/<group_id>/points 提交队伍分数
---

## request

- points int

## response

- status
- data
- message


# DELETE /api/<group_id>/delete 删除队伍
---

## request
## response

- status
- data
- message