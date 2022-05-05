#  Conda 환경 인터프리터 사용 /home/devuser/anaconda3/envs/DE_PYTHON_FLASK/bin/python
#  Flask 메인

#  생성(POST)
#  조회(GET)
#  수정(PUT)
#  삭제(DELETE)
#  헤더조회(HEAD)

from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

todos = {}
count = 1

@api.route('/todos')
class TodoPost(Resource):
    #  생성문
    def post(self):
        global count
        global todos

        idx = count
        count += 1
        #  JSON 타입으로 넘어온 데이터를 변수에 대입
        todos[idx] = request.json.get('data')

        #  데이터를 체크 검증하고 RETURN하는 내용을 구현후

        #  RESULT값을 RETURN.

        return {
            'todo_id': idx,
            'data' : todos[idx]
        }

@api.route('/todos/<int:todo_id>')
class TodoSimple(Resource):

    #  todo_id 에 위치한 데이터를 가져온다
    def get(self, todo_id):
        return {
            'todo_id': todo_id,
            'data' : todos[todo_id]
        }

    #  todo_id 에 위치한 데이터를 수정한다
    def put(self, todo_id):
        todos[todo_id] = request.json.get('data')
        return {
            'todo_id': todo_id,
            'data' : todos[todo_id]
        }

    #  todo_id 에 위치한 데이터를 삭제한다
    def delete(self, todo_id):
        del todos[todo_id]
        return {
            'delete': 'success'
        }


if __name__ == '__main__':
#  host='0.0.0.0' <-- 외부접속 : 도메인으로 접속 되는것까지 확인함.(포트포워딩)
#  port=5550 <-- 5550 포트로 접속
    app.run(debug=True, host='0.0.0.0', port=5550)
