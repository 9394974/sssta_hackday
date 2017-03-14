# GET /api/group 获取所有队伍信息
---
## request
## response
- status
- message
- data list 
   - group_id int
   - points int 
   - name int（队员名字）
   - college int 
     - 0 软院
     - 1 计院
   - grade int
     - 0 15级
     - 1 16级
   - qq string
   - email string
   - phone string
   

# GET /api/group/<group_id> 获取单个队伍信息
---
## request
## response
- status
- message
- data
   - group_id int
   - points int 
   - name int（队员名字）
   - college int 
     - 0 软院
     - 1 计院
   - grade int
     - 0 15级
     - 1 16级
   - qq string
   - email string
   - phone string   
   
# POST /api/group/parcitipate 提交队伍信息
---
## request

- name string
- college int
- grade int 
- qq string
- email string
- phone string

## response
- status
- message
- data
   - group_id int
 